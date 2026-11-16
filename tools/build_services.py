#!/usr/bin/env python3
"""Generates /services/<slug>/index.html pages, shared nav/footer snippets and sitemap.xml.
Run from the repo root:  python3 tools/build_services.py
"""
import os, sys, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from locations_data import LOCS
import blog_data as BL
import guides_data as GD
import articles_data as AD
import projects_data as PD
import media_data as MD

DOMAIN = 'https://andrewhandy.com'
PHONE_DISPLAY = '(656) 231-1836'
PHONE_TEL = '+16562311836'
GA_ID = 'G-H9H5NEZSS8'
GA_SNIPPET = f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>\n<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{GA_ID}");</script>'
VER = '20261116c'   # bump to bust browser cache of site.css/site.js
AREAS = ["Wesley Chapel", "Land O' Lakes", "Zephyrhills", "Dade City", "New Tampa", "Lutz", "Odessa", "Tampa"]
AREAS_TXT = "Wesley Chapel, Land O' Lakes, Zephyrhills, Dade City, New Tampa, Lutz, Odessa"

S = [
 dict(slug='christmas-light-installation', name='Christmas Light Installation', short='Christmas Lights', h1='Christmas Light Installation', icon='christmas-lights.svg', photo=None,
  title='Christmas Light Installation Wesley Chapel FL – Install, Takedown & Storage',
  desc="Christmas light installation in Wesley Chapel, FL: professional C9 roofline lights in any color, cut to fit, installed, taken down in January and stored. The lights are yours. Free estimate.",
  lead="Professional C9 holiday lighting in any color, cut to fit your home, installed, taken down in January and stored until next season. No tangled wires, no leftover cut ends and no ladder falls for you. Call for a free estimate.",
  bullets=["Professional C9 roofline lights in any color or color mix you like","Lights cut and measured to fit your roofline and your home","Installation on roofline, eaves, gutters and other areas","No leftover cut pieces, no tangled strands and no climbing a ladder yourself","Take-down in January","Storage until next holiday season, so you do not need to find room in your garage","The lights belong to you, unlike with companies that rent them"],
  more_tag="How it works", more=("Four steps, <em>no ladder for you</em>",[("📏","Free estimate","Tell me about your home and what you would like lit. I give you a clear estimate for free: call or text (656) 231-1836."),("💡","Cut to fit and installed","Professional C9 lights in the colors you choose, cut to your size and installed neatly with clips made for shingles, gutters, tile and stucco. A typical house takes one to two days, and most are done in one."),("📦","Taken down in January","When the season is over I take everything down, with no tangled strands and nothing left on your roof."),("🏠","Stored for next year","I keep your lights until the next holiday season. They are yours, so next year they are ready to go back up.")]),
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
 dict(slug='tv-shelf-mounting', name='TV, Shelf & Curtain Rod Mounting', short='TV & Shelf Mounting', h1='TV, Shelf & Curtain Rod Mounting', icon='tv.png', photo=None, gallery_h='Recent TV <em>mounting jobs</em>', gallery_r='4/3', gallery=[('tv-mounted-drywall-wall-above-wood-media-console-wesley-chapel.jpg', 'TV mounted on a drywall wall above a wood media console', 'TV Mounting on Drywall'), ('tv-mounted-level-lanai-wall-level-top-wesley-chapel.jpg', 'TV mounted level on a lanai wall with a level on top', 'Lanai TV Mounting'), ('wall-mounted-tv-screened-lanai-florida-wesley-chapel.jpg', 'Wall-mounted TV on a screened lanai in Florida', 'Lanai TV Installation')],
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
 dict(slug='wood-rot-repair', name='Wood Rot & Damage Repair', short='Wood Rot Repair', h1='Wood Rot & Damage Repair', icon='wood.svg', photo=('deck-repair-wesley-chapel.jpg','Before and after repair of rotted wooden steps and railing'),
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
 dict(slug='cabinet-painting-renovation', name='Cabinet Painting & Renovation', short='Cabinet Painting', h1='Cabinet Painting & Renovation', icon='cabinets.svg', photo=('kitchen-cabinet-renovation-wesley-chapel.jpg','Kitchen cabinets before and after renovation'),
  desc="Kitchen and whole-house cabinet painting and renovation in Wesley Chapel, FL. A fresh new look without the cost of full replacement. Andrew Handyman Services.",
  lead="Give your kitchen or whole house a fresh look without paying for full replacement. I paint and renovate cabinets for homeowners in Wesley Chapel, Land O' Lakes, Zephyrhills and nearby.",
  bullets=["Kitchen cabinet painting with proper cleaning, sanding and priming","Bathroom vanities and whole-house cabinets","New hardware, hinges and soft-close upgrades","Door and drawer-front repairs and adjustments","Cabinet box repairs and touch-ups","Smooth, durable finish that is made for daily use"],
  faq=[("Is painting better than replacing cabinets?","If your cabinet boxes are solid, painting or renovating is usually far less expensive and still changes the whole look of the room. I will tell you honestly if replacement is the better choice."),
       ("How long does a cabinet job take?","Most kitchens take several days, because each coat needs time to dry and cure. I give you a clear schedule before I start."),
       ("Can you change the hardware too?","Yes. New handles, knobs and hinges are a quick upgrade that makes painted cabinets look brand new.")],
  related=['new-kitchen-installation','painting','drywall-repair']),
 dict(slug='new-kitchen-installation', name='New Kitchen Installation', short='New Kitchen', h1='New Kitchen Installation', icon='kitchen.svg', gallery_h='Recent <em>kitchen projects</em>', gallery_r='4/3', gallery=[('white-kitchen-cabinets-granite-counters-island-wesley-chapel.jpg', 'White kitchen cabinets with granite counters and an island', 'Kitchen with Granite Island'), ('white-shaker-cabinets-granite-countertop-subway-tile-backsplash-wesley-chapel.jpg', 'White shaker cabinets with granite countertop and subway tile backsplash', 'Granite & Subway Tile Kitchen')], photo=('new-kitchen-installed-by-andrew-handyman-services-wesley-chapel.jpg','New kitchen installed by Andrew Handyman Services'),
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
 dict(slug='media-accent-walls', name='Media & Accent Walls', short='Media & Accent Walls', h1='Media & Accent Walls', icon='media-wall.svg', photo=None, gallery=([('white-shiplap-media-wall-wood-mantel-soundbar-electric-wesley-chapel.jpg', 'White shiplap media wall with wood mantel, soundbar and electric fireplace', 'White Shiplap TV Wall'), ('white-shiplap-tv-wall-mounted-tv-mantel-linear-wesley-chapel.jpg', 'White shiplap TV wall with a mounted TV, mantel and linear fireplace', 'Shiplap Media Wall'), ('dark-stained-wood-plank-tv-wall-mantel-electric-wesley-chapel.jpg', 'Dark stained wood plank TV wall with mantel and electric fireplace', 'Stained Wood TV Wall'), ('floor-to-ceiling-dark-wood-media-wall-tv-wesley-chapel.jpg', 'Floor to ceiling dark wood media wall with TV and fireplace', 'Dark Wood Media Wall'), ('wood-panel-tv-wall-floating-shelves-mantel-linear-wesley-chapel.jpg', 'Wood panel TV wall with floating shelves, mantel and linear fireplace', 'Wood Panel Wall & Floating Shelves')]),
  title=MD.TITLE, desc=MD.DESC,
  lead=MD.LEAD, article=True,
  bullets=["TV and media walls with a clean built-in look","Wood slat, paneled and shiplap accent walls","Fireplace surrounds and feature walls","Custom designs planned around your room and TV","TV mounting with neat cord covers","Painted or stained to match your decor"],
  faq=[("Can you build a wall to my own design?","Yes. Bring a photo or an idea and I will tell you what is possible and give you a clear estimate. I can also suggest layouts that work well for your TV size."),
       ("Is the TV mount included?","I can mount the TV as part of the wall installation, so everything is level and lines up with the design."),
       ("How long does an accent wall take?","A simple accent wall can be finished in a day or two. Larger media walls take longer, and I give you a timeline in the estimate."),
       ("How much does a media wall cost?","An accent wall with TV mounting and a mantel starts from $1,500. A full media wall is typically $3,500 to $4,000, and large custom projects run $6,000 to $10,000 or more. The exact price depends on size, design and materials. Send the wall width and height with photos for a free estimate."),
       ("Can you build a media wall with a fireplace?","Yes. I build the wall around an electric fireplace with a mantel and finish it to match. If a new outlet is needed, a licensed electrician handles that part."),
       ("Do I need to know the exact design?","No. Send photos of your room and a reference of a wall you like, and I will suggest layouts, colors and materials.")],
  related=['tv-shelf-mounting','painting','new-kitchen-installation']),
 dict(slug='deck-repair', name='Deck Repair', short='Deck Repair', h1='Deck Repair', icon='deck.svg', gallery_h='Recent <em>deck &amp; porch jobs</em>', gallery_r='4/3', gallery=[('front-porch-steps-teal-painted-wood-railings-wesley-chapel.jpg', 'Front porch steps and teal painted wood railings', 'Porch Steps & Railings'), ('wood-deck-stairs-painted-treads-black-railings-wesley-chapel.jpg', 'Wood deck stairs with painted treads and black railings', 'Deck Stairs & Railings'), ('backyard-deck-stairs-railing-from-another-angle-wesley-chapel.jpg', 'Backyard deck stairs and railing from another angle', 'Deck Stair Railing Work'), ('porch-platform-new-railing-posts-balusters-wesley-chapel.jpg','Porch platform with new railing posts and balusters','Porch Platform & Railing'), ('porch-new-pressure-treated-deck-boards-posts-wesley-chapel.jpg','Porch with new pressure-treated deck boards and posts','New Deck Boards & Posts'), ('front-view-porch-new-deck-boards-railing-wesley-chapel.jpg','Front view of a porch with new deck boards and railing','Porch, Front View')], photo=('deck-repair-wesley-chapel.jpg','Before and after deck stairs and railing repair'),
  desc="Deck repair in Wesley Chapel, FL: replacement boards, railings, stairs and posts, plus staining and sealing. Make your deck safe again with Andrew Handyman Services.",
  lead="Loose, rotted or worn deck boards, railings and steps repaired so your deck is safe and good-looking again. Serving Wesley Chapel, Land O' Lakes, Zephyrhills and nearby.",
  bullets=["Replacement of rotted or cracked deck boards","Railings, balusters and handrails","Stair treads, risers and stringers","Posts and loose or failing connections","Staining and sealing to protect the wood","Safe, solid result you can trust to walk on"],
  faq=[("Is my deck safe to use?","If boards are soft, railings wobble or stairs feel loose, it is time for a repair. I check the structure and tell you honestly what needs to be fixed first."),
       ("Do deck repairs need a permit?","Small repairs usually do not, but larger structural work can. I tell you upfront what applies before we start."),
       ("Can you stain or seal the deck after repair?","Yes. Sealing or staining protects the wood from Florida sun and rain, and it makes the repair look uniform.")],
  related=['wood-rot-repair','fence-repair','painting']),
 dict(slug='picture-hanging', name='Picture, Mirror & Art Hanging', short='Picture Hanging', h1='Picture, Mirror & Art Hanging', icon='pictures.svg', photo=None, gallery_h='Recent <em>wall decor jobs</em>', gallery_r='4/3', gallery=[('four-decorative-metal-gears-hung-large-format-tile-wesley-chapel.jpg', 'Four decorative metal gears hung on a large-format tile wall', 'Wall Decor on Tile'), ('three-panel-black-white-canvas-art-hung-tile-wesley-chapel.jpg', 'Three-panel black and white canvas art hung on a tile wall', 'Triptych Wall Art'), ('wall-mounted-display-case-mounted-large-tile-wall-wesley-chapel.jpg', 'Wall-mounted display case mounted on a large tile wall', 'Wall-Mounted Display Case')],
  title='Picture Hanging Wesley Chapel FL – Mirrors, Gallery Walls & Heavy Art',
  desc="Picture and mirror hanging in Wesley Chapel, FL: gallery walls laid out and leveled, heavy mirrors and large art anchored to the wall. Free estimate from Andrew Handyman Services.",
  lead="Pictures, mirrors, canvases and gallery walls hung level, centered and secure, on drywall, brick, block and tile. Moving in or redecorating in Wesley Chapel? Send me a photo of the wall for a free estimate.",
  bullets=["Pictures, frames and canvases of any size, hung level and at the right height","Gallery walls planned first, then hung, so the spacing looks right","Heavy mirrors and large art anchored with the correct hardware for the wall","Shadow boxes, wall clocks, wreaths, picture ledges and wall decor","Hanging on drywall, brick, block and tile","Old hooks and nails removed, small nail holes patched on request","Move-in day: the whole house done in one visit"],
  more_tag="Picture hanging", more=("Planned first, <em>then drilled</em>",[("📐","Layout before holes","For a gallery wall I plan the arrangement on the floor or with paper templates, so the first nail goes in the right place and not the third."),("🪞","Heavy mirrors","A big mirror can weigh far more than it looks. I use anchors rated for the weight and the wall, not a nail and hope."),("🧱","Brick, block and tile","Not every wall is drywall. I use the right bit and anchor for each surface so nothing cracks or pulls out."),("🏠","Move-in day","New house, empty walls. Give me the list and I hang everything in one visit: art, mirrors, shelves and more.")]),
  faq=[("How much does it cost to hang pictures?","Estimates are free. The price depends on how many pieces there are, how big and heavy they are and what the wall is made of. Text me a photo at (656) 231-1836 and I will give you a clear number."),
       ("Can you hang a heavy mirror?","Yes. I check the wall, pick anchors rated for the weight and hang it level. If a wall is not a good place for something that heavy, I tell you before I drill."),
       ("Can you plan a gallery wall for me?","Yes. We choose the layout together, I mark it out and then hang everything level with even spacing. If you already have a picture in mind, I can follow it."),
       ("Will you fill the old nail holes?","Small nail holes can be patched when I remove old hangers. If you want paint matched, I can do that too through my drywall and painting services."),
       ("Can you hang pictures on brick, block or tile walls?","Yes. These need different bits and anchors than drywall, and I use the right ones so the wall is not damaged.")],
  related=['tv-shelf-mounting','drywall-repair','furniture-assembly']),
 dict(slug='furniture-assembly', name='Furniture Assembly', short='Furniture Assembly', h1='Furniture Assembly', icon='furniture.svg', photo=None, gallery_h='Recent <em>assembly jobs</em>', gallery_r='4/3', gallery=[('assembled-corner-storage-bed-frame-drawers-led-strip-wesley-chapel.jpg', 'Assembled corner storage bed frame with drawers and LED strip', 'Storage Bed Frame Assembly'), ('assembled-four-door-wood-sideboard-cabinet-dining-room-wesley-chapel.jpg', 'Assembled four-door wood sideboard cabinet in a dining room', 'Sideboard Cabinet Assembly'), ('assembled-dark-console-table-against-wall-wesley-chapel.jpg', 'Assembled dark console table against a wall', 'Console Table Assembly'), ('desk-parts-unpacked-laid-out-before-assembly-wesley-chapel.jpg','Desk parts unpacked and laid out before assembly','Desk Parts Before Assembly'), ('assembled-l-shaped-wood-desk-monitor-risers-wesley-chapel.jpg','Assembled L-shaped wood desk with monitor risers','L-Shaped Desk Assembled')],
  title='Furniture Assembly Wesley Chapel FL – IKEA, Wayfair, Amazon & More',
  desc="Furniture assembly in Wesley Chapel, FL: IKEA, Wayfair, Amazon and Costco furniture, beds, dressers, desks and patio sets, built right and anchored. Free estimate.",
  lead="Beds, dressers, desks, bookcases, patio sets and more, built and placed where you want them. IKEA, Wayfair, Amazon, Costco or any flat-pack brand, in Wesley Chapel and nearby. Text me what you bought for a free estimate.",
  bullets=["IKEA, Wayfair, Amazon, Costco and other flat-pack furniture","Beds, dressers, nightstands, wardrobes and bookcases","Desks, office furniture and shelving units","Patio and outdoor furniture sets","Tall furniture anchored to the wall so it cannot tip over","Parts checked before I start, so missing pieces are caught right away","Move-in day: all your boxes built in one visit"],
  more_tag="Furniture assembly", more=("Built right, <em>placed where you want it</em>",[("📦","Any brand","IKEA, Wayfair, Amazon, Costco or a local store, if it came in a box I can build it."),("🛏️","Beds and dressers","Large pieces take patience and the right order of steps. I build them solid, with no wobble, and move them into place."),("⚓","Anchored for safety","Tall dressers and bookcases can tip, especially with kids at home. I anchor them to the wall on request."),("🏠","Move-in day","New home, lots of boxes. Give me the list and I build the whole set in one visit, then hang the pictures too.")]),
  faq=[("How much does furniture assembly cost?","Estimates are free. The price depends on what you bought, how many pieces there are and how complicated they are. Text me the list or a photo of the boxes at (656) 231-1836."),
       ("Can you assemble furniture I bought online?","Yes. IKEA, Wayfair, Amazon, Costco and other flat-pack brands are all fine. I just need the boxes delivered to the house."),
       ("What if parts are missing?","I check everything against the instructions before I start. If something is missing, I tell you right away so you can ask the manufacturer for the part, and I build the rest."),
       ("Can you anchor a dresser or bookcase to the wall?","Yes. Anchoring tall furniture is a good idea, especially with kids or pets in the house. I use the right anchors for the wall."),
       ("Do you assemble outdoor furniture?","Yes. Patio sets, benches and outdoor storage are fine.")],
  related=['picture-hanging','tv-shelf-mounting','media-accent-walls']),
 dict(slug='door-installation', name='Door Installation & Repair', short='Door Installation', h1='Door Installation & Repair', icon='door.svg',
  photo=('french-double-doors-installed-trimmed-florida-home-wesley-chapel.jpg','French double doors installed and trimmed in a Florida home'), photo_cap='Real job photo: French door installation',
  title='Door Installation Wesley Chapel FL – French Doors, Patio & Interior Doors',
  desc="Door installation and repair in Wesley Chapel, FL: French doors, patio doors, interior and entry doors hung, trimmed and adjusted. Lock replacement too. Free estimate.",
  lead="French doors, patio doors, entry and interior doors installed, trimmed and adjusted so they open smoothly and close tight. Door repair and lock replacement too, in Wesley Chapel and nearby. Call for a free estimate.",
  bullets=["French door and patio door installation","Interior door hanging and replacement","Entry door replacement, hung level and plumb","Door trim and casing around the new door","Doors that stick, rub or will not latch, adjusted","Lock, deadbolt and handle replacement","Weatherstripping and door sweeps so the door closes tight"],
  more_tag="Door installation", more=("Square, plumb and <em>closing right</em>",[("📏","Level and plumb","A door only works well if the opening is square. I check the frame, shim it and set the door so it swings freely and closes evenly."),("🚪","French and patio doors","Double doors need careful alignment so both leaves meet in the middle. I hang them, set the hardware and trim around them."),("🔧","Sticking doors","Rubs, gaps and latches that miss are usually a quick fix. I adjust the hinges, strike plate or door and tell you honestly what is needed."),("🔑","Locks and hardware","New deadbolts, handles and locks fitted and lined up so the key turns smoothly and the door latches every time.")]),
  faq=[("How much does door installation cost?","Estimates are free. The price depends on the type of door (French, patio, entry or interior), the size of the opening and what trim or repair is needed around it. Call or text (656) 231-1836 and I will give you a clear number."),
       ("Do I buy the door myself?","You can bring your own door or I can help you choose one that fits the opening. I confirm the size before ordering, so there are no surprises."),
       ("Can you install a French door where there is only a window or wall?","Cutting a new opening in a wall is structural work. I tell you honestly what I can do and when you need a contractor for that part."),
       ("Do I need a permit to replace a door?","Replacing a door in the same opening usually does not, but rules depend on your city or county and the type of door. I tell you upfront what applies before we start."),
       ("Can you fix a door that sticks or will not close?","Yes. Most sticking doors come down to hinges, the strike plate or swollen wood, and are a quick fix. I look at it and tell you what it needs.")],
  related=['painting','drywall-repair','wood-rot-repair']),
 dict(slug='flooring-installation', name='Flooring Installation', short='Flooring', h1='Flooring Installation', icon='floor.svg', photo=None,
  gallery_h='Flooring <em>before &amp; after</em>', gallery_r='4/3', gallery=[('bedroom-prepped-for-new-flooring-wesley-chapel.jpg','Bedroom prepped for new flooring','Room Before New Flooring'),('new-vinyl-plank-floor-bedroom-white-baseboards-wesley-chapel.jpg','New vinyl plank floor in a bedroom with white baseboards','New Vinyl Plank Floor'),('new-vinyl-plank-floor-meeting-baseboard-under-window-wesley-chapel.jpg','New vinyl plank floor meeting the baseboard under a window','Floor Detail at Baseboard')],
  title='Flooring Installation Wesley Chapel FL – Vinyl Plank & Laminate',
  desc="Flooring installation in Wesley Chapel, FL: luxury vinyl plank, laminate and click-lock floors with baseboards and transitions. Free estimate from Andrew Handyman Services.",
  lead="Luxury vinyl plank, laminate and click-lock flooring installed room by room, with baseboards and transitions fitted neatly. Serving Wesley Chapel, Land O' Lakes, Zephyrhills and nearby. Call for a free estimate.",
  bullets=["Luxury vinyl plank (LVP) and laminate flooring","Click-lock floating floors for bedrooms, living rooms and hallways","Subfloor checked and prepared before the new floor goes down","Baseboards and quarter round reinstalled or replaced","Transitions and thresholds between rooms","Doors trimmed to clear the new floor","Clean cuts around corners, vents and door frames"],
  more_tag="Flooring", more=("A floor that looks <em>right in every corner</em>",[("📐","Prep first","A good floor starts with a flat, clean base. I check the subfloor and fix what needs fixing before a single plank goes down."),("🪵","LVP and laminate","Durable, water-friendly and good-looking, vinyl plank is a popular choice for Florida homes. I help you pick a style that fits your room."),("🪚","Neat edges","Straight rows, tight seams and clean cuts at walls, doors and corners, finished with baseboards and transitions."),("🏠","Room by room","One bedroom or the whole house. I plan the layout so the floor flows from room to room.")]),
  faq=[("How much does flooring installation cost?","Estimates are free. The price depends on the size of the room, the type of flooring and what prep is needed. Call or text (656) 231-1836 and I will give you a clear number."),
       ("Can you install new flooring over my existing floor?","Sometimes. Click-lock plank can often go over a flat, clean, hard floor, but not over carpet. I look at what you have and tell you honestly before we start."),
       ("Do I buy the flooring myself?","You can choose and buy it yourself, or I can help you pick. Either way I tell you how much to order, including extra for cuts, so you do not run short."),
       ("How long does a room take?","A typical bedroom is often done in about a day. Larger areas take longer, and I give you a timeline in the estimate."),
       ("Do you reinstall baseboards?","Yes. Baseboards or quarter round go back on after the floor is down, or I replace them if they are damaged.")],
  related=['painting','door-installation','drywall-repair']),
 dict(slug='leather-vinyl-repair', name='Leather & Vinyl Repair', short='Leather repair', h1='Leather & Vinyl Repair', icon='leather.svg', photo=None,
  gallery_h='Leather repair <em>before &amp; after</em>', gallery_r='4/3', gallery=[('cracked-leather-recliner-headrest-before-repair-wesley-chapel.jpg','Cracked leather recliner headrest before repair','Recliner Headrest: Before'),('recliner-headrest-after-crack-was-repaired-wesley-chapel.jpg','Recliner headrest after the crack was repaired','Recliner Headrest: After'),('torn-vinyl-trim-by-window-before-repair-wesley-chapel.jpg','Torn vinyl trim by a window before repair','Window Trim: Before'),('vinyl-trim-by-window-after-repair-wesley-chapel.jpg','Vinyl trim by a window after repair','Window Trim: After')],
  title='Leather & Vinyl Repair Wesley Chapel FL – Recliners, Sofas, Trim',
  desc="Leather and vinyl repair in Wesley Chapel, FL: cracks, tears and peeling on recliners, sofas, chairs and trim. See before and after photos. Free estimate from Andrew Handyman Services.",
  lead="Cracks, tears and worn spots on leather and vinyl recliners, sofas, chairs and trim, repaired so they blend back in. Serving Wesley Chapel, Land O' Lakes, Zephyrhills and nearby. Call for a free estimate.",
  bullets=["Cracks and splits in leather and faux leather","Torn or peeling vinyl trim and panels","Recliners, sofas, chairs and headrests","Worn spots and scuffs on seats and arms","Color matched so the repair blends in","RV, camper and home furniture","Photo estimate: text me a picture of the damage"],
  more_tag="Leather repair", more=("Fix it before it <em>spreads</em>",[("🛋️","Repair, not replace","A small crack or tear is much cheaper to fix than a new recliner. The sooner it is repaired, the less it spreads."),("🎨","Blends in","I work to match the color and finish so the repair is hard to spot."),("📸","Photo estimate","Text me a couple of photos of the damage and I can tell you if it is a good candidate for repair."),("🚐","Home or RV","Living room furniture, camper seating and vinyl trim around windows and doors.")]),
  faq=[("How much does leather repair cost?","Estimates are free. The price depends on the size and location of the damage. Text a photo to (656) 231-1836 and I will tell you what to expect."),
       ("Can a cracked recliner be repaired?","Small and medium cracks, tears and worn spots usually can. Badly collapsed or missing material is harder, and I will tell you honestly before we start."),
       ("Will the repair be visible?","I work to match color and texture so it blends in. Up close a repair can still be noticeable on some materials, and I will show you what to expect."),
       ("Do you repair faux leather and vinyl?","Yes. Faux leather, vinyl and bonded leather are common on recliners and RV furniture, and they can often be repaired too."),
       ("Do you come to me?","Yes. I come to your home in Wesley Chapel and nearby areas, and the repair is done on site.")],
  related=['furniture-assembly','painting','drywall-repair']),
 dict(slug='fence-repair', name='Fence Repair', short='Fence Repair', h1='Fence Repair', icon='fence.svg', gallery_h='Fence <em>before &amp; after</em>', gallery_r='4/3', gallery=[('old-weathered-wood-fence-before-replacement-wesley-chapel.jpg', 'Old weathered wood fence before replacement', 'Fence Before'), ('new-wood-privacy-fence-along-backyard-garage-wall-wesley-chapel.jpg', 'New wood privacy fence along a backyard garage wall', 'Fence After'), ('new-wood-fence-straight-pickets-backyard-wesley-chapel.jpg', 'New wood fence with straight pickets in a backyard', 'New Wood Fence')], photo=('fence-before-after-repair-wesley-chapel.jpg','Fence before and after repair'),
  desc="Fence repair in Wesley Chapel, FL: broken pickets, leaning posts and damaged gates. Keep your yard secure with Andrew Handyman Services.",
  lead="Broken pickets, leaning posts and damaged gates fixed or replaced to keep your yard secure and your fence looking sharp. Serving Wesley Chapel and nearby communities.",
  bullets=["Broken or rotted pickets and panels replaced","Leaning or loose posts straightened and secured","Gate repair: hinges, latches and sagging gates","Rails and boards reinforced","Staining or painting to refresh the look","Storm damage cleanup and repair"],
  faq=[("Is it worth repairing my fence instead of replacing it?","If the posts are solid, repairing damaged sections is usually much cheaper than replacing the whole fence. I tell you honestly when a section or full replacement makes more sense."),
       ("Can you fix a gate that does not close properly?","Yes. Sagging gates, loose hinges and broken latches are quick repairs that make a big difference."),
       ("Do you repair storm damage?","Yes. After a storm I repair broken boards, damaged panels and leaning posts so your yard is secure again.")],
  related=['deck-repair','wood-rot-repair','painting']),
]
BY = {s['slug']: s for s in S}

GBP_URL = 'https://www.google.com/maps?cid=9147118600077160401'
def biz(area=None):
    """Full LocalBusiness entity used across the site (structured data for search engines and AI assistants)."""
    b = {"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","@id":DOMAIN+"/#business",
         "name":"Andrew Handyman Services","url":DOMAIN+"/","telephone":"+1-656-231-1836",
         "description":"Handyman services in Wesley Chapel, FL and the northern Tampa Bay area: TV and shelf mounting, media and accent walls, painting, drywall repair, cabinets and kitchens, decks and fences, furniture assembly, flooring, Christmas light installation and more.",
         "image":DOMAIN+"/images/img-02.jpg","logo":DOMAIN+"/apple-touch-icon.png",
         "address":{"@type":"PostalAddress","addressLocality":"Wesley Chapel","addressRegion":"FL","postalCode":"33544","addressCountry":"US"},
         "areaServed":([{"@type":"City","name":area}] if area else [{"@type":"City","name":a} for a in AREAS]),
         "knowsAbout":[x["name"] for x in S if not x.get("hidden")],
         "hasMap":GBP_URL,"sameAs":[GBP_URL,"https://share.google/M3UsYRjfswcYytOnC","https://www.instagram.com/andrew_vd83/"]}
    return b

def esc(t): return html.escape(t, quote=True)

def low(t): return t.replace('Christmas','Christmas_').replace('TV','TV_').lower().replace('christmas_','Christmas').replace('tv_','TV')

ICON = lambda s: f"/images/services/{s['icon']}"

def nav_html():
    VIS = [x for x in S if not x.get('hidden')]
    mobloc = ''.join(f'<a href="/locations/{l["slug"]}/">{esc(l["name"])}</a>' for l in LOCS)
    locitems = ''.join(f'<a href="/locations/{l["slug"]}/">{esc(l["name"])}</a>' for l in LOCS)
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
    <li><a href="/about/">About</a></li>
    <li class="nav-dd">
      <a href="/#services" class="nav-dd-toggle" aria-haspopup="true">Services <span class="nav-caret">&#9662;</span></a>
      <div class="nav-dd-menu">{items}</div>
    </li>
    <li class="nav-dd">
      <a href="/#contact" class="nav-dd-toggle" aria-haspopup="true">Locations <span class="nav-caret">&#9662;</span></a>
      <div class="nav-dd-menu nav-dd-loc">{locitems}</div>
    </li>
    <li><a href="/subscription/" class="nav-hl">Subscription</a></li>
    <li><a href="/gift/" class="nav-hl">🎁 Gift</a></li>
    <li><a href="/blog/">Blog</a></li>
    <li><a href="/#reviews">Reviews</a></li>
    <li><a href="/faq/">FAQ</a></li>
    <li><a href="tel:{PHONE_TEL}" class="nav-call">📞 {PHONE_DISPLAY}</a></li>
  </ul>
  <button class="nav-burger" aria-label="Open menu" aria-expanded="false" aria-controls="navMobile"><span></span><span></span><span></span></button>
</nav>
<div class="nav-mobile" id="navMobile">
  <div class="nm-list"><a href="/">Home</a><a href="/about/">About</a></div>
  <div class="nm-h">Services</div>
  <div class="nm-list">{mob}</div>
  <div class="nm-h">Locations</div>
  <div class="nm-list">{mobloc}</div>
  <div class="nm-h">More</div>
  <div class="nm-list"><a href="/subscription/">Handyman Subscription</a><a href="/gift/">🎁 Gift Certificates</a><a href="/blog/">Blog</a><a href="/#reviews">Reviews</a><a href="/faq/">FAQ</a><a href="/#contact">Service Area &amp; Contact</a></div>
  <a href="tel:{PHONE_TEL}" class="nm-call">📞 Call {PHONE_DISPLAY}</a>
</div>
'''

def footer_html():
    locs_f = ', '.join(f'<a href="/locations/{l["slug"]}/" style="color:inherit">{esc(l["city"].split(",")[0])}</a>' for l in LOCS)
    links = ''.join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in S if not s.get('hidden'))
    return f'''<!-- FOOTER -->
<footer>
  <div class="section-wrap">
    <div class="footer-grid">
      <div>
        <div class="f-brand">Andrew Handyman</div>
        <p class="f-tagline">Your trusted local handyman in Wesley Chapel, FL — quality work, honest pricing, always on time.</p>
        <p class="f-areas">Serving {locs_f} and nearby.</p>
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
        <div class="f-contact-row">🔎 <a href="/blog/" style="color:inherit;text-decoration:none">Blog &amp; guides</a></div>
        <div class="f-contact-row">🎁 <a href="/gift/" style="color:inherit;text-decoration:none">Gift certificates</a></div>
        <div class="f-contact-row">🔁 <a href="/subscription/" style="color:inherit;text-decoration:none">Handyman subscription</a></div>
        <div class="f-contact-row">📝 <a href="/posts/" style="color:inherit;text-decoration:none">Recent projects</a></div>
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
{GA_SNIPPET}
{extra}</head>
'''

def page(s):
    url = f'{DOMAIN}/services/{s["slug"]}/'
    city = s.get('city', 'Wesley Chapel')
    title = s.get('title') or f'{s["h1"]} in {city}, FL | Andrew Handyman Services'
    ld = {"@context":"https://schema.org","@type":"Service","name":f'{s["h1"]} in {city}, FL',"serviceType":s['h1'],
          "description":s['desc'],"url":url,
          "provider":{k:v for k,v in biz().items() if k!="@context"},
          "areaServed":[{"@type":"City","name":a} for a in AREAS]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":"Services","item":DOMAIN+"/#services"},
        {"@type":"ListItem","position":3,"name":s['h1'],"item":url}]}
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n<script type="application/ld+json">{json.dumps(bc)}</script>\n'
    bullets = ''.join(f'<li><span class="sp-check"></span><span>{esc(b)}</span></li>' for b in s['bullets'])
    if s['photo']:
        f, alt = s['photo']
        side = f'<figure class="sp-photo"><img src="/images/{f}" alt="{esc(alt)}" loading="lazy"><figcaption>{esc(s.get("photo_cap","Real job photo — before &amp; after"))}</figcaption></figure>'
    else:
        side = f'<div class="sp-side-card"><img src="{ICON(s)}" alt="" width="96" height="96"><h3>Free estimate</h3><p>Tell me what you need and I will get back to you within a few hours.</p><a class="btn-cta" href="/#home">Request an estimate</a><a class="sp-call" href="tel:{PHONE_TEL}">or call {PHONE_DISPLAY}</a></div>'
    if s['slug']=='christmas-light-installation':
        s = dict(s, faq=list(BL.FAQ)+[x for x in s['faq'] if x[0].startswith('Do you also serve')])
        extra += '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in s['faq']]})+'</script>\n'
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
    galsec = ''
    if s.get('gallery'):
        items = ''.join(f'<figure class="sp-gal-item reveal"><img src="/images/{f}" alt="{esc(a)}" loading="lazy"><figcaption>{esc(c)}</figcaption></figure>' for f,a,c in s['gallery'])
        galsec = f'<section class="sp-sec"><div class="section-wrap"><div class="reveal"><div class="section-tag">Real jobs</div><h2 class="section-title">{s.get("gallery_h","Recent TV &amp; <em>media walls</em>")}</h2></div><div class="sp-gal" style="--r:{s.get("gallery_r","3/4")}">{items}</div></div></section>'
        if s.get('more'): a_why, a_area, a_rel = ' sp-alt', '', ' sp-alt'
    areas_l = ', '.join(f'<a href="/locations/{l["slug"]}/">{esc(l["name"])}</a>' for l in LOCS)
    art = MD.ARTICLE.replace('{areas}', areas_l) if s.get('article') else ''
    estform = MD.FORM.replace('{PHONE_TEL}', PHONE_TEL).replace('{PHONE_DISPLAY}', PHONE_DISPLAY) if s.get('article') else ''
    guide = ''
    if s['slug']=='christmas-light-installation':
        toc = ''.join(f'<a href="#{i}">{esc(tt)}</a>' for i,tt in BL.TOC)
        gbody = BL.BODY.replace('{toc}', toc).replace('{calc}', BL.CALC)
        guide = f'''<section class="sp-sec sp-alt" id="guide"><div class="section-wrap"><article class="post">
<div class="section-tag">Complete guide</div>
<h2 class="section-title" style="margin-top:.2rem">Which Christmas lights are right for <em>your house?</em></h2>
<figure class="post-fig post-hero"><img src="/images/blog/{BL.HERO}" alt="{esc(BL.HERO_ALT)}" width="1400" height="1054" loading="lazy"></figure>
{gbody}</article></div></section>
'''
    elif s['slug'].startswith('christmas-light-installation'):
        guide = '<section class="sp-sec"><div class="section-wrap"><a class="post-card post-card-s" href="/services/christmas-light-installation/#guide"><div><span class="section-tag">Guide</span><h2>Not sure which lights to choose?</h2><p>Compare store-bought, permanent and professional C9 lights, see real jobs and use the cost calculator.</p><span class="svc-more">Read the complete guide →</span></div></a></div></section>\n'
    chips = ''.join(f'<span class="area-chip">{esc(a)}</span>' for a in AREAS)
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero{' sp-hero-xmas' if s['slug'].startswith('christmas-light-installation') else ''}"{" style=\"background-image:linear-gradient(90deg,rgba(6,12,24,.86) 0%,rgba(6,12,24,.55) 45%,rgba(6,12,24,.05) 100%),url('/images/blog/stucco-house-night.jpg')\"" if s['slug'].startswith('christmas-light-installation') else ''} >
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

{art}{guide}{more}{galsec}{estform}<section class="sp-sec{a_why}">
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


def loc_page(l):
    url = f'{DOMAIN}/locations/{l["slug"]}/'
    city = l['city']
    title = f'Handyman in {city}, FL | Andrew Handyman Services'
    desc = f'{l["intro"]} Free estimate: call or text (656) 231-1836.'
    if len(desc) > 300: desc = desc[:297].rsplit(' ',1)[0] + '...'
    faq = l['faq'] + [(f'How do I get a free estimate in {city}?', 'Fill in the request form on my website, or call or text (656) 231-1836. Photos help me give you a more accurate estimate. I usually get back to you within a few hours.')]
    ld = biz(city)
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":f"Handyman in {city}","item":url}]}
    extra = ''.join(f'<script type="application/ld+json">{json.dumps(x)}</script>\n' for x in (ld, fq, bc))
    cards = ''.join(f'<a href="/services/{r}/" class="svc-card"><div class="svc-emoji"><img src="{ICON(BY[r])}" alt="" width="62" height="62" loading="lazy"></div><div class="svc-name">{esc(BY[r]["name"])}</div><span class="svc-more">Learn more →</span></a>' for r in l['focus'])
    det = ''.join(f'<details class="sp-q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in faq)
    near = ''.join(f'<a class="area-chip about-svc" href="/locations/{n}/">{esc(next(x["city"] for x in LOCS if x["slug"]==n))}</a>' for n in l['near'])
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> Handyman in {esc(city)}</div>
      <h1 class="sp-h1">Handyman in <em>{esc(city)}, FL</em></h1>
      <p class="sp-lead">{esc(l["intro"])}</p>
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
      <div class="section-tag">{esc(l["group"])}</div>
      <h2 class="section-title">Your local handyman in <em>{esc(city)}</em></h2>
      <p class="sp-p">{esc(l["local"])}</p>
      <p class="sp-p">Every job starts with a free, clear estimate and is backed by my personal guarantee. If you are not completely satisfied with the work, I will make it right.</p>
    </div>
    <div class="reveal"><div class="sp-side-card"><img src="/images/img-01.png" alt="" width="96" height="96"><h3>Free estimate</h3><p>Tell me what you need and I will get back to you within a few hours.</p><a class="btn-cta" href="/#home">Request an estimate</a><a class="sp-call" href="tel:{PHONE_TEL}">or call {PHONE_DISPLAY}</a></div></div>
  </div>
</section>

<section class="sp-sec sp-alt">
  <div class="section-wrap">
    <div class="reveal">
      <div class="section-tag">Popular services</div>
      <h2 class="section-title">What I do in <em>{esc(city)}</em></h2>
    </div>
    <div class="sp-related">{cards}</div>
  </div>
</section>

<section class="sp-sec">
  <div class="section-wrap sp-two">
    <div class="reveal">
      <div class="section-tag">Questions</div>
      <h2 class="section-title">Good to <em>know</em></h2>
      <div class="sp-faq">{det}</div>
    </div>
    <div class="reveal">
      <div class="section-tag">Nearby</div>
      <h2 class="section-title">Also serving <em>nearby</em></h2>
      <p class="sp-p">Based in Wesley Chapel, I also work in:</p>
      <div class="area-chips">{near}</div>
      <p class="sp-p">Not sure I cover your address? Call or text {PHONE_DISPLAY} and I will let you know.</p>
    </div>
  </div>
</section>

<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Need a handyman in {esc(city)}?</h2>
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

def guide_page():
    url = f'{DOMAIN}/guides/{GD.SLUG}/'
    faq = ''.join(f'<details class="sp-q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in GD.FAQ)
    toc = ''.join(f'<a href="#{i}">{esc(t)}</a>' for i,t in GD.TOC)
    areas = ', '.join(f'<a href="/locations/{l["slug"]}/">{esc(l["name"])}</a>' for l in LOCS)
    body_html = GD.BODY.replace('{toc}', toc).replace('{areas}', areas).replace('{faq}', faq)
    art = {"@context":"https://schema.org","@type":"Article","headline":GD.TITLE,"description":GD.DESC,"datePublished":GD.DATE,"dateModified":GD.DATE,
           "mainEntityOfPage":url,"author":{"@type":"Person","name":"Andrew","url":DOMAIN+"/about/"},
           "publisher":{"@type":"Organization","name":"Andrew Handyman Services","url":DOMAIN+"/"}}
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in GD.FAQ]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":"How to find a handyman in Wesley Chapel","item":url}]}
    extra = ''.join(f'<script type="application/ld+json">{json.dumps(x)}</script>\n' for x in (art, fq, bc))
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> <a href="/blog/">Blog</a></div>
      <h1 class="sp-h1">{GD.H1}</h1>
      <p class="sp-lead">{esc(GD.LEAD)}</p>
      <div class="post-meta">By Andrew · Updated November 14, 2026</div>
    </div>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <article class="post">
      {body_html}
    </article>
  </div>
</section>
<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Need a hand around the house?</h2>
    <p class="cta-text">Send a quick request or text a photo of the job. Free estimate.</p>
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
    return head(GD.TITLE, GD.DESC, url, extra) + body

def article_page(a):
    import datetime as _dt
    a = dict(a, date_h=_dt.date.fromisoformat(a['date']).strftime('%B %-d, %Y'))
    url =f'{DOMAIN}/guides/{a["slug"]}/'
    faq = ''.join(f'<details class="sp-q"><summary>{esc(q)}</summary><p>{esc(x)}</p></details>' for q,x in a['faq'])
    toc = ''.join(f'<a href="#{i}">{esc(t)}</a>' for i,t in a['toc'])
    areas = ', '.join(f'<a href="/locations/{l["slug"]}/">{esc(l["name"])}</a>' for l in LOCS)
    body_html = a['body'].replace('{toc}', toc).replace('{areas}', areas).replace('{faq}', faq)
    body_html = body_html.replace('<table class="post-table">', '<div class="post-table-wrap"><table class="post-table">').replace('</table>', '</table></div>')
    hero = f'<figure class="post-hero"><img src="/images/{a["hero"]}" alt="{esc(a["hero_alt"])}" width="1200" height="800" loading="eager"></figure>'
    body_html = hero + body_html
    img = f'{DOMAIN}/images/{a["hero"]}'
    art = {"@context":"https://schema.org","@type":"Article","headline":a['title'],"description":a['desc'],"image":img,"datePublished":a['date'],"dateModified":a['date'],
           "mainEntityOfPage":url,"author":{"@type":"Person","name":"Andrew","url":DOMAIN+"/about/"},
           "publisher":{"@type":"Organization","name":"Andrew Handyman Services","url":DOMAIN+"/"}}
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":x}} for q,x in a['faq']]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":a['title'],"item":url}]}
    extra = ''.join(f'<script type="application/ld+json">{json.dumps(x)}</script>\n' for x in (art, fq, bc))
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> <a href="/blog/">Blog</a></div>
      <h1 class="sp-h1">{a['h1']}</h1>
      <p class="sp-lead">{esc(a['lead'])}</p>
      <div class="post-meta">By Andrew · Updated {a['date_h']}</div>
    </div>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <article class="post">
      {body_html}
    </article>
  </div>
</section>
<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Need a hand around the house?</h2>
    <p class="cta-text">Send a quick request or text a photo of the job. Free estimate.</p>
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
    return head(a['title'], a['desc'], url, extra) + body

def post_page(pr):
    url = f'{DOMAIN}/posts/{pr["slug"]}/'
    paras = ''.join(f'<p>{esc(x)}</p>' for x in pr['paras'])
    faq = ''.join(f'<details class="sp-q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in pr['faq'])
    others = ''.join(f'<li><a href="/posts/{o["slug"]}/">{esc(o["title"])}</a></li>' for o in PD.PROJECTS if o['slug'] != pr['slug'])
    art = {"@context":"https://schema.org","@type":"BlogPosting","headline":pr['title'],"description":pr['desc'],"datePublished":pr['date'],"dateModified":pr['date'],
           "mainEntityOfPage":url,"author":{"@type":"Person","name":"Andrew","url":DOMAIN+"/about/"},
           "publisher":{"@type":"Organization","name":"Andrew Handyman Services","url":DOMAIN+"/"},"sameAs":[PD.GBP]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":"Posts","item":DOMAIN+"/posts/"},
        {"@type":"ListItem","position":3,"name":pr['title'],"item":url}]}
    extra = ''.join(f'<script type="application/ld+json">{json.dumps(x)}</script>\n' for x in (art, bc))
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> <a href="/posts/">Posts</a></div>
      <h1 class="sp-h1">{esc(pr['title'])}</h1>
      <div class="post-meta">By Andrew · {pr['date']}</div>
    </div>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <article class="post">
      {paras}
      <p><a href="/services/{pr['service']}/">More about {esc(pr['svc_name'])} →</a></p>
      <h2>Quick question</h2>
      {faq}
      <p>This project was also posted on my <a href="{PD.GBP}" target="_blank" rel="noopener">Google Business Profile</a>.</p>
      <h2>More recent projects</h2>
      <ul>{others}</ul>
    </article>
  </div>
</section>
<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Have a similar project?</h2>
    <p class="cta-text">Send a quick request or text a photo of the job. Free estimate.</p>
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
    return head(pr['title'] + ' | Andrew Handyman Services', pr['desc'], url, extra) + body

def posts_index():
    url = f'{DOMAIN}/posts/'
    cards = ''.join(f'<li><a href="/posts/{o["slug"]}/"><strong>{esc(o["title"])}</strong></a><br><span>{o["date"]} · {esc(o["svc_name"])}</span></li>' for o in PD.PROJECTS)
    title = 'Recent Projects & Updates | Andrew Handyman Services Wesley Chapel'
    desc = 'Recent handyman projects in Wesley Chapel and Tampa Bay: media walls, custom shelving, accent panels, furniture assembly and hurricane shutters.'
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},{"@type":"ListItem","position":2,"name":"Posts","item":url}]}
    extra = f'<script type="application/ld+json">{json.dumps(bc)}</script>\n'
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> Posts</div>
      <h1 class="sp-h1">Recent projects <em>&amp; updates</em></h1>
      <p class="sp-lead">What I have been working on around Wesley Chapel and Tampa Bay. The same updates are on my <a href="{PD.GBP}" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline">Google Business Profile</a>.</p>
    </div>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <article class="post"><ul>{cards}</ul></article>
  </div>
</section>
</main>
{footer_html()}
<script src="/site.js?v={VER}" defer></script>
</body>
</html>
'''
    return head(title, desc, url, extra) + body

def blog_cards():
    """All blog entries: long guides first, then project posts."""
    items = [(f'/guides/{a["slug"]}/', a['title'], a['lead'], f'/images/{a["hero"]}', a['hero_alt'], 'Guide') for a in AD.ARTICLES]
    items.append((f'/guides/{GD.SLUG}/', GD.TITLE, GD.LEAD, '/images/hero-andrew.jpg', 'Andrew, handyman in Wesley Chapel', 'Guide'))
    cards = ''.join(f'<a class="blog-card" href="{u}"><img src="{i}" alt="{esc(al)}" width="600" height="400" loading="lazy"><div class="blog-card-b"><span class="blog-tag">{tag}</span><h3>{esc(t)}</h3><p>{esc(l)}</p><span class="blog-more">Read the guide →</span></div></a>' for u,t,l,i,al,tag in items)
    cards += ''.join(f'<a class="blog-card blog-card-text" href="/posts/{o["slug"]}/"><div class="blog-card-b"><span class="blog-tag">Project · {o["date"]}</span><h3>{esc(o["title"])}</h3><p>{esc(o["svc_name"])}</p><span class="blog-more">Read more →</span></div></a>' for o in PD.PROJECTS)
    return cards

def blog_page():
    url = f'{DOMAIN}/blog/'
    title = 'Handyman Blog: Guides, Costs & Projects | Andrew Handyman Wesley Chapel'
    desc = 'Practical handyman guides for Florida homeowners: media wall costs, how to mount a TV, how to hire a handyman, plus recent projects in Wesley Chapel and Tampa Bay.'
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},{"@type":"ListItem","position":2,"name":"Blog","item":url}]}
    extra = f'<script type="application/ld+json">{json.dumps(bc)}</script>\n'
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> Blog</div>
      <h1 class="sp-h1">Handyman <em>blog</em></h1>
      <p class="sp-lead">Straight answers on costs, how-tos and real projects from Wesley Chapel and Tampa Bay.</p>
    </div>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <div class="blog-grid">{blog_cards()}</div>
  </div>
</section>
<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Have a project in mind?</h2>
    <p class="cta-text">Send a quick request or text a photo of the job. Free estimate.</p>
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

# Stripe Payment Links for the subscription plans. Paste the permanent links here; until then the buttons call.
SUB_LINKS = {'basic': '', 'plus': '', 'home': ''}

SUB_FAQ = [
 ("How does the handyman subscription work?","You pick a plan, send me your list or a quick request, and we schedule the time. You can also set one fixed day every month and I come by on that date. Call or text (656) 231-1836 to start."),
 ("What counts as a visit?","A visit is one trip to your home with the hours of work included in your plan. The hours are what matter. On the larger plans you can split them into several shorter visits, or use them for one bigger job."),
 ("Do unused hours roll over?","Yes. Hours you do not use roll over to the next month, for up to 3 months in a row. Save them up and a bigger job fits even on the smallest plan."),
 ("What if a job needs more hours than I have?","Extra hours are agreed in advance and depend on the cost of the work. I tell you what the job needs before I start, so there are no surprises."),
 ("What jobs are covered?","Everyday small repairs and installs, the same work I do now: TV mounting, picture hanging, furniture assembly, door and drywall fixes, painting touch-ups, changing light bulbs, tightening loose hardware and similar jobs. Work that legally needs a licensed electrician or plumber is not part of it."),
 ("Can I set it up for a parent or relative?","Yes, that is one of the main reasons for the plan. You can arrange regular help for someone who lives nearby or far away, so small repairs do not pile up."),
 ("Can I still book a single job?","Of course. One-time jobs work exactly as before: send a request or text a photo and you get a free estimate."),
]

def subscription_page():
    url = f'{DOMAIN}/subscription/'
    title = 'Handyman Subscription Wesley Chapel FL – Monthly Plans from $99'
    desc = 'Handyman subscription in Wesley Chapel, FL: monthly plans from $99 for repairs, installs and home upkeep. Hours roll over. Andrew Handyman Services.'
    faq = ''.join(f'<details class="sp-q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in SUB_FAQ)
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in SUB_FAQ]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},{"@type":"ListItem","position":2,"name":"Handyman subscription","item":url}]}
    extra = ''.join(f'<script type="application/ld+json">{json.dumps(x)}</script>\n' for x in (fq, bc))
    why = [("🧰","Nothing to search for","No more hunting for a handyman, comparing quotes or waiting for callbacks. You send a request and it is handled."),
           ("📅","Visits on your schedule","Book a time when you need it, or fix one day every month and I come by on that date."),
           ("💵","Predictable monthly cost","One flat price a month instead of a surprise bill each time. Unused hours roll over, so nothing goes to waste."),
           ("🏠","One person who knows your home","The same handyman every time. I already know your house, so small problems get caught early."),
           ("👪","Great for family","Set it up for a parent or relative and keep their home in order, even if you live far away."),
           ("🎯","Big job? Save up","Hours roll over for up to 3 months, so even the smallest plan can cover a larger project.")]
    def order_btn(k):
        link = SUB_LINKS.get(k)
        if link: return f'<a href="{link}" class="btn-cta" target="_blank" rel="noopener">Order now</a>'
        return f'<a href="tel:{PHONE_TEL}" class="btn-cta">Order now</a>'
    wc = ''.join(f'<div class="sp-why-card reveal"><div class="wc-icon">{i}</div><b>{esc(t)}</b><p>{esc(p)}</p></div>' for i,t,p in why)
    steps = [("1","Pick a plan","Basic, Plus or Home, whichever fits your house. You can change plans later."),
             ("2","Send your list","Text or call with what needs doing. Photos help. We pick the time, or a fixed day each month."),
             ("3","I come and fix it","I show up, take care of the list, check the little things and keep your home in order.")]
    sc = ''.join(f'<div class="sp-why-card reveal"><div class="wc-icon">{n}</div><b>{esc(t)}</b><p>{esc(p)}</p></div>' for n,t,p in steps)
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> Handyman subscription</div>
      <h1 class="sp-h1">Your home, taken care of. <em>Every month.</em></h1>
      <p class="sp-lead">Handyman subscription in Wesley Chapel, FL. Send a request, pick a time, and it is done. Or choose one day each month and I come by to fix, check and tighten whatever your home needs. Plans start at $99 a month.</p>
      <div class="sp-actions">
        <a class="btn-cta" href="tel:{PHONE_TEL}">📞 Call {PHONE_DISPLAY}</a>
        <a class="btn-ghost-cta" href="sms:{PHONE_TEL}">💬 Text to start</a>
      </div>
    </div>
    <div class="sp-hero-icon"><img src="/images/hero-andrew.jpg" alt="Andrew, owner of Andrew Handyman Services, giving a thumbs up" width="280" height="301" style="border-radius:22px;width:min(280px,100%);height:auto"></div>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">Why a subscription</div><h2 class="section-title">Stop searching. <em>Start relaxing.</em></h2></div>
    <p class="sp-intro">Most homes do not need one big repair. They need a steady trickle of small ones: a loose door, a burnt-out bulb, a TV to mount, a shelf, a patch of paint. People put them off because finding someone each time is a hassle. With a subscription it is one number to text and one person who already knows your house.</p>
    <div class="sp-why">{wc}</div>
  </div>
</section>
<section class="sp-sec sp-alt">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">Plans</div><h2 class="section-title">Pick your <em>monthly plan</em></h2></div>
    <div class="sub-plans">
      <div class="sub-plan">
        <h3>Basic</h3>
        <div class="sub-price">$99<small> / month</small></div>
        <div class="sub-hours">Up to 2 hours a month</div>
        <ul><li>1 visit a month</li><li>A look at what needs fixing</li><li>Small repairs and installs</li></ul>
        {order_btn('basic')}
      </div>
      <div class="sub-plan pop">
        <h3>Plus</h3>
        <div class="sub-price">$199<small> / month</small></div>
        <div class="sub-hours">Up to 4 hours a month</div>
        <ul><li>Up to 2 visits a month</li><li>A look at what needs fixing</li><li>Small repairs and installs</li></ul>
        {order_btn('plus')}
      </div>
      <div class="sub-plan">
        <h3>Home</h3>
        <div class="sub-price">$299<small> / month</small></div>
        <div class="sub-hours">Up to 6 hours a month</div>
        <ul><li>Up to 3 visits a month</li><li>Or one larger job</li><li>Small repairs and installs</li></ul>
        {order_btn('home')}
      </div>
    </div>
    <p class="sp-intro"><strong>Hours roll over.</strong> Unused hours carry over to the next month, for up to 3 months in a row, so you can save up for a bigger job on any plan. Extra hours beyond your plan are agreed in advance, depending on the cost of the work.</p>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">How it works</div><h2 class="section-title">Three steps, <em>zero hassle</em></h2></div>
    <div class="sp-why">{sc}</div>
  </div>
</section>
<section class="sp-sec sp-alt">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">A monthly visit</div><h2 class="section-title">What I can do <em>on my visit</em></h2></div>
    <article class="post">
      <p>On a set day each month I come by and go through your list. Typical jobs: changing light bulbs, tightening loose handles, hinges and hardware, <a href="/services/tv-shelf-mounting/">mounting a TV or shelf</a>, <a href="/services/picture-hanging/">hanging pictures</a>, <a href="/services/furniture-assembly/">assembling furniture</a>, fixing a sticking <a href="/services/door-installation/">door</a>, patching small holes in <a href="/services/drywall-repair/">drywall</a> and <a href="/services/painting/">painting touch-ups</a>. I also look around for small problems before they grow. Jobs that legally require a licensed electrician or plumber are not part of the plans.</p>
    </article>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">FAQ</div><h2 class="section-title">Questions <em>about plans</em></h2></div>
    <div class="sp-faq">{faq}</div>
  </div>
</section>
<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Ready to stop worrying about repairs?</h2>
    <p class="cta-text">Call or text, pick your plan and your day. I will take it from there.</p>
    <div class="cta-btns">
      <a href="tel:{PHONE_TEL}" class="btn-cta">📞 Call {PHONE_DISPLAY}</a>
      <a href="sms:{PHONE_TEL}" class="btn-ghost-cta">💬 Text to start</a>
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

# Stripe Payment Links for gift certificates (after payment, redirect each to /gift/redeem/?amount=<value>)
GIFT_AMOUNTS = [145, 285, 478]
GIFT_LINKS = {145: '', 285: '', 478: ''}
GIFT_FAQ = [
 ("How does a gift certificate work?","You buy a certificate for $145, $285 or $478. Right after payment you fill in a short form with the address where the work will be done and what help is needed, and I contact the person to schedule a time. It works like a regular request, except the work is already paid for."),
 ("Who fills in the form, me or the person receiving the gift?","Either. You can fill it in right after you pay, or pass the link to the person you are gifting and they fill in their own address and details."),
 ("What can the certificate be used for?","Everyday handyman work: TV and shelf mounting, picture hanging, furniture assembly, door and drywall repairs, painting touch-ups and similar jobs. Work that legally needs a licensed electrician or plumber is not included."),
 ("What if the job costs more than the certificate?","I tell you what the job needs before I start. If it costs more, the difference is agreed in advance. No surprises."),
 ("Is this a good gift for a parent or an older relative?","Yes, it is one of the main reasons for it. It helps someone who needs a hand around the house without them having to look for a handyman or ask for favors."),
]

def gift_page():
    url = f'{DOMAIN}/gift/'
    title = 'Handyman Gift Certificate Wesley Chapel FL – $145, $285, $478'
    desc = 'Give the gift of a fixed-up home: handyman gift certificates in Wesley Chapel, FL for parents, family and friends. Andrew Handyman Services.'
    faq = ''.join(f'<details class="sp-q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in GIFT_FAQ)
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in GIFT_FAQ]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},{"@type":"ListItem","position":2,"name":"Gift certificates","item":url}]}
    extra = ''.join(f'<script type="application/ld+json">{json.dumps(x)}</script>\n' for x in (fq, bc))
    def buy(a):
        l = GIFT_LINKS.get(a)
        if l: return f'<a href="{l}" class="btn-cta" target="_blank" rel="noopener">Buy now</a>'
        return f'<a href="tel:{PHONE_TEL}" class="btn-cta">Buy now</a>'
    cards = ''.join(f'''<div class="sub-plan{' pop' if a==285 else ''}"><h3>Gift certificate</h3><div class="sub-price">${a}</div><div class="sub-hours">toward handyman work</div><ul><li>Any everyday repair or install</li><li>Pay now, schedule later</li><li>For one address of your choice</li></ul>{buy(a)}</div>''' for a in GIFT_AMOUNTS)
    why = [("🎁","A gift that actually helps","No more socks. Give someone a fixed door, a mounted TV or a finished to-do list."),
           ("👪","Perfect for parents","Help a parent or grandparent who needs a hand around the house, even if you live far away."),
           ("🏡","New homeowners","Housewarming present for people who just moved in and have a list of small jobs."),
           ("🤝","No searching for anyone","The person you gift does not have to find or vet a handyman. I take care of it.")]
    wc = ''.join(f'<div class="sp-why-card reveal"><div class="wc-icon">{i}</div><b>{esc(t)}</b><p>{esc(p)}</p></div>' for i,t,p in why)
    steps = [("1","Choose an amount","$145, $285 or $478, toward any everyday handyman job."),
             ("2","Pay online","Secure checkout. Right after payment you are taken to a short form."),
             ("3","Add the address","Fill in where the work is and what is needed, or pass the link to the person you are gifting. I contact them and schedule a time.")]
    sc = ''.join(f'<div class="sp-why-card reveal"><div class="wc-icon">{n}</div><b>{esc(t)}</b><p>{esc(p)}</p></div>' for n,t,p in steps)
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> Gift certificates</div>
      <h1 class="sp-h1">Give the gift of a <em>fixed-up home</em></h1>
      <p class="sp-lead">A handyman gift certificate for family, friends or anyone who could use a hand around the house. Pick an amount, pay online, and I take care of the rest.</p>
      <div class="sp-actions"><a class="btn-cta" href="#amounts">Choose an amount</a><a class="btn-ghost-cta" href="tel:{PHONE_TEL}">📞 {PHONE_DISPLAY}</a></div>
    </div>
    <div class="sp-hero-icon"><img src="/images/hero-andrew.jpg" alt="Andrew, owner of Andrew Handyman Services, giving a thumbs up" width="280" height="301" style="border-radius:22px;width:min(280px,100%);height:auto"></div>
  </div>
</section>
<section class="sp-sec" id="amounts">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">Certificates</div><h2 class="section-title">Pick an <em>amount</em></h2></div>
    <div class="sub-plans">{cards}</div>
  </div>
</section>
<section class="sp-sec sp-alt">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">Why give it</div><h2 class="section-title">A present <em>that gets used</em></h2></div>
    <div class="sp-why">{wc}</div>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">How it works</div><h2 class="section-title">Three steps, <em>zero hassle</em></h2></div>
    <div class="sp-why">{sc}</div>
  </div>
</section>
<section class="sp-sec sp-alt">
  <div class="section-wrap">
    <div class="reveal"><div class="section-tag">FAQ</div><h2 class="section-title">Questions <em>about gifts</em></h2></div>
    <div class="sp-faq">{faq}</div>
  </div>
</section>
<section class="cta-wrap">
  <div class="cta-inner">
    <h2 class="cta-title">Know someone who needs a hand?</h2>
    <p class="cta-text">Questions about a gift? Call or text and I will help.</p>
    <div class="cta-btns">
      <a href="#amounts" class="btn-cta">Choose an amount</a>
      <a href="sms:{PHONE_TEL}" class="btn-ghost-cta">💬 Text me</a>
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

def redeem_page():
    url = f'{DOMAIN}/gift/redeem/'
    extra = '''<meta name="robots" content="noindex, nofollow">
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>emailjs.init({ publicKey: "AWfp-WF5xgbFiPQ3a" });</script>
<style>.gf label{display:block;font-weight:600;margin:14px 0 6px}.gf input,.gf textarea,.gf select{width:100%;padding:12px 14px;border:1px solid #d9cfbd;border-radius:10px;font:inherit;background:#fff}.gf textarea{min-height:110px}.gf .row{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media(max-width:640px){.gf .row{grid-template-columns:1fr}}.gf .btn-cta{border:0;cursor:pointer;margin-top:22px}.gf-ok{display:none;padding:24px;border-radius:14px;background:#e8f5ec;border:1px solid #bfe3c9}</style>
'''
    body = f'''<body>
{nav_html()}
<main>
<section class="sp-hero">
  <div class="section-wrap sp-hero-inner">
    <div>
      <div class="sp-crumbs"><a href="/">Home</a> <span>›</span> <a href="/gift/">Gift certificates</a></div>
      <h1 class="sp-h1">Schedule your <em>gift certificate</em></h1>
      <p class="sp-lead">Thank you! Tell me where the work will be done and what is needed, and I will contact you to schedule a time. <span id="gAmt"></span></p>
    </div>
  </div>
</section>
<section class="sp-sec">
  <div class="section-wrap">
    <div id="gOk" class="gf-ok"><h2>Request received</h2><p>Thank you. I will contact you soon to schedule a time. If you need me sooner, call or text {PHONE_DISPLAY}.</p></div>
    <form id="gForm" class="gf" onsubmit="return gSend(event)" style="max-width:720px">
      <div class="row">
        <div><label for="gbuyer">Your name (who bought the certificate)</label><input id="gbuyer" required></div>
        <div><label for="gbemail">Your email (used at checkout)</label><input id="gbemail" type="email" required></div>
      </div>
      <div class="row">
        <div><label for="gwho">Who will receive the service (name)</label><input id="gwho" required></div>
        <div><label for="gphone">Phone number for scheduling</label><input id="gphone" type="tel" required></div>
      </div>
      <label for="gaddr">Address where the work will be done</label><input id="gaddr" required placeholder="Street, city, ZIP">
      <label for="gneed">What help is needed</label><textarea id="gneed" required placeholder="For example: mount a TV, hang shelves, fix a door"></textarea>
      <label for="gtime">Preferred days or times (optional)</label><input id="gtime">
      <button class="btn-cta" type="submit" id="gBtn">Send my request</button>
    </form>
  </div>
</section>
</main>
{footer_html()}
<script src="/site.js?v={VER}" defer></script>
<script>
var AM={{145:1,285:1,478:1}}, q=new URLSearchParams(location.search).get('amount'), amt=AM[q]?q:'';
if(amt)document.getElementById('gAmt').textContent='Certificate: $'+amt+'.';
function gSend(e){{e.preventDefault();var b=document.getElementById('gBtn');b.disabled=true;b.textContent='Sending...';
var v=function(i){{return document.getElementById(i).value.trim()}};
var msg='*** PAID GIFT CERTIFICATE'+(amt?' $'+amt:'')+' (confirm payment in Stripe by buyer email) ***\\n\\nBuyer: '+v('gbuyer')+' <'+v('gbemail')+'>\\nRecipient: '+v('gwho')+'\\nPhone: '+v('gphone')+'\\nAddress: '+v('gaddr')+'\\nPreferred time: '+(v('gtime')||'not specified')+'\\n\\nHelp needed:\\n'+v('gneed');
emailjs.send('service_984008h','template_5dybn6g',{{from_name:'[GIFT'+(amt?' $'+amt:'')+' PAID] '+v('gwho'),phone:v('gphone'),message:msg,reply_to:v('gbemail')}})
.then(function(){{document.getElementById('gForm').style.display='none';document.getElementById('gOk').style.display='block';window.scrollTo(0,0)}})
.catch(function(){{b.disabled=false;b.textContent='Send my request';alert('Something went wrong. Please call us directly at {PHONE_DISPLAY}')}});return false}}
</script>
</body>
</html>
'''
    return head('Schedule Your Gift Certificate | Andrew Handyman Services', 'Schedule your handyman gift certificate.', url, extra) + body

def main():
    for s in S:
        d = os.path.join('services', s['slug'])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(s))
    for l in LOCS:
        d = os.path.join('locations', l['slug']); os.makedirs(d, exist_ok=True)
        open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(loc_page(l))
    os.makedirs('about', exist_ok=True)
    open('about/index.html','w',encoding='utf-8').write(about_page())
    os.makedirs('guides/'+GD.SLUG, exist_ok=True)
    open('guides/'+GD.SLUG+'/index.html','w',encoding='utf-8').write(guide_page())
    for a in AD.ARTICLES:
        os.makedirs('guides/'+a['slug'], exist_ok=True)
        open('guides/'+a['slug']+'/index.html','w',encoding='utf-8').write(article_page(a))
    os.makedirs('blog', exist_ok=True)
    open('blog/index.html','w',encoding='utf-8').write(blog_page())
    os.makedirs('gift/redeem', exist_ok=True)
    open('gift/index.html','w',encoding='utf-8').write(gift_page())
    open('gift/redeem/index.html','w',encoding='utf-8').write(redeem_page())
    os.makedirs('subscription', exist_ok=True)
    open('subscription/index.html','w',encoding='utf-8').write(subscription_page())
    os.makedirs('posts', exist_ok=True)
    open('posts/index.html','w',encoding='utf-8').write(posts_index())
    for pr in PD.PROJECTS:
        os.makedirs('posts/'+pr['slug'], exist_ok=True)
        open('posts/'+pr['slug']+'/index.html','w',encoding='utf-8').write(post_page(pr))
    os.makedirs('faq', exist_ok=True)
    open('faq/index.html','w',encoding='utf-8').write(faq_page())
    urls = [DOMAIN + '/', DOMAIN + '/faq/', DOMAIN + '/about/', f'{DOMAIN}/guides/{GD.SLUG}/',] + [f'{DOMAIN}/guides/{a["slug"]}/' for a in AD.ARTICLES] + [f'{DOMAIN}/blog/', f'{DOMAIN}/subscription/', f'{DOMAIN}/gift/', f'{DOMAIN}/posts/'] + [f'{DOMAIN}/posts/{p["slug"]}/' for p in PD.PROJECTS] + [f'{DOMAIN}/services/{s["slug"]}/' for s in S] + [f'{DOMAIN}/locations/{l["slug"]}/' for l in LOCS]
    import re as _re, html as _html
    def _imgs(u):
        path = u.replace(DOMAIN, '').strip('/')
        f = os.path.join(path, 'index.html') if path else 'index.html'
        try: h = open(f, encoding='utf-8').read()
        except OSError: return ''
        seen, out = set(), ''
        for tag in _re.findall(r'<img[^>]*>', h):
            s = _re.search(r'src="/?(images/[^"]+\.jpg)"', tag); a = _re.search(r'alt="([^"]*)"', tag)
            if not s or s.group(1) in seen or s.group(1).endswith('-sq.jpg'): continue
            seen.add(s.group(1))
            cap = f'<image:title>{_html.escape(_html.unescape(a.group(1)))}</image:title>' if a and a.group(1) else ''
            out += f'<image:image><image:loc>{DOMAIN}/{s.group(1)}</image:loc>{cap}</image:image>'
        return out
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + ''.join(f'  <url><loc>{u}</loc><lastmod>2026-11-15</lastmod>{_imgs(u)}</url>\n' for u in urls) + '</urlset>\n'
    open('sitemap.xml', 'w').write(sm)

    # --- AI / search discovery files ---
    svc_lines = '\n'.join(f'- [{x["name"]}]({DOMAIN}/services/{x["slug"]}/): {x["lead"]}' for x in S if not x.get('hidden'))
    loc_lines = '\n'.join(f'- [{l["city"]}]({DOMAIN}/locations/{l["slug"]}/)' for l in LOCS)
    art_lines = '\n'.join(f'- [{a["title"]}]({DOMAIN}/guides/{a["slug"]}/)' for a in AD.ARTICLES)
    post_lines = '\n'.join(f'- [{o["title"]}]({DOMAIN}/posts/{o["slug"]}/)' for o in PD.PROJECTS)
    llms = f"""# Andrew Handyman Services

> Handyman services in Wesley Chapel, Florida and the northern Tampa Bay area (Land O' Lakes, Zephyrhills, Dade City, New Tampa, Lutz, Odessa, Tampa). Run by Andrew, a local handyman. Free estimates. Phone and text: {PHONE_DISPLAY}. Website: {DOMAIN}/

Notes: Andrew does not do work that legally requires a licensed electrician or plumber. Prices are listed only where stated below; otherwise estimates are free.

## Services
{svc_lines}

## Pricing published on the site
- Media & accent walls: accent wall with TV mounting and mantel from $1,500; full media wall typically $3,500 to $4,000; large custom projects $6,000 to $10,000+. See {DOMAIN}/services/media-accent-walls/
- Handyman subscription: Basic $99/month (up to 2 hours), Plus $199/month (up to 4 hours), Home $299/month (up to 6 hours). Unused hours roll over for up to 3 months. See {DOMAIN}/subscription/
- Gift certificates: $145, $285 or $478 toward handyman work. See {DOMAIN}/gift/

## Service areas
{loc_lines}

## Guides and recent projects
- [How to find a handyman in Wesley Chapel]({DOMAIN}/guides/{GD.SLUG}/)
{art_lines}
- [Christmas light installation guide and cost calculator]({DOMAIN}/services/christmas-light-installation/#guide)
- [Blog]({DOMAIN}/blog/)
- [Recent projects]({DOMAIN}/posts/)
{post_lines}

## About and contact
- [About Andrew]({DOMAIN}/about/)
- [FAQ]({DOMAIN}/faq/)
- [Google Business Profile]({GBP_URL})
- Phone and text: {PHONE_DISPLAY}
"""
    open('llms.txt', 'w', encoding='utf-8').write(llms)
    bots = ['OAI-SearchBot', 'ChatGPT-User', 'GPTBot', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'Google-Extended', 'Applebot-Extended', 'Bingbot', 'Googlebot']
    rb = 'User-agent: *\nAllow: /\n\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots) + f'Sitemap: {DOMAIN}/sitemap.xml\n'
    open('robots.txt', 'w').write(rb)
    open('tools/_nav.html', 'w', encoding='utf-8').write(nav_html())
    open('tools/_footer.html', 'w', encoding='utf-8').write(footer_html())
    print('built', len(S), 'service pages')

if __name__ == '__main__':
    main()
