import json
import random

# Verified high quality Unsplash photo IDs (tested HTTP 200 OK)
MEN_PHOTOS = [
    "1602810318383-e386cc2a3ccf", "1583743814966-8936f5b7be1a", "1521572267360-ee0c2909d518",
    "1596755094514-f87e34085b2c", "1617137984095-74e4e5e3613f", "1507679799987-c73779587ccf",
    "1506794778202-cad84cf45f1d", "1488161628813-04466f872be2", "1519085360753-af0119f7cbe7",
    "1500648767791-00dcc994a43e", "1516257984-b1b4d707412e", "1492562080023-ab3db95bfbce",
    "1552374196-1ab2a1c593e8", "1480429370139-e0132c086e2a", "1490114538077-0a7f8cb49891",
    "1507003211169-0a1dd7228f2d", "1539571696357-5a69c17a67c6", "1512436991641-6745cdb1723f",
    "1594938298603-c8148c4dae35", "1624378439575-d8705ad7ae80", "1541099649105-f69ad21f3246",
    "1473966968600-fa801b869a1a", "1584865288642-42078afe6942", "1550246140-5119ae4790b8",
    "1520975954732-35dd22299614", "1504593811423-6dd665756598", "1534030347209-467a5b0ad3e6",
    "1600185365483-26d7a4cc7519", "1495105787522-5334e3ffa0ef", "1516826957135-700dedea698c",
    "1501196354995-cbb51c65aaea", "1487222477894-8943e31ef7b2", "1506634572416-48cdfe530110",
    "1527719327859-c32a228a0a28"
]

WOMEN_PHOTOS = [
    "1515886657613-9f3515b0c78f", "1572804013309-59a88b7e92f1", "1566174053879-31528523f8ae",
    "1595777457583-95e059d581b8", "1496747611176-843222e1e57c", "1539109136881-3be0616acf4b",
    "1509631179647-0177331693ae", "1485230895905-ec40ba36b9bc", "1529139574466-a303027c1d8b",
    "1517841905240-472988babdf9", "1494790108377-be9c29b29330", "1524504388940-b1c1722653e1",
    "1508214751196-bcfd4ca60f91", "1483985988355-763728e1935b", "1516762689617-e1cffcef479d",
    "1558769132-cb1aea458c5e", "1554412933-514a83d2f3c8", "1551803091-e20673f15770",
    "1610030469983-98e550d6193c", "1583391733956-3750e0ff4e8b", "1617627143750-d86bc21e42bb",
    "1502716119720-b23a93e5fe1b", "1539008835657-9e8e9680c956", "1490481651871-ab68de25d43d",
    "1485968579580-b6d095142e6e", "1503342217505-b0a15ec3261c", "1564557287817-3785e38ec1f5"
]

BEAUTY_PHOTOS = [
    "1598440947619-2c35fc9aa908", "1522337360788-8b13dee7a37e", "1526947425960-945c6e72858f",
    "1571781926291-c477ebfd024b", "1535585209827-a15fcdbc4c2d", "1616949755610-8c9bbc08f138",
    "1570172619644-dfd03ed5d881", "1556228720-195a672e8a03", "1620916566398-39f1143ab7be",
    "1583209814683-c023dd293cc6", "1527799820374-dcf8d9d4a388", "1596462502278-27bfdc403348",
    "1512496015851-a90fb38ba796", "1585232351009-aa87416fca90", "1617897903246-719242758050",
    "1563178406-4cdc2923acbc", "1612817288484-6f916006741a", "1576426863848-c21f53c60b19",
    "1505944270255-72b8c68c6a70"
]

FOOTWEAR_PHOTOS = [
    "1549298916-b41d501d3772", "1595950653106-6c9ebd614d3a", "1543163521-1bf539c55dd2",
    "1560769629-975ec94e6a86", "1533867617858-e7b97e060509", "1582588678413-dbf45f4823e9",
    "1608256246200-53e635b5b65f", "1600185365926-3a2ce3cdb9eb", "1515955656352-a1fa3ffcd111",
    "1535043934128-cf0b28d52f95", "1542291026-7eec264c27ff", "1525966222134-fcfa99b8ae77",
    "1606107557195-0e29a4b5b4aa", "1597045566677-8cf032ed6634"
]

WATCHES_PHOTOS = [
    "1523275335684-37898b6baf30", "1524805444758-089113d48a6d", "1522335789203-aabd1fc54bc9",
    "1548036328-c9fa89d128fa", "1584917865442-de89df76afd3", "1511499767150-a48a237f0083",
    "1572635196237-14b3f281503f", "1508296695146-257a814070b4", "1509042239860-f550ce710b93",
    "1533139502658-0198f920d8e8"
]

def make_url(pid):
    return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w=1000&q=85"

# Structure templates
SECTIONS = [
    {
        "category": "Shirts",
        "gender": "Men",
        "count": 70,
        "brands": ["ATELIER MEN", "TOMMY HILFIGER", "STUDIO NOIR", "BOMBAY TAILORS", "KULT BASICS", "RIVIERA ATELIER"],
        "adjectives": ["Pure Cotton Tailored", "Italian Mandarin Collar", "Heavyweight Boxy Supima", "French Cuff Sky Blue", "Textured Pique", "Double-Pocket Safari", "Mercerized Egyptian Cotton", "Houndstooth Oversized", "Organic Washed Denim", "Camp Collar Cuban", "Striped Resort Collar", "Minimalist Poplin"],
        "items": ["Oxford Shirt", "Linen Shirt", "Crewneck T-Shirt", "Polo Shirt", "Overshirt", "Workshirt", "Silk Blend Shirt", "Relaxed Fit Tee", "Flannel Shirt"],
        "photos": MEN_PHOTOS,
        "sizes": ["S", "M", "L", "XL", "XXL"],
        "price_range": (1199, 3999),
        "desc": "Expertly cut from long-staple organic cotton yarns with pearlized buttons and reinforced single-needle tailoring."
    },
    {
        "category": "Pants",
        "gender": "Men",
        "count": 60,
        "brands": ["DENIM LAB", "ATELIER MEN", "STUDIO NOIR", "URBAN NOMAD", "MILANO COUTURE"],
        "adjectives": ["Tapered Fit Stretch", "Relaxed Pleated Wool Blend", "Straight-Leg Raw Selvedge", "Drawstring Elasticated", "Tactical Multi-Pocket", "Washed Cotton Canvas", "High-Rise Double Pleated", "Slim-Fit Stretch", "Cropped Minimalist", "Heavyweight Gabardine"],
        "items": ["Indigo Denim Jeans", "Formal Trousers", "Linen Chinos", "Cargo Pants", "Carpenter Trousers", "Dress Trousers", "Corduroy Trousers", "Ankle Chinos"],
        "photos": MEN_PHOTOS,
        "sizes": ["30", "32", "34", "36", "38"],
        "price_range": (1499, 4599),
        "desc": "Engineered with ergonomic seams and bespoke Italian waist curtaining for all-day comfort and sharp drape."
    },
    {
        "category": "Dresses",
        "gender": "Women",
        "count": 140,
        "brands": ["VIRASAT COUTURE", "STUDIO NYKA", "BLUSH & BLOOM", "AWADH COUTURIER", "KASHI WEAVES", "ATELIER FEMME"],
        "adjectives": ["Handloom Chanderi Silk", "Minimalist Tailored Linen", "Tiered Floral Georgette", "Awadh Hand-Embroidered Chikankari", "Banarasi Katan Silk", "Architectural Asymmetric Satin", "Embroidered Organza", "Pleated Monochrome", "Raw Silk Festive", "Pure Mulberry Silk", "Structured Double-Breasted", "Vintage French Lace"],
        "items": ["Saree with Zari Border", "Summer Co-ord Suit", "Maxi Gown", "Kurta Set with Dupatta", "Cocktail Dress", "Anarkali Ensemble", "Midi Shirt Dress", "Angrakha Kurti", "Wrap Gown", "Blazer Dress"],
        "photos": WOMEN_PHOTOS,
        "sizes": ["XS", "S", "M", "L", "XL"],
        "price_range": (1799, 8999),
        "desc": "Woven with artisanal heritage and contemporary silhouettes, featuring pure silk lining and intricate hand finish."
    },
    {
        "category": "Beauty",
        "gender": "Women",
        "count": 95,
        "brands": ["MAISON DE PARFUM", "L'ELIXIR BOTANIQUE", "ATELIER DERMA", "GLOW LAB PARIS", "AURA BOTANICA"],
        "adjectives": ["Santal Imperial 100ml", "Hyaluronic Acid 2% + B5", "Niacinamide 10% Clarifying", "Rose Water Hydrosol", "Retinol 0.5% Night Youth", "Vitamin C 15% Radiance", "Ceramide Barrier Velvet", "Amber Wood Unisex", "Peptide Firming Eye", "Green Tea Antioxidant", "Botanical Facial Squalane"],
        "items": ["Eau De Parfum", "Hydrating Serum", "Concentrate Drops", "Face Mist", "Renewing Oil", "Brightening Essence", "Moisture Cream", "Treatment Balm"],
        "photos": BEAUTY_PHOTOS,
        "sizes": ["30ml", "50ml", "100ml"],
        "price_range": (899, 5499),
        "desc": "Dermatologically tested clean formulation enriched with cold-pressed bio-actives and cruelty-free botanicals."
    },
    {
        "category": "Footwear",
        "gender": "Unisex",
        "count": 90,
        "brands": ["TUSCAN LEATHER LAB", "ATELIER FOOTWEAR", "MILANO VENEZIA", "NORDIC RUNNER", "SOLE COUTURE"],
        "adjectives": ["Burnished Tuscan Calfskin", "Handcrafted Goodyear-Welted", "Minimalist Monochrome Leather", "Velvet Suede Heeled", "Classic Oxford Wingtip", "Low-Profile Court", "Artisanal Slip-On Penny", "Chunky Sole Lugged"],
        "items": ["Penny Loafers", "Chelsea Boots", "Luxury Sneakers", "Dress Brogues", "Derby Shoes", "Ankle Boots", "Mules", "Court Trainers"],
        "photos": FOOTWEAR_PHOTOS,
        "sizes": ["UK 6", "UK 7", "UK 8", "UK 9", "UK 10", "UK 11"],
        "price_range": (1999, 7999),
        "desc": "Hand-stitched full-grain calfskin leather with memory-foam cushioned footbeds and anti-skid Goodyear rubber soles."
    },
    {
        "category": "Watches",
        "gender": "Unisex",
        "count": 80,
        "brands": ["HERITAGE TIMEPIECES", "CHRONO ATELIER", "GENEVA HOROLOGY", "ATELIER CUIR", "SOLARIS LUXE"],
        "adjectives": ["Minimalist Sapphire Crystal", "Automatic Skeleton Exhibition", "Submariner 200m Steel", "Italian Saffiano Leather", "Aviator Polarized Titanium", "Chronograph Sunburst Dial", "Gold-Plated Bezel Mechanical", "Slim Profile Bauhaus"],
        "items": ["Automatic Watch", "Chronograph Timepiece", "Tote Bag", "Crossbody Bag", "Sunglasses", "Cardholder Wallet", "Travel Duffel", "Dress Timepiece"],
        "photos": WATCHES_PHOTOS,
        "sizes": ["40mm", "42mm", "ONE SIZE"],
        "price_range": (1499, 9999),
        "desc": "Engineered with Japanese Miyota movements, surgical-grade 316L stainless steel, and scratch-resistant sapphire glass."
    }
]

BADGES = ["NEW ARRIVAL", "RUNWAY", "TIMELESS", "LIMITED", "ESSENTIAL", "BESTSELLER"]

products = []
current_id = 1

for sec in SECTIONS:
    count = sec["count"]
    for i in range(count):
        brand = sec["brands"][i % len(sec["brands"])]
        adj = sec["adjectives"][i % len(sec["adjectives"])]
        item = sec["items"][i % len(sec["items"])]
        name = f"{adj} {item}"
        if i >= len(sec["adjectives"]):
            name += f" • Edition { (i // len(sec['adjectives'])) + 1 }"
            
        pid = sec["photos"][i % len(sec["photos"])]
        image_url = make_url(pid)
        
        min_p, max_p = sec["price_range"]
        price = random.randint(min_p // 50, max_p // 50) * 50 - 1
        markup = random.choice([1.35, 1.45, 1.55, 1.70, 1.85])
        orig_price = int(price * markup // 50) * 50 - 1
        discount = int(round((1 - (price / orig_price)) * 100))
        
        rating = round(random.uniform(4.4, 4.95), 1)
        reviews = random.randint(28, 420)
        badge = BADGES[i % len(BADGES)]
        
        prod = {
            "id": current_id,
            "name": name,
            "brand": brand,
            "category": sec["category"],
            "gender": sec["gender"],
            "price": price,
            "originalPrice": orig_price,
            "discountPercent": discount,
            "rating": rating,
            "reviewsCount": reviews,
            "badge": badge,
            "sizes": sec["sizes"],
            "imageUrl": image_url,
            "description": sec["desc"]
        }
        products.append(prod)
        current_id += 1

print(f"Generated {len(products)} products total.")

with open("products_data.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2)

print("Saved to products_data.json successfully.")
