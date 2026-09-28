<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div style="max-width: 680px; margin: 40px auto; background: #fff; border: 1px solid var(--border-color); border-radius: 12px; padding: 40px; text-align: center; box-shadow: var(--shadow-md);">
    <!-- Success Animated Check Icon -->
    <div style="width: 72px; height: 72px; border-radius: 36px; background: #e6f7f3; color: var(--success); font-size: 36px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
        ✓
    </div>

    <h1 style="font-size: 26px; font-weight: 900; color: var(--dark); margin-bottom: 8px;">Order Placed Successfully!</h1>
    <p style="font-size: 15px; color: var(--text-muted); margin-bottom: 24px;">
        Thank you for shopping with TrendVibe! Your order has been placed and is being prepared for dispatch.
    </p>

    <div style="background: var(--bg-light); border-radius: 8px; padding: 20px; text-align: left; margin-bottom: 30px;">
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-color); padding-bottom: 12px; margin-bottom: 12px;">
            <span style="font-size: 13px; color: var(--text-muted);">Order Reference ID:</span>
            <span style="font-size: 14px; font-weight: 800; color: var(--dark);">#${order != null ? order.orderId : 'ORD-2026'}</span>
        </div>

        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-color); padding-bottom: 12px; margin-bottom: 12px;">
            <span style="font-size: 13px; color: var(--text-muted);">Payment Method:</span>
            <span style="font-size: 14px; font-weight: 700;">${order != null ? order.paymentMethod : 'Cash on Delivery'}</span>
        </div>

        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-color); padding-bottom: 12px; margin-bottom: 12px;">
            <span style="font-size: 13px; color: var(--text-muted);">Total Paid:</span>
            <span style="font-size: 16px; font-weight: 800; color: var(--primary);">&#8377;${order != null ? order.totalAmount : '0.00'}</span>
        </div>

        <div>
            <span style="font-size: 13px; color: var(--text-muted); display: block; margin-bottom: 4px;">Delivering To:</span>
            <span style="font-size: 13px; font-weight: 600; color: var(--dark);">${order != null ? order.deliveryAddress : 'Your Address'}</span>
        </div>
    </div>

    <!-- Actions -->
    <div style="display: flex; gap: 16px; justify-content: center;">
        <a href="${pageContext.request.contextPath}/my-orders" class="hero-btn" style="background: var(--dark); color: #fff;">
            VIEW ORDER DETAILS
        </a>
        <a href="${pageContext.request.contextPath}/products" class="hero-btn" style="background: var(--primary); color: #fff;">
            CONTINUE SHOPPING
        </a>
    </div>
</div>

<jsp:include page="footer.jsp" />
