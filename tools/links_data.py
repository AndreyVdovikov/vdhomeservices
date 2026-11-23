# Internal-linking map: which guides relate to which services / posts / guides.
G_MEDIA = 'media-wall-cost-wesley-chapel'
G_TV = 'how-to-mount-a-tv-height-wall-types'
G_ACCENT = 'accent-wall-ideas-slat-shiplap-panels-florida'
G_DECK = 'deck-repair-or-replace-florida'
G_CAB = 'paint-or-replace-kitchen-cabinets'
G_ATTIC = 'attic-ladder-installation-florida'
G_HIRE = 'how-to-find-a-handyman-wesley-chapel'
G_ROT = 'rotted-window-sill-siding-trim-repair-tampa-bay'

# guide -> (related guides, related services)
GUIDE_LINKS = {
 G_MEDIA:  ([G_ACCENT, G_TV, G_HIRE], ['media-accent-walls', 'tv-shelf-mounting', 'painting']),
 G_TV:     ([G_MEDIA, G_ACCENT, G_HIRE], ['tv-shelf-mounting', 'media-accent-walls', 'picture-hanging']),
 G_ACCENT: ([G_MEDIA, G_TV, G_CAB], ['media-accent-walls', 'painting', 'tv-shelf-mounting']),
 G_DECK:   ([G_ROT, G_HIRE, G_CAB], ['deck-repair', 'wood-rot-repair', 'fence-repair']),
 G_ROT:    ([G_DECK, G_HIRE, G_CAB], ['wood-rot-repair', 'painting', 'deck-repair']),
 G_CAB:    ([G_ACCENT, G_HIRE, G_DECK], ['cabinet-painting-renovation', 'new-kitchen-installation', 'painting']),
 G_ATTIC:  ([G_HIRE, G_DECK, G_CAB], ['drywall-repair', 'furniture-assembly', 'painting']),
 G_HIRE:   ([G_MEDIA, G_TV, G_DECK], ['tv-shelf-mounting', 'picture-hanging', 'furniture-assembly']),
}

# service -> guides
SERVICE_GUIDES = {
 'tv-shelf-mounting': [G_TV, G_MEDIA, G_ACCENT],
 'media-accent-walls': [G_MEDIA, G_ACCENT, G_TV],
 'deck-repair': [G_DECK, G_HIRE],
 'wood-rot-repair': [G_ROT, G_DECK, G_HIRE],
 'fence-repair': [G_DECK, G_HIRE],
 'cabinet-painting-renovation': [G_CAB, G_ACCENT],
 'new-kitchen-installation': [G_CAB, G_HIRE],
 'painting': [G_CAB, G_ROT, G_ACCENT],
 'drywall-repair': [G_ATTIC, G_HIRE],
 'furniture-assembly': [G_HIRE, G_ATTIC],
 'picture-hanging': [G_TV, G_HIRE],
 'door-installation': [G_HIRE, G_CAB],
 'appliance-repair': [G_CAB, G_HIRE],
}

# post -> guides
POST_GUIDES = {
 'media-wall-fireplace-shelving-led': [G_MEDIA, G_ACCENT],
 'kitchen-island-slat-accent-panels': [G_ACCENT, G_CAB],
 'built-in-wood-shelving-led': [G_MEDIA, G_ACCENT],
 'move-in-furniture-assembly': [G_HIRE, G_TV],
 'hurricane-shutter-installation': [G_HIRE, G_DECK],
}
