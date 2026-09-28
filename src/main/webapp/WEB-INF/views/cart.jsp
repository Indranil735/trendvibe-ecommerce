<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<c:choose>
    <c:when test="${not empty cart and not empty cart.items}">
        <div class="cart-layout">
            <!-- Left Column: Bag Items -->
            <div class="cart-items-wrapper">
                <div style="background: #fff; padding: 14px 20px; border-radius: 8px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 800; font-size: 14px;">ITEMS IN BAG (${cart.itemCount})</span>
                    <span style="font-size: 12px; color: var(--success); font-weight: 700;">All discounts applied</span>
                </div>

                <c:forEach var="item" items="${cart.items}">
                    <div class="cart-item-card">
                        <div class="cart-item-img">
                            <img src="${item.product != null ? item.product.imageUrl : 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'}" 
                                 alt="${item.product != null ? item.product.productName : 'Item'}"
                                 onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'">
                        </div>

                        <div class="cart-item-details">
                            <h3 class="cart-item-name">${item.product != null ? item.product.productName : 'Product'}</h3>
                            <div class="cart-item-meta">
                                <span>Size: <strong>${item.sizeLabel}</strong></span> &bull; 
                                <span>Price: <strong>&#8377;${item.unitPrice}</strong></span>
                            </div>

                            <div style="font-size: 14px; font-weight: 800; color: var(--dark); margin-bottom: 12px;">
                                Subtotal: &#8377;${item.subtotal}
                            </div>

                            <div class="cart-item-actions">
                                <!-- Quantity modifier -->
                                <form action="${pageContext.request.contextPath}/cart/update" method="POST" style="display: inline-flex;">
                                    <input type="hidden" name="cartItemId" value="${item.cartItemId}">
                                    <div class="qty-control">
                                        <button type="submit" name="quantity" value="${item.quantity - 1}" class="qty-btn" ${item.quantity <= 1 ? 'disabled' : ''}>-</button>
                                        <span class="qty-number">${item.quantity}</span>
                                        <button type="submit" name="quantity" value="${item.quantity + 1}" class="qty-btn">+</button>
                                    </div>
                                </form>

                                <!-- Remove button -->
                                <form action="${pageContext.request.contextPath}/cart/remove" method="POST" style="display: inline;">
                                    <input type="hidden" name="cartItemId" value="${item.cartItemId}">
                                    <button type="submit" class="btn-remove-item">✕ REMOVE</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </c:forEach>
            </div>

            <!-- Right Column: Price Breakup (Myntra/Ajio Style) -->
            <div>
                <div class="price-summary-card">
                    <h3 class="summary-title">PRICE DETAILS (${cart.itemCount} Items)</h3>

                    <div class="summary-row">
                        <span>Total MRP</span>
                        <span>&#8377;${cart.totalMRP}</span>
                    </div>

                    <div class="summary-row">
                        <span>Discount on MRP</span>
                        <span class="discount-text">- &#8377;${cart.totalDiscount}</span>
                    </div>

                    <div class="summary-row">
                        <span>Coupon Discount</span>
                        <span class="discount-text">Apply at Checkout</span>
                    </div>

                    <div class="summary-row">
                        <span>Convenience Fee</span>
                        <span style="color: var(--success); font-weight: 700;">FREE</span>
                    </div>

                    <div class="summary-row total-payable">
                        <span>Total Amount</span>
                        <span>&#8377;${cart.totalAmount}</span>
                    </div>

                    <a href="${pageContext.request.contextPath}/checkout" class="btn-place-order" style="display: block; text-align: center;">
                        PROCEED TO CHECKOUT &rarr;
                    </a>
                </div>

                <div style="margin-top: 16px; font-size: 12px; color: var(--text-muted); text-align: center;">
                    🔒 Safe and Secure Payments. Easy returns. 100% Authentic products.
                </div>
            </div>
        </div>
    </c:when>
    <c:otherwise>
        <!-- Empty Cart State -->
        <div style="background: #fff; border: 1px solid var(--border-color); border-radius: 8px; padding: 64px 20px; text-align: center; max-width: 600px; margin: 40px auto;">
            <div style="font-size: 64px; margin-bottom: 20px;">🛍️</div>
            <h2 style="font-size: 22px; font-weight: 800; margin-bottom: 8px; color: var(--dark);">Hey, your bag feels light!</h2>
            <p style="font-size: 14px; color: var(--text-muted); margin-bottom: 24px;">
                There is nothing in your bag. Let's add some trendy items from our latest fashion drop!
            </p>
            <a href="${pageContext.request.contextPath}/products" class="hero-btn" style="background: var(--primary); color: #fff;">
                START SHOPPING NOW
            </a>
        </div>
    </c:otherwise>
</c:choose>

<jsp:include page="footer.jsp" />
