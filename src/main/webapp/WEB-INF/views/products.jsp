<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div style="display: flex; gap: 32px; align-items: flex-start;">
    <!-- Sidebar Filter (Myntra/Ajio Style) -->
    <aside style="width: 260px; flex-shrink: 0; background: #fff; border: 1px solid var(--border-color); border-radius: 8px; padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding-bottom: 12px; border-bottom: 1px solid var(--border-color);">
            <h3 style="font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">Filters</h3>
            <a href="${pageContext.request.contextPath}/products" style="font-size: 12px; color: var(--primary); font-weight: 700;">CLEAR ALL</a>
        </div>

        <!-- Categories Filter -->
        <div style="margin-bottom: 24px;">
            <h4 style="font-size: 13px; font-weight: 800; text-transform: uppercase; margin-bottom: 12px;">Categories</h4>
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <a href="${pageContext.request.contextPath}/products" 
                   style="font-size: 13px; color: ${empty selectedCategory ? 'var(--primary)' : 'var(--text-muted)'}; font-weight: ${empty selectedCategory ? '700' : '400'};">
                    All Categories
                </a>
                <c:forEach var="cat" items="${categories}">
                    <a href="${pageContext.request.contextPath}/products?category=${cat.categoryId}" 
                       style="font-size: 13px; color: ${selectedCategory == cat.categoryId ? 'var(--primary)' : 'var(--text-muted)'}; font-weight: ${selectedCategory == cat.categoryId ? '700' : '400'};">
                        ${cat.categoryName}
                    </a>
                </c:forEach>
            </div>
        </div>

        <!-- Size Filter -->
        <div style="margin-bottom: 24px;">
            <h4 style="font-size: 13px; font-weight: 800; text-transform: uppercase; margin-bottom: 12px;">Sizes</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <c:forEach var="sz" items="${['S', 'M', 'L', 'XL', 'UK 7', 'UK 8', 'UK 9']}">
                    <a href="${pageContext.request.contextPath}/products?size=${sz}${not empty selectedCategory ? '&category='.concat(selectedCategory) : ''}" 
                       style="padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: 700; border: 1px solid ${selectedSize == sz ? 'var(--primary)' : 'var(--border-color)'}; color: ${selectedSize == sz ? 'var(--primary)' : 'var(--dark)'}; background: ${selectedSize == sz ? 'var(--primary-light)' : '#fff'};">
                        ${sz}
                    </a>
                </c:forEach>
            </div>
        </div>

        <!-- Sort Filter -->
        <div>
            <h4 style="font-size: 13px; font-weight: 800; text-transform: uppercase; margin-bottom: 12px;">Sort By</h4>
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <a href="${pageContext.request.contextPath}/products?sort=recommended${not empty selectedCategory ? '&category='.concat(selectedCategory) : ''}" 
                   style="font-size: 13px; color: ${empty selectedSort || selectedSort == 'recommended' ? 'var(--primary)' : 'var(--text-muted)'}; font-weight: ${empty selectedSort || selectedSort == 'recommended' ? '700' : '400'};">
                    Recommended
                </a>
                <a href="${pageContext.request.contextPath}/products?sort=discount${not empty selectedCategory ? '&category='.concat(selectedCategory) : ''}" 
                   style="font-size: 13px; color: ${selectedSort == 'discount' ? 'var(--primary)' : 'var(--text-muted)'}; font-weight: ${selectedSort == 'discount' ? '700' : '400'};">
                    Better Discount
                </a>
                <a href="${pageContext.request.contextPath}/products?sort=newest${not empty selectedCategory ? '&category='.concat(selectedCategory) : ''}" 
                   style="font-size: 13px; color: ${selectedSort == 'newest' ? 'var(--primary)' : 'var(--text-muted)'}; font-weight: ${selectedSort == 'newest' ? '700' : '400'};">
                    What's New
                </a>
            </div>
        </div>
    </aside>

    <!-- Main Products Listing Area -->
    <section style="flex: 1;">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 20px;">
            <div>
                <h2 style="font-size: 20px; font-weight: 800; color: var(--dark);">
                    <c:choose>
                        <c:when test="${not empty searchQuery}">
                            Results for "${searchQuery}"
                        </c:when>
                        <c:otherwise>
                            All Fashion &amp; Beauty Collection
                        </c:otherwise>
                    </c:choose>
                </h2>
                <span style="font-size: 13px; color: var(--text-muted);">${products != null ? products.size() : 0} items found</span>
            </div>
        </div>

        <c:choose>
            <c:when test="${not empty products}">
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
            </c:when>
            <c:otherwise>
                <div style="background: #fff; border: 1px solid var(--border-color); border-radius: 8px; padding: 60px; text-align: center;">
                    <div style="font-size: 48px; margin-bottom: 16px;">🔍</div>
                    <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 8px;">We couldn't find any matches!</h3>
                    <p style="font-size: 14px; color: var(--text-muted); margin-bottom: 24px;">
                        Try searching with different terms or clear filters to see more products.
                    </p>
                    <a href="${pageContext.request.contextPath}/products" class="hero-btn" style="background: var(--primary); color: #fff;">Clear Filters</a>
                </div>
            </c:otherwise>
        </c:choose>
    </section>
</div>

<jsp:include page="footer.jsp" />
