#!/usr/bin/env python3
"""Static release QA for AKSANIRA. Does not test live hosting, checkout, forms or browser rendering."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import json, re, sys, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
SITE_HOST = 'www.aksanira.my.id'

class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title=0; self.desc=0; self.h1=0; self.canonical=[]; self.missing_alt=0
        self.links=[]; self.images=[]; self.noindex=False; self.ids=[]; self.forms=0
        self.external_blank_without_rel=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='title': self.title+=1
        if tag=='meta' and a.get('name','').lower()=='description' and a.get('content','').strip(): self.desc+=1
        if tag=='meta' and a.get('name','').lower()=='robots' and 'noindex' in a.get('content','').lower(): self.noindex=True
        if tag=='h1': self.h1+=1
        if tag=='link' and a.get('rel','').lower()=='canonical' and a.get('href'): self.canonical.append(a['href'])
        if tag=='a' and a.get('href'):
            self.links.append(a['href'])
            u=urlparse(a['href'])
            if u.scheme in ('http','https') and a.get('target')=='_blank' and not {'noopener','noreferrer'}.issubset(set(a.get('rel','').split())):
                self.external_blank_without_rel+=1
        if tag=='img':
            if not a.get('alt','').strip(): self.missing_alt+=1
            if a.get('src'): self.images.append(a['src'])
        if a.get('id'): self.ids.append(a['id'])
        if tag=='form': self.forms+=1

html=sorted(ROOT.glob('*.html')); errors=[]; warnings=[]; parsed={}; file_text={}
for f in html:
    raw=f.read_text(encoding='utf-8',errors='replace'); file_text[f]=raw
    a=Audit(); a.feed(raw); parsed[f]=a
    for label,val in [('title',a.title),('meta description',a.desc),('H1',a.h1)]:
        if val<1: errors.append(f'{f.name}: missing {label}')
    if len(a.canonical)!=1: errors.append(f'{f.name}: expected exactly one canonical, found {len(a.canonical)}')
    elif urlparse(a.canonical[0]).netloc != SITE_HOST: errors.append(f'{f.name}: canonical must use {SITE_HOST}')
    else:
        cu=urlparse(a.canonical[0]); expected='/' if f.name=='index.html' else '/' + f.stem
        actual=cu.path.rstrip('/') or '/'
        # Explicit canonical aliases are intentional consolidation targets; keep this list reviewed.
        aliases={'tool-guest-capacity.html':'/tools-gratis','tool-payment-schedule.html':'/wedding-budget-planner',
                 'tool-wedding-timeline.html':'/wedding-family-committee-coordinator','vendor-comparison-mini.html':'/tool-vendor-evaluator'}
        if f.name!='404.html' and actual != (expected.rstrip('/') or '/') and actual != aliases.get(f.name):
            errors.append(f'{f.name}: canonical path mismatch; expected {expected} or reviewed alias, found {cu.path}')
        if f.name in aliases and actual != aliases[f.name]: errors.append(f'{f.name}: reviewed canonical alias changed unexpectedly')
        if cu.query or cu.fragment: errors.append(f'{f.name}: canonical should not contain query or fragment')
        if f.name in aliases:
            target_slug=actual.strip('/'); target_file=ROOT/(target_slug+'.html')
            if not target_file.is_file(): errors.append(f'{f.name}: canonical alias target does not resolve to local HTML: {actual}')
    if a.missing_alt: errors.append(f'{f.name}: {a.missing_alt} image(s) missing/empty alt')
    if len(a.ids)!=len(set(a.ids)): errors.append(f'{f.name}: duplicate id attribute')
    if a.h1>1: warnings.append(f'{f.name}: multiple H1 elements ({a.h1})')
    if a.external_blank_without_rel: errors.append(f'{f.name}: external target=_blank link missing noopener noreferrer')

# Local image references and internal routes/fragments.
for f,a in parsed.items():
    for src in a.images:
        u=urlparse(src)
        if u.scheme or u.netloc or src.startswith('data:'): continue
        target=ROOT/unquote(u.path.lstrip('/'))
        if not target.is_file(): errors.append(f'{f.name}: missing local image {src}')
    for href in a.links:
        if href.startswith(('mailto:','tel:','javascript:')): continue
        u=urlparse(href)
        if u.scheme or u.netloc: continue
        path=unquote(u.path)
        if path=='': target=f
        elif path=='/': target=ROOT/'index.html'
        else:
            rel=path.lstrip('/')
            target=ROOT/rel
            if not target.is_file() and (ROOT/(rel+'.html')).is_file(): target=ROOT/(rel+'.html')
            elif not target.is_file() and (ROOT/rel/'index.html').is_file(): target=ROOT/rel/'index.html'
        if not target.is_file():
            warnings.append(f'{f.name}: internal route requires runtime verification: {href}')
        elif u.fragment and target.suffix=='.html':
            dest=parsed.get(target)
            if dest is None:
                dest=Audit(); dest.feed(target.read_text(encoding='utf-8',errors='replace'))
            if unquote(u.fragment) not in dest.ids:
                errors.append(f'{f.name}: broken local fragment {href}')

# Sitemap and robots.
urls=[]; smap=ROOT/'sitemap.xml'; robots=ROOT/'robots.txt'
if not robots.exists(): errors.append('robots.txt missing')
if not smap.exists(): errors.append('sitemap.xml missing')
else:
    try:
        urls=[e.text for e in ET.parse(smap).findall('.//{*}loc')]
        if len(urls)!=len(set(urls)): errors.append('duplicate sitemap URLs')
        for url in urls:
            if urlparse(url).netloc != SITE_HOST: errors.append(f'sitemap URL must use {SITE_HOST}: {url}')
            slug=urlparse(url).path.strip('/'); f=ROOT/('index.html' if not slug else slug+'.html')
            if not f.exists(): warnings.append(f'sitemap route requires Vercel cleanUrls/runtime verification: {url}')
            elif f in parsed and parsed[f].noindex: errors.append(f'noindex page included in sitemap: {url}')
    except Exception as e: errors.append(f'sitemap parse failed: {e}')
if robots.exists() and 'sitemap:' not in robots.read_text(encoding='utf-8',errors='replace').lower():
    warnings.append('robots.txt has no Sitemap directive')

# Expected listing targets and stale price assertions.
expected={
 'https://aksanira.myr.id/catalog/wedding-budget-planner-79298',
 'https://aksanira.myr.id/catalog/wedding-vendor-comparison-planner'}
all_text='\n'.join(file_text.values())
for u in sorted(expected):
    if u not in all_text: errors.append(f'expected Mayar listing URL missing: {u}')
for core_page in ['produk.html','wedding-budget-planner.html','wedding-vendor-comparison-planner.html']:
    raw=file_text.get(ROOT/core_page,'')
    price_blocks=re.findall(r'<div class="[^"]*mayar-price[^"]*"[^>]*>(.*?)</div>',raw,re.I|re.S)
    if any(re.search(r'Rp\s?\d[\d.]*', re.sub(r'<[^>]+>',' ',block)) for block in price_blocks):
        errors.append(f'{core_page}: static Rupiah price inside Mayar price element')
if re.search(r'Harga yang ditampilkan pada katalog merupakan harga produk saat ini', file_text.get(ROOT/'produk.html',''), re.I):
    errors.append('produk.html: stale statement implies catalogue is current price source')

# Vercel JSON and host redirect contract.
try:
    cfg=json.loads((ROOT/'vercel.json').read_text(encoding='utf-8'))
    redirects=cfg.get('redirects',[])
    host_rule=any(r.get('destination','').startswith('https://www.aksanira.my.id/') and any(c.get('type')=='host' and c.get('value')=='aksanira.my.id' for c in r.get('has',[])) for r in redirects)
    if not host_rule: errors.append('vercel.json: apex-to-www host redirect rule missing')
except Exception as e: errors.append(f'vercel.json invalid JSON: {e}')

print(f'HTML pages: {len(html)}')
print(f'Sitemap URLs: {len(urls)}')
print(f'robots.txt: {robots.exists()}')
print(f'Errors: {len(errors)} | Warnings: {len(warnings)}')
for x in errors: print('ERROR:',x)
for x in warnings[:100]: print('WARN:',x)
if errors: sys.exit(1)
