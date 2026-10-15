from playwright.sync_api import sync_playwright
from PIL import Image;import io
R="/workspace/mockup-v6/";base="file://"+R
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
    u=base+"index.html?static"
    pg=b.new_page(viewport={"width":1440,"height":900});pg.goto(u,wait_until="networkidle");pg.evaluate("document.fonts.ready");pg.wait_for_selector("body[data-gl=ok]",state="attached",timeout=20000);pg.wait_for_timeout(1500)
    pg.screenshot(path=R+"desktop-hero.png")
    def chunked(pg,w,scale,path):
        H=pg.evaluate("document.documentElement.scrollHeight");out=Image.new("RGB",(w*scale,H*scale));y=0
        while y<H:
            h=min(2000,H-y);out.paste(Image.open(io.BytesIO(pg.screenshot(full_page=True,clip={"x":0,"y":y,"width":w,"height":h}))),(0,y*scale));y+=h
        out.save(path)
    chunked(pg,1440,1,R+"desktop-full.png")
    print("fonts",pg.evaluate("[document.fonts.check('40px Instrument Serif'),document.fonts.check('16px Inter Tight'),document.body.dataset.gl]"))
    print("hscroll desktop",pg.evaluate("[document.documentElement.scrollWidth,innerWidth,document.querySelector('.hs').scrollLeft]"))
    m=b.new_page(viewport={"width":390,"height":844},device_scale_factor=2);m.goto(u,wait_until="networkidle");m.wait_for_selector("body[data-gl=ok]",state="attached",timeout=20000);m.wait_for_timeout(1500)
    print("hscroll mobile",m.evaluate("[document.documentElement.scrollWidth,innerWidth,document.querySelector('.hs').scrollLeft]"))
    chunked(m,390,2,R+"mobile.png")
    for name,path in [("project-valconf.png","projects/valconf.html"),("blog.png","blog.html"),("article.png","blog/options-api-nuxt.html"),("venture-devolution.png","ventures/devolution-zone.html"),("rd-discrete.png","rd/discrete-profile.html")]:
        q=b.new_page(viewport={"width":1440,"height":900});q.goto(base+path,wait_until="networkidle");q.wait_for_timeout(800);chunked(q,1440,1,R+name)
        print(name,q.evaluate("[document.documentElement.scrollWidth,innerWidth]"))
    b.close()
