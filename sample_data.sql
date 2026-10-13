-- ==========================================================
-- E-COMMERCE SAMPLE DATA (TRENDVIBE ATELIER LUXURY FASHION & BEAUTY)
-- Real-world expanded catalog data for 27 premium products
-- ==========================================================

USE ecommerce_db;

-- 1. SEED CATEGORIES
INSERT INTO categories (category_id, category_name, description, is_active) VALUES
(1, 'Men Fashion', 'Premium shirts, t-shirts, jeans, and formal wear (Atelier Tailored Collection)', TRUE),
(2, 'Women Ethnic & Western', 'Trendy dresses, kurtas, lehengas, tops, and trousers', TRUE),
(3, 'Beauty & Cosmetics', 'Artisanal French perfumes, active botanical serums, and clean cosmetics', TRUE),
(4, 'Footwear & Sneakers', 'Casual sneakers, formal shoes, heels, and running shoes', TRUE),
(5, 'Accessories & Watches', 'Luxury analog watches, sunglasses, leather wallets, and jewelry', TRUE)
ON DUPLICATE KEY UPDATE category_name=VALUES(category_name);

-- 2. SEED USERS
INSERT INTO users (user_id, full_name, email, phone, password, gender, address) VALUES
(1, 'Indranil Soma', 'indranil@example.com', '9876543210', 'password123', 'Male', 'Flat 402, Green Valley Apts, Bangalore, Karnataka - 560001'),
(2, 'Priya Sharma', 'priya@example.com', '9812345678', 'password123', 'Female', 'House 12, Park Street, Kolkata, West Bengal - 700016'),
(3, 'Rahul Verma', 'rahul@example.com', '9123456789', 'password123', 'Male', 'Plot 88, Sector 18, Gurugram, Haryana - 122001')
ON DUPLICATE KEY UPDATE full_name=VALUES(full_name);

-- 3. SEED 27 EXPANDED PRODUCTS
INSERT INTO products (product_id, category_id, product_name, description, discount_percent, image_url, is_active) VALUES
-- Men Fashion
(1, 1, 'Roadster Men Slim Fit Pure Cotton Casual Shirt', 'Olive green casual shirt, has a spread collar, long sleeves, curved hem, and one patch pocket. 100% breathable pure cotton.', 40.00, 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80', TRUE),
(2, 1, 'HIGHLANDER Men Tapered Fit Stretch Jeans', 'Dark blue washed 5-pocket mid-rise jeans, clean look with light fade, waistband with belt loops, button and zip fly closure.', 35.00, 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=800&q=80', TRUE),
(3, 1, 'WROGN Geometric Printed Pure Cotton T-shirt', 'Navy blue and white printed T-shirt, has a round neck, short sleeves with contrast ribbing. Bio-washed for ultra softness.', 25.00, 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80', TRUE),
(4, 1, 'Tommy Hilfiger Classic Oxford Cotton Shirt', 'Classic button-down collar Oxford shirt in sky blue with signature embroidered flag on chest.', 30.00, 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=800&q=80', TRUE),
(5, 1, 'Levi''s 511 Slim Fit Raw Indigo Denim Jeans', 'Authentic Levi''s 511 slim fit stretch denim in dark indigo with trademark red tab on back pocket.', 20.00, 'https://images.unsplash.com/photo-1542272604-780c96856592?auto=format&fit=crop&w=800&q=80', TRUE),
(6, 1, 'HRX Activewear Dry-Fit Breathable Joggers', 'Athletic training joggers with moisture-wicking technology and reflective side tape.', 45.00, 'https://images.unsplash.com/photo-1552902865-b72c031ac5ea?auto=format&fit=crop&w=800&q=80', TRUE),
(7, 1, 'Dennis Lingo Casual Corduroy Spread Collar Overshirt', 'Rich camel brown corduroy jacket shirt, relaxed drop shoulder with twin chest flap pockets.', 50.00, 'https://images.unsplash.com/photo-1598033129183-c4f50c736f10?auto=format&fit=crop&w=800&q=80', TRUE),

-- Women Ethnic & Western
(8, 2, 'Anouk Women Embroidered Anarkali Kurta Set', 'Burgundy and gold embroidered Anarkali kurta with trousers and organza dupatta. Features intricate zari thread work.', 50.00, 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80', TRUE),
(9, 2, 'MANGO Floral Print Fit & Flare Midi Dress', 'Sage green and lavender floral print woven midi dress, has a sweetheart neckline, puff short sleeves, and flared hem.', 30.00, 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80', TRUE),
(10, 2, 'Libas Women Pink Solid Straight Kurta with Palazzos', 'Dusty pink straight calf-length kurta, keyhole neck, three-quarter sleeves, paired with palazzos.', 45.00, 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80', TRUE),
(11, 2, 'Biba Block Printed Festive Tiered Anarkali Gown', 'Royal teal blue block-printed floor-length Anarkali gown with gota patti borders and sequin yoke.', 40.00, 'https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?auto=format&fit=crop&w=800&q=80', TRUE),
(12, 2, 'H&M Ribbed High-Neck Knit Bodycon Dress', 'Soft black ribbed knit midi dress with side slit, high turtle neckline, and long sleeves.', 25.00, 'https://images.unsplash.com/photo-1539109136881-3be0616acf4b?auto=format&fit=crop&w=800&q=80', TRUE),
(13, 2, 'FabIndia Hand-Block Printed Chanderi Silk Saree', 'Traditional magenta and golden zari handloom Chanderi silk saree with matching blouse piece.', 35.00, 'https://images.unsplash.com/photo-1610030469668-935cb7462002?auto=format&fit=crop&w=800&q=80', TRUE),
(14, 2, 'Vero Moda Women Pleated Satin Party Blouse', 'Emerald green cowl neck sleeveless satin top with delicate pleats and button closure.', 30.00, 'https://images.unsplash.com/photo-1564257631407-4deb1f99d992?auto=format&fit=crop&w=800&q=80', TRUE),

-- Beauty & Fine Fragrance
(15, 3, 'Maison De Beauté Velvet Liquid Lip Trio - Nude Rouge', 'Ultra-lightweight matte liquid lipstick infused with Vitamin E. Transfer-proof, 12-hour wear.', 20.00, 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80', TRUE),
(16, 3, 'The Ordinary Niacinamide 10% + Zinc 1% Serum', 'High-strength vitamin and mineral blemish formula. Visibly balances sebum and clarifies pores.', 15.00, 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=800&q=80', TRUE),
(17, 3, 'Forest Essentials Soundarya Radiance Cream with 24K Gold', 'Ayurvedic anti-aging day cream infused with 24K pure gold bhasma and saffron for natural glow.', 10.00, 'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80', TRUE),
(18, 3, 'Kay Beauty 24H Waterproof Matte HD Liquid Eyeliner', 'Deep black precision felt tip liquid eyeliner with smudge-proof, 24-hour stay formula.', 25.00, 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=800&q=80', TRUE),
(19, 3, 'Minimalist Salicylic Acid 2% Gentle Face Cleanser', 'Sulfate-free exfoliating cleanser with LHA and Zinc for acne control and oil balance.', 15.00, 'https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=800&q=80', TRUE),
(20, 3, 'MAC Retro Matte Velvet Lipstick - Ruby Woo', 'Iconic vivid blue-red matte lipstick with long-wearing non-feathering formula.', 10.00, 'https://images.unsplash.com/photo-1599733589046-10c005739ef9?auto=format&fit=crop&w=800&q=80', TRUE),

-- Footwear & Sneakers
(21, 4, 'Nike Air Max SC Leather Running Sneakers', 'White and royal blue heritage track style sneakers with visible Air cushioning and foam midsole.', 20.00, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80', TRUE),
(22, 4, 'Puma Men Black & White Smash V2 Low-Tops', 'Classic tennis-inspired silhouette in soft black suede with signature white Puma formstrip.', 40.00, 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=800&q=80', TRUE),
(23, 4, 'Adidas Originals Stan Smith Iconic White Sneakers', 'Timeless minimalist court sneaker with perforated 3-Stripes and green heel tab.', 30.00, 'https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?auto=format&fit=crop&w=800&q=80', TRUE),
(24, 4, 'Red Tape Men Genuine Leather Chelsea Boots', 'Handcrafted rich cognac brown ankle Chelsea boots with stretch side panels and TPR sole.', 55.00, 'https://images.unsplash.com/photo-1638247025967-b4e38f787b76?auto=format&fit=crop&w=800&q=80', TRUE),

-- Accessories & Watches
(25, 5, 'Fossil Men Chronograph Black Leather Watch', 'Gunmetal stainless steel case with genuine black leather strap. 50m water resistance.', 30.00, 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=800&q=80', TRUE),
(26, 5, 'Ray-Ban Hexagonal Flat Lenses Metal Sunglasses', 'Gold polished hexagonal metal frame with classic G-15 green polarized lenses.', 25.00, 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=800&q=80', TRUE),
(27, 5, 'Titan Raga Aurora Rose Gold Pearl Dial Watch', 'Jewelry-inspired rose gold wristwatch with mother-of-pearl dial and Swarovski crystal accents.', 20.00, 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=800&q=80', TRUE)
ON DUPLICATE KEY UPDATE product_name=VALUES(product_name), discount_percent=VALUES(discount_percent), image_url=VALUES(image_url);

-- 4. SEED SAMPLE CART
INSERT INTO cart (cart_id, user_id) VALUES (1, 1) ON DUPLICATE KEY UPDATE user_id=VALUES(user_id);
INSERT INTO cart_items (cart_item_id, cart_id, product_id, size_label, quantity, unit_price) VALUES
(1, 1, 1, 'M', 1, 899.00),
(2, 1, 15, '4.2 ml', 2, 599.00)
ON DUPLICATE KEY UPDATE quantity=VALUES(quantity);
