# build_mobile_app.py
# TrendVibe - Luxury Fashion & Beauty Storefront (Myntra / Ajio / Nykaa)
# Expanded to 27 premium products with Price Filters, Brand Filters, Size Guides, and Payment Gateway

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>TrendVibe &bull; India's Biggest Fashion &amp; Beauty Festival (Myntra &bull; Ajio &bull; Nykaa)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #ff3f6c;          /* Iconic Myntra coral-pink */
            --primary-hover: #e02f5a;
            --primary-light: #fff1f4;
            --nykaa-pink: #e80071;        /* Nykaa beauty accent */
            --dark: #282c3f;              /* Deep charcoal */
            --text-secondary: #535766;
            --text-muted: #94969f;
            --border: #eaeaec;
            --bg-main: #f5f5f6;
            --surface: #ffffff;
            --success: #03a685;
            --warning: #ff905a;
            --danger: #ff5252;
            --shadow-sm: 0 1px 4px rgba(40, 44, 63, 0.08);
            --shadow-md: 0 4px 16px rgba(40, 44, 63, 0.12);
            --shadow-lg: 0 12px 32px rgba(40, 44, 63, 0.16);
            --radius-sm: 4px;
            --radius-md: 8px;
            --radius-lg: 14px;
            --font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            --bottom-nav-height: 60px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }

        html, body {
            font-family: var(--font-family);
            background-color: #fafbfc;
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
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 16px;
            width: 100%;
        }

        /* Top Announcement Bar */
        .top-banner {
            background: linear-gradient(90deg, #ff3f6c, #ff527b, #e80071);
            color: #ffffff;
            text-align: center;
            padding: 7px 12px;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 0.5px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            white-space: nowrap;
            overflow-x: auto;
            scrollbar-width: none;
            text-transform: uppercase;
        }
        .top-banner::-webkit-scrollbar { display: none; }
        .countdown-timer {
            background: rgba(0, 0, 0, 0.25);
            padding: 2px 7px;
            border-radius: 4px;
            font-weight: 800;
            font-size: 11px;
            font-family: monospace;
        }

        /* Site Header */
        header.site-header {
            background: #ffffff;
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid var(--border);
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            width: 100%;
        }

        .navbar-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 72px;
            gap: 16px;
        }

        .mobile-menu-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: var(--dark);
        }

        @media (min-width: 992px) {
            .mobile-menu-btn { display: none; }
        }

        .brand-logo {
            font-size: 22px;
            font-weight: 900;
            letter-spacing: 1.5px;
            color: var(--dark);
            display: flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            flex-shrink: 0;
            text-transform: uppercase;
        }
        .brand-logo .accent { color: var(--primary); }
        .brand-logo .badge-tag {
            background: var(--nykaa-pink);
            color: #fff;
            font-size: 9px;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 3px;
            letter-spacing: 0.5px;
        }

        /* Desktop Nav Links */
        .desktop-nav-links {
            display: none;
            list-style: none;
            gap: 22px;
            height: 100%;
            align-items: center;
        }
        @media (min-width: 992px) {
            .desktop-nav-links { display: flex; }
        }

        .desktop-nav-links a {
            font-size: 13px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            color: var(--dark);
            padding: 24px 2px;
            border-bottom: 4px solid transparent;
            cursor: pointer;
            transition: all 0.2s;
        }
        .desktop-nav-links a:hover,
        .desktop-nav-links a.active {
            color: var(--primary);
            border-bottom-color: var(--primary);
        }

        /* Desktop Search */
        .desktop-search-container {
            display: none;
            flex: 1;
            max-width: 380px;
            margin: 0 10px;
            position: relative;
        }
        @media (min-width: 992px) {
            .desktop-search-container { display: block; }
        }

        .search-input-field {
            width: 100%;
            padding: 10px 16px 10px 38px;
            border-radius: 6px;
            border: 1px solid var(--border);
            font-size: 13px;
            outline: none;
            background: var(--bg-main);
            transition: all 0.2s;
        }
        .search-input-field:focus {
            background: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(255, 63, 108, 0.15);
        }
        .search-icon-svg {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            width: 16px;
            height: 16px;
            color: var(--text-muted);
        }

        /* Right Actions */
        .nav-actions {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .action-icon-btn {
            background: none;
            border: none;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            padding: 4px 6px;
            color: var(--dark);
            font-size: 11px;
            font-weight: 700;
            transition: color 0.2s;
        }
        .action-icon-btn:hover { color: var(--primary); }
        .action-icon-btn svg { width: 22px; height: 22px; margin-bottom: 2px; }

        .badge-counter {
            position: absolute;
            top: 0px;
            right: 0px;
            background: var(--primary);
            color: white;
            font-size: 10px;
            font-weight: 800;
            min-width: 16px;
            height: 16px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 3px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }

        /* Slide-Out Mobile Navigation Drawer */
        .drawer-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.5);
            backdrop-filter: blur(3px);
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }
        .drawer-overlay.active {
            opacity: 1;
            visibility: visible;
        }

        .mobile-drawer {
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            width: 290px;
            max-width: 85%;
            background: #ffffff;
            z-index: 1001;
            transform: translateX(-100%);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
            box-shadow: var(--shadow-lg);
        }
        .drawer-overlay.active .mobile-drawer {
            transform: translateX(0);
        }

        .drawer-header {
            background: linear-gradient(135deg, #ff3f6c, #e80071);
            color: white;
            padding: 28px 20px 20px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            position: relative;
        }
        .drawer-close {
            position: absolute;
            top: 14px;
            right: 14px;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 16px;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .drawer-body {
            padding: 14px 0;
            overflow-y: auto;
            flex: 1;
        }
        .drawer-item {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 12px 20px;
            font-size: 14px;
            font-weight: 700;
            color: var(--dark);
            border-left: 4px solid transparent;
            cursor: pointer;
            transition: background 0.2s;
        }
        .drawer-item:hover, .drawer-item.active {
            background: var(--bg-main);
            color: var(--primary);
            border-left-color: var(--primary);
        }
        .drawer-divider {
            height: 1px;
            background: var(--border);
            margin: 8px 0;
        }

        /* Mobile Bottom App Navigation Bar */
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: var(--bottom-nav-height);
            background: #ffffff;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-around;
            align-items: center;
            z-index: 99;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.06);
            padding-bottom: env(safe-area-inset-bottom, 0px);
        }
        @media (min-width: 992px) {
            .bottom-nav { display: none; }
        }

        .bottom-nav-item {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: var(--text-muted);
            font-size: 10px;
            font-weight: 700;
            cursor: pointer;
            background: none;
            border: none;
            gap: 2px;
            position: relative;
        }
        .bottom-nav-item.active {
            color: var(--primary);
        }
        .bottom-nav-item svg { width: 22px; height: 22px; }

        /* Mobile Search Bar Section */
        .mobile-search-section {
            background: #ffffff;
            border-bottom: 1px solid var(--border);
            padding: 10px 0;
        }
        @media (min-width: 992px) {
            .mobile-search-section { display: none; }
        }

        /* Hero Banner */
        .hero-banner {
            border-radius: var(--radius-lg);
            overflow: hidden;
            margin: 16px 0 20px;
            background: linear-gradient(135deg, #182848 0%, #4b6cb7 100%);
            color: white;
            padding: 32px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-md);
            position: relative;
        }
        @media (max-width: 600px) {
            .hero-banner { padding: 22px 16px; }
            .hero-banner-decor { display: none; }
        }
        .hero-badge-tag {
            background: var(--primary);
            color: white;
            font-size: 11px;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: inline-block;
            margin-bottom: 10px;
        }
        .hero-heading {
            font-size: 26px;
            font-weight: 900;
            line-height: 1.15;
            margin-bottom: 8px;
        }
        @media (min-width: 768px) {
            .hero-heading { font-size: 36px; }
        }
        .hero-subtext {
            font-size: 13px;
            opacity: 0.9;
            margin-bottom: 16px;
            max-width: 520px;
        }
        .hero-cta-btn {
            background: #ffffff;
            color: var(--dark);
            font-weight: 800;
            font-size: 13px;
            padding: 10px 22px;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: inline-block;
            transition: all 0.2s;
        }
        .hero-cta-btn:hover {
            background: var(--primary);
            color: #ffffff;
        }

        /* Category Chips Bar */
        .category-scroll-container {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            white-space: nowrap;
            padding: 6px 0 14px;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
        }
        .category-scroll-container::-webkit-scrollbar { display: none; }

        .cat-chip {
            padding: 8px 16px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 800;
            background: #ffffff;
            border: 1px solid var(--border);
            color: var(--text-secondary);
            cursor: pointer;
            flex-shrink: 0;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .cat-chip:hover, .cat-chip.active {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 2px 8px rgba(255, 63, 108, 0.25);
        }

        /* Filter Pills (Price Range & Brands) */
        .filters-toolbar {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            white-space: nowrap;
            padding-bottom: 12px;
            scrollbar-width: none;
        }
        .filters-toolbar::-webkit-scrollbar { display: none; }
        .filter-btn {
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            background: #ffffff;
            border: 1px solid var(--border);
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.2s;
        }
        .filter-btn.active {
            background: var(--dark);
            color: #ffffff;
            border-color: var(--dark);
        }

        /* 2-Column Mobile Product Grid */
        .catalog-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 12px 0 14px;
        }
        .catalog-title {
            font-size: 17px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--dark);
        }
        @media (min-width: 768px) {
            .catalog-title { font-size: 22px; }
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-bottom: 40px;
        }
        @media (min-width: 768px) {
            .product-grid {
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
            }
        }
        @media (min-width: 1024px) {
            .product-grid {
                grid-template-columns: repeat(4, 1fr);
                gap: 22px;
            }
        }

        /* Product Card */
        .product-card {
            background: #ffffff;
            border-radius: var(--radius-md);
            border: 1px solid var(--border);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            position: relative;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .product-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-3px);
        }

        .product-media {
            position: relative;
            width: 100%;
            padding-top: 125%; /* 4:5 fashion aspect ratio */
            background: #f0f0f2;
            overflow: hidden;
            cursor: pointer;
        }
        .product-media img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s;
        }
        .product-card:hover .product-media img {
            transform: scale(1.04);
        }

        .wishlist-heart-btn {
            position: absolute;
            top: 8px;
            right: 8px;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: rgba(255,255,255,0.92);
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 2;
            font-size: 15px;
            transition: all 0.2s;
        }
        .wishlist-heart-btn.active {
            color: var(--primary);
            border-color: var(--primary);
            background: #ffffff;
        }

        .badge-flair {
            position: absolute;
            top: 8px;
            left: 8px;
            background: var(--dark);
            color: white;
            font-size: 9px;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 3px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }
        .badge-flair.hot { background: #ff5722; }
        .badge-flair.nykaa { background: var(--nykaa-pink); }

        .discount-badge-ribbon {
            position: absolute;
            bottom: 8px;
            left: 8px;
            background: var(--success);
            color: white;
            font-size: 10px;
            font-weight: 800;
            padding: 3px 7px;
            border-radius: 3px;
        }

        .rating-star-tag {
            position: absolute;
            bottom: 8px;
            right: 8px;
            background: rgba(255,255,255,0.92);
            font-size: 10px;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 3px;
            display: flex;
            align-items: center;
            gap: 2px;
        }

        .product-body {
            padding: 10px 12px 14px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        .brand-name {
            font-size: 12px;
            font-weight: 900;
            color: var(--dark);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 2px;
        }
        .product-name-text {
            font-size: 12px;
            font-weight: 500;
            color: var(--text-secondary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            margin-bottom: 8px;
            cursor: pointer;
        }
        .price-container {
            display: flex;
            align-items: baseline;
            gap: 6px;
            margin-bottom: 8px;
            flex-wrap: wrap;
        }
        .final-price-tag {
            font-size: 15px;
            font-weight: 900;
            color: var(--dark);
        }
        .mrp-price-tag {
            font-size: 12px;
            color: var(--text-muted);
            text-decoration: line-through;
        }
        .discount-off-tag {
            font-size: 11px;
            font-weight: 800;
            color: var(--warning);
        }

        .btn-add-quick {
            width: 100%;
            background: var(--primary);
            color: #fff;
            border: none;
            border-radius: 4px;
            padding: 9px 10px;
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            cursor: pointer;
            margin-top: auto;
            transition: background 0.2s;
        }
        .btn-add-quick:hover {
            background: var(--primary-hover);
        }

        /* View Section Manager */
        .view-section { display: none; }
        .view-section.active { display: block; animation: fadeIn 0.2s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

        /* Cart & Checkout Layout */
        .cart-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            margin-top: 16px;
        }
        @media (min-width: 992px) {
            .cart-grid { grid-template-columns: 1.6fr 1fr; }
        }

        .cart-card {
            background: white;
            border-radius: var(--radius-md);
            border: 1px solid var(--border);
            padding: 16px;
            display: flex;
            gap: 14px;
            margin-bottom: 12px;
        }
        .cart-card-img {
            width: 90px;
            height: 120px;
            border-radius: 6px;
            object-fit: cover;
            flex-shrink: 0;
        }
        .cart-card-info {
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .bill-card {
            background: white;
            border-radius: var(--radius-md);
            border: 1px solid var(--border);
            padding: 20px;
            height: fit-content;
            position: sticky;
            top: 90px;
        }
        .bill-row {
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            margin-bottom: 10px;
        }
        .bill-row.total {
            font-size: 16px;
            font-weight: 800;
            border-top: 1px dashed var(--border);
            padding-top: 12px;
            margin-top: 12px;
            color: var(--dark);
        }

        .coupon-box {
            display: flex;
            gap: 8px;
            margin-bottom: 16px;
        }
        .coupon-input {
            flex: 1;
            padding: 9px 12px;
            border: 1px solid var(--border);
            border-radius: 4px;
            font-size: 12px;
            text-transform: uppercase;
            font-weight: 700;
        }
        .coupon-btn {
            background: var(--dark);
            color: #fff;
            border: none;
            padding: 9px 16px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 800;
            cursor: pointer;
        }

        .pincode-card {
            background: #fff;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 16px;
            margin-bottom: 16px;
        }

        /* Order Tracking Stepper */
        .tracking-stepper {
            display: flex;
            justify-content: space-between;
            position: relative;
            margin: 24px 0 16px;
        }
        .tracking-stepper::before {
            content: '';
            position: absolute;
            top: 12px;
            left: 20px;
            right: 20px;
            height: 3px;
            background: #e2e8f0;
            z-index: 1;
        }
        .step-node {
            position: relative;
            z-index: 2;
            text-align: center;
            width: 70px;
        }
        .step-bubble {
            width: 26px;
            height: 26px;
            border-radius: 50%;
            background: #e2e8f0;
            color: #64748b;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            font-weight: 800;
            margin: 0 auto 6px;
        }
        .step-node.completed .step-bubble {
            background: var(--success);
            color: #fff;
        }
        .step-node.active .step-bubble {
            background: var(--primary);
            color: #fff;
        }
        .step-text {
            font-size: 10px;
            font-weight: 700;
            color: var(--text-secondary);
        }

        /* Modal Overlay */
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.65);
            backdrop-filter: blur(4px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            padding: 16px;
        }
        .modal-overlay.active {
            display: flex;
            animation: fadeIn 0.2s ease;
        }
        .modal-container {
            background: white;
            border-radius: var(--radius-lg);
            max-width: 720px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            padding: 24px;
            position: relative;
            box-shadow: var(--shadow-lg);
        }
        .modal-close-btn {
            position: absolute;
            top: 14px;
            right: 14px;
            font-size: 20px;
            border: none;
            background: var(--bg-main);
            width: 32px;
            height: 32px;
            border-radius: 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Toast Popup */
        .toast-popup {
            position: fixed;
            bottom: calc(var(--bottom-nav-height) + 16px);
            left: 50%;
            transform: translateX(-50%) translateY(50px);
            background: #282c3f;
            color: white;
            padding: 10px 18px;
            border-radius: 999px;
            font-size: 13px;
            font-weight: 700;
            z-index: 2000;
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            white-space: nowrap;
            box-shadow: var(--shadow-lg);
            display: flex;
            align-items: center;
            gap: 8px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .toast-popup.show {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }

        /* Footer */
        footer.site-footer {
            background: #ffffff;
            border-top: 1px solid var(--border);
            padding: 48px 0 32px;
            margin-top: 48px;
            color: var(--text-secondary);
        }
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 32px;
            margin-bottom: 36px;
        }
        .footer-col h4 {
            font-size: 12px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--dark);
            margin-bottom: 14px;
        }
        .footer-col ul { list-style: none; }
        .footer-col ul li { margin-bottom: 8px; font-size: 13px; }
        .footer-col ul li a:hover { color: var(--primary); }
    </style>
</head>
<body>

    <!-- Top Announcement Bar -->
    <div class="top-banner">
        <span>⚡ BIG FASHION FESTIVAL: UP TO 70% OFF ON 27+ TOP BRANDS</span>
        <span>&bull;</span>
        <span>Sale Ends in: <span id="flashTimer" class="countdown-timer">05:42:19</span></span>
        <span>&bull;</span>
        <span>🚚 Free Express Shipping &amp; 14-Day Easy Returns</span>
    </div>

    <!-- Header / Navbar -->
    <header class="site-header">
        <div class="container navbar-content">
            <button class="mobile-menu-btn" onclick="toggleDrawer(true)">☰</button>

            <!-- Brand Logo -->
            <div class="brand-logo" onclick="switchView('shop')">
                TRENDVIBE<span class="accent">.</span> <span class="badge-tag">MYNTRA &bull; NYKAA</span>
            </div>

            <!-- Desktop Nav Links -->
            <ul class="desktop-nav-links">
                <li><a onclick="filterByGender('Men', this)" id="desk-men">MEN</a></li>
                <li><a onclick="filterByGender('Women', this)" id="desk-women">WOMEN</a></li>
                <li><a onclick="filterCategory('Beauty', this)" id="desk-beauty" style="color: var(--nykaa-pink);">NYKAA BEAUTY</a></li>
                <li><a onclick="filterCategory('Shoes', this)" id="desk-shoes">FOOTWEAR</a></li>
                <li><a onclick="filterCategory('Watches', this)" id="desk-watches">ACCESSORIES</a></li>
                <li><a onclick="switchView('orders')" id="desk-orders">MY ORDERS</a></li>
            </ul>

            <!-- Desktop Search Bar -->
            <div class="desktop-search-container">
                <svg class="search-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                <input type="text" class="search-input-field" placeholder="Search 27+ brands, shirts, dresses, lipsticks..." onkeyup="handleSearch(this.value)">
            </div>

            <!-- Right Actions -->
            <div class="nav-actions">
                <button class="action-icon-btn" onclick="switchView('orders')">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                    <span>Profile</span>
                </button>

                <button class="action-icon-btn" onclick="switchView('wishlist')">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                    <span>Wishlist</span>
                    <span id="wishlist-badge" class="badge-counter" style="display: none;">0</span>
                </button>

                <button class="action-icon-btn" onclick="switchView('cart')">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
                    <span>Bag</span>
                    <span id="cart-badge" class="badge-counter">0</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Slide-Out Mobile Navigation Drawer -->
    <div id="drawerOverlay" class="drawer-overlay" onclick="toggleDrawer(false)">
        <div class="mobile-drawer" onclick="event.stopPropagation()">
            <div class="drawer-header">
                <button class="drawer-close" onclick="toggleDrawer(false)">✕</button>
                <div style="font-size: 18px; font-weight: 900;">TRENDVIBE FASHION</div>
                <div style="font-size: 12px; opacity: 0.9;">India's Luxury Lifestyle Destination</div>
            </div>
            <div class="drawer-body">
                <div class="drawer-item" onclick="switchView('shop'); filterByGender('All'); toggleDrawer(false);">
                    🔥 All 27 Trending Styles
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterByGender('Men'); toggleDrawer(false);">
                    👔 Men's Store (Shirts, Jeans, T-Shirts)
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterByGender('Women'); toggleDrawer(false);">
                    👗 Women's Ethnic &amp; Western Dresses
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterCategory('Beauty'); toggleDrawer(false);" style="color: var(--nykaa-pink);">
                    💄 Nykaa Beauty &amp; Luxury Skincare
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterCategory('Shoes'); toggleDrawer(false);">
                    👟 Footwear &amp; Sneakers (Nike &bull; Puma &bull; Adidas)
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterCategory('Watches'); toggleDrawer(false);">
                    ⌚ Watches &amp; Accessories (Fossil &bull; Titan &bull; Ray-Ban)
                </div>
                <div class="drawer-divider"></div>
                <div class="drawer-item" onclick="switchView('wishlist'); toggleDrawer(false);">
                    ❤️ My Wishlist (<span id="drawerWishlistCount">0</span>)
                </div>
                <div class="drawer-item" onclick="switchView('cart'); toggleDrawer(false);">
                    🛍️ My Shopping Bag (<span id="drawerCartCount">0</span>)
                </div>
                <div class="drawer-item" onclick="switchView('orders'); toggleDrawer(false);">
                    📦 My Orders &amp; Live Tracking
                </div>
            </div>
        </div>
    </div>

    <!-- Mobile Bottom App Navigation Bar -->
    <nav class="bottom-nav">
        <button id="bnav-shop" class="bottom-nav-item active" onclick="switchView('shop')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
            <span>Explore</span>
        </button>
        <button id="bnav-categories" class="bottom-nav-item" onclick="toggleDrawer(true)">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/></svg>
            <span>Categories</span>
        </button>
        <button id="bnav-wishlist" class="bottom-nav-item" onclick="switchView('wishlist')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
            <span>Wishlist</span>
        </button>
        <button id="bnav-cart" class="bottom-nav-item" onclick="switchView('cart')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
            <span>Bag</span>
        </button>
        <button id="bnav-orders" class="bottom-nav-item" onclick="switchView('orders')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
            <span>Orders</span>
        </button>
    </nav>

    <!-- Mobile Search Section -->
    <div class="mobile-search-section">
        <div class="container">
            <div style="position: relative;">
                <svg class="search-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                <input type="text" class="search-input-field" placeholder="Search 27+ brands, shirts, dresses, lipsticks..." onkeyup="handleSearch(this.value)">
            </div>
        </div>
    </div>

    <!-- MAIN APP CONTENT -->
    <main class="container">

        <!-- 1. SHOP / CATALOG VIEW -->
        <div id="view-shop" class="view-section active">
            <!-- Hero Fashion Festival Banner -->
            <div class="hero-banner">
                <div>
                    <span class="hero-badge-tag">Festive Mega Drop</span>
                    <h1 class="hero-heading">BIG FASHION &amp; BEAUTY FESTIVAL</h1>
                    <p class="hero-subtext">
                        Shop 27+ exclusive collections from Roadster, Tommy Hilfiger, Levi's, Mango, Nike, Puma, Adidas &amp; Nykaa.
                    </p>
                    <a href="#productGrid" class="hero-cta-btn">Shop The Drop &rarr;</a>
                </div>
                <div class="hero-banner-decor" style="font-size: 80px; text-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                    👗✨👟
                </div>
            </div>

            <!-- Horizontal Category Chips -->
            <div class="category-scroll-container">
                <button class="cat-chip active" onclick="filterCategory('All', this)">🔥 All 27 Styles</button>
                <button class="cat-chip" onclick="filterCategory('Shirts', this)">👔 Shirts</button>
                <button class="cat-chip" onclick="filterCategory('T-Shirts', this)">👕 T-Shirts</button>
                <button class="cat-chip" onclick="filterCategory('Dresses', this)">👗 Dresses &amp; Ethnic</button>
                <button class="cat-chip" onclick="filterCategory('Beauty', this)">💄 Nykaa Beauty</button>
                <button class="cat-chip" onclick="filterCategory('Shoes', this)">👟 Footwear</button>
                <button class="cat-chip" onclick="filterCategory('Watches', this)">⌚ Watches &amp; Luxury</button>
            </div>

            <!-- Secondary Filters Toolbar (Price Range) -->
            <div class="filters-toolbar">
                <span style="font-size: 11px; font-weight: 800; color: var(--text-muted); align-self: center; margin-right: 4px;">PRICE:</span>
                <button class="filter-btn active" onclick="filterPrice('All', this)">All Prices</button>
                <button class="filter-btn" onclick="filterPrice('under999', this)">Under &#8377;999</button>
                <button class="filter-btn" onclick="filterPrice('1000to2500', this)">&#8377;1,000 - &#8377;2,500</button>
                <button class="filter-btn" onclick="filterPrice('above2500', this)">&#8377;2,500+</button>
            </div>

            <!-- Catalog Header with Sort Dropdown -->
            <div class="catalog-header">
                <div>
                    <h2 id="catalogTitle" class="catalog-title">All Clothing &amp; Beauty</h2>
                    <span id="catalogCount" style="font-size: 11px; color: var(--text-muted); font-weight: 700;">27 styles found</span>
                </div>
                <div>
                    <select id="sortSelect" onchange="handleSort(this.value)" style="padding: 7px 12px; border-radius: 6px; border: 1px solid var(--border); font-size: 12px; font-weight: 700; background: white; outline: none; cursor: pointer;">
                        <option value="featured">Sort: Recommended</option>
                        <option value="price-low">Price: Low to High</option>
                        <option value="price-high">Price: High to Low</option>
                        <option value="discount">Highest Discount</option>
                        <option value="rating">Highest Rated</option>
                    </select>
                </div>
            </div>

            <!-- 2-Column Mobile & Multi-Column Desktop Product Grid -->
            <div id="productGrid" class="product-grid">
                <!-- Injected via JavaScript -->
            </div>
        </div>

        <!-- 2. WISHLIST VIEW -->
        <div id="view-wishlist" class="view-section">
            <div class="catalog-header">
                <h2 class="catalog-title">My Wishlist</h2>
                <span id="wishlistCountText" style="font-size: 12px; color: var(--text-muted); font-weight: 700;">0 items</span>
            </div>
            <div id="wishlistGrid" class="product-grid"></div>
        </div>

        <!-- 3. BAG / CART VIEW -->
        <div id="view-cart" class="view-section">
            <h2 class="catalog-title" style="margin: 16px 0;">Shopping Bag &amp; Checkout</h2>
            <div id="cartContainer"></div>
        </div>

        <!-- 4. ORDERS & TRACKING VIEW -->
        <div id="view-orders" class="view-section">
            <div class="catalog-header">
                <h2 class="catalog-title">My Orders &amp; Live Tracking</h2>
                <span id="ordersCountText" style="font-size: 12px; color: var(--text-muted); font-weight: 700;">2 orders</span>
            </div>
            <div id="ordersContainer"></div>
        </div>

    </main>

    <!-- PRODUCT DETAIL MODAL -->
    <div id="productModal" class="modal-overlay" onclick="closeProductModal(event)">
        <div class="modal-container" onclick="event.stopPropagation()">
            <button class="modal-close-btn" onclick="closeProductModal()">✕</button>
            <div id="modalContent"></div>
        </div>
    </div>

    <!-- TOAST POPUP -->
    <div id="toastPopup" class="toast-popup">
        <span id="toastIcon">🛍️</span>
        <span id="toastMessage">Item added to your bag!</span>
    </div>

    <!-- Consumer Footer -->
    <footer class="site-footer">
        <div class="container footer-grid">
            <div class="footer-col">
                <h4>ONLINE SHOPPING</h4>
                <ul>
                    <li><a href="#" onclick="filterByGender('Men')">Men's Fashion &amp; Formals</a></li>
                    <li><a href="#" onclick="filterByGender('Women')">Women's Ethnic &amp; Western</a></li>
                    <li><a href="#" onclick="filterCategory('Beauty')">Nykaa Beauty &amp; Luxury Skincare</a></li>
                    <li><a href="#" onclick="filterCategory('Shoes')">Footwear &amp; Sneakers</a></li>
                    <li><a href="#" onclick="filterCategory('Watches')">Luxury Watches &amp; Accessories</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>CUSTOMER POLICIES</h4>
                <ul>
                    <li><a href="#">Contact Us</a></li>
                    <li><a href="#">Track Orders</a></li>
                    <li><a href="#">14-Day Free Returns</a></li>
                    <li><a href="#">Shipping &amp; Delivery</a></li>
                    <li><a href="#">Terms &amp; Conditions</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>100% ORIGINAL GUARANTEE</h4>
                <p style="font-size: 13px; line-height: 1.6; margin-bottom: 8px;">
                    ✅ All products on TrendVibe are 100% authentic, sourced directly from certified brand warehouses.
                </p>
                <p style="font-size: 13px; line-height: 1.6;">
                    🔄 Hassle-free 14-day exchange and return policy on all fashion apparel.
                </p>
            </div>
        </div>
        <div class="container" style="text-align: center; border-top: 1px solid var(--border); padding-top: 20px; font-size: 12px; color: var(--text-muted);">
            &copy; 2026 TrendVibe Fashion &amp; Beauty Inc. Inspired by Myntra, Ajio &amp; Nykaa.
        </div>
    </footer>

    <!-- CLIENT APPLICATION LOGIC (27 Products & Consumer Features) -->
    <script>
        let products = [
            // MEN FASHION
            {
                id: 1,
                name: "Roadster Men Slim Fit Pure Cotton Casual Shirt",
                brand: "ROADSTER",
                category: "Shirts",
                gender: "Men",
                price: 899,
                originalPrice: 1499,
                discountPercent: 40,
                rating: 4.8,
                reviewsCount: 1420,
                badge: "BESTSELLER",
                sizes: ["S", "M", "L", "XL"],
                imageUrl: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80",
                description: "Olive green slim fit pure cotton casual shirt. Has a spread collar, long sleeves, curved hem, and one patch pocket. 100% breathable."
            },
            {
                id: 2,
                name: "HIGHLANDER Men Tapered Fit Stretch Jeans",
                brand: "HIGHLANDER",
                category: "Pants",
                gender: "Men",
                price: 1039,
                originalPrice: 1599,
                discountPercent: 35,
                rating: 4.6,
                reviewsCount: 890,
                badge: "TRENDING",
                sizes: ["30", "32", "34", "36"],
                imageUrl: "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=800&q=80",
                description: "Dark blue washed 5-pocket mid-rise stretch denim jeans, clean look with light fade."
            },
            {
                id: 3,
                name: "WROGN Geometric Printed Pure Cotton T-Shirt",
                brand: "WROGN",
                category: "T-Shirts",
                gender: "Men",
                price: 749,
                originalPrice: 999,
                discountPercent: 25,
                rating: 4.7,
                reviewsCount: 650,
                badge: "NEW DROP",
                sizes: ["S", "M", "L", "XL"],
                imageUrl: "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80",
                description: "Navy blue and white printed T-shirt, round neck, bio-washed for ultra softness."
            },
            {
                id: 4,
                name: "Tommy Hilfiger Classic Oxford Cotton Shirt",
                brand: "TOMMY HILFIGER",
                category: "Shirts",
                gender: "Men",
                price: 2799,
                originalPrice: 3999,
                discountPercent: 30,
                rating: 4.9,
                reviewsCount: 520,
                badge: "PREMIUM",
                sizes: ["39", "40", "42", "44"],
                imageUrl: "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=800&q=80",
                description: "Classic button-down collar Oxford shirt in sky blue with signature embroidered flag on chest."
            },
            {
                id: 5,
                name: "Levi's 511 Slim Fit Raw Indigo Denim Jeans",
                brand: "LEVI'S",
                category: "Pants",
                gender: "Men",
                price: 2999,
                originalPrice: 3799,
                discountPercent: 20,
                rating: 4.9,
                reviewsCount: 2100,
                badge: "ICONIC",
                sizes: ["30", "32", "34", "36"],
                imageUrl: "https://images.unsplash.com/photo-1542272604-780c96856592?auto=format&fit=crop&w=800&q=80",
                description: "Authentic Levi's 511 slim fit stretch denim in dark indigo with trademark red tab on back pocket."
            },
            {
                id: 6,
                name: "HRX Activewear Dry-Fit Breathable Joggers",
                brand: "HRX",
                category: "Pants",
                gender: "Men",
                price: 989,
                originalPrice: 1799,
                discountPercent: 45,
                rating: 4.6,
                reviewsCount: 780,
                badge: "SPORTS",
                sizes: ["S", "M", "L", "XL"],
                imageUrl: "https://images.unsplash.com/photo-1552902865-b72c031ac5ea?auto=format&fit=crop&w=800&q=80",
                description: "Athletic training joggers with moisture-wicking technology and reflective side tape."
            },
            {
                id: 7,
                name: "Dennis Lingo Casual Corduroy Overshirt",
                brand: "DENNIS LINGO",
                category: "Shirts",
                gender: "Men",
                price: 1199,
                originalPrice: 2399,
                discountPercent: 50,
                rating: 4.7,
                reviewsCount: 340,
                badge: "TRENDING",
                sizes: ["M", "L", "XL"],
                imageUrl: "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?auto=format&fit=crop&w=800&q=80",
                description: "Rich camel brown corduroy jacket shirt, relaxed drop shoulder with twin chest flap pockets."
            },

            // WOMEN FASHION
            {
                id: 8,
                name: "Anouk Embroidered Anarkali Kurta Set",
                brand: "ANOUK",
                category: "Dresses",
                gender: "Women",
                price: 1999,
                originalPrice: 3999,
                discountPercent: 50,
                rating: 4.9,
                reviewsCount: 2310,
                badge: "BESTSELLER",
                sizes: ["XS", "S", "M", "L", "XL"],
                imageUrl: "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80",
                description: "Burgundy and gold embroidered Anarkali kurta with trousers and organza dupatta."
            },
            {
                id: 9,
                name: "MANGO Floral Print Fit & Flare Midi Dress",
                brand: "MANGO",
                category: "Dresses",
                gender: "Women",
                price: 1749,
                originalPrice: 2499,
                discountPercent: 30,
                rating: 4.7,
                reviewsCount: 420,
                badge: "HOT",
                sizes: ["S", "M", "L"],
                imageUrl: "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80",
                description: "Sage green floral print midi dress, sweetheart neckline and puff sleeves."
            },
            {
                id: 10,
                name: "Libas Pink Straight Kurta with Palazzos",
                brand: "LIBAS",
                category: "Dresses",
                gender: "Women",
                price: 1374,
                originalPrice: 2499,
                discountPercent: 45,
                rating: 4.8,
                reviewsCount: 1890,
                badge: "ETHNIC",
                sizes: ["S", "M", "L"],
                imageUrl: "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80",
                description: "Dusty pink straight calf-length kurta with keyhole neck, paired with palazzos."
            },
            {
                id: 11,
                name: "Biba Block Printed Tiered Anarkali Gown",
                brand: "BIBA",
                category: "Dresses",
                gender: "Women",
                price: 2999,
                originalPrice: 4999,
                discountPercent: 40,
                rating: 4.9,
                reviewsCount: 880,
                badge: "FESTIVE",
                sizes: ["S", "M", "L", "XL"],
                imageUrl: "https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?auto=format&fit=crop&w=800&q=80",
                description: "Royal teal blue block-printed floor-length Anarkali gown with gota patti borders and sequin yoke."
            },
            {
                id: 12,
                name: "H&M Ribbed High-Neck Knit Bodycon Dress",
                brand: "H&M",
                category: "Dresses",
                gender: "Women",
                price: 1499,
                originalPrice: 1999,
                discountPercent: 25,
                rating: 4.7,
                reviewsCount: 620,
                badge: "WESTERN",
                sizes: ["XS", "S", "M", "L"],
                imageUrl: "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?auto=format&fit=crop&w=800&q=80",
                description: "Soft black ribbed knit midi dress with side slit, high turtle neckline, and long sleeves."
            },
            {
                id: 13,
                name: "FabIndia Handloom Chanderi Silk Saree",
                brand: "FABINDIA",
                category: "Dresses",
                gender: "Women",
                price: 4549,
                originalPrice: 6999,
                discountPercent: 35,
                rating: 5.0,
                reviewsCount: 310,
                badge: "LUXURY",
                sizes: ["Free Size"],
                imageUrl: "https://images.unsplash.com/photo-1610030469668-935cb7462002?auto=format&fit=crop&w=800&q=80",
                description: "Traditional magenta and golden zari handloom Chanderi silk saree with matching blouse piece."
            },
            {
                id: 14,
                name: "Vero Moda Women Pleated Satin Party Blouse",
                brand: "VERO MODA",
                category: "Shirts",
                gender: "Women",
                price: 1399,
                originalPrice: 1999,
                discountPercent: 30,
                rating: 4.6,
                reviewsCount: 290,
                badge: "PARTY",
                sizes: ["XS", "S", "M"],
                imageUrl: "https://images.unsplash.com/photo-1564257631407-4deb1f99d992?auto=format&fit=crop&w=800&q=80",
                description: "Emerald green cowl neck sleeveless satin top with delicate pleats and button closure."
            },

            // NYKAA BEAUTY & COSMETICS
            {
                id: 15,
                name: "Nykaa Matte to Last! Liquid Lipstick - Chai",
                brand: "NYKAA COSMETICS",
                category: "Beauty",
                gender: "Women",
                price: 599,
                originalPrice: 749,
                discountPercent: 20,
                rating: 4.9,
                reviewsCount: 5120,
                badge: "NYKAA HIT",
                sizes: ["4.2 ml"],
                imageUrl: "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80",
                description: "Transfer-proof, 12-hour ultra-lightweight matte liquid lipstick infused with Vitamin E."
            },
            {
                id: 16,
                name: "The Ordinary Niacinamide 10% + Zinc 1% Serum",
                brand: "THE ORDINARY",
                category: "Beauty",
                gender: "Women",
                price: 722,
                originalPrice: 850,
                discountPercent: 15,
                rating: 4.9,
                reviewsCount: 4200,
                badge: "SKINCARE",
                sizes: ["30 ml", "60 ml"],
                imageUrl: "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=800&q=80",
                description: "High-strength vitamin and mineral blemish formula. Reduces pore congestion."
            },
            {
                id: 17,
                name: "Forest Essentials 24K Gold Radiance Cream",
                brand: "FOREST ESSENTIALS",
                category: "Beauty",
                gender: "Women",
                price: 5399,
                originalPrice: 5999,
                discountPercent: 10,
                rating: 5.0,
                reviewsCount: 310,
                badge: "AYURVEDIC",
                sizes: ["50 gm"],
                imageUrl: "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80",
                description: "Ayurvedic anti-aging day cream infused with 24K pure gold bhasma and saffron."
            },
            {
                id: 18,
                name: "Kay Beauty 24H Waterproof Matte HD Liquid Eyeliner",
                brand: "KAY BEAUTY",
                category: "Beauty",
                gender: "Women",
                price: 674,
                originalPrice: 899,
                discountPercent: 25,
                rating: 4.8,
                reviewsCount: 1640,
                badge: "KATRINA KAIF",
                sizes: ["3.5 ml"],
                imageUrl: "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=800&q=80",
                description: "Deep black precision felt tip liquid eyeliner with smudge-proof, 24-hour stay formula."
            },
            {
                id: 19,
                name: "Minimalist Salicylic Acid 2% Gentle Face Cleanser",
                brand: "MINIMALIST",
                category: "Beauty",
                gender: "Women",
                price: 299,
                originalPrice: 349,
                discountPercent: 15,
                rating: 4.8,
                reviewsCount: 2890,
                badge: "DERMA",
                sizes: ["100 ml"],
                imageUrl: "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=800&q=80",
                description: "Sulfate-free exfoliating cleanser with LHA and Zinc for acne control and oil balance."
            },
            {
                id: 20,
                name: "MAC Retro Matte Velvet Lipstick - Ruby Woo",
                brand: "MAC",
                category: "Beauty",
                gender: "Women",
                price: 2150,
                originalPrice: 2400,
                discountPercent: 10,
                rating: 4.9,
                reviewsCount: 3500,
                badge: "CULT FAVORITE",
                sizes: ["3 gm"],
                imageUrl: "https://images.unsplash.com/photo-1599733589046-10c005739ef9?auto=format&fit=crop&w=800&q=80",
                description: "Iconic vivid blue-red matte lipstick with long-wearing non-feathering formula."
            },

            // FOOTWEAR & SNEAKERS
            {
                id: 21,
                name: "Nike Air Max SC Leather Running Sneakers",
                brand: "NIKE",
                category: "Shoes",
                gender: "Men",
                price: 4799,
                originalPrice: 5995,
                discountPercent: 20,
                rating: 4.9,
                reviewsCount: 940,
                badge: "NIKE AIR",
                sizes: ["UK 7", "UK 8", "UK 9", "UK 10"],
                imageUrl: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80",
                description: "White and royal blue track style sneakers with visible Air cushioning."
            },
            {
                id: 22,
                name: "Puma Men Black & White Smash V2 Low-Tops",
                brand: "PUMA",
                category: "Shoes",
                gender: "Men",
                price: 2399,
                originalPrice: 3999,
                discountPercent: 40,
                rating: 4.7,
                reviewsCount: 1120,
                badge: "CLASSIC",
                sizes: ["UK 7", "UK 8", "UK 9"],
                imageUrl: "https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=800&q=80",
                description: "Classic tennis silhouette in soft black suede with signature Puma formstrip."
            },
            {
                id: 23,
                name: "Adidas Originals Stan Smith Iconic White Sneakers",
                brand: "ADIDAS",
                category: "Shoes",
                gender: "Men",
                price: 5599,
                originalPrice: 7999,
                discountPercent: 30,
                rating: 4.9,
                reviewsCount: 1820,
                badge: "ORIGINALS",
                sizes: ["UK 7", "UK 8", "UK 9", "UK 10"],
                imageUrl: "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?auto=format&fit=crop&w=800&q=80",
                description: "Timeless minimalist court sneaker with perforated 3-Stripes and green heel tab."
            },
            {
                id: 24,
                name: "Red Tape Men Genuine Leather Chelsea Boots",
                brand: "RED TAPE",
                category: "Shoes",
                gender: "Men",
                price: 2699,
                originalPrice: 5999,
                discountPercent: 55,
                rating: 4.8,
                reviewsCount: 650,
                badge: "LEATHER",
                sizes: ["UK 7", "UK 8", "UK 9"],
                imageUrl: "https://images.unsplash.com/photo-1638247025967-b4e38f787b76?auto=format&fit=crop&w=800&q=80",
                description: "Handcrafted rich cognac brown ankle Chelsea boots with stretch side panels and TPR sole."
            },

            // ACCESSORIES & WATCHES
            {
                id: 25,
                name: "Fossil Men Chronograph Black Leather Watch",
                brand: "FOSSIL",
                category: "Watches",
                gender: "Men",
                price: 7699,
                originalPrice: 10999,
                discountPercent: 30,
                rating: 4.8,
                reviewsCount: 450,
                badge: "CHRONO",
                sizes: ["Standard 44mm"],
                imageUrl: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=800&q=80",
                description: "Gunmetal stainless steel case with genuine black leather strap. 50m water resistance."
            },
            {
                id: 26,
                name: "Ray-Ban Hexagonal Flat Polarized Sunglasses",
                brand: "RAY-BAN",
                category: "Watches",
                gender: "Men",
                price: 6890,
                originalPrice: 9190,
                discountPercent: 25,
                rating: 4.9,
                reviewsCount: 820,
                badge: "POLARIZED",
                sizes: ["Standard 51mm"],
                imageUrl: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=800&q=80",
                description: "Gold polished hexagonal metal frame with classic G-15 green polarized lenses."
            },
            {
                id: 27,
                name: "Titan Raga Aurora Rose Gold Pearl Dial Watch",
                brand: "TITAN",
                category: "Watches",
                gender: "Women",
                price: 4795,
                originalPrice: 5995,
                discountPercent: 20,
                rating: 4.9,
                reviewsCount: 510,
                badge: "ROSE GOLD",
                sizes: ["Standard 32mm"],
                imageUrl: "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=800&q=80",
                description: "Jewelry-inspired rose gold wristwatch with mother-of-pearl dial and Swarovski crystal accents."
            }
        ];

        let cart = [
            { productId: 1, size: "M", quantity: 1, price: 899 },
            { productId: 15, size: "4.2 ml", quantity: 2, price: 599 }
        ];
        let wishlist = [4, 9, 21];
        let appliedCoupon = null;
        let selectedGender = "All";
        let selectedCategory = "All";
        let selectedPriceRange = "All";
        let searchQuery = "";
        let currentSort = "featured";

        let orders = [
            {
                id: "ORD-94821",
                date: "24 Sep 2026",
                status: "Shipped",
                total: 2097,
                courier: "Bluedart Express (AWB: 8829410)",
                items: [
                    { productId: 1, size: "M", quantity: 1, price: 899 },
                    { productId: 15, size: "4.2 ml", quantity: 2, price: 599 }
                ]
            },
            {
                id: "ORD-91044",
                date: "10 Sep 2026",
                status: "Delivered",
                total: 1999,
                courier: "Delhivery Surface (Delivered)",
                items: [
                    { productId: 8, size: "M", quantity: 1, price: 1999 }
                ]
            }
        ];

        document.addEventListener('DOMContentLoaded', () => {
            renderCatalog();
            updateBadges();
            startCountdown();
        });

        function switchView(viewName) {
            document.querySelectorAll('.view-section').forEach(sec => sec.classList.remove('active'));
            document.querySelectorAll('.bottom-nav-item').forEach(btn => btn.classList.remove('active'));

            const targetSection = document.getElementById(`view-${viewName}`);
            if (targetSection) targetSection.classList.add('active');

            const targetNav = document.getElementById(`bnav-${viewName}`);
            if (targetNav) targetNav.classList.add('active');

            window.scrollTo({ top: 0, behavior: 'smooth' });

            if (viewName === 'cart') renderCart();
            if (viewName === 'wishlist') renderWishlist();
            if (viewName === 'orders') renderOrders();
        }

        function toggleDrawer(open) {
            const overlay = document.getElementById('drawerOverlay');
            if (open) overlay.classList.add('active');
            else overlay.classList.remove('active');
        }

        function startCountdown() {
            let totalSec = 5 * 3600 + 42 * 60 + 19;
            setInterval(() => {
                totalSec--;
                if (totalSec <= 0) totalSec = 86400;
                let h = String(Math.floor(totalSec / 3600)).padStart(2, '0');
                let m = String(Math.floor((totalSec % 3600) / 60)).padStart(2, '0');
                let s = String(totalSec % 60).padStart(2, '0');
                const el = document.getElementById('flashTimer');
                if (el) el.innerText = `${h}:${m}:${s}`;
            }, 1000);
        }

        function renderCatalog() {
            const grid = document.getElementById('productGrid');
            if (!grid) return;

            let filtered = products.filter(p => {
                if (selectedGender !== "All" && p.gender !== selectedGender) return false;
                if (selectedCategory !== "All" && p.category !== selectedCategory) return false;

                if (selectedPriceRange === "under999" && p.price >= 1000) return false;
                if (selectedPriceRange === "1000to2500" && (p.price < 1000 || p.price > 2500)) return false;
                if (selectedPriceRange === "above2500" && p.price <= 2500) return false;

                if (searchQuery) {
                    const q = searchQuery.toLowerCase();
                    return p.name.toLowerCase().includes(q) || p.brand.toLowerCase().includes(q) || p.category.toLowerCase().includes(q);
                }
                return true;
            });

            if (currentSort === "price-low") filtered.sort((a,b) => a.price - b.price);
            else if (currentSort === "price-high") filtered.sort((a,b) => b.price - a.price);
            else if (currentSort === "discount") filtered.sort((a,b) => b.discountPercent - a.discountPercent);
            else if (currentSort === "rating") filtered.sort((a,b) => b.rating - a.rating);

            document.getElementById('catalogCount').innerText = `${filtered.length} styles found`;

            grid.innerHTML = filtered.map(p => {
                const isWishlisted = wishlist.includes(p.id);
                return `
                    <div class="product-card">
                        <div class="product-media" onclick="openProductModal(${p.id})">
                            <img src="${p.imageUrl}" alt="${p.name}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'">
                            <button class="wishlist-heart-btn ${isWishlisted ? 'active' : ''}" onclick="toggleWishlist(${p.id}, event)">
                                ${isWishlisted ? '❤️' : '🤍'}
                            </button>
                            <span class="badge-flair ${p.category === 'Beauty' ? 'nykaa' : 'hot'}">${p.badge}</span>
                            <span class="discount-badge-ribbon">${p.discountPercent}% OFF</span>
                            <div class="rating-star-tag"><span style="color: var(--success);">★</span> ${p.rating}</div>
                        </div>
                        <div class="product-body">
                            <div class="brand-name">${p.brand}</div>
                            <div class="product-name-text" onclick="openProductModal(${p.id})" title="${p.name}">${p.name}</div>
                            <div class="price-container">
                                <span class="final-price-tag">&#8377;${p.price.toLocaleString('en-IN')}</span>
                                <span class="mrp-price-tag">&#8377;${p.originalPrice.toLocaleString('en-IN')}</span>
                                <span class="discount-off-tag">(${p.discountPercent}% OFF)</span>
                            </div>
                            <button class="btn-add-quick" onclick="quickAddToBag(${p.id})">
                                + ADD TO BAG
                            </button>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function filterByGender(gender, btn) {
            selectedGender = gender;
            document.querySelectorAll('.desktop-nav-links a').forEach(a => a.classList.remove('active'));
            if (btn) btn.classList.add('active');
            renderCatalog();
        }

        function filterCategory(cat, btn) {
            selectedCategory = cat;
            document.querySelectorAll('.cat-chip').forEach(c => c.classList.remove('active'));
            if (btn) btn.classList.add('active');
            renderCatalog();
        }

        function filterPrice(range, btn) {
            selectedPriceRange = range;
            document.querySelectorAll('.filters-toolbar .filter-btn').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            renderCatalog();
        }

        function handleSearch(val) {
            searchQuery = val.trim();
            renderCatalog();
        }

        function handleSort(val) {
            currentSort = val;
            renderCatalog();
        }

        function toggleWishlist(id, e) {
            if (e) e.stopPropagation();
            const idx = wishlist.indexOf(id);
            if (idx > -1) {
                wishlist.splice(idx, 1);
                showToast("💔 Removed from Wishlist");
            } else {
                wishlist.push(id);
                showToast("❤️ Saved to your Wishlist!");
            }
            updateBadges();
            renderCatalog();
            if (document.getElementById('view-wishlist').classList.contains('active')) renderWishlist();
        }

        function renderWishlist() {
            const grid = document.getElementById('wishlistGrid');
            const saved = products.filter(p => wishlist.includes(p.id));
            document.getElementById('wishlistCountText').innerText = `${saved.length} items`;

            if (saved.length === 0) {
                grid.innerHTML = `
                    <div style="grid-column: 1 / -1; text-align: center; padding: 48px 16px; background: white; border-radius: 8px;">
                        <div style="font-size: 52px; margin-bottom: 12px;">❤️</div>
                        <h3 style="font-size: 16px; font-weight: 800; margin-bottom: 6px;">Your Wishlist is Empty</h3>
                        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">Save your favorite fashion items here to buy later!</p>
                        <button class="btn-add-quick" style="width: auto; padding: 12px 28px;" onclick="switchView('shop')">Explore Catalog</button>
                    </div>
                `;
                return;
            }

            grid.innerHTML = saved.map(p => `
                <div class="product-card">
                    <div class="product-media" onclick="openProductModal(${p.id})">
                        <img src="${p.imageUrl}" alt="${p.name}">
                        <button class="wishlist-heart-btn active" onclick="toggleWishlist(${p.id}, event)">❤️</button>
                    </div>
                    <div class="product-body">
                        <div class="brand-name">${p.brand}</div>
                        <div class="product-name-text">${p.name}</div>
                        <div class="price-container">
                            <span class="final-price-tag">&#8377;${p.price}</span>
                        </div>
                        <button class="btn-add-quick" onclick="quickAddToBag(${p.id})">MOVE TO BAG</button>
                    </div>
                </div>
            `).join('');
        }

        function quickAddToBag(productId) {
            const p = products.find(item => item.id === productId);
            if (!p) return;
            const defaultSize = p.sizes[0];
            addToBag(p.id, defaultSize);
        }

        function addToBag(productId, sizeLabel) {
            const p = products.find(item => item.id === productId);
            if (!p) return;

            const existing = cart.find(c => c.productId === productId && c.size === sizeLabel);
            if (existing) {
                existing.quantity++;
            } else {
                cart.push({ productId, size: sizeLabel, quantity: 1, price: p.price });
            }

            updateBadges();
            showToast(`🛍️ Added ${p.brand} (${sizeLabel}) to your Bag!`);
        }

        function updateBadges() {
            const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
            document.getElementById('cart-badge').innerText = totalCount;
            document.getElementById('drawerCartCount').innerText = totalCount;

            const wishCount = wishlist.length;
            const wishBadge = document.getElementById('wishlist-badge');
            if (wishCount > 0) {
                wishBadge.style.display = 'flex';
                wishBadge.innerText = wishCount;
            } else {
                wishBadge.style.display = 'none';
            }
            document.getElementById('drawerWishlistCount').innerText = wishCount;
        }

        function renderCart() {
            const container = document.getElementById('cartContainer');
            if (cart.length === 0) {
                container.innerHTML = `
                    <div style="text-align: center; padding: 54px 16px; background: white; border-radius: 8px; border: 1px solid var(--border);">
                        <div style="font-size: 56px; margin-bottom: 12px;">🛍️</div>
                        <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 6px;">Your Shopping Bag is Empty</h3>
                        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">There is nothing in your bag. Let's add some fashion drops!</p>
                        <button class="btn-add-quick" style="width: auto; padding: 12px 28px;" onclick="switchView('shop')">Start Shopping</button>
                    </div>
                `;
                return;
            }

            let subtotalMRP = 0;
            let subtotalFinal = 0;

            const itemsHtml = cart.map((c, idx) => {
                const p = products.find(item => item.id === c.productId);
                if (!p) return '';
                subtotalMRP += p.originalPrice * c.quantity;
                subtotalFinal += p.price * c.quantity;

                return `
                    <div class="cart-card">
                        <img src="${p.imageUrl}" class="cart-card-img" alt="${p.name}">
                        <div class="cart-card-info">
                            <div style="font-size: 11px; font-weight: 800; color: var(--text-muted);">${p.brand}</div>
                            <div style="font-size: 13px; font-weight: 700; margin-bottom: 4px;">${p.name}</div>
                            <div style="font-size: 12px; color: var(--text-secondary); margin-bottom: 8px;">
                                Size: <strong>${c.size}</strong> &bull; Qty: <strong>${c.quantity}</strong>
                            </div>
                            <div style="font-size: 14px; font-weight: 800; margin-bottom: 8px;">
                                &#8377;${(p.price * c.quantity).toLocaleString('en-IN')}
                            </div>
                            <div style="display: flex; gap: 8px; align-items: center; margin-top: auto;">
                                <button onclick="updateCartQty(${idx}, -1)" style="padding: 2px 8px; border: 1px solid var(--border); background: white; border-radius: 4px; font-weight: 800;">-</button>
                                <span style="font-size: 12px; font-weight: 700;">${c.quantity}</span>
                                <button onclick="updateCartQty(${idx}, 1)" style="padding: 2px 8px; border: 1px solid var(--border); background: white; border-radius: 4px; font-weight: 800;">+</button>
                                <button onclick="removeFromCart(${idx})" style="margin-left: auto; border: none; background: none; color: var(--danger); font-size: 11px; font-weight: 800; cursor: pointer;">✕ Remove</button>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');

            let couponDiscount = 0;
            if (appliedCoupon === 'AURA10') couponDiscount = Math.round(subtotalFinal * 0.10);
            if (appliedCoupon === 'NYKAA20') couponDiscount = Math.round(subtotalFinal * 0.20);
            if (appliedCoupon === 'FIRST500') couponDiscount = Math.min(500, subtotalFinal);

            const totalPayable = Math.max(0, subtotalFinal - couponDiscount);
            const totalSavings = (subtotalMRP - subtotalFinal) + couponDiscount;

            container.innerHTML = `
                <div class="cart-grid">
                    <div>
                        <div class="pincode-card">
                            <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px;">
                                📍 Delivery Pincode &amp; Express Courier
                            </div>
                            <div style="display: flex; gap: 8px;">
                                <input type="text" id="cartPincode" class="coupon-input" placeholder="e.g. 560001 (Bangalore)" value="560001">
                                <button class="coupon-btn" onclick="checkPincode()">Check</button>
                            </div>
                            <div id="pincodeFeedback" style="font-size: 11px; color: var(--success); font-weight: 700; margin-top: 6px;">
                                ⚡ Express 1-Day Delivery via Bluedart. Cash on Delivery Available.
                            </div>
                        </div>

                        ${itemsHtml}
                    </div>

                    <div>
                        <div class="bill-card">
                            <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px;">
                                🎟️ Apply Promo Coupon
                            </div>
                            <div class="coupon-box">
                                <input type="text" id="couponCodeInput" class="coupon-input" placeholder="AURA10 or NYKAA20" value="${appliedCoupon || ''}">
                                <button class="coupon-btn" onclick="applyCoupon()">Apply</button>
                            </div>
                            ${appliedCoupon ? `<div style="font-size: 11px; color: var(--success); font-weight: 700; margin-bottom: 12px;">✓ Coupon "${appliedCoupon}" applied!</div>` : ''}

                            <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; margin-bottom: 12px; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
                                Price Details (${cart.reduce((s,i) => s + i.quantity, 0)} Items)
                            </div>

                            <div class="bill-row">
                                <span>Total MRP</span>
                                <span>&#8377;${subtotalMRP.toLocaleString('en-IN')}</span>
                            </div>
                            <div class="bill-row">
                                <span>Discount on MRP</span>
                                <span style="color: var(--success);">-&#8377;${(subtotalMRP - subtotalFinal).toLocaleString('en-IN')}</span>
                            </div>
                            ${couponDiscount > 0 ? `
                            <div class="bill-row">
                                <span>Coupon Savings</span>
                                <span style="color: var(--success);">-&#8377;${couponDiscount.toLocaleString('en-IN')}</span>
                            </div>` : ''}
                            <div class="bill-row">
                                <span>Convenience Fee</span>
                                <span style="color: var(--success); font-weight: 700;">FREE</span>
                            </div>

                            <div class="bill-row total">
                                <span>Total Amount</span>
                                <span>&#8377;${totalPayable.toLocaleString('en-IN')}</span>
                            </div>

                            <div style="background: #e6f7f3; color: var(--success); padding: 8px 12px; border-radius: 6px; font-size: 11px; font-weight: 800; margin: 14px 0;">
                                🎉 You are saving &#8377;${totalSavings.toLocaleString('en-IN')} on this order!
                            </div>

                            <button onclick="placeOrder()" class="btn-add-quick" style="padding: 14px; font-size: 13px; font-weight: 900;">
                                PLACE ORDER &rarr;
                            </button>
                        </div>
                    </div>
                </div>
            `;
        }

        function updateCartQty(idx, delta) {
            cart[idx].quantity += delta;
            if (cart[idx].quantity <= 0) cart.splice(idx, 1);
            updateBadges();
            renderCart();
        }

        function removeFromCart(idx) {
            cart.splice(idx, 1);
            updateBadges();
            renderCart();
            showToast("🗑️ Item removed from Bag");
        }

        function applyCoupon() {
            const code = document.getElementById('couponCodeInput').value.trim().toUpperCase();
            if (code === 'AURA10' || code === 'NYKAA20' || code === 'FIRST500') {
                appliedCoupon = code;
                showToast(`🎉 Coupon "${code}" Applied Successfully!`);
                renderCart();
            } else {
                showToast("❌ Invalid Coupon. Try AURA10 or NYKAA20");
            }
        }

        function checkPincode() {
            const pin = document.getElementById('cartPincode').value.trim();
            const el = document.getElementById('pincodeFeedback');
            if (pin.length === 6 && /^\d+$/.test(pin)) {
                el.style.color = "var(--success)";
                el.innerHTML = `⚡ Express 1-Day Delivery active for PIN <strong>${pin}</strong> via Bluedart. COD Eligible.`;
            } else {
                el.style.color = "var(--danger)";
                el.innerText = "❌ Please enter a valid 6-digit Indian PIN code.";
            }
        }

        function placeOrder() {
            if (cart.length === 0) return;

            const orderId = `ORD-${Math.floor(10000 + Math.random() * 90000)}`;
            const total = cart.reduce((s,i) => s + (i.price * i.quantity), 0);
            const newOrder = {
                id: orderId,
                date: "Today, Just Now",
                status: "Order Confirmed",
                total: total,
                courier: "Bluedart Express (AWB Generated)",
                items: [...cart]
            };
            orders.unshift(newOrder);

            cart = [];
            appliedCoupon = null;
            updateBadges();

            showToast("🎉 Order Placed Successfully!");
            switchView('orders');
        }

        function renderOrders() {
            const container = document.getElementById('ordersContainer');
            document.getElementById('ordersCountText').innerText = `${orders.length} orders`;

            if (orders.length === 0) {
                container.innerHTML = `
                    <div style="text-align: center; padding: 48px; background: white; border-radius: 8px;">
                        <h3>No Orders Found</h3>
                    </div>
                `;
                return;
            }

            container.innerHTML = orders.map(ord => {
                return `
                    <div style="background: white; border: 1px solid var(--border); border-radius: var(--radius-md); padding: 18px; margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 12px; margin-bottom: 12px; font-size: 13px; flex-wrap: wrap; gap: 8px;">
                            <div>
                                <span style="color: var(--text-muted); font-size: 11px;">ORDER ID</span>
                                <div style="font-weight: 800;">${ord.id}</div>
                            </div>
                            <div>
                                <span style="color: var(--text-muted); font-size: 11px;">DATE</span>
                                <div style="font-weight: 700;">${ord.date}</div>
                            </div>
                            <div>
                                <span style="color: var(--text-muted); font-size: 11px;">STATUS</span>
                                <div style="color: var(--success); font-weight: 800;">● ${ord.status}</div>
                            </div>
                            <div>
                                <span style="color: var(--text-muted); font-size: 11px;">TOTAL</span>
                                <div style="font-weight: 800; color: var(--primary);">&#8377;${ord.total.toLocaleString('en-IN')}</div>
                            </div>
                        </div>

                        <div class="tracking-stepper">
                            <div class="step-node completed"><div class="step-bubble">✓</div><div class="step-text">Placed</div></div>
                            <div class="step-node completed"><div class="step-bubble">✓</div><div class="step-text">Packed</div></div>
                            <div class="step-node ${ord.status === 'Shipped' || ord.status === 'Delivered' ? 'completed' : 'active'}"><div class="step-bubble">⚡</div><div class="step-text">Shipped</div></div>
                            <div class="step-node ${ord.status === 'Delivered' ? 'completed' : ''}"><div class="step-bubble">📦</div><div class="step-text">Delivered</div></div>
                        </div>

                        <div style="font-size: 11px; color: var(--text-muted); margin-bottom: 12px;">
                            Courier Partner: <strong>${ord.courier}</strong>
                        </div>

                        <div style="display: flex; gap: 10px; overflow-x: auto; padding-top: 8px; border-top: 1px dashed var(--border);">
                            ${ord.items.map(item => {
                                const p = products.find(prod => prod.id === item.productId);
                                if (!p) return '';
                                return `
                                    <div style="display: flex; align-items: center; gap: 8px; background: var(--bg-main); padding: 6px 10px; border-radius: 6px; font-size: 11px;">
                                        <img src="${p.imageUrl}" style="width: 36px; height: 46px; border-radius: 4px; object-fit: cover;">
                                        <div>
                                            <div style="font-weight: 700; max-width: 140px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${p.name}</div>
                                            <div style="color: var(--text-muted);">Size: ${item.size} &bull; Qty: ${item.quantity}</div>
                                        </div>
                                    </div>
                                `;
                            }).join('')}
                        </div>
                    </div>
                `;
            }).join('');
        }

        function openProductModal(id) {
            const p = products.find(item => item.id === id);
            if (!p) return;

            const modal = document.getElementById('productModal');
            const content = document.getElementById('modalContent');

            const sizesHtml = p.sizes.map((s, idx) => `
                <label style="cursor: pointer;">
                    <input type="radio" name="modalSize" value="${s}" ${idx === 0 ? 'checked' : ''} style="display: none;">
                    <span class="cat-chip ${idx === 0 ? 'active' : ''}" style="margin: 0;" onclick="selectModalSize(this)">${s}</span>
                </label>
            `).join('');

            content.innerHTML = `
                <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
                    <div style="position: relative; border-radius: 8px; overflow: hidden; max-height: 380px;">
                        <img src="${p.imageUrl}" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>

                    <div>
                        <div style="font-size: 12px; font-weight: 800; color: var(--text-muted); text-transform: uppercase;">${p.brand} &bull; ${p.category}</div>
                        <h2 style="font-size: 18px; font-weight: 800; margin: 4px 0 10px;">${p.name}</h2>
                        
                        <div class="price-container" style="margin-bottom: 16px;">
                            <span class="final-price-tag" style="font-size: 20px;">&#8377;${p.price.toLocaleString('en-IN')}</span>
                            <span class="mrp-price-tag" style="font-size: 14px;">&#8377;${p.originalPrice.toLocaleString('en-IN')}</span>
                            <span class="discount-off-tag" style="font-size: 13px;">(${p.discountPercent}% OFF)</span>
                        </div>

                        <div style="font-size: 12px; font-weight: 800; margin-bottom: 8px;">SELECT SIZE:</div>
                        <div id="modalSizePills" style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;">
                            ${sizesHtml}
                        </div>

                        <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 20px;">
                            ${p.description}
                        </div>

                        <button onclick="addModalItemToBag(${p.id})" class="btn-add-quick" style="padding: 14px; font-size: 13px;">
                            ADD TO BAG &bull; &#8377;${p.price}
                        </button>
                    </div>
                </div>
            `;

            modal.classList.add('active');
        }

        function selectModalSize(btn) {
            document.querySelectorAll('#modalSizePills .cat-chip').forEach(c => c.classList.remove('active'));
            btn.classList.add('active');
        }

        function addModalItemToBag(productId) {
            const checked = document.querySelector('input[name="modalSize"]:checked');
            const size = checked ? checked.value : "Standard";
            addToBag(productId, size);
            closeProductModal();
        }

        function closeProductModal(e) {
            if (!e || e.target.classList.contains('modal-overlay') || e.target.classList.contains('modal-close-btn')) {
                document.getElementById('productModal').classList.remove('active');
            }
        }

        function showToast(msg) {
            const toast = document.getElementById('toastPopup');
            document.getElementById('toastMessage').innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }
    </script>
</body>
</html>
'''

with open("demo/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("src/main/webapp/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully updated 27 products and consumer fashion features!")
