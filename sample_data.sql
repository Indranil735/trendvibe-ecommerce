-- ==========================================================
-- E-COMMERCE SAMPLE DATA (MYNTRA / AJIO / NYKAA STYLE)
-- Real-world catalog data for fashion, footwear, beauty, luxury
-- ==========================================================

USE ecommerce_db;

-- 1. SEED CATEGORIES
INSERT INTO categories (category_id, category_name, description, is_active) VALUES
(1, 'Men Fashion', 'Premium shirts, t-shirts, jeans, and formal wear (Myntra/Ajio style)', TRUE),
(2, 'Women Ethnic & Western', 'Trendy dresses, kurtas, lehengas, tops, and trousers', TRUE),
(3, 'Beauty & Cosmetics', 'Nykaa-inspired skincare, makeup, perfumes, and hair care', TRUE),
(4, 'Footwear & Sneakers', 'Casual sneakers, formal shoes, heels, and running shoes', TRUE),
(5, 'Accessories & Watches', 'Luxury analog watches, sunglasses, leather wallets, and jewelry', TRUE);

-- 2. SEED USERS
-- Default passwords are encrypted or plain for demo: password123
INSERT INTO users (user_id, full_name, email, phone, password, gender, address) VALUES
(1, 'Indranil Soma', 'indranil@example.com', '9876543210', 'password123', 'Male', 'Flat 402, Green Valley Apts, Bangalore, Karnataka - 560001'),
(2, 'Priya Sharma', 'priya@example.com', '9812345678', 'password123', 'Female', 'House 12, Park Street, Kolkata, West Bengal - 700016'),
(3, 'Rahul Verma', 'rahul@example.com', '9123456789', 'password123', 'Male', 'Plot 88, Sector 18, Gurugram, Haryana - 122001');

-- 3. SEED PRODUCTS
INSERT INTO products (product_id, category_id, product_name, description, discount_percent, image_url, is_active) VALUES
-- Men Fashion (Myntra / Ajio style)
(1, 1, 'Roadster Men Slim Fit Pure Cotton Casual Shirt', 'Olive green casual shirt, has a spread collar, long sleeves, curved hem, and one patch pocket. 100% breathable pure cotton.', 40.00, 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80', TRUE),
(2, 1, 'HIGHLANDER Men Tapered Fit Stretch Jeans', 'Dark blue washed 5-pocket mid-rise jeans, clean look with light fade, waistband with belt loops, button and zip fly closure.', 35.00, 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=800&q=80', TRUE),
(3, 1, 'WROGN Geometric Printed Pure Cotton T-shirt', 'Navy blue and white printed T-shirt, has a round neck, short sleeves with contrast ribbing. Bio-washed for ultra softness.', 25.00, 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80', TRUE),

-- Women Ethnic & Western
(4, 2, 'Anouk Women Embroidered Anarkali Kurta Set', 'Burgundy and gold embroidered Anarkali kurta with trousers and organza dupatta. Features intricate zari thread work.', 50.00, 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80', TRUE),
(5, 2, 'MANGO Floral Print Fit & Flare Midi Dress', 'Sage green and lavender floral print woven midi dress, has a sweetheart neckline, puff short sleeves, and flared hem.', 30.00, 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80', TRUE),
(6, 2, 'Libas Women Pink Solid Straight Kurta with Palazzos', 'Dusty pink straight calf-length kurta, has a keyhole neck, three-quarter sleeves, side slits, paired with elasticated palazzos.', 45.00, 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80', TRUE),

-- Beauty & Cosmetics (Nykaa style)
(7, 3, 'Nykaa Matte to Last! Liquid Lipstick - Chai', 'Ultra-lightweight matte liquid lipstick infused with Vitamin E. Transfer-proof, 12-hour long wear, paraben-free formula.', 20.00, 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80', TRUE),
(8, 3, 'The Ordinary Niacinamide 10% + Zinc 1% Serum', 'High-strength vitamin and mineral blemish formula. Visibly reduces blemishes, clears congestion, and balances sebum activity.', 15.00, 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=800&q=80', TRUE),
(9, 3, 'Forest Essentials Soundarya Radiance Cream with 24K Gold', 'Ayurvedic anti-aging day cream infused with 24K pure gold bhasma and saffron for natural glow and deep hydration.', 10.00, 'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80', TRUE),

-- Footwear & Sneakers (Ajio/Myntra style)
(10, 4, 'Nike Air Max SC Leather Running Sneakers', 'White and royal blue heritage track style sneakers with visible Air cushioning. Lightweight foam midsole and durable rubber outsole.', 20.00, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80', TRUE),
(11, 4, 'Puma Men Black & White Smash V2 Low-Tops', 'Classic tennis-inspired silhouette in soft black suede with signature white Puma formstrip and cushioned sockliner.', 40.00, 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=800&q=80', TRUE),

-- Accessories & Luxury Watches
(12, 5, 'Fossil Men Chronograph Black Leather Watch', 'Gunmetal stainless steel case with genuine black leather strap. Features quartz chronograph movement and 50m water resistance.', 30.00, 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=800&q=80', TRUE),
(13, 5, 'Ray-Ban Hexagonal Flat Lenses Metal Sunglasses', 'Gold polished hexagonal metal frame with classic G-15 green polarized lenses. 100% UV protection.', 25.00, 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=800&q=80', TRUE);

-- 4. SEED PRODUCT SIZES & STOCK
INSERT INTO product_sizes (product_id, size_label, stock_quantity, sku_code, is_available) VALUES
-- Roadster Shirt (Product 1)
(1, 'S', 25, 'RD-SHT-01-S', TRUE),
(1, 'M', 40, 'RD-SHT-01-M', TRUE),
(1, 'L', 30, 'RD-SHT-01-L', TRUE),
(1, 'XL', 15, 'RD-SHT-01-XL', TRUE),

-- HIGHLANDER Jeans (Product 2)
(2, '30', 20, 'HL-JNS-02-30', TRUE),
(2, '32', 35, 'HL-JNS-02-32', TRUE),
(2, '34', 25, 'HL-JNS-02-34', TRUE),
(2, '36', 10, 'HL-JNS-02-36', TRUE),

-- WROGN T-shirt (Product 3)
(3, 'S', 50, 'WR-TSH-03-S', TRUE),
(3, 'M', 60, 'WR-TSH-03-M', TRUE),
(3, 'L', 45, 'WR-TSH-03-L', TRUE),
(3, 'XL', 20, 'WR-TSH-03-XL', TRUE),

-- Anouk Kurta (Product 4)
(4, 'XS', 15, 'AK-KRT-04-XS', TRUE),
(4, 'S', 30, 'AK-KRT-04-S', TRUE),
(4, 'M', 40, 'AK-KRT-04-M', TRUE),
(4, 'L', 25, 'AK-KRT-04-L', TRUE),
(4, 'XL', 10, 'AK-KRT-04-XL', TRUE),

-- MANGO Dress (Product 5)
(5, 'S', 20, 'MG-DRS-05-S', TRUE),
(5, 'M', 25, 'MG-DRS-05-M', TRUE),
(5, 'L', 15, 'MG-DRS-05-L', TRUE),

-- Libas Suit (Product 6)
(6, 'S', 30, 'LB-KRT-06-S', TRUE),
(6, 'M', 45, 'LB-KRT-06-M', TRUE),
(6, 'L', 35, 'LB-KRT-06-L', TRUE),

-- Nykaa Lipstick (Product 7 - Beauty shade/size)
(7, '4.2 ml', 100, 'NYK-LIP-07-REG', TRUE),

-- The Ordinary Serum (Product 8)
(8, '30 ml', 85, 'ORD-SRM-08-30ML', TRUE),
(8, '60 ml', 40, 'ORD-SRM-08-60ML', TRUE),

-- Forest Essentials Cream (Product 9)
(9, '50 gm', 30, 'FE-CRM-09-50G', TRUE),

-- Nike Air Max (Product 10 - UK shoe sizes)
(10, 'UK 7', 15, 'NK-AM-10-UK7', TRUE),
(10, 'UK 8', 25, 'NK-AM-10-UK8', TRUE),
(10, 'UK 9', 20, 'NK-AM-10-UK9', TRUE),
(10, 'UK 10', 10, 'NK-AM-10-UK10', TRUE),

-- Puma Smash V2 (Product 11)
(11, 'UK 7', 20, 'PM-SM-11-UK7', TRUE),
(11, 'UK 8', 30, 'PM-SM-11-UK8', TRUE),
(11, 'UK 9', 25, 'PM-SM-11-UK9', TRUE),

-- Fossil Watch (Product 12)
(12, 'Standard (44mm)', 35, 'FSL-WTC-12-STD', TRUE),

-- Ray-Ban Sunglasses (Product 13)
(13, 'Standard (51mm)', 40, 'RB-SUN-13-STD', TRUE);

-- 5. SEED CART AND CART ITEMS (For User 1)
INSERT INTO cart (cart_id, user_id) VALUES
(1, 1);

INSERT INTO cart_items (cart_item_id, cart_id, product_id, size_label, quantity, unit_price) VALUES
(1, 1, 1, 'M', 1, 899.00),
(2, 1, 10, 'UK 8', 1, 4799.00);

-- 6. SEED PAST ORDERS (For User 1)
INSERT INTO orders (order_id, user_id, order_date, total_amount, payment_method, order_status, delivery_address) VALUES
(101, 1, '2026-08-20 14:32:00', 3198.00, 'UPI (Google Pay)', 'Delivered', 'Flat 402, Green Valley Apts, Bangalore, Karnataka - 560001'),
(102, 1, '2026-09-02 11:15:00', 1599.00, 'Credit Card', 'Shipped', 'Flat 402, Green Valley Apts, Bangalore, Karnataka - 560001');

INSERT INTO order_items (order_item_id, order_id, product_id, product_name, quantity, unit_price, subtotal, size_label) VALUES
(1, 101, 4, 'Anouk Women Embroidered Anarkali Kurta Set', 1, 1999.00, 1999.00, 'M'),
(2, 101, 7, 'Nykaa Matte to Last! Liquid Lipstick - Chai', 2, 599.50, 1199.00, '4.2 ml'),
(3, 102, 3, 'WROGN Geometric Printed Pure Cotton T-shirt', 2, 799.50, 1599.00, 'L');
