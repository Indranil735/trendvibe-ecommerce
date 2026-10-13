import json
import os

with open("products_data.json", "r", encoding="utf-8") as f:
    products = json.load(f)

print(f"Loaded {len(products)} products for compilation")

# We will write the complete production HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>TRENDVIBE ATELIER &bull; The Luxury Autumn/Winter Runway &amp; Beauty Collection</title>
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

        /* Top Announcement Bar */
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
        }
        @media (min-width: 768px) {
            .top-banner { font-size: 11px; padding: 8px 16px; letter-spacing: 1.5px; }
        }

        /* Header Navigation */
        .header {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
            height: 58px;
            display: flex;
            align-items: center;
        }
        @media (min-width: 992px) {
            .header { height: 74px; }
        }

        .header-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            height: 100%;
        }

        .logo {
            font-family: var(--font-brand);
            font-size: 17px;
            font-weight: 700;
            letter-spacing: 2.5px;
            color: var(--dark);
            text-transform: uppercase;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        @media (min-width: 768px) {
            .logo { font-size: 22px; letter-spacing: 3.5px; }
        }
        .logo span {
            color: var(--accent);
            font-weight: 400;
            font-family: var(--font-serif);
            font-style: italic;
        }

        .desktop-nav {
            display: none;
            gap: 24px;
            list-style: none;
        }
        @media (min-width: 992px) {
            .desktop-nav { display: flex; }
        }

        .nav-link {
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            color: var(--dark);
            position: relative;
            padding: 8px 0;
            transition: color 0.2s;
        }
        .nav-link:hover, .nav-link.active {
            color: var(--accent);
        }
        .nav-link.active::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: var(--accent);
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        @media (min-width: 768px) {
            .header-actions { gap: 16px; }
        }

        .action-btn {
            background: none;
            border: none;
            cursor: pointer;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--dark);
            padding: 6px;
            border-radius: 50%;
            transition: background 0.2s;
        }
        .action-btn:hover {
            background: rgba(0,0,0,0.04);
        }
        .action-btn svg {
            width: 20px;
            height: 20px;
        }

        .user-greeting-btn {
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.5px;
            background: #f4efe6;
            color: #1a1a1a;
            border: 1px solid var(--accent);
            padding: 4px 10px;
            border-radius: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .user-greeting-btn:hover {
            background: var(--accent);
            color: #ffffff;
        }

        .badge-count {
            position: absolute;
            top: 2px;
            right: 2px;
            background: var(--primary);
            color: #ffffff;
            font-size: 9px;
            font-weight: 700;
            min-width: 15px;
            height: 15px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            line-height: 1;
        }

        /* Hero Banner */
        .hero {
            position: relative;
            width: 100%;
            height: 180px;
            background: #111;
            overflow: hidden;
            display: flex;
            align-items: center;
        }
        @media (min-width: 768px) {
            .hero { height: 320px; }
        }
        @media (min-width: 1200px) {
            .hero { height: 420px; }
        }

        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.65;
            filter: contrast(1.1) brightness(0.9);
        }

        .hero-content {
            position: relative;
            z-index: 2;
            color: #fff;
            max-width: 680px;
            padding: 0 20px;
        }
        @media (min-width: 768px) {
            .hero-content { padding: 0 40px; }
        }

        .hero-tag {
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #d6b882;
            margin-bottom: 4px;
            display: inline-block;
        }
        @media (min-width: 768px) {
            .hero-tag { font-size: 11px; margin-bottom: 8px; }
        }

        .hero-title {
            font-family: var(--font-brand);
            font-size: 20px;
            font-weight: 600;
            line-height: 1.15;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 6px;
        }
        @media (min-width: 768px) {
            .hero-title { font-size: 38px; margin-bottom: 12px; }
        }

        .hero-desc {
            font-size: 11px;
            color: #e0deda;
            max-width: 480px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            margin-bottom: 12px;
        }
        @media (min-width: 768px) {
            .hero-desc { font-size: 14px; -webkit-line-clamp: 3; margin-bottom: 18px; }
        }

        .hero-btn {
            display: inline-block;
            background: #ffffff;
            color: #111111;
            padding: 6px 14px;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            transition: all 0.2s;
        }
        @media (min-width: 768px) {
            .hero-btn { padding: 10px 22px; font-size: 12px; }
        }
        .hero-btn:hover {
            background: #d6b882;
            color: #111;
        }

        /* Horizontal Category Rail */
        .category-rail-wrapper {
            background: #ffffff;
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 58px;
            z-index: 990;
        }
        @media (min-width: 992px) {
            .category-rail-wrapper { top: 74px; }
        }

        .category-rail {
            display: flex;
            align-items: center;
            gap: 8px;
            overflow-x: auto;
            white-space: nowrap;
            padding: 10px 16px;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }
        .category-rail::-webkit-scrollbar { display: none; }

        .cat-chip {
            background: #f5f4f0;
            border: 1px solid var(--border);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.5px;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.2s;
            flex-shrink: 0;
            text-transform: uppercase;
        }
        .cat-chip:hover, .cat-chip.active {
            background: var(--dark);
            color: #ffffff;
            border-color: var(--dark);
        }

        /* Filter & Search Bar */
        .filter-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 0 12px;
            gap: 12px;
            flex-wrap: wrap;
        }

        .search-box {
            position: relative;
            flex: 1;
            min-width: 200px;
            max-width: 380px;
        }
        .search-input {
            width: 100%;
            padding: 8px 12px 8px 34px;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            font-size: 12px;
            background: #ffffff;
            outline: none;
            transition: border-color 0.2s;
        }
        .search-input:focus {
            border-color: var(--dark);
        }
        .search-icon {
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            pointer-events: none;
            width: 14px;
            height: 14px;
        }

        .filter-controls {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .sort-select {
            padding: 8px 12px;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            font-size: 12px;
            font-weight: 500;
            background: #ffffff;
            color: var(--dark);
            outline: none;
            cursor: pointer;
        }

        .items-count {
            font-size: 11px;
            letter-spacing: 0.5px;
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
        }

        /* Product Grid */
        .products-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-bottom: 24px;
        }
        @media (min-width: 576px) {
            .products-grid { gap: 16px; }
        }
        @media (min-width: 768px) {
            .products-grid { grid-template-columns: repeat(3, 1fr); gap: 20px; }
        }
        @media (min-width: 1024px) {
            .products-grid { grid-template-columns: repeat(4, 1fr); gap: 24px; }
        }

        /* Product Card */
        .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: transform 0.2s, box-shadow 0.2s;
            position: relative;
        }
        .card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }

        .card-media {
            position: relative;
            width: 100%;
            padding-top: 133.33%; /* 3:4 aspect ratio */
            background: #f0eee9;
            overflow: hidden;
            cursor: pointer;
        }

        .card-img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }
        .card:hover .card-img {
            transform: scale(1.04);
        }

        .card-badge {
            position: absolute;
            top: 8px;
            left: 8px;
            background: rgba(18, 18, 18, 0.88);
            color: #ffffff;
            font-size: 8px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding: 3px 6px;
            border-radius: 2px;
            backdrop-filter: blur(4px);
            z-index: 2;
        }
        @media (min-width: 768px) {
            .card-badge { font-size: 9px; padding: 4px 8px; }
        }

        .wishlist-btn {
            position: absolute;
            top: 8px;
            right: 8px;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.9);
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 2;
            transition: all 0.2s;
            color: #444;
        }
        .wishlist-btn:hover {
            background: #ffffff;
            transform: scale(1.1);
            color: var(--danger);
        }
        .wishlist-btn.active {
            color: var(--danger);
            fill: var(--danger);
        }

        .quick-view-btn {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            background: rgba(17, 17, 17, 0.92);
            color: #ffffff;
            border: none;
            padding: 8px 0;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            cursor: pointer;
            opacity: 0;
            transform: translateY(100%);
            transition: all 0.25s ease;
            z-index: 3;
        }
        .card:hover .quick-view-btn {
            opacity: 1;
            transform: translateY(0);
        }
        @media (max-width: 768px) {
            /* On mobile, keep button accessible */
            .quick-view-btn { display: none; }
        }

        .card-body {
            padding: 10px 10px 12px;
            display: flex;
            flex-direction: column;
            flex: 1;
        }
        @media (min-width: 768px) {
            .card-body { padding: 14px 14px 16px; }
        }

        .card-brand {
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 1.2px;
            color: var(--accent);
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        @media (min-width: 768px) {
            .card-brand { font-size: 10px; }
        }

        .card-title {
            font-size: 12px;
            font-weight: 600;
            color: var(--dark);
            line-height: 1.35;
            margin-bottom: 6px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            height: 32px;
        }
        @media (min-width: 768px) {
            .card-title { font-size: 13px; height: 36px; }
        }

        .card-rating {
            display: flex;
            align-items: center;
            gap: 4px;
            font-size: 10px;
            color: var(--text-muted);
            margin-bottom: 6px;
        }
        .card-rating .stars {
            color: #e5a93b;
        }

        .card-price-row {
            display: flex;
            align-items: baseline;
            gap: 6px;
            margin-top: auto;
            flex-wrap: wrap;
        }
        .price-current {
            font-size: 14px;
            font-weight: 700;
            color: var(--dark);
        }
        @media (min-width: 768px) {
            .price-current { font-size: 16px; }
        }
        .price-orig {
            font-size: 11px;
            color: var(--text-muted);
            text-decoration: line-through;
        }
        .price-discount {
            font-size: 10px;
            font-weight: 700;
            color: var(--success);
        }

        .add-to-bag-card-btn {
            margin-top: 10px;
            width: 100%;
            background: #ffffff;
            border: 1px solid var(--dark);
            color: var(--dark);
            padding: 7px 0;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: all 0.2s;
        }
        .add-to-bag-card-btn:hover {
            background: var(--dark);
            color: #ffffff;
        }

        /* Pagination / Load More */
        .load-more-section {
            text-align: center;
            padding: 24px 0 40px;
        }
        .load-more-btn {
            background: var(--dark);
            color: #ffffff;
            border: none;
            padding: 12px 32px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: all 0.2s;
        }
        .load-more-btn:hover {
            background: var(--primary-hover);
            transform: translateY(-1px);
        }
        .load-more-info {
            margin-top: 10px;
            font-size: 11px;
            color: var(--text-muted);
            letter-spacing: 0.5px;
        }

        /* Mobile Bottom Nav */
        .mobile-bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: calc(var(--bottom-nav-height) + env(safe-area-inset-bottom, 0px));
            padding-bottom: env(safe-area-inset-bottom, 0px);
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-top: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-around;
            z-index: 1000;
        }
        @media (min-width: 992px) {
            .mobile-bottom-nav { display: none; }
        }

        .bottom-nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            font-size: 9px;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            background: none;
            border: none;
            padding: 6px 12px;
            position: relative;
            cursor: pointer;
            transition: color 0.2s;
        }
        .bottom-nav-item.active, .bottom-nav-item:hover {
            color: var(--dark);
        }
        .bottom-nav-item svg {
            width: 19px;
            height: 19px;
            margin-bottom: 2px;
        }

        /* Modal Base & Overlay */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.65);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            z-index: 2000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 16px;
            opacity: 0;
            transition: opacity 0.25s ease;
        }
        .modal-overlay.active {
            display: flex;
            opacity: 1;
        }

        .modal-card {
            background: #ffffff;
            border-radius: var(--radius-md);
            max-width: 480px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            box-shadow: var(--shadow-lg);
            animation: modalSlide 0.3s ease-out;
        }
        @keyframes modalSlide {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .modal-close-btn {
            position: absolute;
            top: 14px;
            right: 14px;
            background: none;
            border: none;
            font-size: 20px;
            color: var(--dark);
            cursor: pointer;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            transition: background 0.2s;
            z-index: 10;
        }
        .modal-close-btn:hover { background: #f0ede6; }

        /* Auth Tabs & Form */
        .auth-header {
            padding: 24px 24px 16px;
            text-align: center;
            border-bottom: 1px solid var(--border);
        }
        .auth-brand {
            font-family: var(--font-brand);
            font-size: 16px;
            letter-spacing: 2px;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .auth-subtitle {
            font-size: 11px;
            color: var(--text-muted);
            letter-spacing: 0.5px;
        }

        .auth-tabs {
            display: flex;
            border-bottom: 1px solid var(--border);
            background: #faf9f6;
        }
        .auth-tab {
            flex: 1;
            padding: 12px 0;
            text-align: center;
            background: none;
            border: none;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: var(--text-muted);
            cursor: pointer;
            border-bottom: 2px solid transparent;
            transition: all 0.2s;
        }
        .auth-tab.active {
            color: var(--dark);
            border-bottom-color: var(--dark);
            background: #ffffff;
        }

        .auth-body {
            padding: 24px;
        }

        .form-group {
            margin-bottom: 16px;
        }
        .form-label {
            display: block;
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.5px;
            color: var(--dark);
            margin-bottom: 6px;
            text-transform: uppercase;
        }
        .input-wrapper {
            position: relative;
            display: flex;
            align-items: center;
        }
        .phone-prefix {
            position: absolute;
            left: 12px;
            font-size: 13px;
            font-weight: 700;
            color: var(--dark);
            pointer-events: none;
        }
        .form-input {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            font-size: 13px;
            outline: none;
            transition: border-color 0.2s;
            background: #ffffff;
        }
        .form-input.has-prefix {
            padding-left: 48px;
        }
        .form-input:focus {
            border-color: var(--dark);
        }

        .pwd-toggle-btn {
            position: absolute;
            right: 10px;
            background: none;
            border: none;
            cursor: pointer;
            color: var(--text-muted);
            font-size: 11px;
            font-weight: 600;
            padding: 4px;
        }

        .auth-submit-btn {
            width: 100%;
            background: var(--dark);
            color: #ffffff;
            border: none;
            padding: 12px 0;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: background 0.2s;
            margin-top: 8px;
        }
        .auth-submit-btn:hover {
            background: var(--primary-hover);
        }

        .demo-credentials-box {
            margin-top: 18px;
            background: #fdfaf2;
            border: 1px dashed var(--accent);
            padding: 10px 12px;
            border-radius: var(--radius-sm);
            font-size: 11px;
            color: #5c441b;
            line-height: 1.4;
        }
        .demo-credentials-box strong { color: #2c200c; }

        /* Quick View Modal Card */
        .quick-view-card {
            max-width: 820px;
            width: 100%;
            display: grid;
            grid-template-columns: 1fr;
            overflow: hidden;
        }
        @media (min-width: 768px) {
            .quick-view-card { grid-template-columns: 1fr 1fr; }
        }

        .quick-view-gallery {
            position: relative;
            background: #f4f2ed;
            min-height: 320px;
        }
        .quick-view-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .quick-view-info {
            padding: 24px;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            max-height: 80vh;
        }
        .quick-brand {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: var(--accent);
            text-transform: uppercase;
            margin-bottom: 4px;
        }
        .quick-title {
            font-family: var(--font-serif);
            font-size: 20px;
            font-weight: 700;
            line-height: 1.3;
            color: var(--dark);
            margin-bottom: 8px;
        }
        .quick-price-box {
            display: flex;
            align-items: baseline;
            gap: 8px;
            margin-bottom: 16px;
        }
        .quick-cur-price {
            font-size: 20px;
            font-weight: 700;
            color: var(--dark);
        }
        .quick-orig-price {
            font-size: 13px;
            color: var(--text-muted);
            text-decoration: line-through;
        }
        .quick-discount-badge {
            font-size: 11px;
            font-weight: 700;
            color: var(--success);
            background: #e9f5ee;
            padding: 2px 6px;
            border-radius: 2px;
        }

        .size-selector-title {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        .size-pills {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 18px;
        }
        .size-pill {
            padding: 8px 14px;
            border: 1px solid var(--border);
            background: #ffffff;
            font-size: 11px;
            font-weight: 700;
            border-radius: 2px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .size-pill:hover, .size-pill.active {
            border-color: var(--dark);
            background: var(--dark);
            color: #ffffff;
        }

        .pincode-box {
            background: #fbfaf7;
            border: 1px solid var(--border);
            padding: 12px;
            border-radius: var(--radius-sm);
            margin-bottom: 18px;
        }
        .pincode-box-title {
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--dark);
            margin-bottom: 6px;
        }
        .pincode-input-row {
            display: flex;
            gap: 6px;
        }
        .pincode-input {
            flex: 1;
            padding: 7px 10px;
            border: 1px solid var(--border);
            font-size: 12px;
            border-radius: 2px;
            outline: none;
        }
        .pincode-check-btn {
            background: var(--dark);
            color: #ffffff;
            border: none;
            padding: 7px 12px;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            cursor: pointer;
            border-radius: 2px;
        }
        .pincode-result {
            font-size: 11px;
            margin-top: 6px;
            font-weight: 500;
            color: var(--success);
        }

        .quick-actions {
            display: flex;
            gap: 10px;
            margin-top: auto;
        }
        .quick-add-btn {
            flex: 1;
            background: var(--dark);
            color: #ffffff;
            border: none;
            padding: 12px 0;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: background 0.2s;
        }
        .quick-add-btn:hover { background: var(--primary-hover); }

        /* Slide-over Drawers (Bag & Account) */
        .drawer-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.55);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            z-index: 2500;
            display: none;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .drawer-overlay.active {
            display: block;
            opacity: 1;
        }

        .drawer {
            position: fixed;
            top: 0;
            right: 0;
            width: 100%;
            max-width: 420px;
            height: 100%;
            background: #ffffff;
            z-index: 2600;
            box-shadow: -4px 0 24px rgba(0, 0, 0, 0.15);
            display: flex;
            flex-direction: column;
            transform: translateX(100%);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .drawer.active {
            transform: translateX(0);
        }

        .drawer-header {
            padding: 16px 20px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .drawer-title {
            font-family: var(--font-brand);
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }
        .drawer-close {
            background: none;
            border: none;
            font-size: 22px;
            cursor: pointer;
            color: var(--dark);
        }

        .drawer-content {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
        }

        .bag-item {
            display: flex;
            gap: 12px;
            padding-bottom: 16px;
            margin-bottom: 16px;
            border-bottom: 1px solid var(--border);
        }
        .bag-item-img {
            width: 72px;
            height: 96px;
            object-fit: cover;
            border-radius: 2px;
            background: #f5f4f0;
        }
        .bag-item-details {
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        .bag-item-brand {
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 1px;
            color: var(--accent);
            text-transform: uppercase;
        }
        .bag-item-title {
            font-size: 12px;
            font-weight: 600;
            color: var(--dark);
            line-height: 1.3;
            margin-bottom: 4px;
        }
        .bag-item-meta {
            font-size: 11px;
            color: var(--text-muted);
            margin-bottom: 8px;
        }
        .bag-item-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: auto;
        }
        .qty-control {
            display: flex;
            align-items: center;
            border: 1px solid var(--border);
            border-radius: 2px;
        }
        .qty-btn {
            background: none;
            border: none;
            padding: 4px 8px;
            font-size: 12px;
            cursor: pointer;
        }
        .qty-num {
            font-size: 12px;
            font-weight: 600;
            padding: 0 4px;
        }

        .drawer-footer {
            padding: 16px 20px;
            border-top: 1px solid var(--border);
            background: #faf9f6;
        }
        .drawer-total-row {
            display: flex;
            justify-content: space-between;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 12px;
        }
        .checkout-btn {
            width: 100%;
            background: var(--dark);
            color: #ffffff;
            border: none;
            padding: 12px 0;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: background 0.2s;
        }
        .checkout-btn:hover { background: var(--primary-hover); }

        /* Toast Notifications */
        .toast {
            position: fixed;
            bottom: calc(var(--bottom-nav-height) + 20px);
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: rgba(17, 17, 17, 0.95);
            color: #ffffff;
            padding: 10px 20px;
            border-radius: 30px;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.5px;
            box-shadow: var(--shadow-lg);
            z-index: 3000;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s;
            opacity: 0;
            pointer-events: none;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        @media (min-width: 992px) {
            .toast { bottom: 30px; }
        }
        .toast.show {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }

        /* Footer */
        .footer {
            background: #111111;
            color: #b0aba4;
            padding: 48px 0 24px;
            font-size: 12px;
            border-top: 1px solid #222;
        }
        .footer-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 32px;
            margin-bottom: 40px;
        }
        @media (min-width: 768px) {
            .footer-grid { grid-template-columns: 2fr 1fr 1fr 1fr; }
        }
        .footer-brand {
            font-family: var(--font-brand);
            font-size: 18px;
            color: #ffffff;
            letter-spacing: 2px;
            margin-bottom: 12px;
        }
        .footer-desc {
            line-height: 1.6;
            max-width: 320px;
            font-size: 12px;
        }
        .footer-col-title {
            color: #ffffff;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 14px;
        }
        .footer-links {
            list-style: none;
        }
        .footer-links li {
            margin-bottom: 8px;
        }
        .footer-links a:hover {
            color: #ffffff;
        }
        .footer-bottom {
            text-align: center;
            border-top: 1px solid #222;
            padding-top: 24px;
            font-size: 11px;
            color: #777;
        }
    </style>
</head>
<body>

    <!-- Top Announcement Bar -->
    <div class="top-banner">
        Complimentary White-Glove Delivery on Orders Over ₹2,500 &bull; 100% Verified Luxury Atelier
    </div>

    <!-- Header Navigation -->
    <header class="header">
        <div class="container header-inner">
            <a href="#" class="logo" onclick="setCategoryFilter('ALL'); return false;">
                TRENDVIBE <span>Atelier</span>
            </a>

            <ul class="desktop-nav">
                <li><a href="#" class="nav-link active" onclick="setCategoryFilter('ALL'); return false;">All Pieces</a></li>
                <li><a href="#" class="nav-link" onclick="setCategoryFilter('Men'); return false;">Men</a></li>
                <li><a href="#" class="nav-link" onclick="setCategoryFilter('Women'); return false;">Women</a></li>
                <li><a href="#" class="nav-link" onclick="setCategoryFilter('Beauty'); return false;">Clean Beauty</a></li>
                <li><a href="#" class="nav-link" onclick="setCategoryFilter('Footwear'); return false;">Footwear</a></li>
                <li><a href="#" class="nav-link" onclick="setCategoryFilter('Watches'); return false;">Watches &amp; Luxury</a></li>
            </ul>

            <div class="header-actions">
                <!-- User Account Profile Button -->
                <div id="userProfileBtnContainer">
                    <button class="action-btn" onclick="openAuthOrAccount()" title="Account / Sign In">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                    </button>
                </div>

                <!-- Wishlist Button -->
                <button class="action-btn" onclick="showToast('Viewing your luxury wishlist')" title="Wishlist">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                    </svg>
                    <span class="badge-count" id="wishlistCount">0</span>
                </button>

                <!-- Shopping Bag Button -->
                <button class="action-btn" onclick="openBagDrawer()" title="Shopping Bag">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-7z"></path>
                        <line x1="3" y1="6" x2="21" y2="6"></line>
                        <path d="M16 10a4 4 0 0 1-8 0"></path>
                    </svg>
                    <span class="badge-count" id="bagCount">0</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Hero Banner -->
    <section class="hero">
        <img class="hero-bg" src="https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=1600&q=85" alt="TrendVibe Runway" onerror="handleImageFallback(this, 'default')">
        <div class="container">
            <div class="hero-content">
                <span class="hero-tag">Autumn / Winter Atelier</span>
                <h1 class="hero-title">Haute Couture &amp; Modern Minimalism</h1>
                <p class="hero-desc">Over 530 curated masterworks in Italian tailoring, pure silks, clean botanical beauty, and horology.</p>
                <a href="#catalogSection" class="hero-btn">Explore Collection</a>
            </div>
        </div>
    </section>

    <!-- Sticky Horizontal Category Filter Rail -->
    <div class="category-rail-wrapper">
        <div class="container">
            <div class="category-rail" id="categoryRail">
                <button class="cat-chip active" onclick="setCategoryFilter('ALL')">All (535)</button>
                <button class="cat-chip" onclick="setCategoryFilter('Shirts')">Tailored Shirts</button>
                <button class="cat-chip" onclick="setCategoryFilter('Pants')">Denim &amp; Trousers</button>
                <button class="cat-chip" onclick="setCategoryFilter('Dresses')">Silks &amp; Dresses</button>
                <button class="cat-chip" onclick="setCategoryFilter('Beauty')">Clean Beauty &amp; Scents</button>
                <button class="cat-chip" onclick="setCategoryFilter('Footwear')">Artisanal Footwear</button>
                <button class="cat-chip" onclick="setCategoryFilter('Watches')">Watches &amp; Accessories</button>
            </div>
        </div>
    </div>

    <!-- Main Content Area -->
    <main class="container" id="catalogSection">
        <!-- Filter and Search Bar -->
        <div class="filter-bar">
            <div class="search-box">
                <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" class="search-input" id="searchInput" placeholder="Search by name, fabric, brand..." oninput="handleSearch(this.value)">
            </div>

            <div class="filter-controls">
                <span class="items-count" id="displayedCountText">535 Pieces Available</span>
                <select class="sort-select" id="sortSelect" onchange="handleSort(this.value)">
                    <option value="featured">Curated &bull; Featured</option>
                    <option value="price-asc">Price: Low to High</option>
                    <option value="price-desc">Price: High to Low</option>
                    <option value="rating">Top Rated (4.5+)</option>
                    <option value="discount">Highest Discount</option>
                </select>
            </div>
        </div>

        <!-- Product Grid -->
        <div class="products-grid" id="productsGrid">
            <!-- Rendered by JS -->
        </div>

        <!-- Load More Section -->
        <div class="load-more-section" id="loadMoreContainer">
            <button class="load-more-btn" onclick="loadMoreProducts()">Show More Pieces</button>
            <div class="load-more-info" id="loadMoreInfo">Showing 24 of 535 pieces</div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <div class="footer-brand">TRENDVIBE ATELIER</div>
                    <p class="footer-desc">Curating high-craft contemporary fashion, artisanal footwear, and clean botanical fragrances with certified luxury standards.</p>
                </div>
                <div>
                    <h4 class="footer-col-title">Atelier Edits</h4>
                    <ul class="footer-links">
                        <li><a href="#" onclick="setCategoryFilter('Men'); return false;">Men's Runway</a></li>
                        <li><a href="#" onclick="setCategoryFilter('Women'); return false;">Women's Couture</a></li>
                        <li><a href="#" onclick="setCategoryFilter('Beauty'); return false;">Clean Fragrances</a></li>
                        <li><a href="#" onclick="setCategoryFilter('Footwear'); return false;">Leather Footwear</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="footer-col-title">Client Care</h4>
                    <ul class="footer-links">
                        <li><a href="#" onclick="showToast('White-glove delivery tracking'); return false;">Order Tracking</a></li>
                        <li><a href="#" onclick="showToast('Returns: 14 days complimentary'); return false;">Returns Policy</a></li>
                        <li><a href="#" onclick="showToast('Certificate of authenticity included'); return false;">Authenticity Guarantee</a></li>
                        <li><a href="#" onclick="openAuthOrAccount(); return false;">Customer Account</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="footer-col-title">Customer Concierge</h4>
                    <p class="footer-desc" style="margin-bottom: 8px;">Direct client advisor available 7 days a week.</p>
                    <p style="color: #fff; font-weight: 600;">concierge@trendvibe.com</p>
                    <p style="color: #d6cfc7; font-size: 11px; margin-top: 4px;">+91 (080) 4123-LUXE</p>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; 2026 TrendVibe Atelier Inc. All rights reserved. Built for High-Performance Enterprise Commerce.
            </div>
        </div>
    </footer>

    <!-- Mobile Bottom Navigation Bar -->
    <nav class="mobile-bottom-nav">
        <button class="bottom-nav-item active" onclick="setCategoryFilter('ALL')">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
            <span>Shop</span>
        </button>
        <button class="bottom-nav-item" onclick="document.getElementById('categoryRail').scrollIntoView({behavior: 'smooth'})">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="7" height="7"></rect>
                <rect x="14" y="3" width="7" height="7"></rect>
                <rect x="14" y="14" width="7" height="7"></rect>
                <rect x="3" y="14" width="7" height="7"></rect>
            </svg>
            <span>Categories</span>
        </button>
        <button class="bottom-nav-item" onclick="showToast('Opening Wishlist')">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
            </svg>
            <span>Wishlist</span>
        </button>
        <button class="bottom-nav-item" onclick="openBagDrawer()">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-7z"></path>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <path d="M16 10a4 4 0 0 1-8 0"></path>
            </svg>
            <span>Bag (<span id="mobileBagCount">0</span>)</span>
        </button>
        <button class="bottom-nav-item" onclick="openAuthOrAccount()">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <span>Account</span>
        </button>
    </nav>

    <!-- Quick View Modal -->
    <div class="modal-overlay" id="quickViewModal">
        <div class="modal-card quick-view-card">
            <button class="modal-close-btn" onclick="closeModal('quickViewModal')">&times;</button>
            <div class="quick-view-gallery">
                <img id="quickViewImg" class="quick-view-img" src="" alt="Product Photo" onerror="handleImageFallback(this, 'default')">
            </div>
            <div class="quick-view-info">
                <span class="quick-brand" id="quickViewBrand">BRAND</span>
                <h2 class="quick-title" id="quickViewTitle">Product Title</h2>
                <div class="card-rating" style="margin-bottom: 12px;">
                    <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
                    <span id="quickViewRating">4.8 (120 reviews)</span>
                </div>
                <div class="quick-price-box">
                    <span class="quick-cur-price" id="quickViewPrice">₹2,499</span>
                    <span class="quick-orig-price" id="quickViewOrigPrice">₹4,999</span>
                    <span class="quick-discount-badge" id="quickViewDiscount">50% OFF</span>
                </div>

                <div class="size-selector-title">Select Size / Fit:</div>
                <div class="size-pills" id="quickViewSizes">
                    <!-- Sizes injected by JS -->
                </div>

                <div class="pincode-box">
                    <div class="pincode-box-title">Delivery &amp; Serviceability Checker</div>
                    <div class="pincode-input-row">
                        <input type="text" id="quickPincodeInput" class="pincode-input" placeholder="Enter 6-digit Pincode" maxlength="6">
                        <button class="pincode-check-btn" onclick="checkPincodeDelivery()">Check</button>
                    </div>
                    <div class="pincode-result" id="quickPincodeResult"></div>
                </div>

                <p id="quickViewDesc" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 20px;">
                    Description
                </p>

                <div class="quick-actions">
                    <button class="quick-add-btn" id="quickAddBagBtn" onclick="addCurrentQuickViewToBag()">Add to Bag</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Phone Number + Password Authentication Modal (OTP Completely Removed) -->
    <div class="modal-overlay" id="authModal">
        <div class="modal-card">
            <button class="modal-close-btn" onclick="closeModal('authModal')">&times;</button>
            <div class="auth-header">
                <div class="auth-brand">TRENDVIBE ATELIER</div>
                <div class="auth-subtitle">Customer Portal &bull; Phone &amp; Password Access</div>
            </div>

            <!-- Tabs: Sign In / Create Account -->
            <div class="auth-tabs">
                <button class="auth-tab active" id="tabSignIn" onclick="switchAuthTab('signin')">Sign In</button>
                <button class="auth-tab" id="tabSignUp" onclick="switchAuthTab('signup')">Create Account</button>
            </div>

            <!-- Sign In Form -->
            <div class="auth-body" id="signInFormSection">
                <form id="signInForm" onsubmit="handleCustomerSignIn(event)">
                    <div class="form-group">
                        <label class="form-label">Customer Mobile Number</label>
                        <div class="input-wrapper">
                            <span class="phone-prefix">+91</span>
                            <input type="tel" id="loginPhone" class="form-input has-prefix" placeholder="9876543210" maxlength="10" required pattern="[0-9]{10}">
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Password</label>
                        <div class="input-wrapper">
                            <input type="password" id="loginPassword" class="form-input" placeholder="Enter your password" required>
                            <button type="button" class="pwd-toggle-btn" onclick="togglePasswordVisibility('loginPassword', this)">SHOW</button>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; font-size: 11px;">
                        <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                            <input type="checkbox" checked> Remember this device
                        </label>
                        <a href="#" style="color: var(--accent); font-weight: 600;" onclick="showToast('Password reset link sent to registered mobile'); return false;">Forgot?</a>
                    </div>

                    <button type="submit" class="auth-submit-btn">Sign In to Atelier</button>

                    <div class="demo-credentials-box">
                        <strong>Test Credentials:</strong><br>
                        Phone: <code>9876543210</code> &bull; Password: <code>password123</code><br>
                        <small>Or enter any phone number &amp; password in "Create Account" tab.</small>
                    </div>
                </form>
            </div>

            <!-- Create Account / Sign Up Form -->
            <div class="auth-body" id="signUpFormSection" style="display: none;">
                <form id="signUpForm" onsubmit="handleCustomerSignUp(event)">
                    <div class="form-group">
                        <label class="form-label">Full Name</label>
                        <input type="text" id="regName" class="form-input" placeholder="e.g. Rahul Sharma" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Mobile Number</label>
                        <div class="input-wrapper">
                            <span class="phone-prefix">+91</span>
                            <input type="tel" id="regPhone" class="form-input has-prefix" placeholder="9876543210" maxlength="10" required pattern="[0-9]{10}">
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Email Address</label>
                        <input type="email" id="regEmail" class="form-input" placeholder="name@domain.com" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Delivery Pincode</label>
                        <input type="text" id="regPincode" class="form-input" placeholder="6-digit pincode e.g. 110001" maxlength="6" required pattern="[0-9]{6}">
                    </div>

                    <div class="form-group">
                        <label class="form-label">Create Password</label>
                        <div class="input-wrapper">
                            <input type="password" id="regPassword" class="form-input" placeholder="Minimum 6 characters" minlength="6" required>
                            <button type="button" class="pwd-toggle-btn" onclick="togglePasswordVisibility('regPassword', this)">SHOW</button>
                        </div>
                    </div>

                    <button type="submit" class="auth-submit-btn">Create Atelier Account</button>
                </form>
            </div>
        </div>
    </div>

    <!-- Account Details Drawer -->
    <div class="drawer-overlay" id="accountDrawerOverlay" onclick="closeDrawer('accountDrawer')"></div>
    <div class="drawer" id="accountDrawer">
        <div class="drawer-header">
            <div class="drawer-title">CUSTOMER PROFILE</div>
            <button class="drawer-close" onclick="closeDrawer('accountDrawer')">&times;</button>
        </div>
        <div class="drawer-content" id="accountDrawerContent">
            <!-- Injected by JS -->
        </div>
    </div>

    <!-- Shopping Bag Drawer -->
    <div class="drawer-overlay" id="bagDrawerOverlay" onclick="closeDrawer('bagDrawer')"></div>
    <div class="drawer" id="bagDrawer">
        <div class="drawer-header">
            <div class="drawer-title">YOUR ATELIER BAG (<span id="drawerBagCount">0</span>)</div>
            <button class="drawer-close" onclick="closeDrawer('bagDrawer')">&times;</button>
        </div>
        <div class="drawer-content" id="bagDrawerItems">
            <!-- Bag items injected by JS -->
        </div>
        <div class="drawer-footer" id="bagDrawerFooter">
            <div class="drawer-total-row">
                <span>Estimated Subtotal</span>
                <span id="bagSubtotal">₹0</span>
            </div>
            <div style="font-size: 11px; color: var(--success); margin-bottom: 12px; font-weight: 600;">
                &#10003; Complimentary Express Delivery &amp; Luxury Packaging
            </div>
            <button class="checkout-btn" onclick="openCheckoutModal()">Proceed to Checkout</button>
        </div>
    </div>

    <!-- Checkout Modal -->
    <div class="modal-overlay" id="checkoutModal">
        <div class="modal-card">
            <button class="modal-close-btn" onclick="closeModal('checkoutModal')">&times;</button>
            <div class="auth-header">
                <div class="auth-brand">TRENDVIBE ATELIER</div>
                <div class="auth-subtitle">Secure Express Checkout</div>
            </div>
            <div class="auth-body">
                <div id="checkoutAuthNotice" style="background: #fdfaf2; padding: 10px; border-radius: 4px; font-size: 11px; margin-bottom: 14px; border: 1px solid #ebd5b3;">
                    <!-- Injected by JS -->
                </div>

                <form onsubmit="handlePlaceOrder(event)">
                    <div class="form-group">
                        <label class="form-label">Full Name</label>
                        <input type="text" id="checkoutName" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Phone Number</label>
                        <input type="tel" id="checkoutPhone" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Delivery Street Address</label>
                        <input type="text" id="checkoutAddress" class="form-input" placeholder="Flat, Apartment, Street" required>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div class="form-group">
                            <label class="form-label">Pincode</label>
                            <input type="text" id="checkoutPincode" class="form-input" maxlength="6" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">City</label>
                            <input type="text" id="checkoutCity" class="form-input" placeholder="New Delhi" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Payment Mode</label>
                        <select id="checkoutPayment" class="form-input">
                            <option value="upi">UPI (GPay / PhonePe / Paytm Instant QR)</option>
                            <option value="card">Credit / Debit Card (Visa, Mastercard, Amex)</option>
                            <option value="netbanking">Net Banking (HDFC, ICICI, SBI, Axis)</option>
                            <option value="cod">Cash on Delivery (Verified Signature)</option>
                        </select>
                    </div>

                    <div style="background: #f9f9f9; padding: 12px; border-radius: 4px; margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 700;">
                            <span>Total Payable Amount</span>
                            <span id="checkoutTotalAmount">₹0</span>
                        </div>
                    </div>

                    <button type="submit" class="auth-submit-btn">Place Confirmed Order</button>
                </form>
            </div>
        </div>
    </div>

    <!-- Toast Notification -->
    <div class="toast" id="toastNotification">
        <span id="toastMessage">Item added</span>
    </div>

    <!-- Application JavaScript -->
    <script>
        // =========================================================================
        // 1. DATASET & CONSTANTS
        // =========================================================================
        const ALL_PRODUCTS = PRODUCTS_DATA_PLACEHOLDER;

        // Rock-Solid High-Res Category Fallbacks (Guaranteed 200 OK)
        const CATEGORY_FALLBACKS = {
            'Shirts': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=1000&q=85',
            'Pants': 'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=1000&q=85',
            'Dresses': 'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=1000&q=85',
            'Beauty': 'https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?auto=format&fit=crop&w=1000&q=85',
            'Footwear': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=1000&q=85',
            'Watches': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=1000&q=85',
            'default': 'https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=1000&q=85'
        };

        function handleImageFallback(img, category) {
            img.onerror = null; // Prevent loop
            img.src = CATEGORY_FALLBACKS[category] || CATEGORY_FALLBACKS['default'];
        }

        // State
        let currentFilter = 'ALL';
        let searchQuery = '';
        let currentSort = 'featured';
        let displayedCount = 24;
        const BATCH_SIZE = 24;

        let filteredProducts = [...ALL_PRODUCTS];
        let bagItems = JSON.parse(localStorage.getItem('trendvibe_bag') || '[]');
        let wishlistItems = JSON.parse(localStorage.getItem('trendvibe_wishlist') || '[]');
        let activeQuickViewProduct = null;
        let selectedQuickViewSize = null;

        // Preload default registered users in LocalStorage
        function initUsersDb() {
            if (!localStorage.getItem('trendvibe_users_db')) {
                const defaultUsers = [
                    {
                        phone: '9876543210',
                        password: 'password123',
                        name: 'Indranil Mukherjee',
                        email: 'indranil@trendvibe.com',
                        pincode: '110001',
                        city: 'New Delhi'
                    },
                    {
                        phone: '9123456789',
                        password: 'password123',
                        name: 'Ananya Sharma',
                        email: 'ananya@trendvibe.com',
                        pincode: '400001',
                        city: 'Mumbai'
                    }
                ];
                localStorage.setItem('trendvibe_users_db', JSON.stringify(defaultUsers));
            }
        }

        function getCurrentUser() {
            try {
                return JSON.parse(localStorage.getItem('trendvibe_user_session'));
            } catch (e) {
                return null;
            }
        }

        // =========================================================================
        // 2. INITIALIZATION
        // =========================================================================
        document.addEventListener('DOMContentLoaded', () => {
            initUsersDb();
            updateAuthHeader();
            updateBadges();
            applyFiltersAndRender();
        });

        // =========================================================================
        // 3. FILTERING, SEARCH & SORTING
        // =========================================================================
        function setCategoryFilter(category) {
            currentFilter = category;
            displayedCount = BATCH_SIZE;

            // Update desktop nav active state
            document.querySelectorAll('.desktop-nav .nav-link').forEach(link => {
                link.classList.remove('active');
            });

            // Update category chips active state
            document.querySelectorAll('.cat-chip').forEach(chip => {
                chip.classList.remove('active');
                if (chip.textContent.toUpperCase().includes(category.toUpperCase()) || (category === 'ALL' && chip.textContent.includes('All'))) {
                    chip.classList.add('active');
                }
            });

            applyFiltersAndRender();
        }

        function handleSearch(val) {
            searchQuery = val.trim().toLowerCase();
            displayedCount = BATCH_SIZE;
            applyFiltersAndRender();
        }

        function handleSort(val) {
            currentSort = val;
            applyFiltersAndRender();
        }

        function applyFiltersAndRender() {
            filteredProducts = ALL_PRODUCTS.filter(p => {
                // Category filter
                let matchesCategory = true;
                if (currentFilter === 'ALL') {
                    matchesCategory = true;
                } else if (currentFilter === 'Men') {
                    matchesCategory = p.gender === 'Men' || p.category === 'Shirts' || p.category === 'Pants';
                } else if (currentFilter === 'Women') {
                    matchesCategory = p.gender === 'Women' || p.category === 'Dresses';
                } else {
                    matchesCategory = p.category === currentFilter;
                }

                // Search query
                let matchesSearch = true;
                if (searchQuery) {
                    const text = `${p.name} ${p.brand} ${p.category} ${p.description}`.toLowerCase();
                    matchesSearch = text.includes(searchQuery);
                }

                return matchesCategory && matchesSearch;
            });

            // Sorting
            if (currentSort === 'price-asc') {
                filteredProducts.sort((a, b) => a.price - b.price);
            } else if (currentSort === 'price-desc') {
                filteredProducts.sort((a, b) => b.price - a.price);
            } else if (currentSort === 'rating') {
                filteredProducts.sort((a, b) => b.rating - a.rating);
            } else if (currentSort === 'discount') {
                filteredProducts.sort((a, b) => b.discountPercent - a.discountPercent);
            } else {
                // featured: stable default order
                filteredProducts.sort((a, b) => a.id - b.id);
            }

            renderProducts();
        }

        function renderProducts() {
            const grid = document.getElementById('productsGrid');
            const toShow = filteredProducts.slice(0, displayedCount);

            if (toShow.length === 0) {
                grid.innerHTML = `
                    <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px;">
                        <h3 style="font-family: var(--font-brand); font-size: 18px; margin-bottom: 8px;">NO PIECES FOUND</h3>
                        <p style="color: var(--text-muted); font-size: 13px;">Try clearing filters or search keywords.</p>
                        <button onclick="setCategoryFilter('ALL'); document.getElementById('searchInput').value='';" class="load-more-btn" style="margin-top: 16px;">Reset Search</button>
                    </div>
                `;
                document.getElementById('loadMoreContainer').style.display = 'none';
                document.getElementById('displayedCountText').textContent = `0 Pieces Available`;
                return;
            }

            let html = '';
            toShow.forEach(p => {
                const isWishlisted = wishlistItems.some(item => item.id === p.id);
                html += `
                    <div class="card">
                        <div class="card-media" onclick="openQuickView(${p.id})">
                            <span class="card-badge">${p.badge}</span>
                            <button class="wishlist-btn ${isWishlisted ? 'active' : ''}" onclick="toggleWishlist(${p.id}, event)" title="Wishlist">
                                <svg width="15" height="15" viewBox="0 0 24 24" fill="${isWishlisted ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
                                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                                </svg>
                            </button>
                            <img class="card-img" 
                                 src="${p.imageUrl}" 
                                 alt="${p.name}" 
                                 loading="lazy" 
                                 onerror="handleImageFallback(this, '${p.category}')">
                            <button class="quick-view-btn" onclick="openQuickView(${p.id}); event.stopPropagation();">Quick View</button>
                        </div>
                        <div class="card-body">
                            <span class="card-brand">${p.brand}</span>
                            <h3 class="card-title" title="${p.name}">${p.name}</h3>
                            <div class="card-rating">
                                <span class="stars">&#9733;</span>
                                <span>${p.rating} (${p.reviewsCount})</span>
                            </div>
                            <div class="card-price-row">
                                <span class="price-current">&#8377;${p.price.toLocaleString('en-IN')}</span>
                                <span class="price-orig">&#8377;${p.originalPrice.toLocaleString('en-IN')}</span>
                                <span class="price-discount">${p.discountPercent}% OFF</span>
                            </div>
                            <button class="add-to-bag-card-btn" onclick="directAddBag(${p.id})">+ Quick Add &bull; &#8377;${p.price.toLocaleString('en-IN')}</button>
                        </div>
                    </div>
                `;
            });

            grid.innerHTML = html;

            // Update Counter & Load More
            document.getElementById('displayedCountText').textContent = `${filteredProducts.length} Pieces Available`;
            const loadMoreContainer = document.getElementById('loadMoreContainer');
            if (displayedCount >= filteredProducts.length) {
                loadMoreContainer.style.display = 'none';
            } else {
                loadMoreContainer.style.display = 'block';
                document.getElementById('loadMoreInfo').textContent = `Showing ${toShow.length} of ${filteredProducts.length} pieces`;
            }
        }

        function loadMoreProducts() {
            displayedCount += BATCH_SIZE;
            renderProducts();
        }

        // =========================================================================
        // 4. QUICK VIEW MODAL & PINCODE CHECKER
        // =========================================================================
        function openQuickView(id) {
            const p = ALL_PRODUCTS.find(item => item.id === id);
            if (!p) return;

            activeQuickViewProduct = p;
            document.getElementById('quickViewBrand').textContent = p.brand;
            document.getElementById('quickViewTitle').textContent = p.name;
            document.getElementById('quickViewPrice').textContent = `₹${p.price.toLocaleString('en-IN')}`;
            document.getElementById('quickViewOrigPrice').textContent = `₹${p.originalPrice.toLocaleString('en-IN')}`;
            document.getElementById('quickViewDiscount').textContent = `${p.discountPercent}% OFF`;
            document.getElementById('quickViewRating').textContent = `${p.rating} (${p.reviewsCount} verified reviews)`;
            document.getElementById('quickViewDesc').textContent = p.description;
            
            const img = document.getElementById('quickViewImg');
            img.src = p.imageUrl;
            img.onerror = () => handleImageFallback(img, p.category);

            // Render sizes
            const sizesContainer = document.getElementById('quickViewSizes');
            selectedQuickViewSize = p.sizes[0];
            let sizesHtml = '';
            p.sizes.forEach((s, idx) => {
                sizesHtml += `
                    <button class="size-pill ${idx === 0 ? 'active' : ''}" onclick="selectQuickSize('${s}', this)">${s}</button>
                `;
            });
            sizesContainer.innerHTML = sizesHtml;

            // Reset pincode check
            document.getElementById('quickPincodeInput').value = '';
            document.getElementById('quickPincodeResult').textContent = '';

            openModal('quickViewModal');
        }

        function selectQuickSize(size, btn) {
            selectedQuickViewSize = size;
            document.querySelectorAll('#quickViewSizes .size-pill').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        }

        function checkPincodeDelivery() {
            const pin = document.getElementById('quickPincodeInput').value.trim();
            const res = document.getElementById('quickPincodeResult');
            if (pin.length !== 6 || !/^\d+$/.test(pin)) {
                res.textContent = 'Please enter a valid 6-digit Indian pincode.';
                res.style.color = 'var(--danger)';
                return;
            }
            const date = new Date();
            date.setDate(date.getDate() + 3);
            const options = { weekday: 'short', month: 'short', day: 'numeric' };
            res.textContent = `✓ Standard Delivery by ${date.toLocaleDateString('en-IN', options)} to ${pin}. Express 24h dispatch verified.`;
            res.style.color = 'var(--success)';
        }

        function addCurrentQuickViewToBag() {
            if (!activeQuickViewProduct) return;
            addToBag(activeQuickViewProduct, selectedQuickViewSize);
            closeModal('quickViewModal');
        }

        function directAddBag(id) {
            const p = ALL_PRODUCTS.find(item => item.id === id);
            if (!p) return;
            addToBag(p, p.sizes[0]);
        }

        // =========================================================================
        // 5. PHONE + PASSWORD AUTHENTICATION (OTP Completely Removed)
        // =========================================================================
        function updateAuthHeader() {
            const user = getCurrentUser();
            const container = document.getElementById('userProfileBtnContainer');
            if (user) {
                const firstName = user.name.split(' ')[0];
                container.innerHTML = `
                    <button class="user-greeting-btn" onclick="openAccountDrawer()">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                        <span>Hi, ${firstName}</span>
                    </button>
                `;
            } else {
                container.innerHTML = `
                    <button class="action-btn" onclick="openAuthModal()" title="Sign In with Phone & Password">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                    </button>
                `;
            }
        }

        function openAuthOrAccount() {
            if (getCurrentUser()) {
                openAccountDrawer();
            } else {
                openAuthModal();
            }
        }

        function openAuthModal() {
            switchAuthTab('signin');
            openModal('authModal');
        }

        function switchAuthTab(tab) {
            const tabIn = document.getElementById('tabSignIn');
            const tabUp = document.getElementById('tabSignUp');
            const secIn = document.getElementById('signInFormSection');
            const secUp = document.getElementById('signUpFormSection');

            if (tab === 'signin') {
                tabIn.classList.add('active');
                tabUp.classList.remove('active');
                secIn.style.display = 'block';
                secUp.style.display = 'none';
            } else {
                tabUp.classList.add('active');
                tabIn.classList.remove('active');
                secUp.style.display = 'block';
                secIn.style.display = 'none';
            }
        }

        function togglePasswordVisibility(inputId, btn) {
            const input = document.getElementById(inputId);
            if (input.type === 'password') {
                input.type = 'text';
                btn.textContent = 'HIDE';
            } else {
                input.type = 'password';
                btn.textContent = 'SHOW';
            }
        }

        function handleCustomerSignIn(e) {
            e.preventDefault();
            const phone = document.getElementById('loginPhone').value.trim();
            const password = document.getElementById('loginPassword').value.trim();

            const users = JSON.parse(localStorage.getItem('trendvibe_users_db') || '[]');
            const matched = users.find(u => u.phone === phone && u.password === password);

            if (matched) {
                // Successful Sign In
                localStorage.setItem('trendvibe_user_session', JSON.stringify(matched));
                closeModal('authModal');
                updateAuthHeader();
                showToast(`Welcome back, ${matched.name}!`);
            } else {
                // Check if phone exists but password wrong
                const userExists = users.find(u => u.phone === phone);
                if (userExists) {
                    alert('Incorrect password for this mobile number. Please try again or test with password: password123');
                } else {
                    // Offer to auto-register or check
                    if (confirm(`No account found for +91 ${phone}. Would you like to create an account now?`)) {
                        switchAuthTab('signup');
                        document.getElementById('regPhone').value = phone;
                    }
                }
            }
        }

        function handleCustomerSignUp(e) {
            e.preventDefault();
            const name = document.getElementById('regName').value.trim();
            const phone = document.getElementById('regPhone').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const pincode = document.getElementById('regPincode').value.trim();
            const password = document.getElementById('regPassword').value.trim();

            const users = JSON.parse(localStorage.getItem('trendvibe_users_db') || '[]');
            if (users.some(u => u.phone === phone)) {
                alert('An account with this phone number already exists. Please Sign In.');
                switchAuthTab('signin');
                document.getElementById('loginPhone').value = phone;
                return;
            }

            const newUser = {
                name,
                phone,
                email,
                pincode,
                city: 'Delivery Hub',
                password
            };

            users.push(newUser);
            localStorage.setItem('trendvibe_users_db', JSON.stringify(users));
            localStorage.setItem('trendvibe_user_session', JSON.stringify(newUser));

            closeModal('authModal');
            updateAuthHeader();
            showToast(`Account created successfully! Welcome, ${name}.`);
        }

        function openAccountDrawer() {
            const user = getCurrentUser();
            if (!user) {
                openAuthModal();
                return;
            }

            const orders = JSON.parse(localStorage.getItem('trendvibe_orders') || '[]');
            const container = document.getElementById('accountDrawerContent');

            let ordersHtml = '';
            if (orders.length === 0) {
                ordersHtml = '<p style="font-size: 12px; color: var(--text-muted); padding: 12px 0;">No past orders yet. Discover our runway collection.</p>';
            } else {
                orders.forEach(o => {
                    ordersHtml += `
                        <div style="background: #faf9f6; border: 1px solid var(--border); border-radius: 4px; padding: 12px; margin-bottom: 12px;">
                            <div style="display: flex; justify-content: space-between; font-size: 11px; font-weight: 700; margin-bottom: 6px;">
                                <span>ORDER #${o.orderId}</span>
                                <span style="color: var(--success);">${o.status}</span>
                            </div>
                            <div style="font-size: 11px; color: var(--text-muted); margin-bottom: 6px;">${o.date} &bull; ${o.itemsCount} items</div>
                            <div style="font-size: 13px; font-weight: 700;">₹${o.total.toLocaleString('en-IN')}</div>
                        </div>
                    `;
                });
            }

            container.innerHTML = `
                <div style="text-align: center; padding-bottom: 20px; border-bottom: 1px solid var(--border); margin-bottom: 20px;">
                    <div style="width: 56px; height: 56px; background: #f0ece3; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 20px; font-weight: 700; color: var(--dark);">
                        ${user.name.charAt(0)}
                    </div>
                    <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 2px;">${user.name}</h3>
                    <p style="font-size: 12px; color: var(--text-muted);">+91 ${user.phone}</p>
                    <p style="font-size: 12px; color: var(--text-muted);">${user.email}</p>
                    <p style="font-size: 11px; color: var(--accent); margin-top: 4px; font-weight: 600;">Saved Pincode: ${user.pincode}</p>
                </div>

                <div style="margin-bottom: 24px;">
                    <h4 style="font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 12px;">Order History</h4>
                    ${ordersHtml}
                </div>

                <button onclick="handleCustomerSignOut()" class="auth-submit-btn" style="background: #9c2e2e;">Sign Out from Atelier</button>
            `;

            openDrawer('accountDrawer');
        }

        function handleCustomerSignOut() {
            localStorage.removeItem('trendvibe_user_session');
            closeDrawer('accountDrawer');
            updateAuthHeader();
            showToast('You have signed out successfully.');
        }

        // =========================================================================
        // 6. BAG & WISHLIST MANAGEMENT
        // =========================================================================
        function addToBag(product, size) {
            const existing = bagItems.find(item => item.id === product.id && item.size === size);
            if (existing) {
                existing.quantity += 1;
            } else {
                bagItems.push({
                    id: product.id,
                    name: product.name,
                    brand: product.brand,
                    price: product.price,
                    imageUrl: product.imageUrl,
                    category: product.category,
                    size: size || 'Standard',
                    quantity: 1
                });
            }
            saveBag();
            showToast(`Added: ${product.name} (${size || 'Standard'})`);
        }

        function saveBag() {
            localStorage.setItem('trendvibe_bag', JSON.stringify(bagItems));
            updateBadges();
            renderBagDrawer();
        }

        function toggleWishlist(id, e) {
            e.stopPropagation();
            const p = ALL_PRODUCTS.find(item => item.id === id);
            if (!p) return;

            const idx = wishlistItems.findIndex(item => item.id === id);
            if (idx > -1) {
                wishlistItems.splice(idx, 1);
                showToast(`Removed from wishlist: ${p.name}`);
            } else {
                wishlistItems.push(p);
                showToast(`Saved to wishlist: ${p.name}`);
            }
            localStorage.setItem('trendvibe_wishlist', JSON.stringify(wishlistItems));
            updateBadges();
            applyFiltersAndRender();
        }

        function updateBadges() {
            const totalBagQty = bagItems.reduce((acc, item) => acc + item.quantity, 0);
            document.getElementById('bagCount').textContent = totalBagQty;
            document.getElementById('mobileBagCount').textContent = totalBagQty;
            document.getElementById('drawerBagCount').textContent = totalBagQty;
            document.getElementById('wishlistCount').textContent = wishlistItems.length;
        }

        function openBagDrawer() {
            renderBagDrawer();
            openDrawer('bagDrawer');
        }

        function renderBagDrawer() {
            const container = document.getElementById('bagDrawerItems');
            if (bagItems.length === 0) {
                container.innerHTML = `
                    <div style="text-align: center; padding: 60px 20px;">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="color: var(--text-muted); margin-bottom: 12px;">
                            <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-7z"></path>
                            <line x1="3" y1="6" x2="21" y2="6"></line>
                            <path d="M16 10a4 4 0 0 1-8 0"></path>
                        </svg>
                        <h4 style="font-size: 14px; font-weight: 700; margin-bottom: 6px;">YOUR BAG IS EMPTY</h4>
                        <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 18px;">Discover our runway edits and curated fine beauty.</p>
                        <button onclick="closeDrawer('bagDrawer'); setCategoryFilter('ALL');" class="load-more-btn">Explore Runway</button>
                    </div>
                `;
                document.getElementById('bagDrawerFooter').style.display = 'none';
                return;
            }

            document.getElementById('bagDrawerFooter').style.display = 'block';
            let subtotal = 0;
            let html = '';

            bagItems.forEach((item, index) => {
                subtotal += item.price * item.quantity;
                html += `
                    <div class="bag-item">
                        <img class="bag-item-img" src="${item.imageUrl}" alt="${item.name}" onerror="handleImageFallback(this, '${item.category}')">
                        <div class="bag-item-details">
                            <span class="bag-item-brand">${item.brand}</span>
                            <h4 class="bag-item-title">${item.name}</h4>
                            <div class="bag-item-meta">Size: ${item.size} &bull; &#8377;${item.price.toLocaleString('en-IN')}</div>
                            <div class="bag-item-row">
                                <div class="qty-control">
                                    <button class="qty-btn" onclick="updateItemQty(${index}, -1)">&minus;</button>
                                    <span class="qty-num">${item.quantity}</span>
                                    <button class="qty-btn" onclick="updateItemQty(${index}, 1)">&plus;</button>
                                </div>
                                <span style="font-size: 13px; font-weight: 700;">&#8377;${(item.price * item.quantity).toLocaleString('en-IN')}</span>
                            </div>
                        </div>
                    </div>
                `;
            });

            container.innerHTML = html;
            document.getElementById('bagSubtotal').textContent = `₹${subtotal.toLocaleString('en-IN')}`;
        }

        function updateItemQty(index, delta) {
            bagItems[index].quantity += delta;
            if (bagItems[index].quantity <= 0) {
                bagItems.splice(index, 1);
            }
            saveBag();
        }

        // =========================================================================
        // 7. CHECKOUT FLOW
        // =========================================================================
        function openCheckoutModal() {
            if (bagItems.length === 0) return;
            closeDrawer('bagDrawer');

            const user = getCurrentUser();
            const notice = document.getElementById('checkoutAuthNotice');
            if (user) {
                notice.innerHTML = `<strong>Ordering as:</strong> ${user.name} (+91 ${user.phone}) &bull; Saved details pre-filled.`;
                document.getElementById('checkoutName').value = user.name;
                document.getElementById('checkoutPhone').value = user.phone;
                document.getElementById('checkoutPincode').value = user.pincode;
                document.getElementById('checkoutCity').value = user.city || 'New Delhi';
            } else {
                notice.innerHTML = `<strong>Guest Checkout:</strong> Have an account? <a href="#" onclick="closeModal('checkoutModal'); openAuthModal(); return false;" style="color: var(--accent); font-weight: 700;">Sign in with Phone & Password</a> for 1-click orders.`;
                document.getElementById('checkoutName').value = '';
                document.getElementById('checkoutPhone').value = '';
                document.getElementById('checkoutPincode').value = '';
                document.getElementById('checkoutCity').value = '';
            }

            const total = bagItems.reduce((acc, item) => acc + (item.price * item.quantity), 0);
            document.getElementById('checkoutTotalAmount').textContent = `₹${total.toLocaleString('en-IN')}`;

            openModal('checkoutModal');
        }

        function handlePlaceOrder(e) {
            e.preventDefault();
            const name = document.getElementById('checkoutName').value.trim();
            const phone = document.getElementById('checkoutPhone').value.trim();
            const total = bagItems.reduce((acc, item) => acc + (item.price * item.quantity), 0);
            const orderId = Math.floor(100000 + Math.random() * 900000);

            // Record Order
            const orders = JSON.parse(localStorage.getItem('trendvibe_orders') || '[]');
            orders.unshift({
                orderId: orderId,
                date: new Date().toLocaleDateString('en-IN', { month: 'short', day: 'numeric', year: 'numeric' }),
                itemsCount: bagItems.reduce((acc, item) => acc + item.quantity, 0),
                total: total,
                status: 'CONFIRMED &bull; DISPATCH IN 24H',
                customerName: name,
                customerPhone: phone
            });
            localStorage.setItem('trendvibe_orders', JSON.stringify(orders));

            // Clear Bag
            bagItems = [];
            saveBag();

            closeModal('checkoutModal');
            alert(`🎉 Congratulations ${name}!\n\nYour Atelier Order #${orderId} is Confirmed!\nTotal Paid: ₹${total.toLocaleString('en-IN')}\nExpress Dispatch notification sent to +91 ${phone}.`);
            showToast(`Order #${orderId} confirmed successfully!`);
        }

        // =========================================================================
        // 8. HELPERS (MODALS, DRAWERS, TOAST)
        // =========================================================================
        function openModal(id) {
            const el = document.getElementById(id);
            if (el) el.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeModal(id) {
            const el = document.getElementById(id);
            if (el) el.classList.remove('active');
            document.body.style.overflow = '';
        }

        function openDrawer(id) {
            const overlay = document.getElementById(id + 'Overlay');
            const drawer = document.getElementById(id);
            if (overlay) overlay.classList.add('active');
            if (drawer) drawer.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeDrawer(id) {
            const overlay = document.getElementById(id + 'Overlay');
            const drawer = document.getElementById(id);
            if (overlay) overlay.classList.remove('active');
            if (drawer) drawer.classList.remove('active');
            document.body.style.overflow = '';
        }

        let toastTimer = null;
        function showToast(msg) {
            const toast = document.getElementById('toastNotification');
            const toastMsg = document.getElementById('toastMessage');
            toastMsg.textContent = msg;
            toast.classList.add('show');

            if (toastTimer) clearTimeout(toastTimer);
            toastTimer = setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }
    </script>
</body>
</html>
"""

# Replace the PRODUCTS_DATA_PLACEHOLDER with JSON string
products_json_str = json.dumps(products)
full_html = html_template.replace("PRODUCTS_DATA_PLACEHOLDER", products_json_str)

# Write to demo/index.html and src/main/webapp/index.html
os.makedirs("demo", exist_ok=True)
with open("demo/index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Written demo/index.html ({len(full_html)} bytes)")

os.makedirs("src/main/webapp", exist_ok=True)
with open("src/main/webapp/index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Written src/main/webapp/index.html ({len(full_html)} bytes)")
