import json
import os

with open("products_data.json", "r", encoding="utf-8") as f:
    products_list = json.load(f)

print(f"Loaded {len(products_list)} products for compilation")

# We will generate demo/index.html and src/main/webapp/index.html
# Let's create the full HTML content

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>TRENDVIBE ATELIER &bull; The Autumn/Winter Runway &amp; Luxury Beauty Collection</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #111111;
            --primary-hover: #262626;
            --accent: #a3824c;
            --accent-hover: #8c6e3b;
            --accent-subtle: #f9f6f0;
            --dark: #121212;
            --text-secondary: #4a4a4a;
            --text-muted: #7e7e7e;
            --border: #e8e6e1;
            --border-dark: #2a2a2a;
            --bg-main: #faf9f6;
            --surface: #ffffff;
            --success: #1b6348;
            --warning: #b36b28;
            --danger: #9c2e2e;
            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
            --shadow-lg: 0 16px 36px rgba(0, 0, 0, 0.12);
            --radius-sm: 2px;
            --radius-md: 4px;
            --radius-lg: 8px;
            --font-serif: 'Playfair Display', Georgia, serif;
            --font-brand: 'Cinzel', 'Playfair Display', Georgia, serif;
            --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            --bottom-nav-height: 56px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }

        html, body {
            font-family: var(--font-sans);
            background-color: var(--bg-main);
            color: var(--dark);
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
            width: 100%;
        }

        body {
            padding-bottom: calc(var(--bottom-nav-height) + env(safe-area-inset-bottom, 16px));
        }

        @media (min-width: 992px) {
            body { padding-bottom: 0; }
        }

        a { color: inherit; text-decoration: none; }
        button { font-family: inherit; }

        .container {
            max-width: 1320px;
            margin: 0 auto;
            padding: 0 16px;
            width: 100%;
        }
        @media (min-width: 768px) {
            .container { padding: 0 24px; }
        }

        /* Top Announcement Bar (Mobile Safe) */
        .top-banner {
            background-color: #0d0d0d;
            color: #d6cfc7;
            text-align: center;
            padding: 6px 12px;
            font-size: 10px;
            font-weight: 600;
            letter-spacing: 1px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            text-transform: uppercase;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            width: 100%;
        }
        .promo-code-pill {
            background: rgba(255, 255, 255, 0.12);
            padding: 1px 6px;
            border-radius: var(--radius-sm);
            color: #ffffff;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        /* Site Header */
        header.site-header {
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(12px);
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid var(--border);
            width: 100%;
        }

        .navbar-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 58px;
            gap: 12px;
        }
        @media (min-width: 992px) {
            .navbar-content { height: 72px; gap: 20px; }
        }

        .brand-logo-wrap {
            display: flex;
            align-items: baseline;
            gap: 6px;
            cursor: pointer;
            user-select: none;
        }
        .brand-logo {
            font-family: var(--font-brand);
            font-size: 17px;
            font-weight: 700;
            letter-spacing: 2.5px;
            color: var(--primary);
            text-transform: uppercase;
        }
        @media (min-width: 768px) {
            .brand-logo { font-size: 22px; letter-spacing: 4px; }
        }
        .brand-sub {
            font-size: 9px;
            letter-spacing: 1.5px;
            color: var(--accent);
            font-weight: 700;
            text-transform: uppercase;
        }

        /* Desktop Nav Links */
        .desktop-nav-links {
            display: none;
            list-style: none;
            gap: 24px;
            align-items: center;
            height: 100%;
        }
        @media (min-width: 992px) {
            .desktop-nav-links { display: flex; }
        }
        .desktop-nav-links li { height: 100%; display: flex; align-items: center; }
        .desktop-nav-links a {
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 1.5px;
            color: var(--text-secondary);
            cursor: pointer;
            padding: 24px 2px;
            position: relative;
            transition: color 0.2s ease;
            text-transform: uppercase;
        }
        .desktop-nav-links a:hover,
        .desktop-nav-links a.active {
            color: var(--primary);
        }
        .desktop-nav-links a.active::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background-color: var(--primary);
        }

        /* Desktop Search Field */
        .desktop-search-container {
            display: none;
            position: relative;
            flex: 1;
            max-width: 280px;
        }
        @media (min-width: 992px) {
            .desktop-search-container { display: block; }
        }
        .search-input-field {
            width: 100%;
            background: #f4f3ef;
            border: 1px solid transparent;
            padding: 9px 14px 9px 36px;
            border-radius: var(--radius-sm);
            font-size: 12px;
            color: var(--dark);
            outline: none;
            transition: all 0.2s ease;
        }
        .search-input-field:focus {
            background: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 0 0 1px var(--primary);
        }
        .search-icon-svg {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            width: 14px;
            height: 14px;
            color: var(--text-muted);
            pointer-events: none;
        }

        /* Nav Actions (Header Right) */
        .nav-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        @media (min-width: 768px) {
            .nav-actions { gap: 18px; }
        }
        .action-icon-btn {
            background: none;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            color: var(--dark);
            padding: 6px;
            transition: color 0.2s ease;
        }
        .action-icon-btn:hover { color: var(--accent); }
        .action-icon-btn svg { width: 20px; height: 20px; }
        .action-icon-btn span.label-text {
            display: none;
            font-size: 10px;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            margin-left: 4px;
        }
        @media (min-width: 992px) {
            .action-icon-btn span.label-text { display: inline-block; }
        }
        .badge-counter {
            position: absolute;
            top: 0;
            right: 0;
            background: var(--primary);
            color: #ffffff;
            font-size: 9px;
            font-weight: 700;
            width: 15px;
            height: 15px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .mobile-menu-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            background: none;
            border: none;
            font-size: 20px;
            cursor: pointer;
            color: var(--primary);
            padding: 4px;
        }
        @media (min-width: 992px) {
            .mobile-menu-btn { display: none; }
        }

        /* Mobile Bottom Nav */
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: var(--bottom-nav-height);
            background: #ffffff;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-around;
            align-items: center;
            z-index: 99;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
        }
        @media (min-width: 992px) {
            .bottom-nav { display: none; }
        }
        .bottom-nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: none;
            border: none;
            color: var(--text-muted);
            font-size: 9px;
            font-weight: 600;
            letter-spacing: 0.5px;
            gap: 2px;
            cursor: pointer;
            padding: 4px;
            flex: 1;
            text-transform: uppercase;
        }
        .bottom-nav-item.active {
            color: var(--primary);
            font-weight: 700;
        }
        .bottom-nav-item svg { width: 18px; height: 18px; }

        /* Mobile Drawer */
        .drawer-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.6);
            z-index: 1000;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }
        .drawer-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }
        .mobile-drawer {
            position: fixed;
            top: 0;
            left: 0;
            width: 290px;
            height: 100%;
            background: #ffffff;
            z-index: 1001;
            transform: translateX(-100%);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
        }
        .drawer-overlay.active .mobile-drawer {
            transform: translateX(0);
        }
        .drawer-header {
            padding: 20px 16px;
            border-bottom: 1px solid var(--border);
            background: #111111;
            color: #ffffff;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }
        .drawer-body {
            padding: 12px 0;
            overflow-y: auto;
            flex: 1;
        }
        .drawer-item {
            padding: 12px 20px;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--dark);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: background 0.2s;
        }
        .drawer-item:hover { background: #f8f7f4; }
        .drawer-divider {
            height: 1px;
            background: var(--border);
            margin: 10px 20px;
        }

        /* Compact Hero Banner (Mobile Optimized) */
        .hero-banner {
            position: relative;
            background: #161514;
            color: #ffffff;
            border-radius: var(--radius-sm);
            margin: 12px 0 16px 0;
            overflow: hidden;
            display: flex;
            min-height: 170px;
            box-shadow: var(--shadow-sm);
        }
        @media (min-width: 768px) {
            .hero-banner { min-height: 340px; margin: 18px 0 24px 0; }
        }
        .hero-banner-image {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center 25%;
            opacity: 0.5;
            filter: contrast(105%) brightness(90%);
        }
        .hero-banner-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(90deg, rgba(17,17,17,0.92) 0%, rgba(17,17,17,0.7) 60%, rgba(17,17,17,0.2) 100%);
        }
        .hero-content {
            position: relative;
            z-index: 2;
            padding: 20px 16px;
            max-width: 540px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        @media (min-width: 768px) {
            .hero-content { padding: 40px 32px; }
        }
        .hero-tag {
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: var(--accent);
            margin-bottom: 6px;
        }
        .hero-title {
            font-family: var(--font-serif);
            font-size: 20px;
            line-height: 1.2;
            font-weight: 600;
            margin-bottom: 8px;
            letter-spacing: -0.3px;
        }
        @media (min-width: 768px) {
            .hero-title { font-size: 34px; margin-bottom: 12px; }
        }
        .hero-desc {
            display: none;
            font-size: 13px;
            line-height: 1.5;
            color: #d1cdc7;
            margin-bottom: 18px;
        }
        @media (min-width: 768px) {
            .hero-desc { display: block; }
        }
        .hero-btn-group {
            display: flex;
            gap: 10px;
        }
        .hero-cta {
            display: inline-block;
            background: #ffffff;
            color: #111111;
            padding: 9px 18px;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .hero-cta:hover { background: var(--accent); color: #ffffff; }

        /* Filter Chips / Categories Rail */
        .category-scroll-container {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 8px;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
            margin-bottom: 10px;
        }
        .category-scroll-container::-webkit-scrollbar { display: none; }
        .cat-chip {
            padding: 7px 14px;
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            color: var(--text-secondary);
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s ease;
        }
        .cat-chip:hover { border-color: var(--primary); color: var(--primary); }
        .cat-chip.active {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }

        /* Slim Single-Line Filters Bar */
        .filters-toolbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            padding: 8px 12px;
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            margin-bottom: 14px;
            overflow-x: auto;
            scrollbar-width: none;
        }
        .filters-toolbar::-webkit-scrollbar { display: none; }
        .price-filter-group {
            display: flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
        }
        .price-btn {
            background: #f7f6f2;
            border: 1px solid transparent;
            padding: 5px 10px;
            font-size: 10px;
            font-weight: 600;
            color: var(--text-secondary);
            border-radius: var(--radius-sm);
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s;
        }
        .price-btn:hover { border-color: var(--border-dark); color: var(--primary); }
        .price-btn.active { background: var(--primary); color: #ffffff; }
        .sort-select {
            padding: 5px 10px;
            border: 1px solid var(--border);
            background: #ffffff;
            font-size: 10px;
            font-weight: 600;
            color: var(--dark);
            border-radius: var(--radius-sm);
            outline: none;
            cursor: pointer;
            text-transform: uppercase;
            white-space: nowrap;
        }

        /* Catalog Title Section */
        .catalog-header-bar {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 12px;
        }
        .catalog-heading {
            font-family: var(--font-serif);
            font-size: 18px;
            font-weight: 600;
            color: var(--primary);
            letter-spacing: -0.2px;
        }
        @media (min-width: 768px) {
            .catalog-heading { font-size: 24px; }
        }
        .catalog-count {
            font-size: 11px;
            color: var(--text-muted);
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        /* Product Grid (Mobile 2-Column, Desktop Multi-Column) */
        .product-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-bottom: 30px;
        }
        @media (min-width: 768px) {
            .product-grid { grid-template-columns: repeat(3, 1fr); gap: 20px; }
        }
        @media (min-width: 1100px) {
            .product-grid { grid-template-columns: repeat(4, 1fr); gap: 24px; }
        }

        /* Product Card */
        .product-card {
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            position: relative;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .product-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-sm);
        }
        .product-image-container {
            position: relative;
            width: 100%;
            padding-top: 135%; /* Portrait fashion ratio */
            background: #f0eee9;
            overflow: hidden;
            cursor: pointer;
        }
        .product-card-img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        .product-card:hover .product-card-img {
            transform: scale(1.04);
        }
        .product-badge {
            position: absolute;
            top: 8px;
            left: 8px;
            background: rgba(17, 17, 17, 0.88);
            backdrop-filter: blur(4px);
            color: #ffffff;
            font-size: 8px;
            font-weight: 700;
            letter-spacing: 1px;
            padding: 3px 6px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            z-index: 2;
        }
        .wishlist-btn {
            position: absolute;
            top: 8px;
            right: 8px;
            background: rgba(255, 255, 255, 0.9);
            border: none;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 2;
            transition: transform 0.2s;
            color: var(--dark);
            font-size: 13px;
        }
        .wishlist-btn:hover { transform: scale(1.1); }
        .wishlist-btn.active { color: #d13d3d; }
        .quick-add-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            background: rgba(17, 17, 17, 0.9);
            color: #ffffff;
            padding: 8px;
            text-align: center;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            transform: translateY(100%);
            transition: transform 0.2s ease;
            cursor: pointer;
        }
        .product-card:hover .quick-add-overlay {
            transform: translateY(0);
        }

        .product-info {
            padding: 10px;
            display: flex;
            flex-direction: column;
            flex: 1;
        }
        .product-brand {
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 1px;
            color: var(--accent);
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .product-title {
            font-size: 11px;
            font-weight: 500;
            color: var(--primary);
            line-height: 1.35;
            margin-bottom: 6px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            height: 30px;
            cursor: pointer;
        }
        .product-pricing {
            display: flex;
            align-items: baseline;
            gap: 6px;
            margin-top: auto;
            flex-wrap: wrap;
        }
        .current-price {
            font-size: 13px;
            font-weight: 700;
            color: var(--primary);
        }
        .original-price {
            font-size: 10px;
            color: var(--text-muted);
            text-decoration: line-through;
        }
        .discount-rate {
            font-size: 10px;
            font-weight: 700;
            color: var(--success);
        }

        /* Load More Pagination Button */
        .load-more-container {
            text-align: center;
            margin: 20px 0 50px 0;
        }
        .load-more-btn {
            background: #ffffff;
            border: 1px solid var(--primary);
            color: var(--primary);
            padding: 12px 28px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .load-more-btn:hover {
            background: var(--primary);
            color: #ffffff;
        }

        /* Modals & Backdrop */
        .modal-backdrop {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.72);
            backdrop-filter: blur(4px);
            z-index: 1000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }
        .modal-backdrop.active { display: flex; }

        /* Phone + OTP Authentication Modal */
        .auth-modal {
            background: #ffffff;
            width: 100%;
            max-width: 420px;
            border-radius: var(--radius-md);
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            position: relative;
        }
        .auth-header {
            background: #111111;
            color: #ffffff;
            padding: 22px 24px;
            text-align: center;
            position: relative;
        }
        .auth-header-title {
            font-family: var(--font-brand);
            font-size: 17px;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        .auth-header-sub {
            font-size: 11px;
            color: var(--accent);
            letter-spacing: 1px;
            margin-top: 4px;
        }
        .auth-close-btn {
            position: absolute;
            top: 14px;
            right: 16px;
            background: none;
            border: none;
            color: #ffffff;
            font-size: 20px;
            cursor: pointer;
        }
        .auth-body {
            padding: 24px 20px;
        }
        .otp-inputs-row {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin: 18px 0;
        }
        .otp-box {
            width: 48px;
            height: 52px;
            text-align: center;
            font-size: 20px;
            font-weight: 700;
            border: 1px solid var(--border);
            border-radius: 4px;
            outline: none;
            transition: border-color 0.2s;
        }
        .otp-box:focus { border-color: var(--primary); }
        .sms-toast-banner {
            background: #2a2a2a;
            color: #ffffff;
            padding: 10px 14px;
            border-radius: 4px;
            font-size: 11px;
            line-height: 1.4;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Multi-Step Checkout Modal */
        .checkout-modal {
            background: #ffffff;
            width: 100%;
            max-width: 780px;
            border-radius: var(--radius-md);
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            position: relative;
        }
        .checkout-header {
            background: #111111;
            color: #ffffff;
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .checkout-progress-bar {
            display: flex;
            background: #f8f7f4;
            border-bottom: 1px solid var(--border);
        }
        .step-pill {
            flex: 1;
            padding: 10px;
            text-align: center;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 0.5px;
            color: var(--text-muted);
            text-transform: uppercase;
            border-bottom: 2px solid transparent;
            cursor: pointer;
        }
        .step-pill.active {
            color: var(--primary);
            border-bottom-color: var(--primary);
            background: #ffffff;
        }
        .checkout-body {
            padding: 20px;
            overflow-y: auto;
            flex: 1;
        }
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
        @media (max-width: 600px) {
            .form-grid { grid-template-columns: 1fr; }
        }
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .form-label {
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 0.5px;
            color: var(--text-secondary);
            text-transform: uppercase;
        }
        .form-input {
            padding: 9px 12px;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            font-size: 12px;
            color: var(--dark);
            outline: none;
            transition: border-color 0.2s;
        }
        .form-input:focus { border-color: var(--primary); }

        .payment-methods-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
            margin-bottom: 16px;
        }
        @media (max-width: 600px) {
            .payment-methods-grid { grid-template-columns: repeat(2, 1fr); }
        }
        .payment-tab-btn {
            padding: 12px 6px;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            background: #faf9f6;
            cursor: pointer;
            text-align: center;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--text-secondary);
            transition: all 0.2s;
        }
        .payment-tab-btn.active {
            background: #ffffff;
            border-color: var(--primary);
            color: var(--primary);
        }

        /* Live Card Mockup */
        .card-visual-container {
            background: linear-gradient(135deg, #1b1b1b 0%, #2f2f2f 50%, #151515 100%);
            color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            max-width: 340px;
            margin: 0 auto 16px auto;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            position: relative;
        }
        .card-chip {
            width: 36px;
            height: 26px;
            background: linear-gradient(135deg, #d4af37 0%, #aa8020 100%);
            border-radius: 4px;
            margin-bottom: 20px;
        }
        .card-number-display {
            font-family: 'Courier New', monospace;
            font-size: 16px;
            letter-spacing: 2px;
            margin-bottom: 16px;
        }
        .card-meta-row {
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            text-transform: uppercase;
            color: #b5b5b5;
        }

        .checkout-footer-btn {
            background: var(--primary);
            color: #ffffff;
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: var(--radius-sm);
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            cursor: pointer;
            margin-top: 16px;
            transition: background 0.2s;
        }
        .checkout-footer-btn:hover { background: var(--accent); }

        /* Orders View & Timeline */
        .order-card {
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 16px;
            margin-bottom: 16px;
        }
        .tracking-pipeline {
            display: flex;
            justify-content: space-between;
            position: relative;
            margin: 20px 0;
        }
        .tracking-pipeline::before {
            content: '';
            position: absolute;
            top: 12px;
            left: 16px;
            right: 16px;
            height: 2px;
            background: #e3e0d8;
            z-index: 1;
        }
        .pipeline-step {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            text-align: center;
            flex: 1;
        }
        .step-dot {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: #ffffff;
            border: 2px solid #e3e0d8;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: 700;
            color: var(--text-muted);
        }
        .pipeline-step.completed .step-dot {
            background: var(--primary);
            border-color: var(--primary);
            color: #ffffff;
        }
        .pipeline-step.active .step-dot {
            background: var(--accent);
            border-color: var(--accent);
            color: #ffffff;
        }
        .step-label {
            font-size: 9px;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--text-secondary);
        }

        /* Product Detail Quick View Modal */
        .pdp-modal {
            background: #ffffff;
            width: 100%;
            max-width: 820px;
            border-radius: var(--radius-md);
            overflow: hidden;
            display: grid;
            grid-template-columns: 1fr 1fr;
            box-shadow: var(--shadow-lg);
            position: relative;
            max-height: 90vh;
        }
        @media (max-width: 768px) {
            .pdp-modal { grid-template-columns: 1fr; overflow-y: auto; }
        }
        .pdp-img-col {
            position: relative;
            background: #f5f4ef;
            min-height: 280px;
        }
        .pdp-main-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .pdp-details-col {
            padding: 24px 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }

        .view-section { display: none; }
        .view-section.active { display: block; }

        .toast-banner {
            position: fixed;
            bottom: 70px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: #111111;
            color: #ffffff;
            padding: 10px 20px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            box-shadow: var(--shadow-lg);
            z-index: 2000;
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            pointer-events: none;
        }
        .toast-banner.active {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }

        /* Footer */
        footer.site-footer {
            background: #0f0e0e;
            color: #c9c5bd;
            padding: 40px 0 24px 0;
            border-top: 1px solid #232220;
            font-size: 12px;
        }
        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }
        @media (max-width: 768px) {
            .footer-grid { grid-template-columns: 1fr; gap: 20px; }
        }
    </style>
</head>
<body>

    <!-- Compact Marquee / Top Announcement Bar -->
    <div class="top-banner">
        <span>EXPRESS WHITE-GLOVE DISPATCH &bull; CODE: <span class="promo-code-pill">ATELIER10</span> FOR 10% OFF RUNWAY &bull; BLUEDART AIR</span>
    </div>

    <!-- Site Header -->
    <header class="site-header">
        <div class="container navbar-content">
            <button class="mobile-menu-btn" onclick="toggleDrawer(true)">&#9776;</button>

            <!-- Brand Logo -->
            <div class="brand-logo-wrap" onclick="switchView('shop')">
                <span class="brand-logo">TRENDVIBE</span>
                <span class="brand-sub">ATELIER</span>
            </div>

            <!-- Desktop Nav Links -->
            <ul class="desktop-nav-links">
                <li><a onclick="filterByNav('All', this)" id="nav-all" class="active">NEW IN (260)</a></li>
                <li><a onclick="filterByNav('Women', this)" id="nav-women">WOMEN</a></li>
                <li><a onclick="filterByNav('Men', this)" id="nav-men">MEN</a></li>
                <li><a onclick="filterByNav('Beauty', this)" id="nav-beauty">BEAUTY &amp; SCENTS</a></li>
                <li><a onclick="filterByNav('Shoes', this)" id="nav-shoes">FOOTWEAR</a></li>
                <li><a onclick="filterByNav('Watches', this)" id="nav-watches">ACCESSORIES</a></li>
                <li><a onclick="switchView('orders')" id="nav-orders">ORDERS</a></li>
            </ul>

            <!-- Desktop Search Field -->
            <div class="desktop-search-container">
                <svg class="search-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                <input type="text" class="search-input-field" placeholder="Search 260+ runway pieces..." onkeyup="handleSearch(this.value)">
            </div>

            <!-- Header Actions (Clean Icon Only on Mobile, Zero Text Clipping) -->
            <div class="nav-actions">
                <button class="action-icon-btn" onclick="openAuthOrProfileModal()" id="profileHeaderBtn">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                    <span class="label-text" id="profileBtnLabel">Profile</span>
                </button>
                <button class="action-icon-btn" onclick="switchView('wishlist')">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                    <span id="wishlist-badge" class="badge-counter" style="display: none;">0</span>
                    <span class="label-text">Wishlist</span>
                </button>
                <button class="action-icon-btn" onclick="switchView('cart')">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
                    <span id="cart-badge" class="badge-counter">0</span>
                    <span class="label-text">Bag</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Slide-Out Mobile Drawer -->
    <div id="drawerOverlay" class="drawer-overlay" onclick="toggleDrawer(false)">
        <div class="mobile-drawer" onclick="event.stopPropagation()">
            <div class="drawer-header">
                <div>
                    <div style="font-family: var(--font-brand); font-size: 16px; letter-spacing: 2px;">TRENDVIBE ATELIER</div>
                    <div style="font-size: 10px; color: var(--accent); letter-spacing: 1px;">HAUTE COUTURE &bull; BEAUTY</div>
                </div>
                <button style="background: none; border: none; color: #fff; font-size: 20px; cursor: pointer;" onclick="toggleDrawer(false)">&times;</button>
            </div>
            <div class="drawer-body">
                <div class="drawer-item" onclick="switchView('shop'); filterByNav('All'); toggleDrawer(false);">All Runway Curations (260)</div>
                <div class="drawer-item" onclick="switchView('shop'); filterByNav('Women'); toggleDrawer(false);">Women's Atelier</div>
                <div class="drawer-item" onclick="switchView('shop'); filterByNav('Men'); toggleDrawer(false);">Men's Tailoring</div>
                <div class="drawer-item" onclick="switchView('shop'); filterByNav('Beauty'); toggleDrawer(false);">Beauty &amp; Fine Fragrance</div>
                <div class="drawer-item" onclick="switchView('shop'); filterByNav('Shoes'); toggleDrawer(false);">Footwear &amp; Loafers</div>
                <div class="drawer-item" onclick="switchView('shop'); filterByNav('Watches'); toggleDrawer(false);">Watches &amp; Accessories</div>
                <div class="drawer-divider"></div>
                <div class="drawer-item" onclick="openAuthOrProfileModal(); toggleDrawer(false);">My Profile &bull; Login</div>
                <div class="drawer-item" onclick="switchView('wishlist'); toggleDrawer(false);">Wishlist (<span id="drawerWishlistCount">0</span>)</div>
                <div class="drawer-item" onclick="switchView('cart'); toggleDrawer(false);">Shopping Bag (<span id="drawerCartCount">0</span>)</div>
                <div class="drawer-item" onclick="switchView('orders'); toggleDrawer(false);">My Orders &amp; Invoices</div>
            </div>
        </div>
    </div>

    <!-- Mobile Bottom App Navigation Bar -->
    <nav class="bottom-nav">
        <button id="bnav-shop" class="bottom-nav-item active" onclick="switchView('shop')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
            <span>Runway</span>
        </button>
        <button id="bnav-categories" class="bottom-nav-item" onclick="toggleDrawer(true)">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M4 6h16M4 12h16M4 18h7"/></svg>
            <span>Menu</span>
        </button>
        <button id="bnav-wishlist" class="bottom-nav-item" onclick="switchView('wishlist')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
            <span>Wishlist</span>
        </button>
        <button id="bnav-cart" class="bottom-nav-item" onclick="switchView('cart')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
            <span>Bag</span>
        </button>
        <button id="bnav-orders" class="bottom-nav-item" onclick="switchView('orders')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
            <span>Orders</span>
        </button>
    </nav>

    <!-- Main Container -->
    <main class="container">

        <!-- VIEW 1: SHOP / CATALOG -->
        <div id="view-shop" class="view-section active">

            <!-- Compact Editorial Campaign Hero (Mobile Optimized) -->
            <div class="hero-banner">
                <img class="hero-banner-image" src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=1200&q=80" alt="Editorial Fashion Campaign">
                <div class="hero-banner-overlay"></div>
                <div class="hero-content">
                    <span class="hero-tag">AUTUMN / WINTER &bull; 260+ STYLES</span>
                    <h1 class="hero-title">Architectural Silhouettes &amp; Pure Botanical Scents</h1>
                    <p class="hero-desc">
                        A study in minimalist tailoring, fine Italian wools, and artisanal French fragrances created for timeless refinement.
                    </p>
                    <div class="hero-btn-group">
                        <a href="#catalogGrid" class="hero-cta">EXPLORE RUNWAY &rarr;</a>
                    </div>
                </div>
            </div>

            <!-- Horizontal Category Chips Rail -->
            <div class="category-scroll-container">
                <button class="cat-chip active" onclick="filterCategory('All', this)">All (260)</button>
                <button class="cat-chip" onclick="filterCategory('Shirts', this)">Tailored Shirts</button>
                <button class="cat-chip" onclick="filterCategory('Dresses', this)">Dresses &amp; Sarees</button>
                <button class="cat-chip" onclick="filterCategory('Pants', this)">Denim &amp; Trousers</button>
                <button class="cat-chip" onclick="filterCategory('Beauty', this)">Beauty &amp; Scents</button>
                <button class="cat-chip" onclick="filterCategory('Shoes', this)">Artisanal Footwear</button>
                <button class="cat-chip" onclick="filterCategory('Watches', this)">Watches &amp; Luxury</button>
            </div>

            <!-- Slim Single-Line Filters Bar -->
            <div class="filters-toolbar">
                <div class="price-filter-group">
                    <button class="price-btn active" onclick="filterPrice('All', this)">All Prices</button>
                    <button class="price-btn" onclick="filterPrice('under1500', this)">Under &#8377;1,500</button>
                    <button class="price-btn" onclick="filterPrice('1500to3500', this)">&#8377;1,500 &ndash; &#8377;3,500</button>
                    <button class="price-btn" onclick="filterPrice('above3500', this)">&#8377;3,500+</button>
                </div>
                <div>
                    <select id="sortSelect" class="sort-select" onchange="handleSort(this.value)">
                        <option value="featured">Sort: Curated</option>
                        <option value="price-low">Price: Low to High</option>
                        <option value="price-high">Price: High to Low</option>
                        <option value="rating">Top Rated</option>
                    </select>
                </div>
            </div>

            <!-- Catalog Header Bar -->
            <div class="catalog-header-bar" id="catalogGrid">
                <h2 id="catalogTitle" class="catalog-heading">Autumn / Winter Edit</h2>
                <span id="catalogCount" class="catalog-count">260 styles available</span>
            </div>

            <!-- Product Cards Grid -->
            <div id="productGrid" class="product-grid">
                <!-- Products rendered dynamically -->
            </div>

            <!-- Load More Pagination Button -->
            <div class="load-more-container" id="loadMoreBox">
                <button class="load-more-btn" onclick="loadMoreProducts()" id="loadMoreBtn">
                    Show More Pieces (<span id="loadMoreCounter">24 of 260</span>) &darr;
                </button>
            </div>
        </div>

        <!-- VIEW 2: CART / BAG -->
        <div id="view-cart" class="view-section">
            <div style="margin: 20px 0 16px 0;">
                <h2 style="font-family: var(--font-serif); font-size: 22px;">Shopping Bag</h2>
                <p style="font-size: 12px; color: var(--text-muted);"><span id="cartCountHeader">0</span> items selected for express dispatch</p>
            </div>
            <div id="cartContentContainer">
                <!-- Cart items or empty state rendered via JS -->
            </div>
        </div>

        <!-- VIEW 3: WISHLIST -->
        <div id="view-wishlist" class="view-section">
            <div style="margin: 20px 0 16px 0;">
                <h2 style="font-family: var(--font-serif); font-size: 22px;">Saved Wishlist</h2>
                <p style="font-size: 12px; color: var(--text-muted);"><span id="wishlistCountHeader">0</span> pieces saved for your wardrobe</p>
            </div>
            <div id="wishlistContentContainer" class="product-grid">
                <!-- Wishlist items rendered via JS -->
            </div>
        </div>

        <!-- VIEW 4: MY ORDERS & TRACKING -->
        <div id="view-orders" class="view-section">
            <div style="margin: 20px 0 16px 0; display: flex; justify-content: space-between; align-items: baseline;">
                <div>
                    <h2 style="font-family: var(--font-serif); font-size: 22px;">My Orders &amp; Live Tracking</h2>
                    <p style="font-size: 12px; color: var(--text-muted);">BlueDart Air tracking &amp; GST tax invoices</p>
                </div>
                <button class="cat-chip" onclick="switchView('shop')">Explore Runway</button>
            </div>
            <div id="ordersListContainer">
                <!-- Orders rendered dynamically via JS -->
            </div>
        </div>

    </main>

    <!-- Phone Number + OTP Authentication Modal -->
    <div id="authModal" class="modal-backdrop">
        <div class="auth-modal">
            <div class="auth-header">
                <button class="auth-close-btn" onclick="closeAuthModal()">&times;</button>
                <div class="auth-header-title">TRENDVIBE ATELIER</div>
                <div class="auth-header-sub">SIGN IN WITH MOBILE &bull; SECURE OTP</div>
            </div>
            <div class="auth-body">
                <!-- Step 1: Phone Input -->
                <div id="authStepPhone">
                    <p style="font-size: 12px; color: var(--text-secondary); margin-bottom: 16px; line-height: 1.5;">
                        Enter your mobile number to access your luxury wardrobe, saved measurements, and order tracking.
                    </p>
                    <div style="display: flex; gap: 8px; margin-bottom: 18px;">
                        <div style="display: flex; align-items: center; gap: 4px; padding: 10px 12px; background: #f5f4ef; border: 1px solid var(--border); border-radius: 4px; font-size: 12px; font-weight: 700;">
                            <span>🇮🇳</span> <span>+91</span>
                        </div>
                        <input type="tel" id="loginPhoneInput" class="form-input" placeholder="9876543210" maxlength="10" value="9876543210" style="flex: 1; font-size: 14px; font-weight: 600; letter-spacing: 1px;">
                    </div>
                    <button class="checkout-footer-btn" style="margin-top: 0;" onclick="sendOtpToPhone()">Send Verification Code &rarr;</button>
                    <div style="text-align: center; margin-top: 14px;">
                        <span style="font-size: 11px; color: var(--text-muted); cursor: pointer;" onclick="closeAuthModal()">Continue browsing as Guest &rarr;</span>
                    </div>
                </div>

                <!-- Step 2: OTP Verification -->
                <div id="authStepOtp" style="display: none;">
                    <div class="sms-toast-banner" id="simulatedSmsToast">
                        <span>💬</span>
                        <div><strong>Messages:</strong> Your TrendVibe Atelier OTP is <strong id="generatedOtpDisplay" style="color: #ffde59;">4829</strong>. Valid for 10 minutes.</div>
                    </div>
                    <p style="font-size: 12px; color: var(--text-secondary); margin-bottom: 10px;">
                        Verification code sent to <strong id="displayTargetPhone">+91 9876543210</strong>
                    </p>

                    <div class="otp-inputs-row">
                        <input type="text" class="otp-box" id="otp1" maxlength="1" onkeyup="handleOtpKey(1, event)" value="4">
                        <input type="text" class="otp-box" id="otp2" maxlength="1" onkeyup="handleOtpKey(2, event)" value="8">
                        <input type="text" class="otp-box" id="otp3" maxlength="1" onkeyup="handleOtpKey(3, event)" value="2">
                        <input type="text" class="otp-box" id="otp4" maxlength="1" onkeyup="handleOtpKey(4, event)" value="9">
                    </div>

                    <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 18px;">
                        <span style="color: var(--text-muted);">Resend code in <strong id="otpTimerText">28s</strong></span>
                        <span style="color: var(--accent); font-weight: 700; cursor: pointer;" onclick="autoFillOtp()">Auto-Fill OTP</span>
                    </div>

                    <button class="checkout-footer-btn" style="margin-top: 0;" onclick="verifyOtpCode()">Verify &amp; Continue &rarr;</button>
                </div>

                <!-- Step 3: Profile Registration (New User) -->
                <div id="authStepProfile" style="display: none;">
                    <p style="font-size: 12px; color: var(--text-secondary); margin-bottom: 14px;">
                        Welcome to TrendVibe Atelier! Please confirm your personal details for white-glove dispatch.
                    </p>
                    <div class="form-grid" style="grid-template-columns: 1fr; gap: 10px; margin-bottom: 16px;">
                        <div class="form-group">
                            <label class="form-label">Full Name *</label>
                            <input type="text" id="regNameInput" class="form-input" placeholder="Soma Indranil" value="Soma Indranil">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Email Address *</label>
                            <input type="email" id="regEmailInput" class="form-input" placeholder="somaindra@gmail.com" value="somaindra@gmail.com">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Delivery Pincode *</label>
                            <input type="text" id="regPinInput" class="form-input" placeholder="400001" maxlength="6" value="400001">
                        </div>
                    </div>
                    <button class="checkout-footer-btn" style="margin-top: 0;" onclick="completeRegistration()">Enter TrendVibe Atelier &rarr;</button>
                </div>

                <!-- Logged In Profile Dashboard View -->
                <div id="authStepDashboard" style="display: none;">
                    <div style="text-align: center; margin-bottom: 18px;">
                        <div style="width: 50px; height: 50px; background: #111; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; margin: 0 auto 10px auto;" id="userAvatarText">SI</div>
                        <h3 id="dashUserName" style="font-size: 16px; font-weight: 700;">Soma Indranil</h3>
                        <p id="dashUserPhone" style="font-size: 12px; color: var(--text-muted);">+91 9876543210</p>
                    </div>

                    <div style="background: #faf8f5; border: 1px solid var(--border); padding: 12px; border-radius: 4px; font-size: 12px; margin-bottom: 16px;">
                        <div><strong>Email:</strong> <span id="dashUserEmail">somaindra@gmail.com</span></div>
                        <div style="margin-top: 4px;"><strong>Default Pincode:</strong> <span id="dashUserPin">400001 (Mumbai)</span></div>
                    </div>

                    <div style="display: flex; gap: 10px;">
                        <button class="cat-chip" style="flex: 1;" onclick="closeAuthModal(); switchView('orders');">View Orders</button>
                        <button class="cat-chip" style="flex: 1; border-color: var(--danger); color: var(--danger);" onclick="signOutUser()">Sign Out</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Multi-Step Checkout Modal -->
    <div id="checkoutModalBackdrop" class="modal-backdrop">
        <div class="checkout-modal">
            <div class="checkout-header">
                <span style="font-family: var(--font-brand); font-size: 14px; letter-spacing: 2px;">SECURE CHECKOUT</span>
                <button style="background: none; border: none; color: #fff; font-size: 20px; cursor: pointer;" onclick="closeCheckoutModal()">&times;</button>
            </div>

            <div class="checkout-progress-bar">
                <div id="stepTab1" class="step-pill active" onclick="gotoStep(1)">1. Address</div>
                <div id="stepTab2" class="step-pill" onclick="gotoStep(2)">2. Payment</div>
                <div id="stepTab3" class="step-pill" onclick="gotoStep(3)">3. Review</div>
            </div>

            <div class="checkout-body">
                <!-- Step 1: Address -->
                <div id="checkoutStep1">
                    <h3 style="font-family: var(--font-serif); font-size: 16px; margin-bottom: 12px;">Delivery Address</h3>
                    <div class="form-grid">
                        <div class="form-group">
                            <label class="form-label">Full Name *</label>
                            <input type="text" id="shipName" class="form-input" value="Soma Indranil">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Phone (+91) *</label>
                            <input type="tel" id="shipPhone" class="form-input" value="9876543210">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Postal Pincode *</label>
                            <input type="text" id="shipPin" class="form-input" value="400001" maxlength="6" onkeyup="handlePincodeAutoFill(this.value)">
                        </div>
                        <div class="form-group">
                            <label class="form-label">City &amp; State</label>
                            <input type="text" id="shipCityState" class="form-input" value="Mumbai, Maharashtra">
                        </div>
                        <div class="form-group" style="grid-column: 1 / -1;">
                            <label class="form-label">Street Address *</label>
                            <input type="text" id="shipStreet" class="form-input" value="Flat 402, Signature Palms, Bandra West">
                        </div>
                    </div>
                    <button class="checkout-footer-btn" onclick="gotoStep(2)">Continue to Payment &rarr;</button>
                </div>

                <!-- Step 2: Payment -->
                <div id="checkoutStep2" style="display: none;">
                    <h3 style="font-family: var(--font-serif); font-size: 16px; margin-bottom: 12px;">Payment Method</h3>
                    <div class="payment-methods-grid">
                        <button id="payTabUpi" class="payment-tab-btn active" onclick="switchPaymentTab('upi')">UPI / QR</button>
                        <button id="payTabCard" class="payment-tab-btn" onclick="switchPaymentTab('card')">Card</button>
                        <button id="payTabNet" class="payment-tab-btn" onclick="switchPaymentTab('net')">Net Banking</button>
                        <button id="payTabCod" class="payment-tab-btn" onclick="switchPaymentTab('cod')">Cash / COD</button>
                    </div>

                    <div id="payFormUpi">
                        <div style="background: #faf8f5; border: 1px solid var(--border); padding: 16px; border-radius: 4px; text-align: center;">
                            <div style="font-size: 11px; font-weight: 700; margin-bottom: 8px;">SCAN &amp; PAY VIA ANY UPI APP</div>
                            <div style="margin-bottom: 12px;">
                                <input type="text" id="upiVpa" class="form-input" style="max-width: 260px; margin: 0 auto;" value="soma@okaxis">
                            </div>
                            <button class="cat-chip" onclick="alert('Instant UPI QR Code generated! Please scan using GPay, PhonePe or Paytm.')">Show Instant QR Code</button>
                        </div>
                    </div>

                    <div id="payFormCard" style="display: none;">
                        <div class="card-visual-container">
                            <div class="card-chip"></div>
                            <div id="cardMockNumber" class="card-number-display">4532 &bull;&bull;&bull;&bull; &bull;&bull;&bull;&bull; 8892</div>
                            <div class="card-meta-row">
                                <div><span>Holder:</span> <strong id="cardMockHolder">SOMA INDRANIL</strong></div>
                                <div><span>Exp:</span> <strong id="cardMockExpiry">11/29</strong></div>
                            </div>
                        </div>
                        <div class="form-grid">
                            <div class="form-group" style="grid-column: 1 / -1;">
                                <label class="form-label">16-Digit Card Number</label>
                                <input type="text" class="form-input" maxlength="19" value="4532 9012 8847 8892" onkeyup="updateCardMockup(this.value)">
                            </div>
                        </div>
                    </div>

                    <div id="payFormNet" style="display: none;">
                        <div class="form-group">
                            <label class="form-label">Select Bank</label>
                            <select id="bankSelect" class="form-input" style="height: 40px;">
                                <option value="HDFC">HDFC Bank</option>
                                <option value="ICICI">ICICI Bank</option>
                                <option value="SBI">State Bank of India</option>
                                <option value="AXIS">Axis Bank</option>
                            </select>
                        </div>
                    </div>

                    <div id="payFormCod" style="display: none;">
                        <p style="font-size: 12px; color: var(--text-secondary);">
                            Keep exact cash or UPI QR ready for BlueDart delivery executive.
                        </p>
                    </div>

                    <div style="display: flex; gap: 10px; margin-top: 16px;">
                        <button class="cat-chip" onclick="gotoStep(1)">&larr; Back</button>
                        <button class="checkout-footer-btn" style="margin-top: 0; flex: 1;" onclick="gotoStep(3)">Review Order &rarr;</button>
                    </div>
                </div>

                <!-- Step 3: Review -->
                <div id="checkoutStep3" style="display: none;">
                    <h3 style="font-family: var(--font-serif); font-size: 16px; margin-bottom: 10px;">Order Review</h3>
                    <div style="font-size: 11px; background: #faf9f6; border: 1px solid var(--border); padding: 10px; border-radius: 4px; margin-bottom: 12px;">
                        <div><strong>Shipping:</strong> <span id="reviewAddress">Flat 402, Signature Palms, Mumbai, 400001</span></div>
                        <div style="margin-top: 4px;"><strong>Method:</strong> <span id="reviewPaymentMethod">UPI Instant</span></div>
                    </div>

                    <div class="order-summary-box" style="margin-top: 0; padding: 12px;">
                        <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                            <span>Subtotal</span><span id="reviewSubtotal">&#8377;0</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                            <span>Discount</span><span id="reviewDiscount" style="color: var(--success);">-&#8377;0</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                            <span>Shipping</span><span style="color: var(--success);">FREE</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                            <span>GST (18%)</span><span id="reviewGst">&#8377;0</span>
                        </div>
                        <div style="border-top: 1px solid var(--border); padding-top: 8px; margin-top: 8px; display: flex; justify-content: space-between; font-size: 14px; font-weight: 800;">
                            <span>Total Payable</span><span id="reviewGrandTotal">&#8377;0</span>
                        </div>
                    </div>

                    <div style="display: flex; gap: 10px; margin-top: 16px;">
                        <button class="cat-chip" onclick="gotoStep(2)">&larr; Back</button>
                        <button class="checkout-footer-btn" style="margin-top: 0; flex: 1;" onclick="executePayment()">Authorize &amp; Pay &rarr;</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Processing Modal -->
    <div id="processingModal" class="modal-backdrop">
        <div style="background: #ffffff; padding: 30px 24px; border-radius: 6px; text-align: center; max-width: 380px;">
            <div style="width: 40px; height: 40px; border: 3px solid #e8e6e1; border-top-color: #111; border-radius: 50%; margin: 0 auto 16px auto; animation: spin 0.8s linear infinite;"></div>
            <h3 style="font-family: var(--font-serif); font-size: 16px; margin-bottom: 6px;">Authorizing Gateway</h3>
            <p style="font-size: 11px; color: var(--text-secondary);">Connecting via 256-Bit SSL with Indian Banking Switch...</p>
        </div>
    </div>

    <!-- Order Confirmed Success Modal -->
    <div id="successModal" class="modal-backdrop">
        <div style="background: #ffffff; padding: 30px 24px; border-radius: 6px; text-align: center; max-width: 420px;">
            <div style="width: 48px; height: 48px; background: #e9f5ee; color: #1b6348; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; margin: 0 auto 12px auto;">&#10003;</div>
            <h2 style="font-family: var(--font-serif); font-size: 20px; margin-bottom: 8px;">Order Confirmed</h2>
            <p style="font-size: 12px; color: var(--text-secondary); margin-bottom: 16px;">
                Order ID <strong id="successOrderId">#TV-92041</strong> placed successfully. Dispatched within 24 hours.
            </p>
            <div style="display: flex; gap: 10px;">
                <button class="cat-chip" style="flex: 1;" onclick="closeSuccessAndGoOrders()">Track Order</button>
                <button class="checkout-footer-btn" style="flex: 1; margin-top: 0;" onclick="closeSuccessModal()">Shop More</button>
            </div>
        </div>
    </div>

    <!-- Official GST Tax Invoice Modal -->
    <div id="invoiceModal" class="modal-backdrop">
        <div class="checkout-modal" style="max-width: 680px;">
            <div class="checkout-header">
                <span style="font-family: var(--font-brand); font-size: 13px; letter-spacing: 2px;">OFFICIAL GST TAX INVOICE</span>
                <button style="background: none; border: none; color: #fff; font-size: 20px; cursor: pointer;" onclick="document.getElementById('invoiceModal').classList.remove('active')">&times;</button>
            </div>
            <div class="checkout-body" style="background: #faf8f5;">
                <div style="background: #ffffff; border: 1px solid #d5d2ca; padding: 24px; font-size: 11px;">
                    <div style="display: flex; justify-content: space-between; border-bottom: 2px solid #111; padding-bottom: 12px; margin-bottom: 16px;">
                        <div>
                            <h3 style="font-family: var(--font-brand); font-size: 16px;">TRENDVIBE ATELIER PVT LTD</h3>
                            <p>GSTIN: 27AABCT9481E1Z8 &bull; Bandra Kurla Complex, Mumbai</p>
                        </div>
                        <div style="text-align: right;">
                            <h4>TAX INVOICE</h4>
                            <p>Invoice: <strong id="invNum">INV-849201</strong></p>
                        </div>
                    </div>
                    <table style="width: 100%; border-collapse: collapse; margin-bottom: 14px;">
                        <thead>
                            <tr style="background: #f7f6f2;">
                                <th style="border: 1px solid #e0ded9; padding: 6px; text-align: left;">Item</th>
                                <th style="border: 1px solid #e0ded9; padding: 6px;">HSN</th>
                                <th style="border: 1px solid #e0ded9; padding: 6px;">Qty</th>
                                <th style="border: 1px solid #e0ded9; padding: 6px;">Total</th>
                            </tr>
                        </thead>
                        <tbody id="invoiceTableBody">
                            <!-- Populated dynamically -->
                        </tbody>
                    </table>
                    <div style="text-align: right; font-size: 13px; font-weight: 700;">
                        Grand Total: <span id="invGrandTotal">&#8377;0</span>
                    </div>
                </div>
                <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 14px;">
                    <button class="cat-chip" onclick="window.print()">Print / Save PDF</button>
                    <button class="checkout-footer-btn" style="width: auto; padding: 8px 18px; margin-top: 0;" onclick="document.getElementById('invoiceModal').classList.remove('active')">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Product Detail Modal -->
    <div id="pdpModal" class="modal-backdrop">
        <div class="pdp-modal">
            <button style="position: absolute; top: 10px; right: 10px; background: rgba(0,0,0,0.6); color: #fff; border: none; width: 28px; height: 28px; border-radius: 50%; font-size: 16px; cursor: pointer; z-index: 10;" onclick="closePdpModal()">&times;</button>
            <div class="pdp-img-col">
                <img id="pdpModalImg" class="pdp-main-image" src="" alt="Product">
            </div>
            <div class="pdp-details-col">
                <span id="pdpModalBrand" class="product-brand" style="font-size: 11px;">ATELIER</span>
                <h2 id="pdpModalTitle" style="font-family: var(--font-serif); font-size: 18px; margin-bottom: 8px;">Product Title</h2>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-bottom: 10px;">
                    <span id="pdpModalPrice" style="font-size: 18px; font-weight: 700;">&#8377;0</span>
                    <span id="pdpModalOrigPrice" style="font-size: 12px; color: var(--text-muted); text-decoration: line-through;">&#8377;0</span>
                    <span id="pdpModalDiscount" style="font-size: 11px; color: var(--success); font-weight: 700;">0% OFF</span>
                </div>
                <p id="pdpModalDesc" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 14px;">
                    Tailored with luxury fabrics for refined silhouette and comfort.
                </p>
                <div id="pdpModalSizes" style="display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap;"></div>
                <div style="display: flex; gap: 10px; margin-top: auto;">
                    <button id="pdpAddBagBtn" class="checkout-footer-btn" style="margin-top: 0; flex: 2;" onclick="addCurrentPdpToCart()">Add To Bag</button>
                    <button id="pdpWishlistBtn" class="cat-chip" style="flex: 1;" onclick="toggleCurrentPdpWishlist()">Wishlist</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Toast Notification -->
    <div id="toastNotification" class="toast-banner">Item added to your bag</div>

    <!-- Footer -->
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <div style="font-family: var(--font-brand); font-size: 16px; letter-spacing: 2px; color: #fff; margin-bottom: 8px;">TRENDVIBE ATELIER</div>
                    <p style="font-size: 11px; line-height: 1.6; color: #9c978f;">
                        High-fashion luxury e-commerce platform delivering curated runway silhouettes, fine leather goods, and French perfumery across India.
                    </p>
                </div>
                <div>
                    <h4 style="font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 8px;">Collections</h4>
                    <p><a onclick="filterByNav('Women')">Women's Couture</a></p>
                    <p><a onclick="filterByNav('Men')">Men's Tailoring</a></p>
                    <p><a onclick="filterByNav('Beauty')">Beauty &amp; Scents</a></p>
                </div>
                <div>
                    <h4 style="font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 8px;">Concierge</h4>
                    <p><a onclick="switchView('orders')">Track Orders</a></p>
                    <p><a onclick="openAuthOrProfileModal()">My Profile</a></p>
                </div>
                <div>
                    <h4 style="font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 8px;">Legal</h4>
                    <p>&copy; 2026 TrendVibe Atelier Pvt Ltd</p>
                    <p>All Rights Reserved.</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- JAVASCRIPT APPLICATION LOGIC -->
    <script>
        // Injected 260+ Curated Products Dataset
        const allProducts = ALL_PRODUCTS_DATA_PLACEHOLDER;

        // State Management
        let cart = [];
        let wishlist = [];
        let currentFilterCategory = "All";
        let currentPriceFilter = "All";
        let currentSearchQuery = "";
        let currentSort = "featured";
        let currentPdpProduct = null;
        let selectedPdpSize = "";
        let currentPaymentMethod = "upi";

        // Pagination State
        const ITEMS_PER_PAGE = 24;
        let displayedCount = 24;

        // User Auth State
        let currentUser = null;
        let pendingOtpCode = "4829";

        // Seed Orders
        let orders = [
            {
                orderId: "ORD-94821",
                orderDate: "03 Oct 2026",
                status: "In Transit",
                statusStep: 3,
                carrier: "BlueDart Express Air (AWB: 88294109)",
                address: "Flat 402, Signature Palms, Bandra West, Mumbai 400001",
                total: 2097,
                items: [
                    { name: "Pure Cotton Tailored Oxford Shirt", brand: "ATELIER MEN", size: "M", price: 899, quantity: 1, imageUrl: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80" },
                    { name: "Velvet Matte Liquid Lip Trio Collection", brand: "MAISON DE BEAUTÉ", size: "Set of 3", price: 999, quantity: 1, imageUrl: "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80" }
                ]
            }
        ];

        // Init App
        function initApp() {
            loadUserFromStorage();
            renderCatalog();
            renderOrders();
            updateBadges();

            // First-time visitor check for Auth modal
            if (!currentUser && !localStorage.getItem("trendvibe_guest_dismissed")) {
                setTimeout(() => {
                    openAuthModal();
                }, 1200);
            }
        }

        function loadUserFromStorage() {
            const saved = localStorage.getItem("trendvibe_user");
            if (saved) {
                try {
                    currentUser = JSON.parse(saved);
                    updateUserHeaderUI();
                } catch(e) {}
            }
        }

        function updateUserHeaderUI() {
            const label = document.getElementById("profileBtnLabel");
            if (currentUser) {
                const firstName = currentUser.name.split(" ")[0];
                label.innerText = `Hi, ${firstName}`;
                document.getElementById("shipName").value = currentUser.name;
                document.getElementById("shipPhone").value = currentUser.phone;
                document.getElementById("shipPin").value = currentUser.pincode || "400001";
            } else {
                label.innerText = "Profile";
            }
        }

        // Auth Modal Handlers
        function openAuthModal() {
            document.getElementById("authStepPhone").style.display = "block";
            document.getElementById("authStepOtp").style.display = "none";
            document.getElementById("authStepProfile").style.display = "none";
            document.getElementById("authStepDashboard").style.display = "none";
            document.getElementById("authModal").classList.add("active");
        }

        function openAuthOrProfileModal() {
            if (currentUser) {
                document.getElementById("authStepPhone").style.display = "none";
                document.getElementById("authStepOtp").style.display = "none";
                document.getElementById("authStepProfile").style.display = "none";
                document.getElementById("authStepDashboard").style.display = "block";

                document.getElementById("dashUserName").innerText = currentUser.name;
                document.getElementById("dashUserPhone").innerText = "+91 " + currentUser.phone;
                document.getElementById("dashUserEmail").innerText = currentUser.email;
                document.getElementById("dashUserPin").innerText = currentUser.pincode || "400001";
                const initials = currentUser.name.split(" ").map(n => n[0]).join("").toUpperCase();
                document.getElementById("userAvatarText").innerText = initials || "TV";

                document.getElementById("authModal").classList.add("active");
            } else {
                openAuthModal();
            }
        }

        function closeAuthModal() {
            localStorage.setItem("trendvibe_guest_dismissed", "true");
            document.getElementById("authModal").classList.remove("active");
        }

        function sendOtpToPhone() {
            const phone = document.getElementById("loginPhoneInput").value.trim();
            if (phone.length !== 10) {
                alert("Please enter a valid 10-digit Indian mobile number.");
                return;
            }
            pendingOtpCode = Math.floor(1000 + Math.random() * 9000).toString();
            document.getElementById("generatedOtpDisplay").innerText = pendingOtpCode;
            document.getElementById("displayTargetPhone").innerText = "+91 " + phone;

            document.getElementById("authStepPhone").style.display = "none";
            document.getElementById("authStepOtp").style.display = "block";

            // Focus on first box
            setTimeout(() => {
                document.getElementById("otp1").focus();
            }, 300);
        }

        function handleOtpKey(index, e) {
            const val = e.target.value;
            if (val && index < 4) {
                document.getElementById(`otp${index + 1}`).focus();
            }
        }

        function autoFillOtp() {
            document.getElementById("otp1").value = pendingOtpCode[0];
            document.getElementById("otp2").value = pendingOtpCode[1];
            document.getElementById("otp3").value = pendingOtpCode[2];
            document.getElementById("otp4").value = pendingOtpCode[3];
        }

        function verifyOtpCode() {
            const entered = document.getElementById("otp1").value +
                            document.getElementById("otp2").value +
                            document.getElementById("otp3").value +
                            document.getElementById("otp4").value;

            if (entered !== pendingOtpCode && entered !== "4829") {
                alert("Invalid verification code. Please check the simulated SMS toast above.");
                return;
            }

            // Check if existing user in localStorage
            const saved = localStorage.getItem("trendvibe_user");
            if (saved) {
                currentUser = JSON.parse(saved);
                updateUserHeaderUI();
                closeAuthModal();
                showToast(`Welcome back, ${currentUser.name}!`);
            } else {
                // New user registration
                document.getElementById("authStepOtp").style.display = "none";
                document.getElementById("authStepProfile").style.display = "block";
            }
        }

        function completeRegistration() {
            const name = document.getElementById("regNameInput").value.trim() || "Soma Indranil";
            const email = document.getElementById("regEmailInput").value.trim() || "somaindra@gmail.com";
            const pin = document.getElementById("regPinInput").value.trim() || "400001";
            const phone = document.getElementById("loginPhoneInput").value.trim() || "9876543210";

            currentUser = {
                name: name,
                email: email,
                pincode: pin,
                phone: phone
            };
            localStorage.setItem("trendvibe_user", JSON.stringify(currentUser));
            updateUserHeaderUI();
            closeAuthModal();
            showToast(`Welcome to TrendVibe Atelier, ${name}!`);
        }

        function signOutUser() {
            currentUser = null;
            localStorage.removeItem("trendvibe_user");
            updateUserHeaderUI();
            closeAuthModal();
            showToast("Signed out successfully");
        }

        // Render Product Catalog with 260+ Items & Pagination
        function getFilteredProducts() {
            return allProducts.filter(p => {
                let matchCat = true;
                if (currentFilterCategory !== "All") {
                    matchCat = p.category === currentFilterCategory || p.gender === currentFilterCategory;
                }

                let matchPrice = true;
                if (currentPriceFilter === "under1500") matchPrice = p.price < 1500;
                else if (currentPriceFilter === "1500to3500") matchPrice = p.price >= 1500 && p.price <= 3500;
                else if (currentPriceFilter === "above3500") matchPrice = p.price > 3500;

                let matchSearch = true;
                if (currentSearchQuery.trim() !== "") {
                    const q = currentSearchQuery.toLowerCase();
                    matchSearch = p.name.toLowerCase().includes(q) ||
                                  p.brand.toLowerCase().includes(q) ||
                                  p.category.toLowerCase().includes(q);
                }

                return matchCat && matchPrice && matchSearch;
            });
        }

        function renderCatalog() {
            const grid = document.getElementById("productGrid");
            if (!grid) return;

            let filtered = getFilteredProducts();

            if (currentSort === "price-low") filtered.sort((a,b) => a.price - b.price);
            else if (currentSort === "price-high") filtered.sort((a,b) => b.price - a.price);
            else if (currentSort === "rating") filtered.sort((a,b) => b.rating - a.rating);

            document.getElementById("catalogCount").innerText = `${filtered.length} styles available`;

            // Pagination slice
            const toShow = filtered.slice(0, displayedCount);

            // Update Load More Counter
            const loadBox = document.getElementById("loadMoreBox");
            if (displayedCount >= filtered.length) {
                loadBox.style.display = "none";
            } else {
                loadBox.style.display = "block";
                document.getElementById("loadMoreCounter").innerText = `${toShow.length} of ${filtered.length}`;
            }

            if (toShow.length === 0) {
                grid.innerHTML = `
                    <div style="grid-column: 1 / -1; padding: 40px 10px; text-align: center; color: var(--text-muted);">
                        <p style="font-size: 14px; margin-bottom: 8px;">No matching pieces found.</p>
                        <button class="cat-chip" onclick="filterCategory('All')">Clear Filters</button>
                    </div>
                `;
                return;
            }

            grid.innerHTML = toShow.map(item => {
                const isWishlisted = wishlist.includes(item.id);
                return `
                    <div class="product-card">
                        <div class="product-image-container" onclick="openPdpModal(${item.id})">
                            <img class="product-card-img" src="${item.imageUrl}" alt="${item.name}" loading="lazy">
                            <span class="product-badge">${item.badge}</span>
                            <button class="wishlist-btn ${isWishlisted ? 'active' : ''}" onclick="event.stopPropagation(); toggleWishlist(${item.id})">
                                &#9829;
                            </button>
                            <div class="quick-add-overlay" onclick="event.stopPropagation(); quickAdd(${item.id})">
                                + Quick Add &bull; &#8377;${item.price}
                            </div>
                        </div>
                        <div class="product-info">
                            <span class="product-brand">${item.brand}</span>
                            <div class="product-title" onclick="openPdpModal(${item.id})">${item.name}</div>
                            <div class="product-pricing">
                                <span class="current-price">&#8377;${item.price.toLocaleString('en-IN')}</span>
                                <span class="original-price">&#8377;${item.originalPrice.toLocaleString('en-IN')}</span>
                                <span class="discount-rate">${item.discountPercent}% OFF</span>
                            </div>
                        </div>
                    </div>
                `;
            }).join("");
        }

        function loadMoreProducts() {
            displayedCount += ITEMS_PER_PAGE;
            renderCatalog();
        }

        // Filtering
        function filterByNav(categoryOrGender, el) {
            document.querySelectorAll(".desktop-nav-links a").forEach(a => a.classList.remove("active"));
            if (el) el.classList.add("active");

            currentFilterCategory = categoryOrGender;
            document.getElementById("catalogTitle").innerText = categoryOrGender === "All" ? "Autumn / Winter Edit" : `${categoryOrGender} Edit`;
            displayedCount = ITEMS_PER_PAGE;

            // Sync chips
            document.querySelectorAll(".cat-chip").forEach(btn => btn.classList.remove("active"));
            const matchBtn = Array.from(document.querySelectorAll(".cat-chip")).find(b => b.innerText.includes(categoryOrGender));
            if (matchBtn) matchBtn.classList.add("active");

            switchView('shop');
            renderCatalog();
        }

        function filterCategory(cat, el) {
            document.querySelectorAll(".cat-chip").forEach(b => b.classList.remove("active"));
            if (el) el.classList.add("active");
            currentFilterCategory = cat;
            document.getElementById("catalogTitle").innerText = cat === "All" ? "Autumn / Winter Edit" : `${cat} Edit`;
            displayedCount = ITEMS_PER_PAGE;
            renderCatalog();
        }

        function filterPrice(range, el) {
            document.querySelectorAll(".price-btn").forEach(b => b.classList.remove("active"));
            if (el) el.classList.add("active");
            currentPriceFilter = range;
            displayedCount = ITEMS_PER_PAGE;
            renderCatalog();
        }

        function handleSort(val) {
            currentSort = val;
            renderCatalog();
        }

        function handleSearch(val) {
            currentSearchQuery = val;
            displayedCount = ITEMS_PER_PAGE;
            renderCatalog();
        }

        // Quick View PDP Modal
        function openPdpModal(id) {
            const p = allProducts.find(x => x.id === id);
            if (!p) return;
            currentPdpProduct = p;
            selectedPdpSize = p.sizes[0];

            document.getElementById("pdpModalImg").src = p.imageUrl;
            document.getElementById("pdpModalBrand").innerText = p.brand;
            document.getElementById("pdpModalTitle").innerText = p.name;
            document.getElementById("pdpModalPrice").innerHTML = `&#8377;${p.price.toLocaleString('en-IN')}`;
            document.getElementById("pdpModalOrigPrice").innerHTML = `&#8377;${p.originalPrice.toLocaleString('en-IN')}`;
            document.getElementById("pdpModalDiscount").innerText = `${p.discountPercent}% OFF`;
            document.getElementById("pdpModalDesc").innerText = p.description;

            const sizeBox = document.getElementById("pdpModalSizes");
            sizeBox.innerHTML = p.sizes.map((s, idx) => `
                <button class="cat-chip ${idx === 0 ? 'active' : ''}" onclick="selectPdpSize('${s}', this)">${s}</button>
            `).join("");

            const isWish = wishlist.includes(p.id);
            document.getElementById("pdpWishlistBtn").innerText = isWish ? "Saved \u2665" : "Wishlist";

            document.getElementById("pdpModal").classList.add("active");
        }

        function closePdpModal() {
            document.getElementById("pdpModal").classList.remove("active");
            currentPdpProduct = null;
        }

        function selectPdpSize(s, el) {
            selectedPdpSize = s;
            document.querySelectorAll("#pdpModalSizes .cat-chip").forEach(b => b.classList.remove("active"));
            el.classList.add("active");
        }

        function addCurrentPdpToCart() {
            if (!currentPdpProduct) return;
            addToCartWithDetails(currentPdpProduct, selectedPdpSize);
            closePdpModal();
        }

        function toggleCurrentPdpWishlist() {
            if (!currentPdpProduct) return;
            toggleWishlist(currentPdpProduct.id);
            const isWish = wishlist.includes(currentPdpProduct.id);
            document.getElementById("pdpWishlistBtn").innerText = isWish ? "Saved \u2665" : "Wishlist";
        }

        function quickAdd(id) {
            const p = allProducts.find(x => x.id === id);
            if (p) addToCartWithDetails(p, p.sizes[0]);
        }

        function addToCartWithDetails(product, size) {
            const existing = cart.find(x => x.id === product.id && x.size === size);
            if (existing) {
                existing.quantity += 1;
            } else {
                cart.push({
                    id: product.id,
                    name: product.name,
                    brand: product.brand,
                    price: product.price,
                    originalPrice: product.originalPrice,
                    size: size,
                    imageUrl: product.imageUrl,
                    quantity: 1
                });
            }
            showToast(`${product.name.slice(0, 22)}... added`);
            updateBadges();
            if (document.getElementById("view-cart").classList.contains("active")) {
                renderCart();
            }
        }

        function toggleWishlist(id) {
            if (wishlist.includes(id)) {
                wishlist = wishlist.filter(x => x !== id);
                showToast("Removed from wishlist");
            } else {
                wishlist.push(id);
                showToast("Saved to wishlist");
            }
            updateBadges();
            renderCatalog();
            if (document.getElementById("view-wishlist").classList.contains("active")) {
                renderWishlist();
            }
        }

        function showToast(msg) {
            const t = document.getElementById("toastNotification");
            t.innerText = msg;
            t.classList.add("active");
            setTimeout(() => t.classList.remove("active"), 2200);
        }

        function updateBadges() {
            const cartQty = cart.reduce((acc, i) => acc + i.quantity, 0);
            document.getElementById("cart-badge").innerText = cartQty;
            document.getElementById("drawerCartCount").innerText = cartQty;
            const cartH = document.getElementById("cartCountHeader");
            if (cartH) cartH.innerText = cartQty;

            const wishBadge = document.getElementById("wishlist-badge");
            wishBadge.innerText = wishlist.length;
            wishBadge.style.display = wishlist.length > 0 ? "flex" : "none";
            document.getElementById("drawerWishlistCount").innerText = wishlist.length;
            const wishH = document.getElementById("wishlistCountHeader");
            if (wishH) wishH.innerText = wishlist.length;
        }

        // View Switching
        function switchView(viewName) {
            document.querySelectorAll(".view-section").forEach(s => s.classList.remove("active"));
            document.querySelectorAll(".bottom-nav-item").forEach(b => b.classList.remove("active"));

            const targetView = document.getElementById(`view-${viewName}`);
            if (targetView) targetView.classList.add("active");

            const bnav = document.getElementById(`bnav-${viewName}`);
            if (bnav) bnav.classList.add("active");

            if (viewName === "cart") renderCart();
            if (viewName === "wishlist") renderWishlist();
            if (viewName === "orders") renderOrders();

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function toggleDrawer(open) {
            const overlay = document.getElementById("drawerOverlay");
            if (open) overlay.classList.add("active");
            else overlay.classList.remove("active");
        }

        // Cart
        function renderCart() {
            const container = document.getElementById("cartContentContainer");
            if (!container) return;

            if (cart.length === 0) {
                container.innerHTML = `
                    <div style="background: #ffffff; border: 1px solid var(--border); padding: 40px 16px; text-align: center; border-radius: 4px;">
                        <h3 style="font-family: var(--font-serif); font-size: 18px; margin-bottom: 6px;">Your Bag is Empty</h3>
                        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 18px;">Explore 260+ curated runway pieces.</p>
                        <button class="checkout-footer-btn" style="width: auto; padding: 10px 24px; margin: 0 auto;" onclick="switchView('shop')">Explore Collections</button>
                    </div>
                `;
                return;
            }

            const subtotal = cart.reduce((acc, i) => acc + (i.price * i.quantity), 0);
            const totalMrp = cart.reduce((acc, i) => acc + (i.originalPrice * i.quantity), 0);
            const discount = totalMrp - subtotal;
            const gst = Math.round(subtotal * 0.18);
            const grandTotal = subtotal + gst;

            container.innerHTML = `
                <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
                    <div>
                        ${cart.map((item, idx) => `
                            <div style="display: flex; gap: 12px; background: #ffffff; border: 1px solid var(--border); border-radius: 4px; padding: 12px; margin-bottom: 12px;">
                                <img src="${item.imageUrl}" style="width: 75px; height: 100px; object-fit: cover; border-radius: 2px;" alt="${item.name}">
                                <div style="flex: 1; display: flex; flex-direction: column;">
                                    <span style="font-size: 9px; font-weight: 700; color: var(--accent); text-transform: uppercase;">${item.brand}</span>
                                    <h4 style="font-size: 12px; font-weight: 600; margin: 2px 0 6px 0;">${item.name}</h4>
                                    <div style="font-size: 11px; color: var(--text-secondary); margin-bottom: 4px;">Size: <strong>${item.size}</strong> &bull; Qty: <strong>${item.quantity}</strong></div>
                                    <div style="font-size: 13px; font-weight: 700; margin-top: auto;">&#8377;${(item.price * item.quantity).toLocaleString('en-IN')}</div>
                                </div>
                                <button style="background: none; border: none; color: var(--text-muted); font-size: 18px; cursor: pointer;" onclick="removeFromCart(${idx})">&times;</button>
                            </div>
                        `).join("")}
                    </div>

                    <div>
                        <div style="background: #ffffff; border: 1px solid var(--border); padding: 16px; border-radius: 4px;">
                            <h3 style="font-family: var(--font-serif); font-size: 16px; margin-bottom: 12px;">Order Summary</h3>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                                <span>MRP Total</span><span>&#8377;${totalMrp.toLocaleString('en-IN')}</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                                <span>Privilege Discount</span><span style="color: var(--success);">-&#8377;${discount.toLocaleString('en-IN')}</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                                <span>BlueDart Shipping</span><span style="color: var(--success);">FREE</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                                <span>GST (18%)</span><span>&#8377;${gst.toLocaleString('en-IN')}</span>
                            </div>
                            <div style="border-top: 1px solid var(--border); padding-top: 10px; margin-top: 8px; display: flex; justify-content: space-between; font-size: 15px; font-weight: 800;">
                                <span>Total Payable</span><span>&#8377;${grandTotal.toLocaleString('en-IN')}</span>
                            </div>
                            <button class="checkout-footer-btn" onclick="openCheckoutModal()">Proceed to Checkout &rarr;</button>
                        </div>
                    </div>
                </div>
            `;
        }

        function removeFromCart(idx) {
            cart.splice(idx, 1);
            updateBadges();
            renderCart();
        }

        // Wishlist
        function renderWishlist() {
            const container = document.getElementById("wishlistContentContainer");
            if (!container) return;

            if (wishlist.length === 0) {
                container.innerHTML = `
                    <div style="grid-column: 1 / -1; background: #ffffff; border: 1px solid var(--border); padding: 40px 16px; text-align: center; border-radius: 4px;">
                        <h3 style="font-family: var(--font-serif); font-size: 18px; margin-bottom: 6px;">Your Wishlist is Empty</h3>
                        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 18px;">Save your favorite runway pieces.</p>
                        <button class="checkout-footer-btn" style="width: auto; padding: 10px 24px; margin: 0 auto;" onclick="switchView('shop')">Explore Collections</button>
                    </div>
                `;
                return;
            }

            const wishProds = allProducts.filter(p => wishlist.includes(p.id));
            container.innerHTML = wishProds.map(item => `
                <div class="product-card">
                    <div class="product-image-container" onclick="openPdpModal(${item.id})">
                        <img class="product-card-img" src="${item.imageUrl}" alt="${item.name}">
                        <button class="wishlist-btn active" onclick="event.stopPropagation(); toggleWishlist(${item.id})">&#9829;</button>
                    </div>
                    <div class="product-info">
                        <span class="product-brand">${item.brand}</span>
                        <div class="product-title" onclick="openPdpModal(${item.id})">${item.name}</div>
                        <div class="product-pricing">
                            <span class="current-price">&#8377;${item.price.toLocaleString('en-IN')}</span>
                        </div>
                        <button class="cat-chip" style="margin-top: 10px; width: 100%;" onclick="quickAdd(${item.id})">Move to Bag</button>
                    </div>
                </div>
            `).join("");
        }

        // Checkout Modal
        function openCheckoutModal() {
            if (cart.length === 0) {
                alert("Your shopping bag is empty.");
                return;
            }
            if (!currentUser) {
                openAuthModal();
                return;
            }
            gotoStep(1);
            document.getElementById("checkoutModalBackdrop").classList.add("active");
        }

        function closeCheckoutModal() {
            document.getElementById("checkoutModalBackdrop").classList.remove("active");
        }

        function gotoStep(stepNum) {
            document.getElementById("stepTab1").classList.remove("active");
            document.getElementById("stepTab2").classList.remove("active");
            document.getElementById("stepTab3").classList.remove("active");
            document.getElementById("checkoutStep1").style.display = "none";
            document.getElementById("checkoutStep2").style.display = "none";
            document.getElementById("checkoutStep3").style.display = "none";

            document.getElementById(`stepTab${stepNum}`).classList.add("active");
            document.getElementById(`checkoutStep${stepNum}`).style.display = "block";

            if (stepNum === 3) {
                const name = document.getElementById("shipName").value;
                const street = document.getElementById("shipStreet").value;
                const pin = document.getElementById("shipPin").value;
                document.getElementById("reviewAddress").innerText = `${street}, Pincode: ${pin} (Attn: ${name})`;

                const pNames = { upi: "UPI Instant QR", card: "Credit/Debit Card (SSL)", net: "Net Banking", cod: "Cash on Delivery" };
                document.getElementById("reviewPaymentMethod").innerText = pNames[currentPaymentMethod];

                const subtotal = cart.reduce((acc, i) => acc + (i.price * i.quantity), 0);
                const totalMrp = cart.reduce((acc, i) => acc + (i.originalPrice * i.quantity), 0);
                const discount = totalMrp - subtotal;
                const gst = Math.round(subtotal * 0.18);
                const grandTotal = subtotal + gst;

                document.getElementById("reviewSubtotal").innerHTML = `&#8377;${totalMrp.toLocaleString('en-IN')}`;
                document.getElementById("reviewDiscount").innerHTML = `-&#8377;${discount.toLocaleString('en-IN')}`;
                document.getElementById("reviewGst").innerHTML = `&#8377;${gst.toLocaleString('en-IN')}`;
                document.getElementById("reviewGrandTotal").innerHTML = `&#8377;${grandTotal.toLocaleString('en-IN')}`;
            }
        }

        function switchPaymentTab(tab) {
            currentPaymentMethod = tab;
            document.querySelectorAll(".payment-tab-btn").forEach(b => b.classList.remove("active"));
            document.getElementById(`payTab${tab.charAt(0).toUpperCase() + tab.slice(1)}`).classList.add("active");

            document.getElementById("payFormUpi").style.display = tab === "upi" ? "block" : "none";
            document.getElementById("payFormCard").style.display = tab === "card" ? "block" : "none";
            document.getElementById("payFormNet").style.display = tab === "net" ? "block" : "none";
            document.getElementById("payFormCod").style.display = tab === "cod" ? "block" : "none";
        }

        function handlePincodeAutoFill(pin) {
            if (pin.length === 6) {
                const map = { "400001": "Mumbai, Maharashtra", "110001": "New Delhi, Delhi", "560001": "Bengaluru, Karnataka", "700001": "Kolkata, West Bengal" };
                document.getElementById("shipCityState").value = map[pin] || "Metro Fulfillment Hub, India";
            }
        }

        function updateCardMockup(val) {
            const clean = val.replace(/\\D/g, "");
            let formatted = "";
            for (let i = 0; i < clean.length; i++) {
                if (i > 0 && i % 4 === 0) formatted += " ";
                formatted += clean[i];
            }
            document.getElementById("cardMockNumber").innerText = formatted || "4532 \u2022\u2022\u2022\u2022 \u2022\u2022\u2022\u2022 8892";
        }

        function executePayment() {
            closeCheckoutModal();
            document.getElementById("processingModal").classList.add("active");

            setTimeout(() => {
                document.getElementById("processingModal").classList.remove("active");

                const newId = "ORD-" + Math.floor(10000 + Math.random() * 90000);
                const subtotal = cart.reduce((acc, i) => acc + (i.price * i.quantity), 0);
                const gst = Math.round(subtotal * 0.18);
                const total = subtotal + gst;

                const newOrder = {
                    orderId: newId,
                    orderDate: "Today, 13 Oct 2026",
                    status: "Placed",
                    statusStep: 1,
                    carrier: "BlueDart Air Express (AWB: 88" + Math.floor(100000 + Math.random() * 900000) + ")",
                    address: document.getElementById("reviewAddress").innerText,
                    total: total,
                    items: [...cart]
                };

                orders.unshift(newOrder);
                cart = [];
                updateBadges();

                document.getElementById("successOrderId").innerText = newId;
                document.getElementById("successModal").classList.add("active");
            }, 1600);
        }

        function closeSuccessModal() {
            document.getElementById("successModal").classList.remove("active");
            switchView('shop');
        }

        function closeSuccessAndGoOrders() {
            document.getElementById("successModal").classList.remove("active");
            switchView('orders');
        }

        // Orders View
        function renderOrders() {
            const container = document.getElementById("ordersListContainer");
            if (!container) return;

            if (orders.length === 0) {
                container.innerHTML = `<div style="text-align: center; padding: 30px; color: var(--text-muted);">No orders placed yet.</div>`;
                return;
            }

            container.innerHTML = orders.map(ord => `
                <div class="order-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <div>
                            <strong style="font-family: var(--font-brand); font-size: 13px;">${ord.orderId}</strong>
                            <span style="font-size: 11px; color: var(--text-muted); margin-left: 8px;">${ord.orderDate}</span>
                        </div>
                        <strong style="font-size: 14px;">&#8377;${ord.total.toLocaleString('en-IN')}</strong>
                    </div>

                    <div class="tracking-pipeline">
                        <div class="pipeline-step ${ord.statusStep >= 1 ? (ord.statusStep === 1 ? 'active' : 'completed') : ''}">
                            <div class="step-dot">&#10003;</div><span class="step-label">Placed</span>
                        </div>
                        <div class="pipeline-step ${ord.statusStep >= 2 ? (ord.statusStep === 2 ? 'active' : 'completed') : ''}">
                            <div class="step-dot">&#10003;</div><span class="step-label">Dispatched</span>
                        </div>
                        <div class="pipeline-step ${ord.statusStep >= 3 ? (ord.statusStep === 3 ? 'active' : 'completed') : ''}">
                            <div class="step-dot">&#9889;</div><span class="step-label">In Transit</span>
                        </div>
                        <div class="pipeline-step ${ord.statusStep >= 4 ? 'completed' : ''}">
                            <div class="step-dot">&#9989;</div><span class="step-label">Delivered</span>
                        </div>
                    </div>

                    <div style="font-size: 11px; color: var(--text-secondary); margin-bottom: 10px;">
                        <strong>Courier:</strong> ${ord.carrier}
                    </div>

                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <button class="cat-chip" onclick="openInvoiceModal('${ord.orderId}')">&#128196; Download Tax Invoice</button>
                        <button class="cat-chip" onclick="alert('Courier Status: Package dispatched from Mumbai fulfillment center. Expected delivery in 24 hours.')">&#128666; Courier Track</button>
                    </div>
                </div>
            `).join("");
        }

        function openInvoiceModal(orderId) {
            const ord = orders.find(x => x.orderId === orderId);
            if (!ord) return;

            document.getElementById("invNum").innerText = "INV-" + ord.orderId.replace("ORD-", "");
            document.getElementById("invGrandTotal").innerHTML = `&#8377;${ord.total.toLocaleString('en-IN')}`;

            document.getElementById("invoiceTableBody").innerHTML = ord.items.map(it => `
                <tr>
                    <td style="border: 1px solid #e0ded9; padding: 6px;">${it.name} (${it.size || 'M'})</td>
                    <td style="border: 1px solid #e0ded9; padding: 6px; text-align: center;">6109</td>
                    <td style="border: 1px solid #e0ded9; padding: 6px; text-align: center;">${it.quantity || 1}</td>
                    <td style="border: 1px solid #e0ded9; padding: 6px; text-align: right;">&#8377;${it.price * (it.quantity || 1)}</td>
                </tr>
            `).join("");

            document.getElementById("invoiceModal").classList.add("active");
        }

        window.addEventListener("DOMContentLoaded", initApp);
    </script>
</body>
</html>
"""

# Embed the products data into the template
products_json_string = json.dumps(products_list)
final_html = html_template.replace("ALL_PRODUCTS_DATA_PLACEHOLDER", products_json_string)

# Write demo/index.html
with open("demo/index.html", "w", encoding="utf-8") as f:
    f.write(final_html)
print(f"Wrote demo/index.html ({len(final_html)} bytes)")

# Write src/main/webapp/index.html
with open("src/main/webapp/index.html", "w", encoding="utf-8") as f:
    f.write(final_html)
print(f"Wrote src/main/webapp/index.html ({len(final_html)} bytes)")

# Write build_mobile_app.py
with open("build_mobile_app.py", "w", encoding="utf-8") as f:
    f.write("# build_mobile_app.py\n# Auto-generated builder for TrendVibe Atelier\n")
    f.write(f"html_content = {repr(final_html)}\n\n")
    f.write("""if __name__ == '__main__':
    with open('demo/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open('src/main/webapp/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Compiled TrendVibe Atelier with 260 products!')
""")
print("Wrote build_mobile_app.py!")

