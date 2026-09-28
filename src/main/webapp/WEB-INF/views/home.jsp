<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<!-- Hero Banner (Myntra / Ajio / Nykaa theme) -->
<section class="hero-banner-section">
    <div class="hero-slide">
        <div class="hero-content">
            <span class="hero-badge">Trending Festive Drop</span>
            <h1 class="hero-title">BIG FASHION &amp; BEAUTY FESTIVAL</h1>
            <p class="hero-desc">
                Discover the latest arrivals in menswear, ethnic elegance, streetwear sneakers, and Nykaa luxury skincare.
            </p>
            <a href="${pageContext.request.contextPath}/products" class="hero-btn">Explore Full Catalog &rarr;</a>
        </div>
        <div class="hero-image-decor" style="font-size: 110px; opacity: 0.9; text-shadow: 0 8px 24px rgba(0,0,0,0.3);">
            👗✨👟
        </div>
    </div>
</section>

<!-- Shop By Category Section -->
<div class="section-heading">
    <h2 class="section-title">Shop by Category</h2>
    <a href="${pageContext.request.contextPath}/products" style="color: var(--primary); font-size: 13px; font-weight: 700;">View All &rarr;</a>
</div>

<div class="category-row">
    <a href="${pageContext.request.contextPath}/products?category=1" class="category-card">
        <div class="cat-icon">👔</div>
        <div class="cat-name">Men's Fashion</div>
        <div class="cat-count">Casual, Denim, Formal</div>
    </a>
    <a href="${pageContext.request.contextPath}/products?category=2" class="category-card">
        <div class="cat-icon">👗</div>
        <div class="cat-name">Women's Ethnic &amp; Western</div>
        <div class="cat-count">Kurtas, Dresses, Sarees</div>
    </a>
    <a href="${pageContext.request.contextPath}/products?category=3" class="category-card" style="border-bottom: 3px solid var(--nykaa-pink);">
        <div class="cat-icon">💄</div>
        <div class="cat-name">Beauty &amp; Nykaa</div>
        <div class="cat-count">Lipsticks, Serums, Gold Bhasma</div>
    </a>
    <a href="${pageContext.request.contextPath}/products?category=4" class="category-card">
        <div class="cat-icon">👟</div>
        <div class="cat-name">Sneakers &amp; Shoes</div>
        <div class="cat-count">Nike, Puma, Low-Tops</div>
    </a>
    <a href="${pageContext.request.contextPath}/products?category=5" class="category-card">
        <div class="cat-icon">⌚</div>
        <div class="cat-name">Luxury Accessories</div>
        <div class="cat-count">Fossil, Ray-Ban, Leather</div>
    </a>
</div>

<!-- Trending Products Section -->
<div class="section-heading">
    <h2 class="section-title">Trending Styles &amp; Best Sellers</h2>
    <span style="font-size: 13px; color: var(--text-muted); font-weight: 600;">Handpicked for You</span>
</div>

<div class="product-grid">
    <c:forEach var="p" items="${products}">
        <div class="product-card">
            <a href="${pageContext.request.contextPath}/product-details?id=${p.productId}" class="product-card-media">
                <img src="${p.imageUrl}" alt="${p.productName}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'">
                <c:if test="${p.discountPercent > 0}">
                    <span class="discount-badge">${p.discountPercent.intValue()}% OFF</span>
                </c:if>
            </a>

            <div class="product-card-body">
                <div class="product-brand">${p.categoryName}</div>
                <a href="${pageContext.request.contextPath}/product-details?id=${p.productId}" class="product-name" title="${p.productName}">
                    ${p.productName}
                </a>

                <!-- Available sizes preview -->
                <c:if test="${not empty p.sizes}">
                    <div class="product-sizes-preview">
                        <c:forEach var="s" items="${p.sizes}" end="4">
                            <span class="size-pill-sm">${s.sizeLabel}</span>
                        </c:forEach>
                    </div>
                </c:if>

                <div class="price-row">
                    <span class="price-final">&#8377;${p.finalPrice}</span>
                    <c:if test="${p.discountPercent > 0}">
                        <span class="price-mrp">&#8377;${p.basePrice}</span>
                        <span class="price-off">(${p.discountPercent.intValue()}% OFF)</span>
                    </c:if>
                </div>
            </div>
        </div>
    </c:forEach>
</div>

<jsp:include page="footer.jsp" />
