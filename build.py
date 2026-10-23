import json, html
STORE='https://chromewebstore.google.com/detail/REPLACE_ID'; BUY='https://payhip.com/b/qokFH'; ZIP='basedrop-1.0.0.zip'; BASE='https://haihan19955.github.io/basedrop/'
FAQ=[
("Does Airtable let you download all attachments at once?","Not natively. Airtable has no built-in button to download every attachment in a table, so you normally open each file one by one. BaseDrop adds that missing bulk download."),
("How do I download all attachments from an Airtable table?","Install BaseDrop, paste a read-only personal access token, pick the base, table (and optionally a view) and the attachment fields, then click Download ZIP. Every file is saved into organized ZIP files with an index.csv."),
("Does it work on the Airtable Free plan?","Yes. BaseDrop uses the official Airtable Web API, which is available on the Free plan. Listing records costs 1 API call per 100 records (Free plan: 1,000 calls per workspace per month). Downloading the files themselves does not use API calls, and BaseDrop shows exactly how many calls each run used."),
("Is my data safe?","Your token is stored only in your browser and only sent to api.airtable.com. Files go straight from Airtable's file servers to your computer – they never pass through a BaseDrop server. The token only needs read scopes."),
("Can I rename files after a field?","Yes (Pro). Use templates such as {field:Client} - {field:Name} - {n}, and optionally put each record in its own folder, including nested folders like {field:Status}/{field:Name}."),
("What about very large tables?","BaseDrop downloads with rate-limit-safe pacing (under Airtable's 5 requests/second), retries failed files, and splits big exports into multiple ZIP parts so your browser does not run out of memory."),
("Can I export a whole base?","Yes (Pro). Whole-base mode exports every table that has attachment fields, one folder per table."),
("What does the free version include?","Up to 50 files per run with original file names, from any table or view, plus index.csv. Pro removes the limit and unlocks renaming, folders and whole-base export."),
("How does the license work?","Pro is a one-time purchase on Payhip. You receive a license key by email; paste it into BaseDrop. One key works on up to 3 of your own browsers. Refunds automatically deactivate the key."),
("Is BaseDrop made by Airtable?","No. BaseDrop is an independent tool and is not affiliated with or endorsed by Airtable."),
]
def page(fn,title,desc,body,extra=''):
    open(fn,'w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{BASE}{'' if fn=='index.html' else fn}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="{BASE}screenshot.png"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="icon.png"><link rel="stylesheet" href="style.css">{extra}</head><body><header><a href="./">BaseDrop · Bulk Attachment Downloader for Airtable</a></header><main>{body}</main><footer><a href="guides.html">Guides</a> · <a href="faq.html">FAQ</a> · <a href="privacy.html">Privacy</a> · Not affiliated with Airtable · Made by SteadyFlowSheets</footer></body></html>''')
faqld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]})
faqhtml=''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q,a in FAQ)
page('index.html','Download All Attachments from Airtable – BaseDrop (Free Chrome Extension)','Bulk download every Airtable attachment from a table, view or whole base as organized ZIP files. Rename by field, folder per record, index.csv. Works on the Free plan.',f'''
<div class="hero"><img src="icon.png" width="72" alt=""><h1>Download all attachments from Airtable – in one click</h1><p>Airtable has no “download all” button. BaseDrop adds it: every file from a table, a filtered view or a whole base, saved as organized ZIPs.</p>
<a class="btn" href="install.html">Install free</a><a class="btn alt" href="{BUY}">Get Pro (one-time)</a><p style="font-size:.9rem;color:#556">Chrome Web Store listing: <b>coming soon</b> (in review). Until then you can <a href="install.html">load it manually in 1 minute</a>.</p><img class="shot" src="screenshot.png" alt="BaseDrop downloading Airtable attachments with progress bar"></div>
<div class="grid"><div class="card"><h2>Organized, not a mess</h2><p>Rename files after any field (<code>{{field:Client}} - {{field:Name}}</code>), one folder per record, plus an <b>index.csv</b> mapping every file to its record.</p></div>
<div class="card"><h2>Private by design</h2><p>Files go straight from Airtable to your computer. Read-only token, stored only in your browser. No BaseDrop server sees your data.</p></div>
<div class="card"><h2>Built for big tables</h2><p>Respects Airtable's rate limits, retries failures and splits large exports into multiple ZIP parts.</p></div>
<div class="card"><h2>Works on the Free plan</h2><p>Uses the official Airtable API. 1 API call per 100 records – and BaseDrop tells you exactly how many calls each run used.</p></div></div>
<div class="card"><h2>Free vs Pro</h2><table class="price"><tr><th></th><th>Free</th><th>Pro – $19 one-time</th></tr><tr><td>Files per run</td><td>50</td><td>Unlimited</td></tr><tr><td>Table or view, index.csv</td><td>✓</td><td>✓</td></tr><tr><td>Rename by field templates</td><td>–</td><td>✓</td></tr><tr><td>Folder per record (nested)</td><td>–</td><td>✓</td></tr><tr><td>Whole-base export</td><td>–</td><td>✓</td></tr><tr><td>Browsers per license</td><td>–</td><td>3</td></tr></table><p><a class="btn alt" href="{BUY}">Buy Pro</a></p></div>
<h2>FAQ</h2>{faqhtml}''',f'<script type="application/ld+json">{faqld}</script>')
page('faq.html','BaseDrop FAQ – Bulk Download Airtable Attachments','Answers about downloading all Airtable attachments: Free plan API limits, privacy, renaming, large tables and licensing.',f'<h1>Frequently asked questions</h1>{faqhtml}',f'<script type="application/ld+json">{faqld}</script>')
page('privacy.html','BaseDrop Privacy Policy','BaseDrop privacy policy.','''<h1>Privacy policy</h1><div class="card"><p>Last updated: 2026-10-22</p>
<p><b>What BaseDrop stores:</b> your Airtable personal access token, your license key and a random device ID, saved only in your browser's extension storage (chrome.storage.local).</p>
<p><b>Where data goes:</b> the token is sent only to api.airtable.com. Attachment files are downloaded directly from Airtable's file servers (*.airtableusercontent.com, dl.airtable.com) to your computer. BaseDrop has no server that receives your records or files.</p>
<p><b>License check:</b> when you activate Pro, your license key and random device ID are sent to our license server, which asks Payhip whether the key is valid. We store the key and up to 3 device IDs to enforce the device limit. Nothing else is collected.</p>
<p><b>No analytics, no ads, no selling of data.</b></p><p>Not affiliated with Airtable.</p></div>''')
page('install.html','Install BaseDrop – Bulk Attachment Downloader for Airtable','How to install BaseDrop in Chrome, Edge or Brave.',f'''<h1>Install BaseDrop</h1>
<div class="card"><h2>Chrome Web Store – coming soon</h2><p>BaseDrop has been submitted to the Chrome Web Store. Once approved, a one-click install button will appear here and updates will be automatic.</p></div>
<div class="card"><h2>Load it manually (works today)</h2><ol>
<li><a class="btn" href="{ZIP}" download>Download BaseDrop v1.0.0 (.zip)</a> and unzip it to a folder you will keep.</li>
<li>Open <code>chrome://extensions</code> (Edge: <code>edge://extensions</code>, Brave: <code>brave://extensions</code>).</li>
<li>Turn on <b>Developer mode</b> (top-right).</li>
<li>Click <b>Load unpacked</b> and select the unzipped folder.</li>
<li>Click the BaseDrop icon in the toolbar, paste your Airtable token and download.</li></ol>
<p>Manual installs do not auto-update; when the store version is live, remove this copy and install from the store. Your Pro license key works in both.</p></div>
<div class="card cta"><h2>Need more than 50 files per run?</h2><p>BaseDrop Pro – one-time $19: unlimited files, rename by field, folders, whole-base export.</p><a class="btn alt" href="{BUY}">Buy Pro on Payhip</a></div>''')
import sys,types;m=types.ModuleType('build_common');m.page=page;m.BASE=BASE;sys.modules['build_common']=m
import guides;GP=guides.build()
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{p}</loc></url>' for p in ['','install.html','faq.html','privacy.html']+GP)+'</urlset>')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n'); open('.nojekyll','w').write('')
