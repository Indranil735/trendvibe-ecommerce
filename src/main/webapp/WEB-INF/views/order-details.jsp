<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div style="max-width: 860px; margin: 0 auto;">
    <div style="margin-bottom: 20px;">
        <a href="${pageContext.request.contextPath}/my-orders" style="font-size: 13px; font-weight: 700; color: var(--primary);">
            &larr; Back to My Orders
        </a>
    </div>

    <c:choose>
        <c:when test="${not empty order}">
            <div style="background: #fff; border: 1px solid var(--border-color); border-radius: 8px; padding: 32px; box-shadow: var(--shadow-sm);">
                <!-- Header -->
                <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid var(--border-color); padding-bottom: 20px; margin-bottom: 24px;">
                    <div>
                        <h2 style="font-size: 22px; font-weight: 900; color: var(--dark); margin-bottom: 4px;">
                            Order #${order.orderId}
                        </h2>
                        <div style="font-size: 13px; color: var(--text-muted);">
                            Placed on ${order.orderDate} &bull; Status: <strong style="color: var(--success);">${order.orderStatus}</strong>
                        </div>
                    </div>

                    <button type="button" onclick="window.print()" class="hero-btn" style="background: var(--bg-light); color: var(--dark); padding: 8px 16px; font-size: 12px;">
                        🖨️ Print Invoice
                    </button>
                </div>

                <!-- Status Progress Tracker -->
                <div style="background: var(--bg-light); border-radius: 8px; padding: 20px; margin-bottom: 28px;">
                    <div style="display: flex; justify-content: space-between; position: relative;">
                        <div style="text-align: center; flex: 1;">
                            <div style="width: 28px; height: 28px; border-radius: 14px; background: var(--success); color: #fff; line-height: 28px; margin: 0 auto 6px; font-weight: 800; font-size: 12px;">✓</div>
                            <div style="font-size: 12px; font-weight: 700;">Ordered</div>
                        </div>
                        <div style="text-align: center; flex: 1;">
                            <div style="width: 28px; height: 28px; border-radius: 14px; background: var(--success); color: #fff; line-height: 28px; margin: 0 auto 6px; font-weight: 800; font-size: 12px;">✓</div>
                            <div style="font-size: 12px; font-weight: 700;">Processing</div>
                        </div>
                        <div style="text-align: center; flex: 1;">
                            <div style="width: 28px; height: 28px; border-radius: 14px; background: var(--primary); color: #fff; line-height: 28px; margin: 0 auto 6px; font-weight: 800; font-size: 12px;">⚡</div>
                            <div style="font-size: 12px; font-weight: 700;">Shipped</div>
                        </div>
                        <div style="text-align: center; flex: 1;">
                            <div style="width: 28px; height: 28px; border-radius: 14px; background: #ddd; color: #666; line-height: 28px; margin: 0 auto 6px; font-weight: 800; font-size: 12px;">🚚</div>
                            <div style="font-size: 12px; font-weight: 700; color: #888;">Delivered</div>
                        </div>
                    </div>
                </div>

                <!-- Items Purchased -->
                <h3 style="font-size: 15px; font-weight: 800; text-transform: uppercase; margin-bottom: 16px;">Items in this Shipment</h3>
                <div style="border: 1px solid var(--border-color); border-radius: 6px; overflow: hidden; margin-bottom: 28px;">
                    <c:forEach var="item" items="${order.orderItems}">
                        <div style="display: flex; gap: 16px; align-items: center; padding: 16px; border-bottom: 1px solid #f0f0f0;">
                            <img src="${item.imageUrl != null ? item.imageUrl : 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'}" 
                                 alt="${item.productName}" 
                                 style="width: 60px; height: 75px; object-fit: cover; border-radius: 4px;"
                                 onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80'">

                            <div style="flex: 1;">
                                <h4 style="font-size: 14px; font-weight: 800; margin-bottom: 4px;">${item.productName}</h4>
                                <div style="font-size: 13px; color: var(--text-muted);">
                                    Size: <strong>${item.sizeLabel}</strong> &bull; Qty: <strong>${item.quantity}</strong>
                                </div>
                            </div>

                            <div style="font-size: 15px; font-weight: 800; color: var(--dark);">
                                &#8377;${item.subtotal}
                            </div>
                        </div>
                    </c:forEach>
                </div>

                <!-- Address & Payment Summary Split -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; border-top: 1px solid var(--border-color); padding-top: 20px;">
                    <div>
                        <h4 style="font-size: 13px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px;">Delivery Address</h4>
                        <p style="font-size: 13px; color: var(--dark); line-height: 1.6;">
                            ${order.deliveryAddress}
                        </p>
                    </div>

                    <div style="background: var(--bg-light); padding: 16px; border-radius: 6px;">
                        <h4 style="font-size: 13px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px;">Payment Details</h4>
                        <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
                            <span>Method:</span>
                            <strong>${order.paymentMethod}</strong>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 800; color: var(--primary); border-top: 1px dashed var(--border-color); padding-top: 8px;">
                            <span>Total Billed:</span>
                            <span>&#8377;${order.totalAmount}</span>
                        </div>
                    </div>
                </div>
            </div>
        </c:when>
        <c:otherwise>
            <div style="text-align: center; padding: 40px;">
                <h3>Order not found.</h3>
            </div>
        </c:otherwise>
    </c:choose>
</div>

<jsp:include page="footer.jsp" />
