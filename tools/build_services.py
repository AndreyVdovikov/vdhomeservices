#!/usr/bin/env python3
"""Generates /services/<slug>/index.html pages, shared nav/footer snippets and sitemap.xml.
Run from the repo root:  python3 tools/build_services.py
"""
import os, json, html

DOMAIN = 'https://andrewhandy.com'
PHONE_DISPLAY = '(656) 231-1836'
PHONE_TEL = '+16562311836'
VER = '20261105c'   # bump to bust browser cache of site.css/site.js
AREAS = ["Wesley Chapel", "Land O' Lakes", "Zephyrhills", "Dade City", "New Tampa", "Lutz", "Odessa", "Tampa"]
AREAS_TXT = "Wesley Chapel, Land O' Lakes, Zephyrhills, Dade City, New Tampa, Lutz, Odessa"

S = [
 dict(slug='tv-shelf-mounting', name='TV, Shelf & Curtain Rod Mounting', short='TV & Shelf Mounting', h1='TV, Shelf & Curtain Rod Mounting', icon='tv.png', photo=None,
  desc="TV mounting, shelf and curtain rod installation in Wesley Chapel, FL and nearby. Level, secure and clean. Call Andrew Handyman Services for a free estimate.",
  lead="Wall-mounting done level, secure and clean. I mount TVs, shelves, curtain rods, mirrors and other interior items for homeowners in Wesley Chapel and the surrounding Tampa Bay area.",
  bullets=["TV mounting with fixed, tilting or full-motion brackets","Floating shelves and heavy-duty shelving, anchored into studs or rated anchors","Curtain rods, blinds and drapery hardware","Mirrors, art and picture frames hung level","Soundbars and other small wall-mounted items","Neat finish: cord covers and a clean work area when I leave"],
  faq=[("Do I need to buy the mount myself?","You can supply your own bracket, or I can point you to a mount that fits your TV and wall. I confirm everything before I start so there are no surprises."),
       ("Can you mount a TV on any wall?","Most drywall, brick and stucco walls work well. I check what is behind the wall first and tell you upfront if a wall is not a good fit."),
       ("How long does it take?","A standard TV mount is usually done within an hour or two. Shelves and curtain rods are quicker, and larger jobs are quoted ahead of time.")],
  related=['media-accent-walls','drywall-repair','painting']),
 dict(slug='drywall-repair', name='Drywall Repair', short='Drywall Repair', h1='Drywall Repair', icon='drywall.svg', photo=None,
  desc="Drywall repair in Wesley Chapel, FL: holes, cracks, water damage and texture matching. Smooth, paint-ready results from Andrew Handyman Services.",
  lead="Holes, cracks, dents and water damage patched and finished so smoothly you will never know they were there. Serving homeowners in Wesley Chapel, Land O' Lakes, Zephyrhills and nearby.",
  bullets=["Holes from doorknobs, anchors and old TV mounts","Cracks and settling lines in walls and ceilings","Water-damaged sections cut out and replaced (after the leak is fixed)","Texture matching: orange peel, knockdown and smooth","Sanding, priming and a paint-ready finish","Ceiling patches and corner bead repair"],
  faq=[("Will the patch be visible afterwards?","I match the surrounding texture and prime the repair so it blends in. For a flawless look I can also paint the wall, so the repair disappears completely."),
       ("Can you fix water-damaged drywall?","Yes, once the source of the leak is repaired. I cut out the damaged section, patch and finish it. If I see an active leak or mold I will tell you before starting."),
       ("Do you paint after the repair?","Yes. Painting is available as part of the same visit, which saves you a second trip and a second appointment.")],
  related=['painting','wood-rot-repair','tv-shelf-mounting']),
 dict(slug='wood-rot-repair', name='Wood Rot & Damage Repair', short='Wood Rot Repair', h1='Wood Rot & Damage Repair', icon='wood.svg', photo=('img-06.jpg','Before and after repair of rotted wooden steps and railing'),
  desc="Rotted or damaged wood repair in Wesley Chapel, FL: trim, door and window frames, posts and steps. Andrew Handyman Services repairs it before it spreads.",
  lead="Florida humidity and summer rain are hard on wood. I repair or replace rotted and damaged wooden elements inside and outside your home before the damage spreads.",
  bullets=["Rotted trim, fascia boards and exterior siding sections","Door frames, jambs and window casings","Porch posts, railings and wooden steps","Wood filler and hardener for small damaged areas","Full board replacement where repair is not enough","Primed and painted to match so the repair is protected"],
  faq=[("Do you repair or replace rotted wood?","Small damaged spots can often be repaired. When the wood is too far gone I replace the board. I show you what I find and explain which option makes sense."),
       ("Why does wood rot so quickly in Florida?","Constant humidity, heavy summer rain and unprotected end grain let moisture into the wood. Proper sealing and paint after the repair is what stops it from coming back."),
       ("Can you repair damage on my deck or stairs?","Yes. Rotted deck boards, stair treads and railings are common repairs. Larger structural work may need a permit and I will tell you upfront.")],
  related=['deck-repair','fence-repair','painting']),
 dict(slug='painting', name='Interior & Exterior Painting', short='Painting', h1='Interior & Exterior Painting', icon='painting.svg', photo=None,
  desc="Interior and exterior painting in Wesley Chapel, FL: walls, ceilings, trim and doors with crisp lines and careful prep. Free estimates from Andrew Handyman Services.",
  lead="Walls, ceilings, trim and exteriors painted with careful prep, crisp lines and a clean finish. I paint homes and rooms for customers in Wesley Chapel and nearby neighborhoods.",
  bullets=["Interior walls, ceilings, trim and baseboards","Doors, door frames and accent walls","Exterior walls, stucco and trim","Prep done right: patching, caulking and priming","Floors and furniture protected, tidy cleanup","Color advice if you are not sure what to pick"],
  faq=[("Do you move furniture and cover the floors?","I protect floors and furniture and tape off edges. If you can clear small items beforehand it helps, and I handle the rest."),
       ("Can you paint in Florida heat and humidity?","Yes. Exterior work is planned around weather and surface moisture so the paint cures properly and lasts."),
       ("Who supplies the paint?","Either way works. You can pick the paint yourself or I can recommend a quality product for the surface and give you an exact estimate.")],
  related=['cabinet-painting-renovation','drywall-repair','wood-rot-repair']),
 dict(slug='cabinet-painting-renovation', name='Cabinet Painting & Renovation', short='Cabinet Painting', h1='Cabinet Painting & Renovation', icon='cabinets.svg', photo=('img-04.jpg','Kitchen cabinets before and after renovation'),
  desc="Kitchen and whole-house cabinet painting and renovation in Wesley Chapel, FL. A fresh new look without the cost of full replacement. Andrew Handyman Services.",
  lead="Give your kitchen or whole house a fresh look without paying for full replacement. I paint and renovate cabinets for homeowners in Wesley Chapel, Land O' Lakes, Zephyrhills and nearby.",
  bullets=["Kitchen cabinet painting with proper cleaning, sanding and priming","Bathroom vanities and whole-house cabinets","New hardware, hinges and soft-close upgrades","Door and drawer-front repairs and adjustments","Cabinet box repairs and touch-ups","Smooth, durable finish that is made for daily use"],
  faq=[("Is painting better than replacing cabinets?","If your cabinet boxes are solid, painting or renovating is usually far less expensive and still changes the whole look of the room. I will tell you honestly if replacement is the better choice."),
       ("How long does a cabinet job take?","Most kitchens take several days, because each coat needs time to dry and cure. I give you a clear schedule before I start."),
       ("Can you change the hardware too?","Yes. New handles, knobs and hinges are a quick upgrade that makes painted cabinets look brand new.")],
  related=['new-kitchen-installation','painting','drywall-repair']),
 dict(slug='new-kitchen-installation', name='New Kitchen Installation', short='New Kitchen', h1='New Kitchen Installation', icon='kitchen.svg', photo=('img-08.jpg','New kitchen installed by Andrew Handyman Services'),
  desc="New kitchen installation in Wesley Chapel, FL: cabinets, countertops, backsplash and finishing. Andrew Handyman Services handles your kitchen remodel start to finish.",
  lead="Full kitchen remodels handled start to finish: old cabinets out, new cabinets in, countertops, backsplash and finishing touches. Serving Wesley Chapel and the surrounding area.",
  bullets=["Removal of old cabinets and countertops","New cabinet installation, level, plumb and secure","Countertop installation and cutouts","Tile backsplash","Trim, paint and finishing details","Handles, hardware and final adjustments"],
  faq=[("Do you handle plumbing and electrical in a kitchen remodel?","I take care of cabinets, countertops, backsplash and finishing. Work that legally requires a licensed plumber or electrician is not part of my service, but I can tell you exactly what to line up so the schedule stays smooth."),
       ("Do I need to buy the cabinets myself?","You can choose your own cabinets, or I can help you plan a layout and order. Either way I give you a written estimate before work starts."),
       ("How long does a kitchen installation take?","It depends on the size and the materials, and I give you a clear timeline in the estimate. Most of the work is done in the home, so I keep the area as clean and usable as possible.")],
  related=['cabinet-painting-renovation','painting','media-accent-walls']),
 dict(slug='hurricane-shutters', name='Hurricane Shutters', short='Hurricane Shutters', h1='Hurricane Shutters', icon='shutters.svg', photo=None,
  desc="Hurricane shutter installation in Wesley Chapel, FL: roll-down, accordion and motorized shutters. Be ready before storm season. Andrew Handyman Services.",
  lead="Be ready before the next storm. I install roll-down, accordion and motorized hurricane shutters to protect your windows and doors, for homes in Wesley Chapel and across Pasco and north Hillsborough.",
  bullets=["Roll-down hurricane shutters","Accordion shutters for windows, doors and lanais","Motorized shutter options","Careful measuring and secure mounting","Adjustments and repairs on existing shutters","Clear estimate before any work starts"],
  faq=[("Which type of shutter is right for my home?","It depends on your budget, how often you want to open and close them, and the openings you need to cover. I explain the options and give you a clear estimate for each one."),
       ("Do hurricane shutters need a permit?","Shutter projects often do. I walk you through what applies to your address before we start so there are no surprises."),
       ("When should I install them?","Atlantic hurricane season runs June 1 to November 30. Booking well before the season gives you the most choice and avoids the last-minute rush.")],
  related=['wood-rot-repair','painting','media-accent-walls']),
 dict(slug='media-accent-walls', name='Media & Accent Walls', short='Media & Accent Walls', h1='Media & Accent Walls', icon='media-wall.svg', photo=None,
  desc="Media walls, TV walls and custom accent walls in Wesley Chapel, FL. Wood slats, panels, fireplace surrounds and more from Andrew Handyman Services.",
  lead="A statement feature for your living room. I build and install TV walls, accent walls and fireplace surrounds designed around your space, in Wesley Chapel and nearby.",
  bullets=["TV and media walls with a clean built-in look","Wood slat, paneled and shiplap accent walls","Fireplace surrounds and feature walls","Custom designs planned around your room and TV","TV mounting with neat cord covers","Painted or stained to match your decor"],
  faq=[("Can you build a wall to my own design?","Yes. Bring a photo or an idea and I will tell you what is possible and give you a clear estimate. I can also suggest layouts that work well for your TV size."),
       ("Is the TV mount included?","I can mount the TV as part of the wall installation, so everything is level and lines up with the design."),
       ("How long does an accent wall take?","A simple accent wall can be finished in a day or two. Larger media walls take longer, and I give you a timeline in the estimate.")],
  related=['tv-shelf-mounting','painting','new-kitchen-installation']),
 dict(slug='deck-repair', name='Deck Repair', short='Deck Repair', h1='Deck Repair', icon='deck.svg', photo=('img-06.jpg','Before and after deck stairs and railing repair'),
  desc="Deck repair in Wesley Chapel, FL: replacement boards, railings, stairs and posts, plus staining and sealing. Make your deck safe again with Andrew Handyman Services.",
  lead="Loose, rotted or worn deck boards, railings and steps repaired so your deck is safe and good-looking again. Serving Wesley Chapel, Land O' Lakes, Zephyrhills and nearby.",
  bullets=["Replacement of rotted or cracked deck boards","Railings, balusters and handrails","Stair treads, risers and stringers","Posts and loose or failing connections","Staining and sealing to protect the wood","Safe, solid result you can trust to walk on"],
  faq=[("Is my deck safe to use?","If boards are soft, railings wobble or stairs feel loose, it is time for a repair. I check the structure and tell you honestly what needs to be fixed first."),
       ("Do deck repairs need a permit?","Small repairs usually do not, but larger structural work can. I tell you upfront what applies before we start."),
       ("Can you stain or seal the deck after repair?","Yes. Sealing or staining protects the wood from Florida sun and rain, and it makes the repair look uniform.")],
  related=['wood-rot-repair','fence-repair','painting']),
 dict(slug='fence-repair', name='Fence Repair', short='Fence Repair', h1='Fence Repair', icon='fence.svg', photo=('img-05.jpg','Fence before and after repair'),
  desc="Fence repair in Wesley Chapel, FL: broken pickets, leaning posts and damaged gates. Keep your yard secure with Andrew Handyman Services.",
  lead="Broken pickets, leaning posts and damaged gates fixed or replaced to keep your yard secure and your fence looking sharp. Serving Wesley Chapel and nearby communities.",
  bullets=["Broken or rotted pickets and panels replaced","Leaning or loose posts straightened and secured","Gate repair: hinges, latches and sagging gates","Rails and boards reinforced","Staining or painting to refresh the look","Storm damage cleanup and repair"],
  faq=[("Is it worth repairing my fence instead of replacing it?","If the posts are solid, repairing damaged sections is usually much cheaper than replacing the whole fence. I tell you honestly when a section or full replacement makes more sense."),
       ("Can you fix a gate that does not close properly?","Yes. Sagging gates, loose hinges and broken latches are quick repairs that make a big difference."),
       ("Do you repair storm damage?","Yes. After a storm I repair broken boards, damaged panels and leaning posts so your yard is secure again.")],
  related=['deck-repair','wood-rot-repair','painting']),
]
BY = {s['slug']: s for s in S}

def esc(t): return html.escape(t, quote=True)

ICON = lambda s: f"/images/services/{s['icon']}"

def nav_html():
    items = ''.join(f'<a href="/services/{s["slug"]}/"><img src="{ICON(s)}" alt="" width="26" height="26" loading="lazy"><span>{esc(s["name"])}</span></a>' for s in S)
    mob = ''.join(f'<a href="/services/{s["slug"]}/">{esc(s["name"])}</a>' for s in S)
    return f'''<!-- NAV -->
<nav id="nav">
  <a href="/" class="nav-logo">
    <div class="nav-logo-icon" style="background:none;box-shadow:none;width:44px;height:44px;border-radius:0;overflow:visible;">
      <img src="/images/img-01.png" alt="Andrew Handyman Logo" style="width:44px;height:44px;object-fit:contain;border-radius:0;">
    </div>
    <div class="nav-logo-text">Andrew Handyman<span>Wesley Chapel, FL</span></div>
  </a>
  <ul class="nav-links">
    <li class="nav-dd">
      <a href="/#services" class="nav-dd-toggle" aria-haspopup="true">Services <span class="nav-caret">&#9662;</span></a>
      <div class="nav-dd-menu">{items}</div>
    </li>
    <li><a href="/#reviews">Reviews</a></li>
    <li><a href="/#contact">Area</a></li>
    <li><a href="tel:{PHONE_TEL}" class="nav-call">📞 {PHONE_DISPLAY}</a></li>
  </ul>
  <button class="nav-burger" aria-label="Open menu" aria-expanded="false" aria-controls="navMobile"><span></span><span></span><span></span></button>
</nav>
<div class="nav-mobile" id="navMobile">
  <div class="nm-h">Services</div>
  <div class="nm-list">{mob}</div>
  <div class="nm-h">More</div>
  <div class="nm-list"><a href="/#reviews">Reviews</a><a href="/#contact">Service Area &amp; Contact</a></div>
  <a href="tel:{PHONE_TEL}" class="nm-call">📞 Call {PHONE_DISPLAY}</a>
</div>
'''

def footer_html():
    links = ''.join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in S)
    return f'''<!-- FOOTER -->
<footer>
  <div class="section-wrap">
    <div class="footer-grid">
      <div>
        <div class="f-brand">Andrew Handyman</div>
        <p class="f-tagline">Your trusted local handyman in Wesley Chapel, FL — quality work, honest pricing, always on time.</p>
        <p class="f-areas">Serving {AREAS_TXT} and nearby.</p>
      </div>
      <div>
        <div class="f-h">Services</div>
        <ul class="f-links f-two">{links}</ul>
      </div>
      <div>
        <div class="f-h">Contact</div>
        <div class="f-contact-row">📞 <a href="tel:{PHONE_TEL}" style="color:inherit;text-decoration:none">{PHONE_DISPLAY}</a></div>
        <div class="f-contact-row">📍 Wesley Chapel, FL 33544</div>
        <div class="f-contact-row">🕘 Opens 9 AM Tue–Sat</div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Andrew Handyman Services · Wesley Chapel, Florida</span>
      <a href="https://share.google/M3UsYRjfswcYytOnC" target="_blank" rel="noopener" class="f-badge" style="text-decoration:none">⭐ 4.7 · 26 Google Reviews</a>
    </div>
  </div>
</footer>
'''

def head(title, desc, url, extra=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#1a3a5c">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Andrew Handyman Services">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/images/img-02.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/site.css?v={VER}">
{extra}</head>
'''

def page(s):
    url = f'{DOMAIN}/services/{s["slug"]}/'
    title = f'{s["h1"]} in Wesley Chapel, FL | Andrew Handyman Services'
    ld = {"@context":"https://schema.org","@type":"Service","name":f'{s["h1"]} in Wesley Chapel, FL',"serviceType":s['h1'],
          "description":s['desc'],"url":url,
          "provider":{"@type":"HomeAndConstructionBusiness","name":"Andrew Handyman Services","telephone":"+1-656-231-1836","url":DOMAIN+"/"},
          "areaServed":[{"@type":"City","name":a} for a in AREAS]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":"Services","item":DOMAIN+"/#services"},
        {"@type":"ListItem","position":3,"name":s['h1'],"item":url}]}
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n<script type="application/ld+json">{json.dumps(bc)}</script>\n'
    bullets = ''.join(f'<li><span class="sp-check"></span><span>{esc(b)}</span></li>' for b in s['bullets'])
    if s['photo']:
        f, alt = s['photo']
        side = f'<figure class="sp-photo"><img src="/images/{f}" alt="{esc(alt)}" loading="lazy"><figcaption>Real job photo — before &amp; after</figcaption></figure>'
    else:
        side = f'<div class="sp-side-card"><img src="{ICON(s)}" alt="" width="96" height="96"><h3>Free estimate</h3><p>Tell me what you need and I will get back to you within a few hours.</p><a class="btn-cta" href="/#home">Request an estimate</a><a class="sp-call" href="tel:{PHONE_TEL}">or call {PHONE_DISPLAY}</a></div>'
    faq = ''.join(f'<details class="sp-q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in s['faq'])
    rel = ''.join(f'<a href="/services/{r}/" class="svc-card"><div class="svc-emoji"><img src="{ICON(BY[r])}" alt="" width="62" height="62" loading="lazy"></div><div class="svc-name">{esc(BY[r]["name"])}</div><span class="svc-more">Learn more →</span></a>' for r in s['related'])
    chips = ''.join(f'<span class="area-chip">{esc(a)}</span>' for a in AREAS)
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> <a href="/#services">Services</a> <span>›</span> {esc(s["short"])}</div>
      <h1 class="sp-h1">{esc(s["h1"])} in <em>Wesley Chapel, FL</em></h1>
      <p class="sp-lead">{esc(s["lead"])}</p>
      <div class="sp-actions">
        <a class="btn-cta" href="/#home">Get a free estimate</a>
        <a class="btn-ghost-cta" href="tel:{PHONE_TEL}">📞 {PHONE_DISPLAY}</a>
        <a class="btn-ghost-cta" href="sms:{PHONE_TEL}">💬 Text to book</a>
      </div>
      <a class="sp-rating" href="https://share.google/M3UsYRjfswcYytOnC" target="_blank" rel="noopener">⭐ 4.7 · 26 Google Reviews</a>
    </div>
    <div class="sp-hero-icon"><img src="{ICON(s)}" alt="{esc(s["h1"])}" width="150" height="150"></div>
  </div>
</section>

<section class="sp-sec">
  <div class="section-wrap sp-two">
    <div class="reveal">
      <div class="section-tag">What I do</div>
      <h2 class="section-title">{esc(s["h1"])} <em>done right</em></h2>
      <ul class="sp-list">{bullets}</ul>
      <p class="sp-note">Every job starts with a clear estimate, so you know the price before work begins.</p>
    </div>
    <div class="reveal">{side}</div>
  </div>
</section>

<section class="sp-sec sp-alt">
  <div class="section-wrap">
    <div class="reveal">
      <div class="section-tag">Why Andrew</div>
      <h2 class="section-title">A local handyman you can <em>count on</em></h2>
    </div>
    <div class="sp-why">
      <div class="sp-why-card reveal"><div class="wc-icon">📍</div><b>Locally based</b><p>I live in Wesley Chapel, so response is fast and travel is short.</p></div>
      <div class="sp-why-card reveal d1"><div class="wc-icon">💬</div><b>Honest estimates</b><p>Clear pricing before the work starts. No surprises on the final bill.</p></div>
      <div class="sp-why-card reveal d2"><div class="wc-icon">🕘</div><b>On time, every time</b><p>I show up when I say I will and respect your schedule.</p></div>
      <div class="sp-why-card reveal d3"><div class="wc-icon">✨</div><b>Clean &amp; careful</b><p>Your home is treated like my own, with tidy work and a clean finish.</p></div>
    </div>
  </div>
</section>

<section class="sp-sec">
  <div class="section-wrap sp-two">
    <div class="reveal">
      <div class="section-tag">Service area</div>
      <h2 class="section-title">{esc(s["short"])} near <em>you</em></h2>
      <p class="sp-p">Andrew Handyman Services is based in Wesley Chapel and provides {esc(s["short"].lower())} across the northern Tampa Bay area, including {AREAS_TXT} and nearby neighborhoods.</p>
      <div class="area-chips">{chips}</div>
      <p class="sp-p">Not sure if I cover your address? Call or text {PHONE_DISPLAY} and I will let you know.</p>
    </div>
    <div class="reveal">
      <div class="section-tag">Questions</div>
      <h2 class="section-title">Good to <em>know</em></h2>
      <div class="sp-faq">{faq}</div>
    </div>
  </div>
</section>

<section class="sp-sec sp-alt">
  <div class="section-wrap">
    <div class="reveal">
      <div class="section-tag">More services</div>
      <h2 class="section-title">Related <em>services</em></h2>
    </div>
    <div class="sp-related">{rel}</div>
  </div>
</section>

<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Ready for {esc(s["short"].lower())}?</h2>
    <p class="cta-text">Send a quick request or call. I will get back to you fast with a clear estimate.</p>
    <div class="cta-btns">
      <a href="tel:{PHONE_TEL}" class="btn-cta">📞 Call {PHONE_DISPLAY}</a>
      <a href="/#home" class="btn-ghost-cta">Book Online ↑</a>
    </div>
  </div>
</section>
</main>

{footer_html()}
<script src="/site.js?v={VER}" defer></script>
</body>
</html>
'''
    return head(title, s['desc'], url, extra) + body

def main():
    for s in S:
        d = os.path.join('services', s['slug'])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(s))
    urls = [DOMAIN + '/'] + [f'{DOMAIN}/services/{s["slug"]}/' for s in S]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    open('sitemap.xml', 'w').write(sm)
    open('tools/_nav.html', 'w', encoding='utf-8').write(nav_html())
    open('tools/_footer.html', 'w', encoding='utf-8').write(footer_html())
    print('built', len(S), 'service pages')

if __name__ == '__main__':
    main()
