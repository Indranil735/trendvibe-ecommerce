<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ taglib prefix="fn" uri="jakarta.tags.functions" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TrendVibe | Myntra &amp; Nykaa Fashion &amp; Beauty Store</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/style.css">
    <link rel="icon" href="https://img.icons8.com/color/48/shopping-bag.png" type="image/png">
</head>
<body>

    <!-- Top Announcement Bar -->
    <div class="top-announcement-bar">
        ⚡ END OF SEASON SALE: UP TO 70% OFF ON TOP BRANDS + FREE SHIPPING ON ALL ORDERS!
    </div>

    <!-- Header & Navbar -->
    <header class="site-header">
        <div class="header-container">
            <!-- Brand Logo -->
            <a href="${pageContext.request.contextPath}/home" class="brand-logo">
                TRENDVIBE <span class="badge-beauty">NYKAA &bull; AJIO</span>
            </a>

            <!-- Main Navigation Categories -->
            <nav class="main-nav">
                <a href="${pageContext.request.contextPath}/products?category=1">Men</a>
                <a href="${pageContext.request.contextPath}/products?category=2">Women</a>
                <a href="${pageContext.request.contextPath}/products?category=3" style="color: var(--nykaa-pink);">Beauty &amp; Nykaa</a>
                <a href="${pageContext.request.contextPath}/products?category=4">Footwear</a>
                <a href="${pageContext.request.contextPath}/products?category=5">Accessories</a>
            </nav>

            <!-- Search Bar -->
            <div class="search-container">
                <form action="${pageContext.request.contextPath}/products" method="GET">
                    <div class="search-box">
                        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                        </svg>
                        <input type="text" name="q" value="${param.q}" placeholder="Search for products, brands and more...">
                    </div>
                </form>
            </div>

            <!-- Header Actions -->
            <div class="header-actions">
                <!-- Profile / User Dropdown -->
                <div class="dropdown-wrapper">
                    <div class="action-item">
                        <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                        </svg>
                        <span>${sessionScope.user != null ? sessionScope.user.fullName : 'Profile'}</span>
                    </div>

                    <div class="dropdown-menu">
                        <c:choose>
                            <c:when test="${not empty sessionScope.user}">
                                <div class="dropdown-header">
                                    <div class="user-title">Hello, ${sessionScope.user.fullName}</div>
                                    <div class="user-sub">${sessionScope.user.email}</div>
                                </div>
                                <a href="${pageContext.request.contextPath}/my-orders">📦 My Orders</a>
                                <a href="${pageContext.request.contextPath}/profile">👤 Edit Profile</a>
                                <a href="${pageContext.request.contextPath}/cart">🛍️ My Bag</a>
                                <a href="${pageContext.request.contextPath}/logout" style="color: var(--danger); font-weight: 700;">🚪 Logout</a>
                            </c:when>
                            <c:otherwise>
                                <div class="dropdown-header">
                                    <div class="user-title">Welcome to TrendVibe</div>
                                    <div class="user-sub">To access account and manage orders</div>
                                </div>
                                <a href="${pageContext.request.contextPath}/login" style="font-weight: 700; color: var(--primary);">🔑 LOGIN / SIGNUP</a>
                                <a href="${pageContext.request.contextPath}/my-orders">📦 Orders</a>
                                <a href="${pageContext.request.contextPath}/cart">🛍️ Bag</a>
                            </c:otherwise>
                        </c:choose>
                    </div>
                </div>

                <!-- Bag / Cart -->
                <a href="${pageContext.request.contextPath}/cart" class="action-item">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                    </svg>
                    <span>Bag</span>
                    <c:if test="${not empty cart and cart.itemCount > 0}">
                        <span class="badge-count">${cart.itemCount}</span>
                    </c:if>
                </a>
            </div>
        </div>
    </header>

    <main class="main-wrapper">
