<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div style="max-width: 960px; margin: 0 auto;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
        <h2 style="font-size: 22px; font-weight: 800; text-transform: uppercase; color: var(--dark);">
            My Orders (${orders != null ? orders.size() : 0})
        </h2>
        <a href="${pageContext.request.contextPath}/products" style="font-size: 13px; font-weight: 700; color: var(--primary);">
            &plus; Shop More Styles
        </a>
    </div>

    <c:choose>
        <c:when test="${not empty orders}">
            <div style="display: flex; flex-direction: column; gap: 24px;">
                <c:forEach var="ord" items="${orders}">
                    <div style="background: #fff; border: 1px solid var(--border-color); border-radius: 8px; overflow: hidden; box-shadow: var(--shadow-sm);">
                        <!-- Order Card Header -->
                        <div style="background: var(--bg-light); padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); font-size: 13px;">
                            <div style="display: flex; gap: 24px;">
                                <div>
                                    <span style="color: var(--text-muted); display: block;">ORDER PLACED</span>
                                    <strong style="color: var(--dark);">${ord.orderDate}</strong>
                                </div>
                                <div>
                                    <span style="color: var(--text-muted); display: block;">TOTAL</span>
                                    <strong style="color: var(--dark);">&#8377;${ord.totalAmount}</strong>
                                </div>
                                <div>
                                    <span style="color: var(--text-muted); display: block;">SHIP TO</span>
                                    <strong style="color: var(--dark); max-width: 200px; display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="${ord.deliveryAddress}">
                                        ${ord.deliveryAddress}
                                    </strong>
                                </div>
                            </div>

                            <div style="text-align: right;">
                                <span style="display: inline-block; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 800; background: #e6f7f3; color: var(--success);">
                                    ● ${ord.orderStatus}
                                </span>
                                <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Order #${ord.orderId}</div>
                            </div>
                        </div>

                        <!-- Order Items List -->
                        <div style="padding: 20px;">
                            <c:forEach var="item" items="${ord.orderItems}">
                                <div style="display: flex; gap: 16px; align-items: center; padding: 12px 0; border-bottom: 1px solid #f0f0f0;">
                                    <img src="${item.imageUrl != null ? item.imageUrl : 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'}" 
                                         alt="${item.productName}" 
                                         style="width: 70px; height: 90px; object-fit: cover; border-radius: 4px; border: 1px solid var(--border-color);"
                                         onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'">

                                    <div style="flex: 1;">
                                        <h4 style="font-size: 14px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">
                                            ${item.productName}
                                        </h4>
                                        <div style="font-size: 13px; color: var(--text-muted);">
                                            Size: <strong>${item.sizeLabel}</strong> &bull; Qty: <strong>${item.quantity}</strong> &bull; Unit: <strong>&#8377;${item.unitPrice}</strong>
                                        </div>
                                    </div>

                                    <div style="font-size: 15px; font-weight: 800; color: var(--dark);">
                                        &#8377;${item.subtotal}
                                    </div>
                                </div>
                            </c:forEach>
                        </div>

                        <!-- Order Card Footer -->
                        <div style="padding: 12px 20px; background: #fafafa; border-top: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 12px; color: var(--text-muted);">Payment: <strong>${ord.paymentMethod}</strong></span>
                            <a href="${pageContext.request.contextPath}/order-details?id=${ord.orderId}" style="font-size: 13px; font-weight: 700; color: var(--primary);">
                                View Invoice Details &rarr;
                            </a>
                        </div>
                    </div>
                </c:forEach>
            </div>
        </c:when>
        <c:otherwise>
            <div style="background: #fff; border: 1px solid var(--border-color); border-radius: 8px; padding: 60px 20px; text-align: center;">
                <div style="font-size: 56px; margin-bottom: 16px;">📦</div>
                <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 8px;">No Orders Placed Yet!</h3>
                <p style="font-size: 14px; color: var(--text-muted); margin-bottom: 24px;">
                    Looks like you haven't bought any items yet. Explore the top trending outfits and accessories.
                </p>
                <a href="${pageContext.request.contextPath}/products" class="hero-btn" style="background: var(--primary); color: #fff;">
                    DISCOVER STYLES
                </a>
            </div>
        </c:otherwise>
    </c:choose>
</div>

<jsp:include page="footer.jsp" />
