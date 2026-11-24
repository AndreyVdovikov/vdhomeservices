# TV mounting cost calculator page. ALL PRICES LIVE HERE (single source of truth, injected into the page JS).
SLUG = 'tv-mounting-cost-calculator'
TITLE = 'TV Mounting Cost Calculator – Wesley Chapel, FL | Andrew Handyman'
DESC = 'Instant TV mounting price for Wesley Chapel and Tampa Bay: pick your TV size, wall type and extras, see the cost, the right mounting height and the TV dimensions. Free estimate: (656) 231-1836.'
H1 = 'TV Mounting <em>Cost Calculator</em>'
LEAD = 'Pick your TV size, the wall and any extras, and get a price in seconds, plus the screen dimensions and the right height to hang it. Final price is always confirmed before any work starts.'

# Base price by screen size (diagonal, inches). Source: Andrey. 'upto' is inclusive.
TIERS = [
    {'upto': 55,  'price': 80,  'label': 'Up to 55"'},
    {'upto': 65,  'price': 120, 'label': '56" to 65"'},
    {'upto': 85,  'price': 150, 'label': '66" to 85"'},
    {'upto': 999, 'price': 250, 'label': '86" and larger'},
]
SIZES = [32, 43, 50, 55, 65, 75, 85, 98]
MASONRY_PCT = 10   # concrete / brick / block / stone: +10%

# Extras. NOTE: prices are PLACEHOLDERS until Andrey confirms them.
ADDONS = [
    {'id': 'cords',  'name': 'Cord cover on the wall', 'note': 'Paintable raceway hides the cables', 'price': 25},
    {'id': 'inwall', 'name': 'Hide low-voltage cables in the wall', 'note': 'HDMI and similar cables only, no power', 'price': 60},
    {'id': 'bar',    'name': 'Soundbar mounting', 'note': 'Bracket under or beside the TV', 'price': 30},
    {'id': 'mount',  'name': 'I bring the mount (tilt)', 'note': 'Tilting bracket included in the price', 'price': 45},
    {'id': 'mountf', 'name': 'I bring the mount (full-motion)', 'note': 'Swivel and pull-out arm included', 'price': 85},
]
# 'mount' and 'mountf' are mutually exclusive in the UI.

INTRO = [
 "Most TV mounting jobs in Wesley Chapel, Land O' Lakes and Lutz are the same few decisions: how big the screen is, what the wall is made of, and whether you want the cables out of sight. This calculator turns those choices into a price, so you know where you stand before you pick up the phone.",
 "The base price depends on the screen size, because bigger TVs are heavier, need a stronger bracket and take two people to lift. Standard drywall with wood studs is the baseline. Concrete, brick, block and stone walls take longer and need masonry anchors, so they add ten percent. Everything else is optional and shown as a separate line, so you can see exactly what each extra costs.",
]

HOW_H = 'How the price is calculated'
HOW = [
 "The base price is set by the diagonal size of the screen: up to 55 inches is $80, 56 to 65 inches is $120, 66 to 85 inches is $150, and anything larger, including 98 and 100 inch screens, is $250. A concrete, brick or block wall adds ten percent to the total. Extra TVs in the same visit are priced the same way, one line each.",
 "The number you see is an estimate. Hidden problems such as a plaster wall, a tile backsplash or a bracket that does not fit the TV can change the job, and I always tell you about that before I start. If you send a photo of the wall and the TV model, I can usually confirm the price in a few minutes.",
]

SIZE_H = 'TV sizes in inches: width, height and mounting height'
SIZE_P = [
 "People search for TV dimensions all the time, because the diagonal size on the box says nothing about the wall space you need. The table below uses the standard 16:9 shape of modern TVs. The recommended center height puts the middle of the screen at about 42 to 45 inches from the floor for a living room where you sit on a sofa, which is a comfortable eye level. In a bedroom, where you watch lying down, mount it a little higher.",
 "Viewing distance matters as much as size. For a 4K TV, sitting about one and a half times the diagonal away is a good starting point, and closer than that is fine for 4K because the picture stays sharp. The calculator above shows the distance range for the size you pick.",
]

FAQ = [
 ("How much does TV mounting cost in Wesley Chapel, FL?", "For a standard drywall wall, I charge $80 for TVs up to 55 inches, $120 for 56 to 65 inch TVs, $150 for 66 to 85 inch TVs and $250 for 86 inch and larger screens. Concrete, brick or block walls add ten percent, and extras such as hiding cables or mounting a soundbar are priced separately."),
 ("Do I need to buy the TV mount myself?", "You can, and it is the cheapest way. Buy a bracket rated for your TV size and weight and I will install it. If you prefer, I bring a tilt or full-motion mount, and the calculator shows the added cost."),
 ("Can you hide the TV cables?", "Yes, in two ways. A paintable cord cover on the wall is quick and inexpensive. For a cleaner look I can route low-voltage cables such as HDMI inside the wall. I do not do electrical work, so if you want a power outlet moved behind the TV, that part needs a licensed electrician."),
 ("What height should I mount my TV?", "For a living room where you sit on a sofa, put the center of the screen at about 42 to 45 inches from the floor. Above a fireplace the TV usually ends up higher, so a tilting or pull-down mount helps. The calculator shows the center height and the bottom edge for your TV size."),
 ("Can you mount a TV on a brick or concrete wall?", "Yes. These walls need masonry drilling and special anchors, which takes longer, so the price is ten percent higher than on drywall."),
 ("Do you mount TVs on a lanai or outdoors?", "Yes, many Florida homes have a TV on a screened lanai. Use an outdoor-rated TV or a protected spot, and tell me about the wall type when you request the price."),
 ("How long does it take?", "Most single TV jobs take about an hour. Larger screens, masonry walls and hidden cables take longer."),
]
