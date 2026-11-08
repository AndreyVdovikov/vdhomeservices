#!/usr/bin/env python3
"""Generates /services/<slug>/index.html pages, shared nav/footer snippets and sitemap.xml.
Run from the repo root:  python3 tools/build_services.py
"""
import os, json, html

DOMAIN = 'https://andrewhandy.com'
PHONE_DISPLAY = '(656) 231-1836'
PHONE_TEL = '+16562311836'
VER = '20261107g'   # bump to bust browser cache of site.css/site.js
AREAS = ["Wesley Chapel", "Land O' Lakes", "Zephyrhills", "Dade City", "New Tampa", "Lutz", "Odessa", "Tampa"]
AREAS_TXT = "Wesley Chapel, Land O' Lakes, Zephyrhills, Dade City, New Tampa, Lutz, Odessa"

S = [
 dict(slug='christmas-light-installation', name='Christmas Light Installation', short='Christmas Lights', h1='Christmas Light Installation', icon='christmas-lights.svg', photo=None,
  title='Christmas Light Installation Wesley Chapel FL – Install, Takedown & Storage',
  desc="Christmas light installation in Wesley Chapel, FL: professional C9 roofline lights in any color, cut to fit, installed, taken down in January and stored. The lights are yours. Free estimate.",
  lead="Professional C9 holiday lighting in any color, cut to fit your home, installed, taken down in January and stored until next season. No tangled wires, no leftover cut ends and no ladder falls for you. Call for a free estimate.",
  bullets=["Professional C9 roofline lights in any color or color mix you like","Lights cut and measured to fit your roofline and your home","Installation on roofline, eaves, gutters and other areas","No leftover cut pieces, no tangled strands and no climbing a ladder yourself","Take-down in January","Storage until next holiday season, so you do not need to find room in your garage","The lights belong to you, unlike with companies that rent them"],
  more_tag="How it works", more=("Four steps, <em>no ladder for you</em>",[("📏","Free estimate","Tell me about your home and what you would like lit. I give you a clear estimate for free: call or text (656) 231-1836."),("💡","Cut to fit and installed","Professional C9 lights in the colors you choose, cut to your size and installed neatly."),("📦","Taken down in January","When the season is over I take everything down, with no tangled strands and nothing left on your roof."),("🏠","Stored for next year","I keep your lights until the next holiday season. They are yours, so next year they are ready to go back up.")]),
  faq=[("Who owns the lights?","You do. Unlike companies that rent lights and take them back, the lights we install are yours, and we store them for you after take-down."),
       ("When do you take the lights down and where do they go?","We take them down in January and store them until the next holiday season, ready to be installed again."),
       ("Can I choose the colors?","Yes. Warm white, cool white, multicolor or any color mix that you like. Tell me what you have in mind and we will plan it together."),
       ("How do I get an estimate for holiday lighting?","Estimates are free. The price depends on the size of your home and the areas you want lit, so call or text (656) 231-1836 and I will take care of it."),
       ("Do you also serve Land O' Lakes?","Yes. See my Christmas light installation page for Land O' Lakes, or call to check your address.")],
  related=['christmas-light-installation-land-o-lakes','fence-repair','painting']),
 dict(slug='christmas-light-installation-land-o-lakes', name="Christmas Light Installation Land O' Lakes", short="Christmas Lights Land O' Lakes", h1='Christmas Light Installation', city="Land O' Lakes", hidden=True, parent='christmas-light-installation', icon='christmas-lights.svg', photo=None,
  title="Christmas Light Installation Land O' Lakes FL | Install, Takedown & Storage",
  desc="Christmas light installation in Land O' Lakes, FL: professional C9 lights in any color, cut to fit your roofline, installed, taken down in January and stored. Free estimate from Andrew Handyman Services.",
  lead="Land O' Lakes homeowners: get professional C9 Christmas lights cut to fit your house, installed, taken down in January and stored for next year. You keep the lights, and you never touch a ladder. Call for a free estimate.",
  area_note="Land O' Lakes is a short drive from my base in Wesley Chapel, so I can schedule installs and January take-downs without long waits.",
  bullets=["C9 holiday lights for roofline, eaves and gutters in any color","Lights cut to the size of your home, with no leftover pieces","Neat, safe installation, with no ladder work for you","January take-down once the season is over","Storage until next year, so your garage stays free","The lights are yours to keep, not rented"],
  more_tag="Land O' Lakes", more=("Holiday lights for <em>your Land O' Lakes home</em>",[("📍","Close to home","I am based in Wesley Chapel, right next door, and I work in Land O' Lakes regularly."),("🎨","Your colors, your design","Classic warm white, bright cool white, red and green or a mix of colors. You choose the look."),("🪜","No ladder, no tangles","I do the climbing and the cutting. After the season the lights come down cleanly instead of in a knot."),("🎁","Yours next year too","Because the lights belong to you, next season we hang them again from storage.")]),
  faq=[("Do you install Christmas lights in Land O' Lakes?","Yes. I install roofline and eave C9 lights in Land O' Lakes and nearby areas. Call or text (656) 231-1836 to check your address."),
       ("Are the lights rented or do I own them?","You own them. We install them, take them down in January and store them for you until next season."),
       ("What does an estimate cost?","Nothing. Estimates are free. Call or text and I will tell you what to expect for your home."),
       ("When should I book?","Earlier is better, as the holiday season fills up. Call or text me as soon as you decide, and I will schedule your installation.")],
  related=['christmas-light-installation','fence-repair','painting']),
 dict(slug='tv-shelf-mounting', name='TV, Shelf & Curtain Rod Mounting', short='TV & Shelf Mounting', h1='TV, Shelf & Curtain Rod Mounting', icon='tv.png', photo=None,
  title='TV Mounting Wesley Chapel FL – Any Size, Over Fireplace, Hidden Wires',
  desc="TV mounting in Wesley Chapel, FL: 43 to 98 inch TVs, over brick or stone fireplaces, lanai and outdoor walls, with hidden wires. Shelves and curtain rods too. Free estimate.",
  lead="TV mounting for every size, from 43 to 98 inches, on drywall, brick, stone and lanai walls, with neat, hidden wires. I also hang shelves and curtain rods in Wesley Chapel and nearby. Call for a free estimate.",
  bullets=["TV mounting for any size, including 65, 75, 85 and larger screens","Fixed, tilting and full-motion brackets, installed level and secure","TVs above brick or stone fireplaces","Samsung Frame and other thin TVs","Floating shelves and heavy-duty shelving, anchored properly","Curtain rods, blinds and drapery hardware, including high ceilings","Cords hidden in a cord cover or through the wall with a cable pass-through kit"],
  more_tag="TV mounting", more=("Every size, <em>every wall</em>",[("📺","Big screens","I mount 43 to 98 inch TVs, including 65, 75 and 85 inch models. Large TVs are heavy, so I plan the lift and the bracket carefully before the TV goes up."),("🔥","Over the fireplace","Brick and stone fireplaces are common in Wesley Chapel homes. I use the right anchors and show you the best height before I drill."),("🔌","Hidden wires","Cords go into a cord cover or behind the wall with a pass-through kit, so you see a clean TV and no cables."),("🌴","Lanai & outdoor","Outdoor TVs on a lanai or screened porch are mounted on a bracket that is rated for the wall and the location.")]),
  faq=[("How much does it cost to mount a 65 inch TV?","Estimates are free. The price depends on the size of the TV, the wall (drywall, brick or stone) and whether you want the wires hidden. Call or text (656) 231-1836 and I will give you a clear number."),
       ("Do I need to buy the mount myself?","You can supply your own bracket, or I can point you to a mount that fits your TV and wall. I confirm everything before I start so there are no surprises."),
       ("Can you mount a TV above a brick or stone fireplace?","Yes. I check the surface and use the right anchors. If a fireplace is too hot or the wall is not a good fit, I tell you before I start."),
       ("Can you mount a TV outside on a lanai?","Yes, on a suitable wall with a bracket and TV that are made for outdoor use. Call me with the details of your lanai."),
       ("Can you hide the wires?","I hide the cords in a cord cover or route them behind the wall with a cable pass-through kit. I do not install new outlets."),
       ("How long does it take?","A standard TV mount is usually done within an hour or two. Larger screens, fireplaces and wire concealment take longer, and I tell you the time ahead.")],
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

def low(t): return t.replace('Christmas','Christmas_').replace('TV','TV_').lower().replace('christmas_','Christmas').replace('tv_','TV')

ICON = lambda s: f"/images/services/{s['icon']}"

def nav_html():
    VIS = [x for x in S if not x.get('hidden')]
    items = ''.join(f'<a href="/services/{s["slug"]}/"><img src="{ICON(s)}" alt="" width="26" height="26" loading="lazy"><span>{esc(s["name"])}</span></a>' for s in VIS)
    mob = ''.join(f'<a href="/services/{s["slug"]}/">{esc(s["name"])}</a>' for s in VIS)
    return f'''<!-- NAV -->
<nav id="nav">
  <a href="/" class="nav-logo">
    <div class="nav-logo-icon" style="background:none;box-shadow:none;width:44px;height:44px;border-radius:0;overflow:visible;">
      <img src="/images/img-01.png" alt="Andrew Handyman Logo" style="width:44px;height:44px;object-fit:contain;border-radius:0;">
    </div>
    <div class="nav-logo-text">Andrew Handyman<span>Wesley Chapel, FL</span></div>
  </a>
  <ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li class="nav-dd">
      <a href="/#services" class="nav-dd-toggle" aria-haspopup="true">Services <span class="nav-caret">&#9662;</span></a>
      <div class="nav-dd-menu">{items}</div>
    </li>
    <li><a href="/about/">About</a></li>
    <li><a href="/#reviews">Reviews</a></li>
    <li><a href="/faq/">FAQ</a></li>
    <li><a href="/#contact">Area</a></li>
    <li><a href="tel:{PHONE_TEL}" class="nav-call">📞 {PHONE_DISPLAY}</a></li>
  </ul>
  <button class="nav-burger" aria-label="Open menu" aria-expanded="false" aria-controls="navMobile"><span></span><span></span><span></span></button>
</nav>
<div class="nav-mobile" id="navMobile">
  <div class="nm-h">Services</div>
  <div class="nm-list">{mob}</div>
  <div class="nm-h">More</div>
  <div class="nm-list"><a href="/">Home</a><a href="/about/">About</a><a href="/#reviews">Reviews</a><a href="/faq/">FAQ</a><a href="/#contact">Service Area &amp; Contact</a></div>
  <a href="tel:{PHONE_TEL}" class="nm-call">📞 Call {PHONE_DISPLAY}</a>
</div>
'''

def footer_html():
    links = ''.join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in S if not s.get('hidden'))
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
        <div class="f-contact-row">👤 <a href="/about/" style="color:inherit;text-decoration:none">About Andrew</a></div>
        <div class="f-contact-row">❓ <a href="/faq/" style="color:inherit;text-decoration:none">FAQ</a></div>
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
    city = s.get('city', 'Wesley Chapel')
    title = s.get('title') or f'{s["h1"]} in {city}, FL | Andrew Handyman Services'
    ld = {"@context":"https://schema.org","@type":"Service","name":f'{s["h1"]} in {city}, FL',"serviceType":s['h1'],
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
    sshort = s['h1'] if s.get('city') else s['short']
    par = BY.get(s.get('parent'))
    crumb_parent = f'<a href="/services/{par["slug"]}/">{esc(par["short"])}</a> <span>›</span> ' if par else ''
    more = ''
    a_why, a_area, a_rel = ' sp-alt', '', ' sp-alt'
    if s.get('more'):
        mt, cards = s['more']
        mc = ''.join(f'<div class="sp-why-card reveal"><div class="wc-icon">{ic}</div><b>{esc(t)}</b><p>{esc(p)}</p></div>' for ic,t,p in cards)
        more = f'<section class="sp-sec sp-alt"><div class="section-wrap"><div class="reveal"><div class="section-tag">{esc(s.get("more_tag","Details"))}</div><h2 class="section-title">{mt}</h2></div><div class="sp-why">{mc}</div></div></section>\n'
        a_why, a_area, a_rel = '', ' sp-alt', ''
    chips = ''.join(f'<span class="area-chip">{esc(a)}</span>' for a in AREAS)
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> <a href="/#services">Services</a> <span>›</span> {crumb_parent}{esc(s["short"])}</div>
      <h1 class="sp-h1">{esc(s["h1"])} in <em>{esc(city)}, FL</em></h1>
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

{more}<section class="sp-sec{a_why}">
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

<section class="sp-sec{a_area}">
  <div class="section-wrap sp-two">
    <div class="reveal">
      <div class="section-tag">Service area</div>
      <h2 class="section-title">{esc(sshort)} near <em>you</em></h2>
      <p class="sp-p">{esc(s.get('area_note',''))} Andrew Handyman Services is based in Wesley Chapel and provides {esc(low(sshort))} in {esc(city)} and across the northern Tampa Bay area, including {AREAS_TXT} and nearby neighborhoods.</p>
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

<section class="sp-sec{a_rel}">
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
    <h2 class="cta-title">Ready for {esc(low(sshort))}?</h2>
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


FAQ = [
 ("About Andrew & my service", [
  ("Who is Andrew Handyman Services?","I am Andrew, a local handyman based in Wesley Chapel, FL. I help homeowners with repairs, painting, mounting, remodeling and seasonal projects like Christmas lights. Every job is handled by me personally."),
  ("Which areas do you serve?","Wesley Chapel, Land O' Lakes, Zephyrhills, Dade City, New Tampa, Lutz, Odessa and nearby neighborhoods. If you are not sure whether I cover your address, call or text (656) 231-1836."),
  ("What services do you offer?","TV, shelf and curtain rod mounting, drywall repair, wood rot and damage repair, interior and exterior painting, cabinet painting and renovation, new kitchen installation, hurricane shutters, media and accent walls, deck repair, fence repair and Christmas light installation."),
  ("What are your hours?","I open at 9 AM, Tuesday through Saturday. You can send a request through the website or text me at any time, and I will get back to you as soon as I can."),
 ]),
 ("Estimates & booking", [
  ("Is the estimate really free?","Yes. Estimates are free, and you get a clear price before any work starts, so there are no surprises on the final bill."),
  ("How do I book?","Fill in the form at the top of the home page, call or text (656) 231-1836. I usually get back to you within a few hours."),
  ("Can I send photos of the job?","Yes. The request form has a photo upload, and you can also text photos to (656) 231-1836. Photos help me give you a more accurate estimate."),
  ("Do you give prices over the phone or online?","I do not publish fixed prices, because every home and job is different. Call or text with a few details and a photo, and I will give you a free estimate."),
  ("Do I need to buy the materials myself?","It depends on the job. You can pick your own materials, such as a TV mount, paint or cabinets, or I can recommend and supply them. Either way I tell you everything in the estimate before work starts."),
  ("How long will my job take?","Small jobs such as a TV mount or a drywall patch are often done in a few hours. Larger jobs such as cabinets, kitchens or media walls take longer, and I give you a timeline in the estimate."),
 ]),
 ("Repairs & installations", [
  ("Can you mount a TV on any wall and hide the wires?","I mount TVs of all sizes on drywall, brick and stone, including above a fireplace and on a lanai. I hide cords in a cord cover or route them behind the wall with a cable pass-through kit. I do not install new outlets."),
  ("Will a drywall repair be visible afterwards?","I match the texture and prime the repair so it blends in. I can also paint the wall so the repair disappears completely."),
  ("Do you repair rotted wood or replace it?","Small damaged spots can often be repaired. When the wood is too far gone I replace the board. I show you what I find and explain which option makes sense."),
  ("Is painting my cabinets better than replacing them?","If your cabinet boxes are solid, painting or renovating is usually far less expensive and still changes the whole look of the room. I will tell you honestly if replacement is the better choice."),
  ("Is it worth repairing my fence or deck instead of replacing it?","If the posts and frame are solid, repairing damaged sections is usually much cheaper than replacing everything. I tell you honestly when a section or a full replacement makes more sense."),
  ("Do hurricane shutters need a permit?","Shutter projects often do. I walk you through what applies to your address before we start. Atlantic hurricane season runs June 1 to November 30, so booking early gives you the most choice."),
  ("Can you build a media or accent wall to my own design?","Yes. Bring a photo or an idea and I will tell you what is possible and give you a clear estimate. I can also mount the TV as part of the wall."),
 ]),
 ("Christmas light installation", [
  ("Who owns the Christmas lights?","You do. Unlike companies that rent lights and take them back, the lights we install are yours, and we store them for you after take-down."),
  ("What does the Christmas light service include?","Professional C9 lights in any color, cut to fit your home and installed, with no leftover pieces, no tangled strands and no ladder work for you. In January I take the lights down and store them until the next season."),
  ("Can I choose the colors?","Yes. Warm white, cool white, multicolor or any color mix that you like."),
 ]),
 ("Licenses, trust & reviews", [
  ("Do you do electrical or plumbing work?","No. Work that legally requires a licensed electrician or plumber is not part of my service. I can tell you what to line up with a licensed professional so your project stays on schedule."),
  ("Where can I read reviews?","On Google (4.7 stars, 26 reviews), Facebook, Yelp and Thumbtack. All 48 reviews from the four platforms are on the home page in the Reviews section."),
  ("What if I am not sure my project is something you do?","Just ask. Call or text (656) 231-1836 or send a photo, and I will tell you honestly whether I can help or who you should call instead."),
 ]),
]

def faq_page():
    url = DOMAIN + '/faq/'
    title = 'FAQ | Andrew Handyman Services, Wesley Chapel FL'
    desc = 'Answers about Andrew Handyman Services in Wesley Chapel, FL: free estimates, service areas, TV mounting, drywall, painting, cabinets, fences, decks and Christmas lights.'
    qa = [x for _, items in FAQ for x in items]
    ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":"FAQ","item":url}]}
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n<script type="application/ld+json">{json.dumps(bc)}</script>\n'
    secs = ''
    for i,(gt,items) in enumerate(FAQ):
        cls = ' sp-alt' if i % 2 else ''
        det = ''.join(f'<details class="sp-q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in items)
        secs += f'<section class="sp-sec{cls}"><div class="section-wrap faq-wrap"><div class="reveal"><h2 class="section-title">{esc(gt)}</h2><div class="sp-faq">{det}</div></div></div></section>\n'
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> FAQ</div>
      <h1 class="sp-h1">Frequently asked <em>questions</em></h1>
      <p class="sp-lead">Quick answers about estimates, booking, my services and service area. Can't find yours? Call or text {PHONE_DISPLAY}.</p>
      <div class="sp-actions">
        <a class="btn-cta" href="/#home">Get a free estimate</a>
        <a class="btn-ghost-cta" href="tel:{PHONE_TEL}">📞 {PHONE_DISPLAY}</a>
        <a class="btn-ghost-cta" href="sms:{PHONE_TEL}">💬 Text to book</a>
      </div>
    </div>
  </div>
</section>
{secs}
<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Still have a question?</h2>
    <p class="cta-text">Send a quick request or call. I will get back to you fast.</p>
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
    return head(title, desc, url, extra) + body


def about_page():
    url = DOMAIN + '/about/'
    title = 'About Andrew | Handyman in Wesley Chapel, FL'
    desc = "Meet Andrew, your local handyman in Wesley Chapel, FL. Quality, quick solutions for home repairs and improvements, backed by a personal guarantee. Free estimate."
    ld = {"@context":"https://schema.org","@type":"AboutPage","name":"About Andrew Handyman Services","url":url,
          "mainEntity":{"@type":"Person","name":"Andrew","jobTitle":"Handyman","worksFor":{"@type":"HomeAndConstructionBusiness","name":"Andrew Handyman Services","url":DOMAIN+"/"},
                        "image":DOMAIN+"/images/andrew-about.jpg"}}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":"About","item":url}]}
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n<script type="application/ld+json">{json.dumps(bc)}</script>\n'
    chips = ''.join(f'<span class="area-chip">{esc(a)}</span>' for a in AREAS)
    svc = ''.join(f'<a class="area-chip about-svc" href="/services/{x["slug"]}/">{esc(x["name"])}</a>' for x in S if not x.get('hidden'))
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> About</div>
      <h1 class="sp-h1">Greetings, I'm <em>Andrew</em></h1>
      <p class="sp-lead">Your handyman in Wesley Chapel, FL. Quality, quick solutions for the repairs and improvements your home needs.</p>
      <div class="sp-actions">
        <a class="btn-cta" href="/#home">Get a free estimate</a>
        <a class="btn-ghost-cta" href="tel:{PHONE_TEL}">📞 {PHONE_DISPLAY}</a>
        <a class="btn-ghost-cta" href="sms:{PHONE_TEL}">💬 Text to book</a>
      </div>
    </div>
  </div>
</section>

<section class="sp-sec">
  <div class="section-wrap sp-two">
    <div class="reveal">
      <div class="section-tag">About me</div>
      <h2 class="section-title">Ready to make your home <em>work better?</em></h2>
      <p class="sp-p">Greetings, I'm Andrew and I'm your handyman. Ready to make your home work better with my help? Let's get started! Don't let those home repairs wait any longer.</p>
      <p class="sp-p">I offer a wide range of work around the house. My specialty is providing quality and quick solutions to any home improvement and repair needs of your home.</p>
      <div class="about-guarantee"><b>Every job is backed by my personal guarantee.</b> If you're not completely satisfied with the work, I'll make it right, no questions asked.</div>
      <h3 class="about-h3">What distinguishes my services</h3>
      <ul class="sp-list"><li><span class="sp-check"></span><span>I perform all types of minor repairs</span></li><li><span class="sp-check"></span><span>Professional assembly and installation of furniture of any brands</span></li><li><span class="sp-check"></span><span>Installation of shelves, cornices, TVs and other interior items</span></li></ul>
    </div>
    <div class="reveal"><img class="about-photo" src="/images/andrew-about.jpg" alt="Andrew, handyman in Wesley Chapel, FL, giving a thumbs up" width="600" height="750" loading="lazy"></div>
  </div>
</section>

<section class="sp-sec sp-alt">
  <div class="section-wrap">
    <div class="reveal">
      <div class="section-tag">What I do</div>
      <h2 class="section-title">Services for <em>your home</em></h2>
      <div class="area-chips">{svc}</div>
    </div>
  </div>
</section>

<section class="sp-sec">
  <div class="section-wrap sp-two">
    <div class="reveal">
      <div class="section-tag">Reviews</div>
      <h2 class="section-title">What neighbors <em>say</em></h2>
      <p class="sp-p">48 reviews across Google, Facebook, Yelp and Thumbtack, with a 4.7 rating on Google. <a href="/#reviews">Read the reviews</a>.</p>
    </div>
    <div class="reveal">
      <div class="section-tag">Service area</div>
      <h2 class="section-title">Where I <em>work</em></h2>
      <p class="sp-p">Based in Wesley Chapel and serving the northern Tampa Bay area.</p>
      <div class="area-chips">{chips}</div>
    </div>
  </div>
</section>

<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Let's get started</h2>
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
    return head(title, desc, url, extra) + body

def main():
    for s in S:
        d = os.path.join('services', s['slug'])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(s))
    os.makedirs('about', exist_ok=True)
    open('about/index.html','w',encoding='utf-8').write(about_page())
    os.makedirs('faq', exist_ok=True)
    open('faq/index.html','w',encoding='utf-8').write(faq_page())
    urls = [DOMAIN + '/', DOMAIN + '/faq/', DOMAIN + '/about/'] + [f'{DOMAIN}/services/{s["slug"]}/' for s in S]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    open('sitemap.xml', 'w').write(sm)
    open('tools/_nav.html', 'w', encoding='utf-8').write(nav_html())
    open('tools/_footer.html', 'w', encoding='utf-8').write(footer_html())
    print('built', len(S), 'service pages')

if __name__ == '__main__':
    main()
