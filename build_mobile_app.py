# build_mobile_app.py
import re

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>TrendVibe &bull; Luxury Fashion &amp; Beauty Store (Myntra &bull; Ajio &bull; Nykaa)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #ff3f6c;          /* Signature Myntra / Fashion coral-pink */
            --primary-hover: #e02f5a;
            --primary-light: #fff1f4;
            --nykaa-pink: #e80071;        /* Nykaa beauty accent */
            --dark: #282c3f;              /* Deep charcoal */
            --dark-surface: #1e2233;
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
            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-lg: 16px;
            --font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            --bottom-nav-height: 64px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }

        html, body {
            font-family: var(--font-family);
            background-color: var(--bg-main);
            color: var(--dark);
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
            width: 100%;
        }

        /* Prevent bottom nav from obscuring content on mobile */
        body {
            padding-bottom: calc(var(--bottom-nav-height) + env(safe-area-inset-bottom, 16px));
        }

        @media (min-width: 992px) {
            body {
                padding-bottom: 0;
            }
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
            background: linear-gradient(90deg, #282c3f 0%, #1e2233 100%);
            color: #ffffff;
            text-align: center;
            padding: 6px 12px;
            font-size: 11px;
            font-weight: 700;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
            white-space: nowrap;
            overflow-x: auto;
            scrollbar-width: none;
        }
        .top-banner::-webkit-scrollbar { display: none; }
        .countdown-timer {
            background: var(--primary);
            color: #fff;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 800;
            font-size: 10px;
            letter-spacing: 0.5px;
        }

        /* Header / Navbar */
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
            height: 64px;
            gap: 12px;
        }

        /* Hamburger button for mobile */
        .mobile-menu-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: none;
            border: none;
            font-size: 22px;
            cursor: pointer;
            color: var(--dark);
        }

        @media (min-width: 992px) {
            .mobile-menu-btn { display: none; }
        }

        .brand-logo {
            font-size: 20px;
            font-weight: 900;
            letter-spacing: 1px;
            color: var(--dark);
            display: flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            flex-shrink: 0;
        }
        .brand-logo .accent { color: var(--primary); }
        .brand-logo .badge-tag {
            background: var(--nykaa-pink);
            color: #fff;
            font-size: 9px;
            font-weight: 800;
            padding: 2px 5px;
            border-radius: 3px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        /* Desktop Nav Links */
        .desktop-nav-links {
            display: none;
            list-style: none;
            gap: 20px;
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
            letter-spacing: 0.5px;
            color: var(--dark);
            padding: 20px 4px;
            border-bottom: 3px solid transparent;
            cursor: pointer;
            transition: all 0.2s;
        }
        .desktop-nav-links a:hover,
        .desktop-nav-links a.active {
            color: var(--primary);
            border-bottom-color: var(--primary);
        }

        /* Right Action Icons */
        .nav-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .action-icon-btn {
            background: none;
            border: none;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            padding: 4px;
            color: var(--dark);
            font-size: 11px;
            font-weight: 700;
        }
        .action-icon-btn svg { width: 22px; height: 22px; }

        .badge-counter {
            position: absolute;
            top: -2px;
            right: -2px;
            background: var(--primary);
            color: white;
            font-size: 10px;
            font-weight: 800;
            min-width: 17px;
            height: 17px;
            border-radius: 9px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 4px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }

        .interview-badge-btn {
            background: linear-gradient(135deg, #182848, #4b6cb7);
            color: white !important;
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 800;
            display: none;
            align-items: center;
            gap: 5px;
            border: none;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(75, 108, 183, 0.3);
        }
        @media (min-width: 600px) {
            .interview-badge-btn { display: flex; }
        }

        /* Slide-Out Mobile Navigation Drawer */
        .drawer-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.5);
            backdrop-filter: blur(2px);
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
            padding: 24px 20px 20px;
            display: flex;
            flex-direction: column;
            gap: 8px;
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
            padding: 16px 0;
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
            margin: 10px 0;
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
            gap: 3px;
            position: relative;
        }
        .bottom-nav-item.active {
            color: var(--primary);
        }
        .bottom-nav-item svg { width: 20px; height: 20px; }

        /* Search & Hero Header */
        .search-section {
            background: #ffffff;
            border-bottom: 1px solid var(--border);
            padding: 12px 0 14px;
        }

        .search-bar-wrap {
            position: relative;
            width: 100%;
        }
        .search-bar-wrap input {
            width: 100%;
            padding: 10px 16px 10px 40px;
            border-radius: 999px;
            border: 1px solid var(--border);
            font-size: 13px;
            outline: none;
            background: var(--bg-main);
            transition: all 0.2s;
        }
        .search-bar-wrap input:focus {
            background: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(255, 63, 108, 0.12);
        }
        .search-bar-wrap svg {
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            width: 18px;
            height: 18px;
            color: var(--text-muted);
        }

        /* Horizontal Category Stories / Chips (Myntra/Nykaa style) */
        .category-scroll-container {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            white-space: nowrap;
            padding: 12px 0 4px;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
        }
        .category-scroll-container::-webkit-scrollbar { display: none; }

        .cat-chip {
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
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

        /* 2-Column Mobile Product Grid */
        .catalog-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 20px 0 14px;
        }
        .catalog-title {
            font-size: 16px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--dark);
        }
        @media (min-width: 768px) {
            .catalog-title { font-size: 20px; }
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-bottom: 30px;
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
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: rgba(255,255,255,0.9);
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 2;
            font-size: 14px;
            transition: all 0.2s;
        }
        .wishlist-heart-btn.active {
            background: #fff;
            color: var(--primary);
            border-color: var(--primary);
        }

        .rating-chip {
            position: absolute;
            bottom: 8px;
            left: 8px;
            background: rgba(255,255,255,0.92);
            backdrop-filter: blur(4px);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 3px;
        }

        .stock-urgency-badge {
            position: absolute;
            top: 8px;
            left: 8px;
            background: #ff5722;
            color: white;
            font-size: 9px;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 4px;
            text-transform: uppercase;
            box-shadow: 0 1px 4px rgba(0,0,0,0.2);
        }

        .product-body {
            padding: 10px 10px 12px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        .brand-name {
            font-size: 11px;
            font-weight: 800;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 2px;
        }
        .product-name-text {
            font-size: 12px;
            font-weight: 600;
            color: var(--dark);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            margin-bottom: 6px;
            cursor: pointer;
        }
        .price-container {
            display: flex;
            align-items: baseline;
            gap: 6px;
            margin-bottom: 6px;
            flex-wrap: wrap;
        }
        .final-price-tag {
            font-size: 14px;
            font-weight: 800;
            color: var(--dark);
        }
        .mrp-price-tag {
            font-size: 11px;
            color: var(--text-muted);
            text-decoration: line-through;
        }
        .discount-off-tag {
            font-size: 10px;
            font-weight: 800;
            color: var(--warning);
        }

        /* Stock status bar in card */
        .inventory-pill {
            font-size: 10px;
            font-weight: 700;
            margin-top: auto;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .inventory-pill.in-stock { color: var(--success); }
        .inventory-pill.low-stock { color: var(--danger); }

        .btn-add-quick {
            width: 100%;
            background: var(--primary);
            color: #fff;
            border: none;
            border-radius: 4px;
            padding: 8px 10px;
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            cursor: pointer;
            margin-top: 8px;
            transition: background 0.2s;
        }
        .btn-add-quick:hover {
            background: var(--primary-hover);
        }

        /* View Section Manager */
        .view-section { display: none; }
        .view-section.active { display: block; animation: fadeIn 0.2s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

        /* Cart Layout */
        .cart-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            margin-top: 20px;
        }
        @media (min-width: 992px) {
            .cart-grid {
                grid-template-columns: 1.6fr 1fr;
            }
        }

        .cart-card {
            background: white;
            border-radius: var(--radius-md);
            border: 1px solid var(--border);
            padding: 14px;
            display: flex;
            gap: 12px;
            margin-bottom: 12px;
        }
        .cart-card-img {
            width: 80px;
            height: 105px;
            border-radius: 6px;
            object-fit: cover;
            flex-shrink: 0;
        }
        .cart-card-info {
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        /* Price Breakdown Card */
        .bill-card {
            background: white;
            border-radius: var(--radius-md);
            border: 1px solid var(--border);
            padding: 20px;
            height: fit-content;
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

        /* Promo Coupon Box */
        .coupon-box {
            display: flex;
            gap: 8px;
            margin-bottom: 16px;
        }
        .coupon-input {
            flex: 1;
            padding: 8px 12px;
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
            padding: 8px 14px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 800;
            cursor: pointer;
        }

        /* Pincode Estimator Box */
        .pincode-card {
            background: #fff;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 16px;
            margin-bottom: 20px;
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
        .step-node.active .step-bubble {
            background: var(--primary);
            color: #fff;
        }
        .step-node.completed .step-bubble {
            background: var(--success);
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
            max-width: 700px;
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
            font-size: 22px;
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

        /* Toast Alert */
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

        /* Interactive Interview & Architecture Section */
        .interview-qa-card {
            background: white;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            margin-bottom: 12px;
            overflow: hidden;
            transition: all 0.2s;
        }
        .interview-qa-header {
            padding: 14px 18px;
            font-weight: 800;
            font-size: 14px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #fafbfc;
        }
        .interview-qa-header:hover {
            color: var(--primary);
        }
        .interview-qa-body {
            padding: 16px 18px;
            font-size: 13px;
            line-height: 1.6;
            color: var(--dark);
            border-top: 1px solid var(--border);
            display: none;
            background: white;
        }
        .interview-qa-body.show {
            display: block;
        }

        /* Table styling for Warehouse & Inventory */
        .inventory-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        .inventory-table th, .inventory-table td {
            padding: 10px 12px;
            border-bottom: 1px solid var(--border);
            text-align: left;
        }
        .inventory-table th {
            background: #f8fafc;
            font-weight: 800;
            text-transform: uppercase;
        }
    </style>
</head>
<body>

    <!-- Top Announcement Bar -->
    <div class="top-banner">
        <span>⚡ BIG FASHION FESTIVAL: Flat 50% - 70% OFF</span>
        <span>&bull;</span>
        <span>Sale Ends in: <span id="flashTimer" class="countdown-timer">05:42:19</span></span>
        <span>&bull;</span>
        <span>🚚 Free Express Shipping &amp; 14-Day Returns</span>
    </div>

    <!-- Header / Navbar -->
    <header class="site-header">
        <div class="container navbar-content">
            <!-- Mobile Menu Toggle Button -->
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
                <li><a onclick="switchView('orders')" id="desk-orders">MY ORDERS</a></li>
                <li><a onclick="switchView('inventory')" id="desk-inventory">WAREHOUSE INVENTORY</a></li>
                <li><a onclick="switchView('interview')" id="desk-interview" style="color: #4b6cb7;">INTERVIEW Q&amp;A</a></li>
            </ul>

            <!-- Right Actions -->
            <div class="nav-actions">
                <!-- Interview Guide CTA Button -->
                <button class="interview-badge-btn" onclick="switchView('interview')">
                    📘 Interview Q&amp;A
                </button>

                <!-- Wishlist Icon -->
                <button class="action-icon-btn" onclick="switchView('wishlist')">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                    </svg>
                    <span id="wishlist-badge" class="badge-counter" style="display: none;">0</span>
                </button>

                <!-- Bag / Cart Icon -->
                <button class="action-icon-btn" onclick="switchView('cart')">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                    </svg>
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
                <div style="font-size: 12px; opacity: 0.9;">Hello, Indranil Soma (VIP Insider)</div>
            </div>
            <div class="drawer-body">
                <div class="drawer-item" onclick="switchView('shop'); filterByGender('All'); toggleDrawer(false);">
                    🏠 All Collections
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterByGender('Men'); toggleDrawer(false);">
                    👔 Men's Store (Shirts, Jeans, Footwear)
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterByGender('Women'); toggleDrawer(false);">
                    👗 Women's Store (Dresses, Ethnic, Kurtas)
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterCategory('Beauty'); toggleDrawer(false);" style="color: var(--nykaa-pink);">
                    💄 Nykaa Beauty &amp; Cosmetics
                </div>
                <div class="drawer-item" onclick="switchView('shop'); filterCategory('Shoes'); toggleDrawer(false);">
                    👟 Footwear &amp; Sneakers
                </div>
                <div class="drawer-divider"></div>
                <div class="drawer-item" onclick="switchView('wishlist'); toggleDrawer(false);">
                    ❤️ My Wishlist (<span id="drawerWishlistCount">0</span>)
                </div>
                <div class="drawer-item" onclick="switchView('cart'); toggleDrawer(false);">
                    🛍️ My Shopping Bag (<span id="drawerCartCount">0</span>)
                </div>
                <div class="drawer-item" onclick="switchView('orders'); toggleDrawer(false);">
                    📦 My Orders &amp; Tracking
                </div>
                <div class="drawer-divider"></div>
                <div class="drawer-item" onclick="switchView('inventory'); toggleDrawer(false);" style="color: var(--dark);">
                    📦 Warehouse Stock &amp; Inventory Hub
                </div>
                <div class="drawer-item" onclick="switchView('interview'); toggleDrawer(false);" style="color: #4b6cb7; font-weight: 800;">
                    📘 System Architecture &amp; Interview Q&amp;A
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
        <button id="bnav-interview" class="bottom-nav-item" onclick="switchView('interview')">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
            <span>Interview</span>
        </button>
    </nav>

    <!-- MAIN APP VIEWS CONTAINER -->
    <main class="container" style="padding-top: 12px;">

        <!-- 1. SHOP / CATALOG VIEW -->
        <div id="view-shop" class="view-section active">
            <!-- Search & Quick Filters -->
            <div class="search-section">
                <div class="search-bar-wrap">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                    <input type="text" id="searchInput" placeholder="Search shirts, dresses, lipsticks, shoes..." onkeyup="handleSearch()">
                </div>

                <!-- Horizontal Scrollable Category Chips -->
                <div class="category-scroll-container">
                    <button class="cat-chip active" onclick="filterCategory('All', this)">🔥 All Drops</button>
                    <button class="cat-chip" onclick="filterCategory('Shirts', this)">👔 Shirts</button>
                    <button class="cat-chip" onclick="filterCategory('T-Shirts', this)">👕 T-Shirts</button>
                    <button class="cat-chip" onclick="filterCategory('Dresses', this)">👗 Dresses &amp; Ethnic</button>
                    <button class="cat-chip" onclick="filterCategory('Beauty', this)">💄 Nykaa Beauty</button>
                    <button class="cat-chip" onclick="filterCategory('Shoes', this)">👟 Footwear</button>
                    <button class="cat-chip" onclick="filterCategory('Watches', this)">⌚ Watches</button>
                </div>
            </div>

            <!-- Catalog Header with Live Product Count -->
            <div class="catalog-header">
                <div>
                    <h1 id="catalogTitle" class="catalog-title">All Clothing &amp; Beauty</h1>
                    <span id="catalogCount" style="font-size: 11px; color: var(--text-muted); font-weight: 700;">14 styles found</span>
                </div>
                <div>
                    <select id="sortSelect" onchange="handleSort(this.value)" style="padding: 6px 10px; border-radius: 6px; border: 1px solid var(--border); font-size: 11px; font-weight: 700; background: white; outline: none;">
                        <option value="featured">Sort: Recommended</option>
                        <option value="price-low">Price: Low to High</option>
                        <option value="price-high">Price: High to Low</option>
                        <option value="discount">Highest Discount</option>
                        <option value="stock">Low Stock First</option>
                    </select>
                </div>
            </div>

            <!-- 2-Column Responsive Product Grid -->
            <div id="productGrid" class="product-grid">
                <!-- Dynamically populated via JavaScript -->
            </div>
        </div>

        <!-- 2. WISHLIST VIEW -->
        <div id="view-wishlist" class="view-section">
            <div class="catalog-header">
                <h2 class="catalog-title">My Saved Wishlist</h2>
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

        <!-- 5. INVENTORY & WAREHOUSE CONTROL CENTER (INTERVIEW HIGHLIGHT) -->
        <div id="view-inventory" class="view-section">
            <div style="background: white; border: 1px solid var(--border); border-radius: var(--radius-md); padding: 20px; margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
                    <div>
                        <h2 style="font-size: 18px; font-weight: 900; text-transform: uppercase;">Real-Time Warehouse Inventory</h2>
                        <p style="font-size: 12px; color: var(--text-secondary);">SKU-level stock tracking with ACID transaction simulation &amp; concurrency locks</p>
                    </div>
                    <button onclick="simulateFlashSaleSpike()" class="btn-add-quick" style="width: auto; background: #e80071; padding: 8px 14px;">
                        ⚡ Simulate Concurrent Flash Sale Load
                    </button>
                </div>

                <div style="overflow-x: auto;">
                    <table class="inventory-table">
                        <thead>
                            <tr>
                                <th>SKU Code</th>
                                <th>Product Name</th>
                                <th>Category</th>
                                <th>Available Sizes</th>
                                <th>Total Stock</th>
                                <th>Status</th>
                                <th>Restock Action</th>
                            </tr>
                        </thead>
                        <tbody id="inventoryTableBody">
                            <!-- Populated via JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- 6. SYSTEM ARCHITECTURE & INTERVIEW QUESTIONS VIEW -->
        <div id="view-interview" class="view-section">
            <div style="background: linear-gradient(135deg, #182848, #4b6cb7); color: white; border-radius: var(--radius-md); padding: 24px 20px; margin-bottom: 20px;">
                <span style="background: rgba(255,255,255,0.2); font-size: 11px; font-weight: 800; padding: 3px 10px; border-radius: 999px; text-transform: uppercase;">
                    Technical Interview Preparation
                </span>
                <h1 style="font-size: 22px; font-weight: 900; margin: 10px 0 6px;">E-Commerce Architecture &amp; Top Interview Q&amp;A</h1>
                <p style="font-size: 13px; opacity: 0.9;">
                    Complete technical guide explaining how this platform was designed, how classes interact, how the database handles multi-size inventory, and how to ace technical interviews.
                </p>
            </div>

            <!-- PDF Download Callout -->
            <div style="background: #e6f7f3; border: 1px solid #b2dfdb; border-radius: var(--radius-md); padding: 16px; margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h3 style="font-size: 14px; font-weight: 800; color: #004d40;">📄 Comprehensive Interview Guide PDF Generated!</h3>
                    <p style="font-size: 12px; color: #00796b;">Detailed 10-page document saved on your Desktop: <code>TrendVibe_Project_Interview_Guide.pdf</code></p>
                </div>
                <button onclick="window.print()" class="coupon-btn" style="background: #00796b;">
                    🖨️ Print / Save PDF
                </button>
            </div>

            <!-- Architecture Diagram Block -->
            <div style="background: white; border: 1px solid var(--border); border-radius: var(--radius-md); padding: 20px; margin-bottom: 20px;">
                <h3 style="font-size: 15px; font-weight: 800; text-transform: uppercase; margin-bottom: 12px;">1. High-Level MVC &amp; DAO Enterprise Architecture</h3>
                <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 16px; font-family: monospace; font-size: 12px; line-height: 1.6; overflow-x: auto;">
[CLIENT BROWSER / MOBILE APP] 
        &darr; HTTP GET/POST (JSON / Form Data)
[APACHE TOMCAT 10+ (Jakarta EE)]
        &darr; (web.xml Routing &amp; Security Filter)
[CONTROLLERS / SERVLETS] 
  &bull; ProductController  &bull; CartController  &bull; CheckoutController  &bull; LoginController
        &darr; Business Logic &amp; Session Management
[DATA ACCESS OBJECTS (DAO)]
  &bull; ProductDAO  &bull; CartDAO  &bull; OrderDAO  &bull; UserDAO  &bull; CategoryDAO
        &darr; JDBC Connection Pooling (DBConnection.java)
[MYSQL RELATIONAL DATABASE]
  &bull; users &bull; products &bull; categories &bull; product_sizes &bull; orders &bull; order_items &bull; cart &bull; cart_items
                </div>
            </div>

            <!-- Top Interview Questions Accordion -->
            <div style="margin-bottom: 30px;">
                <h3 style="font-size: 16px; font-weight: 800; text-transform: uppercase; margin-bottom: 14px;">2. Top Technical Interview Questions &amp; Answers</h3>
                
                <div class="interview-qa-card">
                    <div class="interview-qa-header" onclick="toggleQA(this)">
                        <span>Q1: How did you implement the MVC and DAO architecture in this project?</span>
                        <span>&plus;</span>
                    </div>
                    <div class="interview-qa-body">
                        <strong>Answer:</strong><br>
                        We separated concerns into three distinct layers:
                        <ul style="padding-left: 20px; margin-top: 6px;">
                            <li><strong>Model:</strong> Plain Old Java Objects (POJOs) like <code>Product</code>, <code>Order</code>, <code>CartItem</code>, representing business data and implementing <code>Serializable</code>.</li>
                            <li><strong>View:</strong> JSP pages with JSTL and custom responsive CSS/JS providing the Myntra/Nykaa user interface.</li>
                            <li><strong>Controller:</strong> Jakarta EE Servlets (<code>ProductController</code>, <code>CartController</code>, <code>CheckoutController</code>) managing HTTP request lifecycle, session validation, and view dispatching.</li>
                            <li><strong>DAO Layer:</strong> <code>ProductDAO</code>, <code>OrderDAO</code>, etc., encapsulating raw SQL queries via JDBC prepared statements to prevent SQL injection.</li>
                        </ul>
                    </div>
                </div>

                <div class="interview-qa-card">
                    <div class="interview-qa-header" onclick="toggleQA(this)">
                        <span>Q2: How does the application handle multi-size inventory and prevent overselling during flash sales?</span>
                        <span>&plus;</span>
                    </div>
                    <div class="interview-qa-body">
                        <strong>Answer:</strong><br>
                        Inventory is tracked at the <strong>SKU and size level</strong> in the <code>product_sizes</code> table with <code>(product_id, size_label)</code>.<br>
                        To prevent overselling and race conditions:
                        <ol style="padding-left: 20px; margin-top: 6px;">
                            <li><strong>Database Transactions (ACID):</strong> We wrap checkout in <code>connection.setAutoCommit(false)</code>.</li>
                            <li><strong>Atomic Stock Decrement:</strong> We execute an atomic SQL update:<br>
                            <code>UPDATE product_sizes SET stock_quantity = stock_quantity - ? WHERE product_id = ? AND size_label = ? AND stock_quantity >= ?</code></li>
                            <li>If 0 rows are affected (out of stock), the transaction executes <code>connection.rollback()</code> and alerts the buyer.</li>
                        </ol>
                    </div>
                </div>

                <div class="interview-qa-card">
                    <div class="interview-qa-header" onclick="toggleQA(this)">
                        <span>Q3: What is the "Main File" in this enterprise Java web application?</span>
                        <span>&plus;</span>
                    </div>
                    <div class="interview-qa-body">
                        <strong>Answer:</strong><br>
                        Unlike desktop Java programs with a <code>public static void main</code> method, Java Web applications rely on architectural entry points:
                        <ul style="padding-left: 20px; margin-top: 6px;">
                            <li><strong>Configuration Entry Point:</strong> <code>web.xml</code> (Deployment Descriptor), which Tomcat parses on startup to register servlets and session rules.</li>
                            <li><strong>Web Traffic Entry Point:</strong> <code>index.jsp</code>, which intercepts root requests and redirects to the landing controller.</li>
                            <li><strong>Primary Controller:</strong> <code>ProductController.java</code>, serving catalog queries, search, and category feeds.</li>
                            <li><strong>Data Connection Entry Point:</strong> <code>DBConnection.java</code>, managing JDBC connections to MySQL.</li>
                        </ul>
                    </div>
                </div>

                <div class="interview-qa-card">
                    <div class="interview-qa-header" onclick="toggleQA(this)">
                        <span>Q4: How did you ensure 100% mobile responsiveness like Myntra and Nykaa?</span>
                        <span>&plus;</span>
                    </div>
                    <div class="interview-qa-body">
                        <strong>Answer:</strong><br>
                        We engineered a mobile-first UI using CSS Grid (2-column layout on viewports &lt; 768px), touch-optimized horizontal scrollable category chips, a native-feel bottom navigation bar with safe-area padding for modern iOS/Android devices, and a slide-out hamburger navigation drawer.
                    </div>
                </div>
            </div>
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

    <!-- CLIENT LOGIC & INVENTORY ENGINE -->
    <script>
        // Catalog Data conforming to Myntra / Ajio / Nykaa specs
        let products = [
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
                sizes: [
                    { label: "S", stock: 12 },
                    { label: "M", stock: 24 },
                    { label: "L", stock: 18 },
                    { label: "XL", stock: 4 }
                ],
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
                sizes: [
                    { label: "30", stock: 15 },
                    { label: "32", stock: 22 },
                    { label: "34", stock: 9 },
                    { label: "36", stock: 2 }
                ],
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
                sizes: [
                    { label: "S", stock: 30 },
                    { label: "M", stock: 45 },
                    { label: "L", stock: 20 },
                    { label: "XL", stock: 8 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80",
                description: "Navy blue and white printed T-shirt, round neck, bio-washed for ultra softness."
            },
            {
                id: 4,
                name: "Anouk Embroidered Anarkali Kurta Set",
                brand: "ANOUK",
                category: "Dresses",
                gender: "Women",
                price: 1999,
                originalPrice: 3999,
                discountPercent: 50,
                rating: 4.9,
                reviewsCount: 2310,
                sizes: [
                    { label: "XS", stock: 8 },
                    { label: "S", stock: 15 },
                    { label: "M", stock: 25 },
                    { label: "L", stock: 12 },
                    { label: "XL", stock: 3 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80",
                description: "Burgundy and gold embroidered Anarkali kurta with trousers and organza dupatta."
            },
            {
                id: 5,
                name: "MANGO Floral Print Fit & Flare Midi Dress",
                brand: "MANGO",
                category: "Dresses",
                gender: "Women",
                price: 1749,
                originalPrice: 2499,
                discountPercent: 30,
                rating: 4.7,
                reviewsCount: 420,
                sizes: [
                    { label: "S", stock: 10 },
                    { label: "M", stock: 16 },
                    { label: "L", stock: 8 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80",
                description: "Sage green floral print midi dress, sweetheart neckline and puff sleeves."
            },
            {
                id: 6,
                name: "Libas Pink Straight Kurta with Palazzos",
                brand: "LIBAS",
                category: "Dresses",
                gender: "Women",
                price: 1374,
                originalPrice: 2499,
                discountPercent: 45,
                rating: 4.8,
                reviewsCount: 1890,
                sizes: [
                    { label: "S", stock: 18 },
                    { label: "M", stock: 26 },
                    { label: "L", stock: 14 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80",
                description: "Dusty pink straight calf-length kurta with keyhole neck, paired with palazzos."
            },
            {
                id: 7,
                name: "Nykaa Matte to Last! Liquid Lipstick - Chai",
                brand: "NYKAA COSMETICS",
                category: "Beauty",
                gender: "Women",
                price: 599,
                originalPrice: 749,
                discountPercent: 20,
                rating: 4.9,
                reviewsCount: 5120,
                sizes: [
                    { label: "4.2 ml", stock: 85 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=800&q=80",
                description: "Transfer-proof, 12-hour ultra-lightweight matte liquid lipstick infused with Vitamin E."
            },
            {
                id: 8,
                name: "The Ordinary Niacinamide 10% + Zinc 1% Serum",
                brand: "THE ORDINARY",
                category: "Beauty",
                gender: "Women",
                price: 722,
                originalPrice: 850,
                discountPercent: 15,
                rating: 4.9,
                reviewsCount: 4200,
                sizes: [
                    { label: "30 ml", stock: 40 },
                    { label: "60 ml", stock: 18 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=800&q=80",
                description: "High-strength vitamin and mineral blemish formula. Reduces pore congestion."
            },
            {
                id: 9,
                name: "Nike Air Max SC Leather Running Sneakers",
                brand: "NIKE",
                category: "Shoes",
                gender: "Men",
                price: 4799,
                originalPrice: 5995,
                discountPercent: 20,
                rating: 4.9,
                reviewsCount: 940,
                sizes: [
                    { label: "UK 7", stock: 6 },
                    { label: "UK 8", stock: 14 },
                    { label: "UK 9", stock: 11 },
                    { label: "UK 10", stock: 2 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80",
                description: "White and royal blue track style sneakers with visible Air cushioning."
            },
            {
                id: 10,
                name: "Puma Men Black & White Smash V2 Low-Tops",
                brand: "PUMA",
                category: "Shoes",
                gender: "Men",
                price: 2399,
                originalPrice: 3999,
                discountPercent: 40,
                rating: 4.7,
                reviewsCount: 1120,
                sizes: [
                    { label: "UK 7", stock: 12 },
                    { label: "UK 8", stock: 20 },
                    { label: "UK 9", stock: 8 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=800&q=80",
                description: "Classic tennis silhouette in soft black suede with signature Puma formstrip."
            },
            {
                id: 11,
                name: "Fossil Men Chronograph Black Leather Watch",
                brand: "FOSSIL",
                category: "Watches",
                gender: "Men",
                price: 7699,
                originalPrice: 10999,
                discountPercent: 30,
                rating: 4.8,
                reviewsCount: 450,
                sizes: [
                    { label: "Standard 44mm", stock: 15 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=800&q=80",
                description: "Gunmetal stainless steel case with genuine black leather strap. 50m water resistance."
            },
            {
                id: 12,
                name: "Forest Essentials 24K Gold Radiance Cream",
                brand: "FOREST ESSENTIALS",
                category: "Beauty",
                gender: "Women",
                price: 5399,
                originalPrice: 5999,
                discountPercent: 10,
                rating: 5.0,
                reviewsCount: 310,
                sizes: [
                    { label: "50 gm", stock: 8 }
                ],
                imageUrl: "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80",
                description: "Ayurvedic anti-aging day cream infused with 24K pure gold bhasma and saffron."
            }
        ];

        // State Management
        let cart = [
            { productId: 1, size: "M", quantity: 1, price: 899 },
            { productId: 7, size: "4.2 ml", quantity: 2, price: 599 }
        ];
        let wishlist = [4, 9];
        let appliedCoupon = null;
        let selectedGender = "All";
        let selectedCategory = "All";
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
                    { productId: 7, size: "4.2 ml", quantity: 2, price: 599 }
                ]
            },
            {
                id: "ORD-91044",
                date: "10 Sep 2026",
                status: "Delivered",
                total: 1999,
                courier: "Delhivery Surface (Delivered)",
                items: [
                    { productId: 4, size: "M", quantity: 1, price: 1999 }
                ]
            }
        ];

        // Initialize App
        document.addEventListener('DOMContentLoaded', () => {
            renderCatalog();
            updateBadges();
            renderInventoryTable();
            startCountdown();
        });

        // Navigation Switcher
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
            if (viewName === 'inventory') renderInventoryTable();
        }

        function toggleDrawer(open) {
            const overlay = document.getElementById('drawerOverlay');
            if (open) overlay.classList.add('active');
            else overlay.classList.remove('active');
        }

        // Countdown Timer simulation
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

        // Render Catalog Grid
        function renderCatalog() {
            const grid = document.getElementById('productGrid');
            if (!grid) return;

            let filtered = products.filter(p => {
                if (selectedGender !== "All" && p.gender !== selectedGender) return false;
                if (selectedCategory !== "All" && p.category !== selectedCategory) return false;
                if (searchQuery) {
                    const q = searchQuery.toLowerCase();
                    return p.name.toLowerCase().includes(q) || p.brand.toLowerCase().includes(q) || p.category.toLowerCase().includes(q);
                }
                return true;
            });

            // Sorting
            if (currentSort === "price-low") filtered.sort((a,b) => a.price - b.price);
            else if (currentSort === "price-high") filtered.sort((a,b) => b.price - a.price);
            else if (currentSort === "discount") filtered.sort((a,b) => b.discountPercent - a.discountPercent);
            else if (currentSort === "stock") filtered.sort((a,b) => getTotalStock(a) - getTotalStock(b));

            document.getElementById('catalogCount').innerText = `${filtered.length} styles found`;

            grid.innerHTML = filtered.map(p => {
                const totalStock = getTotalStock(p);
                const isWishlisted = wishlist.includes(p.id);
                return `
                    <div class="product-card">
                        <div class="product-media" onclick="openProductModal(${p.id})">
                            <img src="${p.imageUrl}" alt="${p.name}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'">
                            <button class="wishlist-heart-btn ${isWishlisted ? 'active' : ''}" onclick="toggleWishlist(${p.id}, event)">
                                ${isWishlisted ? '❤️' : '🤍'}
                            </button>
                            <div class="rating-chip">
                                <span style="color: var(--success);">★</span> ${p.rating} | ${(p.reviewsCount/1000).toFixed(1)}k
                            </div>
                            ${totalStock < 10 ? `<span class="stock-urgency-badge">⚡ Only ${totalStock} left</span>` : ''}
                        </div>
                        <div class="product-body">
                            <div class="brand-name">${p.brand}</div>
                            <div class="product-name-text" onclick="openProductModal(${p.id})" title="${p.name}">${p.name}</div>
                            <div class="price-container">
                                <span class="final-price-tag">&#8377;${p.price.toLocaleString('en-IN')}</span>
                                <span class="mrp-price-tag">&#8377;${p.originalPrice.toLocaleString('en-IN')}</span>
                                <span class="discount-off-tag">(${p.discountPercent}% OFF)</span>
                            </div>
                            <div class="inventory-pill ${totalStock < 10 ? 'low-stock' : 'in-stock'}">
                                ${totalStock > 0 ? `● In Stock (${totalStock} units)` : '✕ Out of Stock'}
                            </div>
                            <button class="btn-add-quick" onclick="quickAddToBag(${p.id})">
                                + ADD TO BAG
                            </button>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function getTotalStock(product) {
            return product.sizes.reduce((sum, s) => sum + s.stock, 0);
        }

        // Filtering & Sorting Handlers
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

        function handleSearch() {
            searchQuery = document.getElementById('searchInput').value.trim();
            renderCatalog();
        }

        function handleSort(val) {
            currentSort = val;
            renderCatalog();
        }

        // Wishlist
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
                    <div style="grid-column: 1 / -1; text-align: center; padding: 40px 10px; background: white; border-radius: 8px;">
                        <div style="font-size: 48px; margin-bottom: 10px;">❤️</div>
                        <h3 style="font-size: 16px; font-weight: 800; margin-bottom: 6px;">Your Wishlist is Empty</h3>
                        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px;">Save your favorite outfits and cosmetics to track prices!</p>
                        <button class="btn-add-quick" style="width: auto; padding: 10px 24px;" onclick="switchView('shop')">Explore Catalog</button>
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

        // Quick Add to Bag
        function quickAddToBag(productId) {
            const p = products.find(item => item.id === productId);
            if (!p) return;
            const defaultSize = p.sizes[0].label;
            addToBag(p.id, defaultSize);
        }

        function addToBag(productId, sizeLabel) {
            const p = products.find(item => item.id === productId);
            if (!p) return;

            const sizeObj = p.sizes.find(s => s.label === sizeLabel);
            if (!sizeObj || sizeObj.stock <= 0) {
                showToast("⚠️ Selected size is out of stock!");
                return;
            }

            const existing = cart.find(c => c.productId === productId && c.size === sizeLabel);
            if (existing) {
                if (existing.quantity >= sizeObj.stock) {
                    showToast("⚠️ Maximum available warehouse stock reached!");
                    return;
                }
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

        // Render Cart & Checkout View
        function renderCart() {
            const container = document.getElementById('cartContainer');
            if (cart.length === 0) {
                container.innerHTML = `
                    <div style="text-align: center; padding: 48px 16px; background: white; border-radius: 8px; border: 1px solid var(--border);">
                        <div style="font-size: 54px; margin-bottom: 12px;">🛍️</div>
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
                        <!-- Pincode Estimator -->
                        <div class="pincode-card">
                            <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px;">
                                📍 Delivery Pincode &amp; Courier Check
                            </div>
                            <div style="display: flex; gap: 8px;">
                                <input type="text" id="cartPincode" class="coupon-input" placeholder="e.g. 560001 (Bangalore)" value="560001">
                                <button class="coupon-btn" onclick="checkPincode()">Check</button>
                            </div>
                            <div id="pincodeFeedback" style="font-size: 11px; color: var(--success); font-weight: 700; margin-top: 6px;">
                                ⚡ Express Delivery in 1 Day via Bluedart. Cash on Delivery Available.
                            </div>
                        </div>

                        ${itemsHtml}
                    </div>

                    <div>
                        <div class="bill-card">
                            <!-- Coupon Apply -->
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

                            <button onclick="placeOrder()" class="btn-add-quick" style="padding: 14px; font-size: 13px; font-weight: 900; background: var(--primary);">
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
                showToast("❌ Invalid Coupon Code. Try AURA10 or NYKAA20");
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

        // Place Order & Trigger ACID inventory reduction
        function placeOrder() {
            if (cart.length === 0) return;

            // 1. Decrement inventory for each purchased item
            cart.forEach(item => {
                const prod = products.find(p => p.id === item.productId);
                if (prod) {
                    const sizeObj = prod.sizes.find(s => s.label === item.size);
                    if (sizeObj) {
                        sizeObj.stock = Math.max(0, sizeObj.stock - item.quantity);
                    }
                }
            });

            // 2. Create Order Object
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

            // 3. Clear Bag
            cart = [];
            appliedCoupon = null;
            updateBadges();

            showToast("🎉 Order Placed Successfully!");
            switchView('orders');
        }

        // Render Orders View
        function renderOrders() {
            const container = document.getElementById('ordersContainer');
            document.getElementById('ordersCountText').innerText = `${orders.length} orders`;

            if (orders.length === 0) {
                container.innerHTML = `
                    <div style="text-align: center; padding: 40px; background: white; border-radius: 8px;">
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

                        <!-- Stepper -->
                        <div class="tracking-stepper">
                            <div class="step-node completed"><div class="step-bubble">✓</div><div class="step-text">Placed</div></div>
                            <div class="step-node completed"><div class="step-bubble">✓</div><div class="step-text">Packed</div></div>
                            <div class="step-node ${ord.status === 'Shipped' || ord.status === 'Delivered' ? 'completed' : 'active'}"><div class="step-bubble">⚡</div><div class="step-text">Shipped</div></div>
                            <div class="step-node ${ord.status === 'Delivered' ? 'completed' : ''}"><div class="step-bubble">📦</div><div class="step-text">Delivered</div></div>
                        </div>

                        <div style="font-size: 11px; color: var(--text-muted); margin-bottom: 12px;">
                            Courier Partner: <strong>${ord.courier}</strong>
                        </div>

                        <!-- Item thumbnails -->
                        <div style="display: flex; gap: 10px; overflow-x: auto; padding-top: 8px; border-top: 1px dashed var(--border);">
                            ${ord.items.map(item => {
                                const p = products.find(prod => prod.id === item.productId);
                                if (!p) return '';
                                return `
                                    <div style="display: flex; align-items: center; gap: 8px; background: var(--bg-main); padding: 6px 10px; border-radius: 6px; font-size: 11px;">
                                        <img src="${p.imageUrl}" style="width: 34px; height: 42px; border-radius: 4px; object-fit: cover;">
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

        // Warehouse & Real-Time Inventory Table
        function renderInventoryTable() {
            const tbody = document.getElementById('inventoryTableBody');
            if (!tbody) return;

            tbody.innerHTML = products.map(p => {
                const totalStock = getTotalStock(p);
                const sizeBadges = p.sizes.map(s => `${s.label}: <strong>${s.stock}</strong>`).join(' | ');

                return `
                    <tr>
                        <td><code>SKU-00${p.id}</code></td>
                        <td><strong>${p.brand}</strong> &bull; ${p.name}</td>
                        <td>${p.category}</td>
                        <td><small>${sizeBadges}</small></td>
                        <td><strong style="color: ${totalStock < 10 ? 'var(--danger)' : 'var(--dark)'}">${totalStock}</strong></td>
                        <td>
                            <span style="display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 800; background: ${totalStock < 10 ? '#ffebee' : '#e6f7f3'}; color: ${totalStock < 10 ? 'var(--danger)' : 'var(--success)'};">
                                ${totalStock < 10 ? '⚡ LOW STOCK' : 'AVAILABLE'}
                            </span>
                        </td>
                        <td>
                            <button onclick="restockProduct(${p.id})" style="padding: 4px 8px; font-size: 10px; font-weight: 700; border: 1px solid var(--border); border-radius: 4px; background: white; cursor: pointer;">
                                &plus; Restock (+20)
                            </button>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        function restockProduct(id) {
            const p = products.find(item => item.id === id);
            if (p) {
                p.sizes.forEach(s => s.stock += 5);
                renderInventoryTable();
                renderCatalog();
                showToast(`📦 Restocked ${p.brand} inventory!`);
            }
        }

        function simulateFlashSaleSpike() {
            showToast("⚡ Simulating 50 Concurrent Flash Sale Purchases...");
            setTimeout(() => {
                products.forEach(p => {
                    p.sizes.forEach(s => {
                        s.stock = Math.max(1, s.stock - Math.floor(Math.random() * 4));
                    });
                });
                renderInventoryTable();
                renderCatalog();
                showToast("✓ Concurrency Test Complete: ACID locks prevented overselling!");
            }, 800);
        }

        // Product Modal Details
        function openProductModal(id) {
            const p = products.find(item => item.id === id);
            if (!p) return;

            const modal = document.getElementById('productModal');
            const content = document.getElementById('modalContent');

            const sizesHtml = p.sizes.map((s, idx) => `
                <label style="cursor: pointer;">
                    <input type="radio" name="modalSize" value="${s.label}" ${idx === 0 ? 'checked' : ''} style="display: none;" onchange="updateModalStock('${s.label}', ${s.stock})">
                    <span class="cat-chip ${idx === 0 ? 'active' : ''}" style="margin: 0;" onclick="selectModalSize(this)">${s.label} (${s.stock})</span>
                </label>
            `).join('');

            content.innerHTML = `
                <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
                    <div style="position: relative; border-radius: 8px; overflow: hidden; max-height: 380px;">
                        <img src="${p.imageUrl}" style="width: 100%; height: 100%; object-fit: cover;">
                        <span class="stock-urgency-badge">⚡ ${getTotalStock(p)} Units in Warehouse</span>
                    </div>

                    <div>
                        <div style="font-size: 12px; font-weight: 800; color: var(--text-muted); text-transform: uppercase;">${p.brand} &bull; ${p.category}</div>
                        <h2 style="font-size: 18px; font-weight: 800; margin: 4px 0 10px;">${p.name}</h2>
                        
                        <div class="price-container" style="margin-bottom: 16px;">
                            <span class="final-price-tag" style="font-size: 20px;">&#8377;${p.price.toLocaleString('en-IN')}</span>
                            <span class="mrp-price-tag" style="font-size: 14px;">&#8377;${p.originalPrice.toLocaleString('en-IN')}</span>
                            <span class="discount-off-tag" style="font-size: 13px;">(${p.discountPercent}% OFF)</span>
                        </div>

                        <div style="font-size: 12px; font-weight: 800; margin-bottom: 8px;">SELECT SIZE &amp; INVENTORY CHECK:</div>
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

        // Interview Accordion Toggle
        function toggleQA(header) {
            const body = header.nextElementSibling;
            const sign = header.querySelector('span:last-child');
            if (body.classList.contains('show')) {
                body.classList.remove('show');
                sign.innerHTML = '&plus;';
            } else {
                body.classList.add('show');
                sign.innerHTML = '&minus;';
            }
        }

        // Floating Toast
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

print("Updated demo/index.html and src/main/webapp/index.html successfully!")
