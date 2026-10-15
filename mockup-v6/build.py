import re, html
from pathlib import Path
R=Path('/workspace/mockup-v6')
v5=open('/workspace/mockup-v5/index.html').read()
THREE=v5[v5.index('<script type="importmap">'):v5.index('</body>')]  # importmap + three module, unchanged

FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'
def head(title,p,desc=''):
    return f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n<title>{title}</title>\n{FONTS}\n<link rel="stylesheet" href="{p}assets/style.css"></head><body>\n'
def nav(p,home=False):
    h='' if home else p+'index.html'
    return (f'<nav><a class="logo" href="{h or "#"}">alex<span>.</span>m</a><a class="lk" href="{h}#work">Work</a><a class="lk" href="{h}#ventures">Ventures</a>'
            f'<a class="lk" href="{h}#rd">R&amp;D</a><a class="lk" href="{h}#journey">Journey</a><a class="talk" href="{p}blog.html">Blog</a></nav>\n')
def footer(p):
    return (f'<footer><div class="glow"></div><div class="wm">Alex <em>Mosneagu</em></div>'
            f'<div class="base"><span>© 2026 Alex Mosneagu</span><span>Bucharest, RO</span><a href="#top">Back to top ↑</a></div></footer>\n')
def sh(idx,n,h2,pp):
    return f'<div class="sh"><div class="idx">// {idx}<b>{n}</b></div><h2>{h2}</h2><p>{pp}</p></div>'
e=html.escape

# ---------------- data ----------------
ventures=[
 dict(slug='liveflow',a='Live',b='Flow',place='Italy',role='Associate',lime=True,
  desc='Frontend on the LiveFlow product, full stack on LiveFlow Academy. An enterprise platform unifying workflow orchestration, AI automation and human collaboration.',
  products=['LiveFlow','LiveFlow Academy'],badge='We Make Future 2026',
  long=['LiveFlow is an enterprise platform that unifies workflow orchestration, AI automation and human collaboration.','My part: frontend on the LiveFlow product, and full stack on LiveFlow Academy.']),
 dict(slug='devolution-zone',a='Devolution ',b='Zone',place='White-label',role='Administrator & Full Stack Developer',
  desc='A white-label development department: web, marketing, AI and outsourcing.',
  products=['Discrete Profile'],badge='Web Summit 2024 · Portugal',
  long=['Devolution Zone is a white-label development department covering web, marketing, AI and outsourcing.','Its product Discrete Profile was presented at Web Summit 2024 in Portugal.']),
 dict(slug='old-studio-concept',a='Old Studio ',b='Concept',place='White-label',role='Sole administrator & Full Stack Developer',
  desc='White-label development. The studio is currently inactive.',products=[],badge=None,inactive=True,
  long=['Old Studio Concept is a white-label development studio, founded in 2016 and currently inactive.','Work covered PHP / Laravel / Symfony / Slim, e-commerce on WordPress and custom MVC, CI/CD deploys, Vue and React SPAs, and UI/UX.']),
 dict(slug='let-go-trading',a='Let Go ',b='Trading',place='White-label',role='Associate & Product Builder',
  desc='White-label products.',products=[],badge=None,
  long=['Let Go Trading builds white-label products.','My role: associate and product builder.']),
]
projects=[
 dict(slug='valconf',name='ValConf',tag='Website · Editorial',cat='Website',
  line='Website for a premium apparel factory in Romania: editorial design, full-screen video hero.',
  facts=[('Type','Website'),('Client','Premium apparel factory'),('Country','Romania'),('Design','Editorial')],
  paras=['A website for a premium apparel factory in Romania.','The design is editorial, built around a full-screen video hero.'],
  feats=['Editorial design','Full-screen video hero','Premium apparel factory, Romania']),
 dict(slug='privasee360',name='Privasee360',tag='Website · 3D',cat='Website',
  line='Website for an AI-era data privacy / GDPR software product, with an interactive 3D robot mascot.',
  facts=[('Type','Website'),('Product','Data privacy / GDPR software'),('Context','AI era'),('Feature','Interactive 3D mascot')],
  paras=['A website for an AI-era data privacy / GDPR software product.','It features an interactive 3D robot mascot.'],
  feats=['Data privacy / GDPR','AI-era product','Interactive 3D robot mascot']),
 dict(slug='luce-2025-shop',name='Luce 2025 Shop',tag='E-commerce · WooCommerce',cat='E-commerce',
  line='Official shop for the Vatican Jubilee 2025 mascot: international e-commerce on WooCommerce with custom design.',
  facts=[('Type','E-commerce'),('Platform','WooCommerce'),('Reach','International'),('Design','Custom')],
  paras=['The official shop for the Vatican Jubilee 2025 mascot.','International e-commerce on WooCommerce with a custom design.'],
  feats=['Official Jubilee 2025 mascot shop','International e-commerce','WooCommerce, custom design']),
 dict(slug='anteco-brun',name='Anteco Brun',tag='CRM · AI',cat='CRM',
  line='CRM for stock and product transformation with AI task automation.',
  facts=[('Type','CRM'),('Domain','Stock & product transformation'),('Automation','AI tasks'),('—','')],
  paras=['A CRM for stock and product transformation.','It includes AI task automation.'],
  feats=['Stock management','Product transformation','AI task automation']),
 dict(slug='nextservice',name='NextService',tag='Platform · Nuxt + Laravel',cat='Platform',
  line='Nuxt + Laravel service platform: REST API, customer flows, admin tooling, auth and role-based access. My own product.',
  facts=[('Type','Service platform'),('Frontend','Nuxt'),('Backend','Laravel'),('Ownership','My own product')],
  paras=['A service platform built with Nuxt and Laravel.','It covers a REST API, customer flows, admin tooling, and auth with role-based access. This is my own product.'],
  feats=['REST API','Customer flows & admin tooling','Auth & role-based access']),
 dict(slug='liveflow-academy',name='LiveFlow Academy',tag='Marketplace · Nuxt 4',cat='Marketplace',
  line='Udemy-style course marketplace in Nuxt 4 + TypeScript with SSR, catalog and search, checkout, learner dashboard.',
  facts=[('Type','Course marketplace'),('Stack','Nuxt 4 + TypeScript'),('Rendering','SSR'),('Venture','LiveFlow')],
  paras=['A Udemy-style course marketplace built in Nuxt 4 and TypeScript with SSR.','It includes a catalog with search, checkout, and a learner dashboard.'],
  feats=['Catalog & search','Checkout','Learner dashboard']),
]
DP_POINTS=['An SDK that builds user profiles locally with machine learning','No server-side profile storage','GDPR by design','Targeting rules updated in real time from a control panel']
rd=[
 dict(slug='utilitara',name='Utilitara',st=['POC','AI'],desc='A free, complete PDF toolkit in the spirit of iLovePDF, plus AI features: summaries and chat with PDFs.'),
 dict(slug='one-cool-hub',name='One Cool Hub',st=['POC'],desc='My own product: WordPress and Shopify plugins with a CMS per plugin, analytics and automation.'),
 dict(slug='nextservice',name='NextService',st=['POC'],desc='Nuxt + Laravel service platform: REST API, customer flows, admin tooling, auth and role-based access.'),
 dict(slug='carpat',name='carpat',st=['POC'],desc='A toolkit for Romanian forms: CNP, CUI, IBAN, phone and ID validators, plus Vue 3, React and Svelte components on a zero-dependency core.'),
 dict(slug='acttrace',name='ActTrace',st=['POC'],desc='A zero-config browser library that correlates DOM events, network calls and DOM mutations into one readable console trace per user interaction.'),
 dict(slug='ai-lead-generation',name='AI-Powered Lead Generation & Outreach Platform',st=['POC','AI'],desc='A Python crawling engine plus a LangGraph AI agent layer for prospecting and outreach.'),
 dict(slug='discrete-profile',name='Discrete Profile',st=['On market','AI'],desc='The first on-device marketing platform: an SDK that builds user profiles locally with machine learning.'),
]
posts=[
 dict(slug='a1',url='blog.html#a1',n='01',tag='Privacy · ML',title='How on-device ML changes privacy-first marketing',
  ex='Most marketing profiles live on a server, collecting more than they need. Building them on the device with machine learning flips that model: personalization stays local, and privacy becomes a design choice instead of a patch.'),
 dict(slug='a2',url='blog.html#a2',n='02',tag='AI · R&D',title='From idea to POC in days with AI-assisted development',
  ex='AI-assisted development shortens the path from a rough idea to something you can click through. Here is the workflow I use: design the system first, then let AI help me build the prototype fast.'),
 dict(slug='a3',url='blog.html#a3',n='03',tag='R&D · Tools',title='What I learned building carpat and ActTrace',
  ex='carpat and ActTrace both started as small itches: repetitive validation code and unreadable browser consoles. Building them taught me a lot about scope, sensible defaults and keeping a core dependency-free.'),
 dict(slug='options-api-nuxt',url='blog/options-api-nuxt.html',n='04',tag='Nuxt · Vue',title='Structuring a Nuxt project with the Options API',
  ex='The Options API still gives a Nuxt project a clear, predictable shape. Here is how I organize pages, components and data so the codebase stays easy to read and test.'),
]
SKILLS=['Vue.js','Nuxt','TypeScript','JavaScript','React','Tailwind','Laravel','PHP','Python','LangGraph','Node.js','Vitest','Jest','Cypress','Detox','GitLab CI','Azure','MySQL / MariaDB / MongoDB / Firebase']
def badges(st):
    m={'POC':'poc','AI':'ai','On market':'mk','Idea':''}
    return '<div class="bd">'+''.join(f'<span class="{m[s]}">{s}</span>' for s in st)+'</div>'
def h3(v): return f'{e(v["a"])}<em>{e(v["b"])}</em>'

# ---------------- index ----------------
def vcard(i,v):
    pr=''.join(f'<span>{e(x)}</span>' for x in v['products'])
    bd=f'<span class="bdg">◆ {e(v["badge"])}</span>' if v['badge'] else ('<span class="bdg in">Inactive</span>' if v.get('inactive') else '')
    return (f'<a class="vc{" l" if v.get("lime") else ""}" href="ventures/{v["slug"]}.html"><div class="top"><span>Venture 0{i+1}</span><span>{e(v["place"])}</span></div>'
     f'<h3>{h3(v)}</h3><div class="role">{e(v["role"])}</div><p class="desc">{e(v["desc"])}</p>'
     +(f'<div class="pr">{pr}</div>' if pr else '')+f'<div class="foot">{bd or "<span></span>"}<span class="go">View venture →</span></div></a>')
def prow(i,p):
    return (f'<a class="row" href="projects/{p["slug"]}.html"><span class="i">P/0{i+1}</span><div class="main"><h3>{e(p["name"])}</h3><p>{e(p["line"])}</p></div>'
            f'<span class="t">{e(p["tag"])}</span><span class="go">View project →</span></a>')
def lcard(r):
    return f'<a class="lc" href="rd/{r["slug"]}.html">{badges(r["st"])}<h4>{e(r["name"])}</h4><p>{e(r["desc"])}</p></a>'
def acard(p):
    return (f'<a class="ar" href="{p["url"]}"><div class="th"><b>{p["n"]}</b><span>{e(p["tag"])}</span></div><div class="m">Article</div><h4>{e(p["title"])}</h4><p>{e(p["ex"])}</p></a>')

code_js=re.search(r'<script>\nconst src=.*?tick\(\);\n</script>',v5,re.S).group(0)
new_src=r"""const src=[['c','<!-- AlexMosneagu.vue -->'],['','\n<'],['t','script'],['','>\nexport default {\n  name: '],['s',"'AlexMosneagu'"],['',',\n  data() {\n    return {\n      role: '],['s',"'Frontend Tech Lead'"],['',',\n      years: '],['s',"'9+'"],['',',\n      city: '],['s',"'Bucharest'"],['',",\n      stack: ['Vue', 'Nuxt', 'TS', 'React']\n    }\n  },\n  computed: {\n    focus() { return "],['s',"'full stack'"],['',' }\n  },\n  methods: {\n    ship(idea) { '],['c','// idea → POC → market'],['','\n      return this.build(idea) }\n  }\n}\n</'],['t','script'],['','>']];"""
code_js=re.sub(r"const src=.*?\]\];",lambda m:new_src,code_js,count=1,flags=re.S)

idx=head('Alex Mosneagu — Frontend Tech Lead & Full Stack Developer','')+nav('',True)+f'''
<header class="hero" id="top"><div id="gl"></div><div class="wrap">
 <div class="hgrid"><div>
  <h1>Full stack.<br>Tech <em>lead.</em></h1>
  <p>Frontend Tech Lead and full stack developer with 9+ years of Vue, Nuxt, TypeScript and React. I build products, and R&amp;D prototypes on the side.</p>
  <div class="ctas"><a class="pill pri" href="#work">See my work →</a><a class="pill sec" href="blog.html">Read the blog</a></div>
 </div>
 <div class="code"><div class="bar"><i></i><i></i><i></i><span>AlexMosneagu.vue</span></div><pre id="code"></pre></div></div>
 <div class="meta"><span>Based in <b>Bucharest, RO</b></span><span>Stack <b>Vue · Nuxt · TS · React · Tailwind</b></span><span>Shown at <b>Web Summit 2024 · We Make Future 2026</b></span><span>Scroll <b>↓</b></span></div>
</div></header>

<div class="mq"><div>Vue <em>·</em> Nuxt <em>·</em> TypeScript <em>·</em> React <em>·</em> Tailwind <em>·</em> Tech leadership <em>·</em> R&amp;D <em>·</em> Vue <em>·</em> Nuxt <em>·</em> TypeScript <em>·</em> React <em>·</em> Tailwind <em>·</em> Tech leadership <em>·</em> R&amp;D <em>·</em></div></div>

<div class="wrap"><div class="stats">
 <div class="stat"><div class="n">9<sup>+</sup></div><div class="l">Years experience</div></div>
 <div class="stat"><div class="n">4</div><div class="l">Ventures</div></div>
 <div class="stat"><div class="n sm">Web Summit<br><em class="lime">2024 · Portugal</em></div><div class="l">Presented at</div></div>
 <div class="stat"><div class="n sm">We Make Future<br><em class="lime">2026</em></div><div class="l">Showcased at</div></div>
</div></div>

<section id="about"><div class="wrap">
 {sh('about','01','Code that <em>ships.</em><br>Teams that scale.','Frontend Tech Lead &amp; full stack developer.')}
 <div class="about"><div><p><strong>9+ years</strong> building for the web, from custom PHP platforms and e-commerce to modern SPAs. <strong>Technical Lead Frontend at HCLTech</strong> since Jan 2025, working on frontend architecture, code standards and testing strategy.</p>
 <p style="margin-top:22px">I care about <strong>clean, typed, well-tested code</strong>. I'm constantly in R&amp;D mode: prototypes, frontend observability, browser-native tooling and AI agents with LangGraph. I design systems first, then build fast with AI-assisted development. I ran my own studio for years.</p></div>
 <div class="sk"><div class="on">Frontend architecture<span>HCLTech</span></div><div>Code standards<span>reviews &amp; typing</span></div><div>Testing strategy<span>unit &amp; E2E</span></div><div>R&amp;D &amp; AI agents<span>LangGraph</span></div><div>Languages<span>Romanian · Italian · English</span></div></div></div>
 <div class="chips">{''.join(f'<span class="{"f" if s in ("Vue.js","Nuxt","TypeScript","React") else ""}">{e(s)}</span>' for s in SKILLS)}</div>
</div></section>

<section id="ventures" style="padding-top:40px"><div class="wrap">{sh('ventures','02','Ventures<br><em>I\'m part of.</em>','Four ventures, each with its own role. Drag / scroll →')}</div>
 <div class="hs">
  {''.join(vcard(i,v) for i,v in enumerate(ventures))}
 </div>
</section>

<section id="work"><div class="wrap">{sh('work','03','Selected <em>projects.</em>','Websites, e-commerce and platforms.')}
 {''.join(prow(i,p) for i,p in enumerate(projects))}
</div></section>

<section id="rd"><div class="wrap">{sh('r&amp;d','04','R&amp;D <em>Lab.</em>','Experiments from idea to proof of concept to market.')}
 <a class="prod" href="rd/discrete-profile.html" style="color:inherit"><div><div class="bd"><span class="mk">On market</span><span class="ai">AI</span></div><h3>Discrete <em>Profile</em></h3>
  <p class="lead">The first on-device marketing platform. An SDK that builds user profiles locally with machine learning.</p><span class="more">Read more →</span></div>
  <ul>{''.join(f'<li>{e(x)}</li>' for x in DP_POINTS)}<li>Presented at Web Summit 2024</li></ul></a>
 <div class="lab">{''.join(lcard(r) for r in rd if r['slug']!='discrete-profile')}</div>
</div></section>

<section id="journey"><div class="wrap">{sh('journey','05','The <em>journey.</em>','9+ years, from custom PHP to modern SPAs.')}
 <div class="tl">
  <div class="it now"><div class="when">Jan 2025 – Present</div><h3>Technical Lead<br><em>HCLTech</em></h3><ul><li>Own frontend architecture and technical decisions</li><li>Code standards, review practices, testing strategy (unit and E2E)</li><li>Collaborate with product and backend</li><li>Guide developers</li></ul></div>
  <div class="it"><div class="when">Jun 2023 – Feb 2025</div><h3>Frontend Developer<br><em>Spark Radiance</em></h3><ul><li>Vue.js apps and reusable components</li><li>Performance and UX</li><li>Unit and E2E tests</li><li>CI/CD</li></ul></div>
  <div class="it"><div class="when">2016 – now inactive</div><h3>Founder &amp; Full-Stack Developer<br><em>Old Studio Concept</em></h3><ul><li>PHP / Laravel / Symfony / Slim</li><li>E-commerce on WordPress and custom MVC</li><li>CI/CD deploys</li><li>Vue and React SPAs, UI/UX</li></ul></div>
  <div class="it"><div class="when">2019 – 2022<small>Education</small></div><h3>Computer Science<br><em>Titu Maiorescu University</em></h3><ul></ul></div>
 </div>
</div></section>

<section id="writing"><div class="wrap">{sh('blog','06','Latest <em>articles.</em>','Notes on frontend, R&amp;D and AI-assisted development.')}
 <div class="art">{''.join(acard(p) for p in posts)}</div>
 <div class="ctas" style="margin-top:50px"><a class="pill sec" href="blog.html">All articles →</a></div>
</div></section>
'''+footer('')+code_js+'\n'+THREE+'</body></html>\n'
(R/'index.html').write_text(idx)

# ---------------- subpage template ----------------
def crumb(p,section,sid,cur):
    return f'<div class="crumb"><a href="{p}index.html">Home</a><span>/</span><a href="{p}index.html#{sid}">{section}</a><span>/</span><span>{e(cur)}</span></div>'
def page(title,p,body): return head(title+' — Alex Mosneagu',p)+nav(p)+body+footer(p)+'</body></html>\n'

def project_page(i,pr):
    P='../'
    prev=projects[i-1]; nxt=projects[(i+1)%len(projects)]
    facts=''.join(f'<div><span>{e(k)}</span><b>{e(v)}</b></div>' for k,v in pr['facts'] if k!='—')
    # facts: pad to 4 w/ category
    nf=len([1 for k,v in pr['facts'] if k!='—'])
    if nf<4: facts+='<div><span>Category</span><b>'+e(pr['cat'])+'</b></div>'
    feats=''.join(f'<div><span>0{j+1}</span><h4>{e(f)}</h4></div>' for j,f in enumerate(pr['feats']))
    frame=''
    if pr['slug']=='valconf':
        frame='<div class="frame"><div class="bar"><i></i><i></i><i></i><span>ValConf — hero</span></div><div class="vid"><div class="play">▶</div><h5>Val<em>Conf</em></h5><small>Full-screen video hero · Editorial design</small></div></div>'
    body=f'''<header class="ph" id="top"><div class="glow"></div><div class="wrap">{crumb(P,'Work','work',pr['name'])}
 <div class="bd"><span class="ai">{e(pr['cat'])}</span></div><h1>{e(pr['name'])}</h1><p class="lead">{e(pr['line'])}</p>
 <div class="facts">{facts}</div>{frame}</div></header>
<section class="sx"><div class="wrap"><div class="txt"><div class="idx">// overview<b>01</b></div><div class="body">{''.join(f'<p>{e(x)}</p>' for x in pr['paras'])}</div></div></div></section>
<section class="sx"><div class="wrap"><div class="txt"><div class="idx">// highlights<b>02</b></div><div><div class="feat" style="margin-top:0">{feats}</div></div></div>
 <div class="pn"><a href="{prev['slug']}.html"><span>← Previous</span><b>{e(prev['name'])}</b></a><a href="{nxt['slug']}.html"><span>Next →</span><b>{e(nxt['name'])}</b></a></div></div></section>
'''
    (R/'projects'/f'{pr["slug"]}.html').write_text(page(pr['name'],P,body))
for i,pr in enumerate(projects): project_page(i,pr)

def venture_page(i,v):
    P='../'
    nxt=ventures[(i+1)%len(ventures)]; prev=ventures[i-1]
    facts=[('Role',v['role']),('Country' if v['place']=='Italy' else 'Type',v['place']),('Status','Inactive') if v.get('inactive') else ('Venture',f'0{i+1} of 04')]
    if v['products']: facts.append(('Products',' · '.join(v['products'])))
    elif v['badge']: facts.append(('Showcased',v['badge']))
    else: facts.append(('Focus',v['desc'].rstrip('.').replace(' The studio is currently inactive','')))
    fh=''.join(f'<div><span>{e(k)}</span><b>{e(x)}</b></div>' for k,x in facts)
    bd=(f'<span class="bdg" style="margin-top:26px">◆ {e(v["badge"])}</span>' if v['badge'] else ('<span class="bdg in" style="margin-top:26px">Inactive</span>' if v.get('inactive') else ''))
    prods=''
    if v['products']:
        cards=''.join(f'<a class="lc" href="{"../rd/discrete-profile.html" if x=="Discrete Profile" else "liveflow-academy-na"}"><div class="bd"><span class="mk">Product</span></div><h4>{e(x)}</h4></a>' if x=='Discrete Profile' else
                      (f'<a class="lc" href="../projects/liveflow-academy.html"><div class="bd"><span class="mk">Product</span></div><h4>{e(x)}</h4></a>' if x=='LiveFlow Academy' else f'<div class="lc"><div class="bd"><span class="mk">Product</span></div><h4>{e(x)}</h4></div>') for x in v['products'])
        prods=f'<section class="sx"><div class="wrap"><div class="txt"><div class="idx">// products<b>02</b></div><div><div class="pcards" style="margin-top:0">{cards}</div></div></div></div></section>'
    body=f'''<header class="ph" id="top"><div class="glow"></div><div class="wrap">{crumb(P,'Ventures','ventures',v['name'] if 'name' in v else v['a']+v['b'])}
 <div class="bd"><span class="ai">Venture 0{i+1}</span></div><h1>{e(v["a"])}<em>{e(v["b"])}</em></h1><p class="lead">{e(v["desc"])}</p>{bd}
 <div class="facts">{fh}</div></div></header>
<section class="sx"><div class="wrap"><div class="txt"><div class="idx">// about<b>01</b></div><div class="body">{''.join(f'<p>{e(x)}</p>' for x in v['long'])}</div></div></div></section>
{prods}
<section class="sx"><div class="wrap"><div class="pn"><a href="{prev['slug']}.html"><span>← Previous</span><b>{e(prev['a']+prev['b'])}</b></a><a href="{nxt['slug']}.html"><span>Next →</span><b>{e(nxt['a']+nxt['b'])}</b></a></div></div></section>
'''
    (R/'ventures'/f'{v["slug"]}.html').write_text(page(v['a']+v['b'],P,body))
for i,v in enumerate(ventures): venture_page(i,v)

def rd_page(i,r):
    P='../'
    prev=rd[i-1]; nxt=rd[(i+1)%len(rd)]
    paras=[r['desc']]
    extra=''
    if r['slug']=='discrete-profile':
        paras=['The first on-device marketing platform: an SDK that builds user profiles locally with machine learning.','Presented at Web Summit 2024.']
        extra='<section class="sx"><div class="wrap"><div class="txt"><div class="idx">// how it works<b>02</b></div><div><div class="feat" style="margin-top:0;grid-template-columns:repeat(2,1fr)">'+''.join(f'<div><span>0{j+1}</span><h4>{e(x)}</h4></div>' for j,x in enumerate(DP_POINTS))+'</div></div></div></div></section>'
    facts=[('Status',' · '.join(r['st'])),('Type','Product' if r['slug']=='discrete-profile' else 'R&D project'),('Section','R&D Lab')]
    fh=''.join(f'<div><span>{e(k)}</span><b>{e(x)}</b></div>' for k,x in facts)
    name=e(r['name'])
    body=f'''<header class="ph" id="top"><div class="glow"></div><div class="wrap">{crumb(P,'R&amp;D','rd',r['name'])}
 {badges(r['st'])}<h1 style="font-size:clamp(44px,{'6' if len(r['name'])>20 else '9'}vw,{'96' if len(r['name'])>20 else '148'}px)">{name}</h1><p class="lead">{e(r['desc'])}</p>
 <div class="facts" style="grid-template-columns:repeat(3,1fr)">{fh}</div></div></header>
<section class="sx"><div class="wrap"><div class="txt"><div class="idx">// overview<b>01</b></div><div class="body">{''.join(f'<p>{e(x)}</p>' for x in paras)}</div></div></div></section>
{extra}
<section class="sx"><div class="wrap"><div class="pn"><a href="{prev['slug']}.html"><span>← Previous</span><b>{e(prev['name'])}</b></a><a href="{nxt['slug']}.html"><span>Next →</span><b>{e(nxt['name'])}</b></a></div></div></section>
'''
    (R/'rd'/f'{r["slug"]}.html').write_text(page(r['name'],P,body))
for i,r in enumerate(rd): rd_page(i,r)

# ---------------- blog index ----------------
def brow(p):
    live=p['slug']=='options-api-nuxt'
    return (f'<a class="brow" id="{p["slug"] if not live else "a4"}" href="{p["url"] if live else "#"+p["slug"]}"><span class="i">{p["n"]}</span><div><h3>{e(p["title"])}</h3><p>{e(p["ex"])}</p></div>'
            f'<span class="t">{e(p["tag"])}</span><span class="go{"" if live else " s"}">{"Read article →" if live else "Coming soon"}</span></a>')
blog=f'''<header class="ph" id="top"><div class="glow"></div><div class="wrap">{'<div class="crumb"><a href="index.html">Home</a><span>/</span><span>Blog</span></div>'}
 <div class="idx" style="font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--lime)">// blog</div><h1>Notes &amp; <em>articles.</em></h1><p class="lead">Writing about frontend, R&amp;D and AI-assisted development.</p></div></header>
<section style="padding:20px 0 60px"><div class="wrap">{''.join(brow(p) for p in posts)}</div></section>
'''
(R/'blog.html').write_text(head('Blog — Alex Mosneagu','')+nav('')+blog+footer('')+'</body></html>\n')

# ---------------- article ----------------
def code(s):
    s=e(s)
    return s
art='''<header class="ph art-h" id="top"><div class="glow"></div><div class="wrap"><div class="crumb"><a href="../index.html">Home</a><span>/</span><a href="../blog.html">Blog</a><span>/</span><span>Options API in Nuxt</span></div>
 <div class="bd"><span class="ai">Nuxt · Vue</span></div><h1>Structuring a Nuxt project with the <em>Options API.</em></h1><p class="lead">A practical layout for pages, components and logic that stays readable and easy to test.</p></div></header>
<article class="post">
<p>The Composition API gets most of the attention, but the Options API still works very well in Nuxt, especially on teams where many people touch the same code. Its biggest advantage is predictability: every component has the same shape.</p>
<h2>Start with the folders</h2>
<p>Keep Nuxt's conventions and add a little structure on top. Pages stay thin and only compose components. Reusable logic lives in <code>composables/</code>, and domain types in <code>types/</code>.</p>
<pre>pages/        // routes, thin
components/   // UI, one folder per feature
composables/  // shared logic (useCurrency, useAuth)
types/        // TypeScript interfaces</pre>
<h2>One order for every component</h2>
<p>Pick an order for the options and never break it: <code>name</code>, <code>props</code>, <code>emits</code>, <code>setup</code>, <code>data</code>, <code>computed</code>, <code>watch</code>, <code>methods</code>, then lifecycle hooks. Reviewers always know where to look.</p>
<pre><span class="t">export default</span> defineComponent({
  name: <span class="s">'ProductCard'</span>,
  props: { product: { type: Object <span class="t">as</span> PropType&lt;Product&gt;, required: <span class="t">true</span> } },
  emits: [<span class="s">'select'</span>],
  setup() {
    <span class="t">const</span> { format } = useCurrency()
    <span class="t">return</span> { format }
  },
  data() { <span class="t">return</span> { expanded: <span class="t">false</span> } },
  computed: {
    price(): string { <span class="t">return</span> this.format(this.product.price) }
  },
  methods: {
    toggle() { this.expanded = !this.expanded }
  }
})</pre>
<h2>Share logic with composables</h2>
<p>Options API does not mean giving up composables. Call them in <code>setup()</code> and return what the template needs. You keep the readable options layout while reusing the same logic as the rest of the app.</p>
<h2>Keep it testable</h2>
<p>Keep methods small and move anything non-trivial into plain functions or composables. With Vitest you can test those directly, and mount the component only to check what it renders and emits. Cypress then covers the full flow.</p>
<p>The result is a codebase where new developers find things quickly and reviews focus on behavior, not on style.</p>
<div class="end"><a href="../blog.html">← Back to blog</a><a href="#top">Back to top ↑</a></div>
</article>
'''
(R/'blog'/'options-api-nuxt.html').write_text(head('Structuring a Nuxt project with the Options API — Alex Mosneagu','../')+nav('../')+art+'<div style="height:100px"></div>'+footer('../')+'</body></html>\n')
print('ok')
