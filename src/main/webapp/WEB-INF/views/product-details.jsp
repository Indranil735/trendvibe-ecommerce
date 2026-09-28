<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div class="detail-layout">
    <!-- Product Gallery Left Column -->
    <div class="detail-gallery">
        <div class="detail-main-img">
            <img src="${product.imageUrl}" alt="${product.productName}" onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'">
        </div>
    </div>

    <!-- Product Details Right Column -->
    <div class="detail-info">
        <div style="font-size: 14px; font-weight: 800; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">
            ${product.categoryName}
        </div>
        <h1 class="product-title">${product.productName}</h1>
        <p class="product-subtitle">${product.description}</p>

        <!-- Pricing Section -->
        <div class="detail-pricing">
            <span class="final">&#8377;${product.finalPrice}</span>
            <c:if test="${product.discountPercent > 0}">
                <span class="mrp">&#8377;${product.basePrice}</span>
                <span class="off-tag">(${product.discountPercent.intValue()}% OFF)</span>
            </c:if>
            <span style="font-size: 12px; color: var(--success); font-weight: 700; margin-left: auto;">inclusive of all taxes</span>
        </div>

        <!-- Add to Bag Form -->
        <form action="${pageContext.request.contextPath}/cart/add" method="POST" id="addToCartForm">
            <input type="hidden" name="productId" value="${product.productId}">
            <input type="hidden" name="returnUrl" value="${pageContext.request.contextPath}/product-details?id=${product.productId}">

            <!-- Size Selector -->
            <div class="size-selector-title">
                <span>SELECT SIZE</span>
                <span style="color: var(--primary); font-size: 12px; cursor: pointer;">SIZE CHART &gt;</span>
            </div>

            <div class="size-selector-pills">
                <c:choose>
                    <c:when test="${not empty product.sizes}">
                        <c:forEach var="sz" items="${product.sizes}" varStatus="loop">
                            <label>
                                <input type="radio" name="sizeLabel" value="${sz.sizeLabel}" class="size-radio" ${loop.first ? 'checked' : ''} required>
                                <span class="size-btn">${sz.sizeLabel}</span>
                            </label>
                        </c:forEach>
                    </c:when>
                    <c:otherwise>
                        <label>
                            <input type="radio" name="sizeLabel" value="Free Size" class="size-radio" checked required>
                            <span class="size-btn">Free Size</span>
                        </label>
                    </c:otherwise>
                </c:choose>
            </div>

            <!-- Action Buttons -->
            <div class="detail-actions">
                <button type="submit" class="btn-add-to-bag">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                    </svg>
                    ADD TO BAG
                </button>
                <button type="button" class="btn-wishlist" onclick="alert('Added to your Wishlist ❤️')">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                    </svg>
                    WISHLIST
                </button>
            </div>
        </form>

        <!-- Delivery Pincode Checker -->
        <div class="pincode-box">
            <div style="font-size: 13px; font-weight: 800; text-transform: uppercase; color: var(--dark);">
                DELIVERY OPTIONS 🚚
            </div>
            <div class="pincode-input-row">
                <input type="text" id="pincodeInput" placeholder="Enter pincode (e.g. 560001)" maxlength="6">
                <button type="button" onclick="checkPincode()">Check</button>
            </div>
            <div id="pincodeResult" style="font-size: 12px; margin-top: 8px; font-weight: 600;">
                Please enter PIN code to check delivery time &amp; Pay on Delivery availability.
            </div>
        </div>

        <!-- Trust Badges -->
        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 13px; color: var(--text-muted); border-top: 1px solid var(--border-color); padding-top: 16px;">
            <div>✅ 100% Original Products guaranteed</div>
            <div>🔄 Pay on delivery might be available</div>
            <div>📦 Easy 14 days returns &amp; exchanges</div>
        </div>
    </div>
</div>

<!-- Related Products -->
<c:if test="${not empty relatedProducts}">
    <div style="margin-top: 50px;">
        <div class="section-heading">
            <h2 class="section-title">Similar Styles You May Like</h2>
        </div>
        <div class="product-grid">
            <c:forEach var="rp" items="${relatedProducts}" end="3">
                <div class="product-card">
                    <a href="${pageContext.request.contextPath}/product-details?id=${rp.productId}" class="product-card-media">
                        <img src="${rp.imageUrl}" alt="${rp.productName}" onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'">
                        <c:if test="${rp.discountPercent > 0}">
                            <span class="discount-badge">${rp.discountPercent.intValue()}% OFF</span>
                        </c:if>
                    </a>
                    <div class="product-card-body">
                        <div class="product-brand">${rp.categoryName}</div>
                        <a href="${pageContext.request.contextPath}/product-details?id=${rp.productId}" class="product-name">
                            ${rp.productName}
                        </a>
                        <div class="price-row">
                            <span class="price-final">&#8377;${rp.finalPrice}</span>
                        </div>
                    </div>
                </div>
            </c:forEach>
        </div>
    </div>
</c:if>

<script>
function checkPincode() {
    const input = document.getElementById('pincodeInput').value.trim();
    const result = document.getElementById('pincodeResult');
    if (input.length === 6 && /^\d+$/.test(input)) {
        result.style.color = 'var(--success)';
        result.innerHTML = '⚡ Express Delivery available by tomorrow! Cash on Delivery eligible.';
    } else {
        result.style.color = 'var(--danger)';
        result.innerHTML = '❌ Please enter a valid 6-digit Indian postal code.';
    }
}
</script>

<jsp:include page="footer.jsp" />
