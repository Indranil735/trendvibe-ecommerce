import json
import os
import sys

# ==============================================================================
# 1. GENERATE 260 RICH, CURATED FASHION PRODUCTS
# ==============================================================================

categories_data = [
    {
        "category": "Shirts",
        "gender": "Men",
        "brands": ["ATELIER MEN", "TOMMY HILFIGER", "STUDIO NOIR", "BOMBAY TAILORS", "KULT BASICS", "RIVIERA"],
        "names": [
            "Pure Cotton Tailored Oxford Shirt",
            "French Cuff Sky Blue Linen Shirt",
            "Heavyweight Boxy Supima Cotton T-Shirt",
            "Italian Mandarin Collar Linen Shirt",
            "Monochrome Graphic Relaxed Tee",
            "Striped Resort Collar Silk Blend Shirt",
            "Textured Pique Cotton Polo Shirt",
            "Military Utility Flight Shirt Jacket",
            "Organic Washed Denim Workshirt",
            "Houndstooth Oversized Flannel Overshirt",
            "Mercerized Egyptian Cotton Crewneck Tee",
            "Double-Pocket Safari Cotton Shirt",
            "Camp Collar Vintage Cuban Shirt"
        ],
        "images": [
            "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1620012253295-c15c429f66bf?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1576566588028-4147f3842f27?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1581655353564-df123a1eb820?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1603252109303-2751441dd157?auto=format&fit=crop&w=800&q=80"
        ],
        "base_prices": [899, 1299, 1499, 1899, 2499, 2999, 3499],
        "badges": ["RUNWAY", "NEW ARRIVAL", "TIMELESS", "PREMIUM", "ESSENTIAL"]
    },
    {
        "category": "Pants",
        "gender": "Men",
        "brands": ["STUDIO NOIR", "DENIM LAB", "ATELIER MEN", "URBAN NOMAD", "MILANO COUTURE"],
        "names": [
            "Tapered Fit Stretch Indigo Denim",
            "Relaxed Pleated Wool Blend Trousers",
            "Straight-Leg Raw Selvedge Denim Jeans",
            "Tailored Wool Twill Formal Trousers",
            "Drawstring Elasticated Linen Chinos",
            "Tactical Multi-Pocket Cargo Trousers",
            "Washed Cotton Canvas Carpenter Pants",
            "High-Rise Double Pleated Dress Trousers",
            "Slim-Fit Stretch Corduroy Trousers",
            "Cropped Minimalist Ankle Chinos",
            "Italian Wool Houndstooth Trousers",
            "Lightwash Distressed Vintage Denim",
            "Heavyweight Gabardine Utility Pants"
        ],
        "images": [
            "https://images.unsplash.com/photo-1542272604-780c96856592?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584865288642-42078afe6942?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=800&q=80"
        ],
        "base_prices": [1199, 1499, 1899, 2299, 2899, 3499, 4299],
        "badges": ["EDITORIAL", "TIMELESS", "CLASSIC", "LIMITED", "RUNWAY"]
    },
    {
        "category": "Dresses",
        "gender": "Women",
        "brands": ["VIRASAT COUTURE", "STUDIO NYKA", "BLUSH & BLOOM", "AWADH COUTURIER", "KASHI WEAVES", "ATELIER FEMME"],
        "names": [
            "Handloom Chanderi Silk Saree with Zari Border",
            "Minimalist Tailored Linen Co-ord Summer Suit",
            "Tiered Floral Silk Georgette Maxi Gown",
            "Awadh Hand-Embroidered Chikankari Kurta Set",
            "Imperial Banarasi Katan Silk Floral Zari Saree",
            "Architectural Asymmetric Satin Cocktail Dress",
            "Embroidered Organza Anarkali Set with Dupatta",
            "Pleated Monochrome Midi Shirt Dress",
            "Raw Silk Festive Angrakha Kurti Ensemble",
            "Pure Mulberry Silk Printed Wrap Gown",
            "Hand-Block Printed Mulmul Cotton Suit",
            "Structured Double-Breasted Blazer Dress",
            "Vintage French Lace Tiered Evening Dress"
        ],
        "images": [
            "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=800&q=80"
        ],
        "base_prices": [1599, 1999, 2499, 2999, 3799, 4999, 6499],
        "badges": ["HERITAGE", "RUNWAY", "COUTURE", "BESTSELLER", "LUXE"]
    },
    {
        "category": "Beauty",
        "gender": "Women",
        "brands": ["MAISON DE BEAUTÉ", "BOTANIQUE LAB", "DERM SHIELD", "KOHL ATELIER", "L'ORIENT PARFUMS", "HERBAL AURA"],
        "names": [
            "Velvet Matte Liquid Lip Trio Collection",
            "Vitamin C 15% Radiance Glow Active Serum",
            "Barrier Restoring Ceramide Hydro-Cream",
            "Dramatic Carbon Waterproof Gel Eyeliner",
            "Arabian Royal Oud Eau De Parfum (100ml)",
            "Rosemary Peptides Hair Density Elixir",
            "French Damask Rose Hydrating Face Mist",
            "Hyaluronic Acid 2% + B5 Moisture Infusion",
            "Niacinamide 10% Pore Refining Clarifying Serum",
            "Cold-Pressed Moroccan Argan Miracle Oil",
            "Silky Luminous Lightweight Cushion Foundation",
            "Santal & Bergamot Artisanal Eau De Cologne",
            "Midnight Retinol 0.3% Renewal Night Cream"
        ],
        "images": [
            "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1608248597359-3d14fdf37648?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1601049541289-9b1b7bbbfe19?auto=format&fit=crop&w=800&q=80"
        ],
        "base_prices": [499, 699, 899, 1299, 1899, 2499, 3299],
        "badges": ["ICONIC", "CLEAN BEAUTY", "EXQUISITE", "DERMA PICK", "VIRAL"]
    },
    {
        "category": "Shoes",
        "gender": "Men",
        "brands": ["MONK & STITCH", "KICKVIBE LAB", "GLAMORA MILAN", "VELOCE SPORTS", "AURA COMFORT", "FIRENZE BOOTMAKERS"],
        "names": [
            "Retro Monochrome Chunky High-Top Sneakers",
            "Handcrafted Calfskin Leather Penny Loafers",
            "Architectural Strappy Stiletto Block Heels",
            "Air-Cushioned Ultra Pace Performance Trainers",
            "Sculpted Ergonomic Cloud Slide Sandals",
            "Italian Suede Goodyear Welted Chelsea Boots",
            "Oxford Brogues in Burnished Espresso Calfskin",
            "Minimalist Low-Profile Clean White Court Sneakers",
            "Pointed Toe D'Orsay Formal Leather Flats",
            "Chunky Lug-Sole Combat Derby Shoes",
            "Hand-Woven Leather Huarache Loafers",
            "Athletic Knit Hybrid Slip-On Runners",
            "Square Toe Contemporary Mule Sandals"
        ],
        "images": [
            "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1533867617858-e7b97e060509?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1603808033192-082d6919d3e1?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1520639888713-7851133b1ed0?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=800&q=80"
        ],
        "base_prices": [1199, 1799, 2299, 2899, 3599, 4299, 5499],
        "badges": ["ARTISANAL", "STREETWEAR", "RUNWAY", "COMFORT", "HANDMADE"]
    },
    {
        "category": "Watches",
        "gender": "Men",
        "brands": ["VANGUARD HOROLOGY", "LUXE ACCENTS", "SOLSTICE EYEWEAR", "CUOIO FIRENZE", "GENEVA STUDIO"],
        "names": [
            "Classic Chronograph Emerald Dial Timepiece",
            "18K Gold Plated Minimalist Paperclip Chain",
            "Handcrafted Acetate Polarized Retro Sunglasses",
            "Genuine Florence Leather Crossbody Saddle Bag",
            "Automatic Open-Heart Skeleton Leather Watch",
            "Full-Grain Saffiano Leather Bifold Wallet",
            "Pavé Diamond Accent Vermeil Tennis Bracelet",
            "Aviator Titanium Framed Polarized Sunglasses",
            "Textured Silk Twill Hand-Rolled Pocket Square",
            "Pebbled Italian Leather Top-Handle Tote Bag",
            "Minimalist Ceramic Case Bauhaus Dress Watch",
            "Brushed Gold Geometric Signet Statement Ring",
            "Braided Vachetta Leather Antique Brass Belt"
        ],
        "images": [
            "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=800&q=80"
        ],
        "base_prices": [1499, 1999, 2999, 3999, 4999, 6999, 8999],
        "badges": ["COLLECTOR", "VERMEIL", "LIMITED EDITION", "LUXURY", "UV400"]
    }
]

generated_products = []
p_id = 1

# Generate 260 products by varying adjectives, editions, and variants across categories
variants = [
    ("Noir Edition", 1.0, 0),
    ("Heritage Edit", 1.1, 1),
    ("Runway Premiere", 1.25, 2),
    ("Artisanal Craft", 0.95, 3),
]

while len(generated_products) < 260:
    for cat in categories_data:
        if len(generated_products) >= 260:
            break
        for i, name in enumerate(cat["names"]):
            if len(generated_products) >= 260:
                break
            brand = cat["brands"][p_id % len(cat["brands"])]
            image = cat["images"][p_id % len(cat["images"])]
            base_p = cat["base_prices"][p_id % len(cat["base_prices"])]
            badge = cat["badges"][p_id % len(cat["badges"])]
            
            # Variant modifier for diversity
            v_name, price_mult, discount_offset = variants[p_id % len(variants)]
            full_title = f"{name} &bull; {v_name}" if (p_id % 3 == 0) else name
            final_price = int(base_p * price_mult)
            disc = 25 + ((p_id * 7) % 26)
            orig_price = int(final_price / (1 - disc / 100))
            
            # Category sizes
            if cat["category"] in ["Shirts", "Dresses"]:
                sizes = ["XS", "S", "M", "L", "XL"]
            elif cat["category"] == "Pants":
                sizes = ["30", "32", "34", "36"]
            elif cat["category"] == "Shoes":
                sizes = ["UK 7", "UK 8", "UK 9", "UK 10"]
            elif cat["category"] == "Beauty":
                sizes = ["30 ml", "50 ml", "100 ml"]
            else:
                sizes = ["Standard", "Adjustable"]
                
            rating = round(4.5 + ((p_id % 5) * 0.1), 1)
            reviews = 120 + ((p_id * 83) % 2400)
            
            prod = {
                "id": p_id,
                "name": full_title,
                "brand": brand,
                "category": cat["category"],
                "gender": cat["gender"],
                "price": final_price,
                "originalPrice": orig_price,
                "discountPercent": disc,
                "rating": rating,
                "reviewsCount": reviews,
                "badge": badge,
                "sizes": sizes,
                "imageUrl": image,
                "description": f"Curated from the {brand} runway studio. Meticulously crafted for supreme elegance and timeless longevity."
            }
            generated_products.append(prod)
            p_id += 1

print(f"Total curated products generated: {len(generated_products)}")

# Serialize products to JSON for embedding into client JavaScript
products_json = json.dumps(generated_products, indent=2)

with open("products_data.json", "w", encoding="utf-8") as f:
    f.write(products_json)

print("Saved products_data.json!")
