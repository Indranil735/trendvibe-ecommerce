# 🛍️ TrendVibe — Enterprise E-Commerce Fashion Platform (Myntra, Ajio & Nykaa Inspired)

[![Live Demo](https://img.shields.io/badge/Demo-GitHub%20Pages-brightgreen)](https://indranil735.github.io/trendvibe-ecommerce/)
[![Deploy to Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=white)](https://render.com)
[![Java](https://img.shields.io/badge/Java-Jakarta%20EE%2010-ED8B00?logo=openjdk&logoColor=white)](https://jakarta.ee)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?logo=mysql&logoColor=white)](https://mysql.com)

A high-performance, full-stack E-Commerce web application inspired by **Myntra, Ajio, and Nykaa**. Designed with an enterprise Java MVC architecture (Jakarta EE, Servlets, JSP, JDBC, MySQL) and a responsive, mobile-first consumer storefront featuring 27 curated fashion and beauty products.

---

## 🌟 Live Storefront Links

- **GitHub Pages Live App:** [https://indranil735.github.io/trendvibe-ecommerce/](https://indranil735.github.io/trendvibe-ecommerce/)
- **Render Deployment Ready:** Includes `render.yaml`, `Dockerfile`, and `server.py` for 1-click cloud container hosting.

---

## 🏗️ Architecture & Technology Stack

| Layer | Technologies Used |
|---|---|
| **Frontend** | HTML5, CSS3 (Mobile-first Fashion Design System, Glassmorphic UI), Vanilla JavaScript |
| **View Layer** | JSP (JavaServer Pages), Jakarta JSTL (Core & Formatting Tags) |
| **Controller & Routing** | Java Servlets (`jakarta.servlet.*`), Servlet Filters (`AuthFilter`) |
| **Data Access Layer** | JDBC (Java Database Connectivity) with `PreparedStatement` & DAO Pattern |
| **Database** | MySQL 8.0+ (`ecommerce_db`) with 8 normalized relational tables |
| **Build & Dependencies** | Apache Maven (`pom.xml`) |
| **Cloud Deployment** | Render (`render.yaml`, `Dockerfile`), GitHub Pages (`gh-pages`) |
| **Target IDE & Server** | Eclipse IDE for Enterprise Java / Apache Tomcat 10+ |

---

## 👗 Curated 27-Product Catalog Across 5 Categories

1. **Men’s Wear**:
   - Oversized Acid Wash Heavyweight Tee (AURA Street)
   - Tailored Oxford Linen Shirt (Bombay Tailors)
   - Relaxed Pleated Trousers (Atelier Men)
   - Cargo Utility Flight Jacket (Urban Nomad)
   - Minimalist Monochrome Hoodie (Kult Basics)
   - Striped Resort Collar Polo (Riviera Men)

2. **Women’s Wear (Ethnic & Western)**:
   - Handloom Chanderi Anarkali Set (Virasat Ethnic)
   - Linen Co-ord Summer Set (Studio Nyka)
   - Floral Georgette Maxi Dress (Blush & Bloom)
   - Chikankari Embroidered Kurta Set (Awadh Couturier)
   - Sculpt Fit High-Rise Denim (Denim Lab)
   - Banarasi Silk Zari Saree (Kashi Weaves)

3. **Nykaa Beauty & Grooming**:
   - Matte Velvet Liquid Lip Trio (Nykaa Luxe)
   - Vitamin C Radiance Glow Serum (Aura Glow)
   - Hydrating Ceramide Moisturizer (Derm Shield)
   - 24H Waterproof Dramatic Gel Eyeliner (Kohl Queen)
   - Arabian Oud Eau De Parfum (L’Orient Perfumery)
   - Rosemary Hair Growth Density Elixir (Botanical Herbals)

4. **Footwear & Sneakers**:
   - Retro Chunky High-Top Sneakers (KickVibe)
   - Handcrafted Leather Penny Loafers (Monk & Stitch)
   - Strappy Stiletto Block Heels (Glamora)
   - Air-Cushioned Ultra Pace Trainers (Veloce Sports)
   - Minimalist Cloud Slides (Aura Comfort)

5. **Luxury Watches & Accessories**:
   - Classic Chronograph Emerald Dial Watch (Vanguard Timepieces)
   - 18K Gold Plated Paperclip Chain (Luxe Accents)
   - Acetate Retro Polarized Sunglasses (Solstice Eyewear)
   - Genuine Italian Leather Crossbody Bag (Cuoio Firenze)

---

## ⚡ Key Features

- **Dynamic Filtering & Price Segments**:
  - Filter by category (`All`, `Men`, `Women`, `Beauty`, `Footwear`, `Accessories`).
  - Price segment pills: `Under ₹999`, `₹1,000 - ₹2,500`, `₹2,500+`.
  - Brand badges: `BESTSELLER`, `NYKAA HIT`, `LUXE PICK`, `TRENDING`.
- **Instant Search**: Real-time debounce searching across titles, brands, and categories.
- **PIN Code Delivery Check**: Live Indian postal code estimator calculating delivery dates and express courier availability.
- **Cart & Discount Engine**:
  - Add to cart with size selection (`S`, `M`, `L`, `XL`, `Free Size`).
  - Promo code verification (`AURA10` for 10% off, `NYKAA20` for 20% off, `FIRST500` for ₹500 off).
  - Real-time subtotal, GST (18%), and delivery fee calculation.
- **User Authentication & Profile**:
  - Simulated customer login and session tracking.
  - Role-based Admin dashboard for product creation and catalog audits.
- **Responsive Mobile Experience**: Native app-like bottom navigation, sticky header, and touch-optimized gestures.

---

## 🚀 Deployment to Render (Step-by-Step)

This repository includes full configuration for deploying on **Render** (free cloud container tier):

### Option 1: Render Web Service via Git (Recommended)
1. Sign in to [Render.com](https://render.com).
2. Click **New +** > **Web Service**.
3. Connect your GitHub repository: `Indranil735/trendvibe-ecommerce`.
4. Render will automatically detect `render.yaml` or you can configure manually:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python3 server.py`
   - **Plan:** `Free`
5. Click **Create Web Service**.
6. Render will provision the container and give you a live HTTPS URL (e.g., `https://trendvibe-ecommerce.onrender.com`).

### Option 2: Render Docker Web Service
1. On Render, select **Docker** runtime.
2. Render will build directly from the included `Dockerfile` and expose the service on port 8080.

---

## 💻 Local Setup in Eclipse IDE (Jakarta EE & Tomcat)

1. **Clone or copy the project:**
   ```bash
   git clone https://github.com/Indranil735/trendvibe-ecommerce.git
   ```
2. **Execute MySQL Schemas:**
   ```sql
   SOURCE schema.sql;
   SOURCE sample_data.sql;
   ```
3. **Import into Eclipse:**
   - **File** > **Import...** > **Maven** > **Existing Maven Projects**.
   - Browse to `ecommerce-app` directory.
4. **Run on Tomcat 10:**
   - Right-click project > **Run As** > **Run on Server** > Select **Tomcat 10.1**.
   - Browse `http://localhost:8080/ecommerce-app/`.

---

## 📄 Interview Preparation Guide

The standalone interview guide PDF for this project is generated at:
`Desktop/TrendVibe_Project_Interview_Guide.pdf`

Contains 25+ technical interview questions and answers covering:
- Java Servlets lifecycle and thread safety
- JDBC Connection Pooling vs `DriverManager`
- Pessimistic vs Optimistic Locking for flash sale inventory
- Session Management & Security Filters
- Database Normalization (3NF) across all 8 tables
