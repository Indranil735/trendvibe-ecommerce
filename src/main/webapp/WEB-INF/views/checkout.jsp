<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div style="max-width: 960px; margin: 0 auto;">
    <h2 style="font-size: 22px; font-weight: 800; text-transform: uppercase; margin-bottom: 24px; color: var(--dark);">
        Checkout &amp; Payment
    </h2>

    <form action="${pageContext.request.contextPath}/checkout/place-order" method="POST">
        <div class="cart-layout">
            <!-- Left: Address & Payment Selection -->
            <div style="display: flex; flex-direction: column; gap: 24px;">
                <!-- 1. Delivery Address Card -->
                <div style="background: #fff; border: 1px solid var(--border-color); border-radius: 8px; padding: 24px;">
                    <h3 style="font-size: 15px; font-weight: 800; text-transform: uppercase; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <span>📍</span> Delivery Address
                    </h3>

                    <div class="form-group">
                        <label for="deliveryAddress">Shipping / Full Address</label>
                        <textarea id="deliveryAddress" name="deliveryAddress" rows="3" required>${user != null && not empty user.address ? user.address : 'Flat 402, Green Valley Apartments, Outer Ring Road, Bangalore, Karnataka - 560001'}</textarea>
                    </div>
                </div>

                <!-- 2. Payment Method Card -->
                <div style="background: #fff; border: 1px solid var(--border-color); border-radius: 8px; padding: 24px;">
                    <h3 style="font-size: 15px; font-weight: 800; text-transform: uppercase; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                        <span>💳</span> Select Payment Method
                    </h3>

                    <div style="display: flex; flex-direction: column; gap: 12px;">
                        <label style="display: flex; align-items: center; gap: 12px; padding: 14px; border: 1px solid var(--border-color); border-radius: 6px; cursor: pointer;">
                            <input type="radio" name="paymentMethod" value="UPI (Google Pay / PhonePe)" checked>
                            <div>
                                <div style="font-size: 14px; font-weight: 700;">UPI (Google Pay, PhonePe, Paytm, QR)</div>
                                <div style="font-size: 12px; color: var(--text-muted);">Instant zero-fee payment</div>
                            </div>
                        </label>

                        <label style="display: flex; align-items: center; gap: 12px; padding: 14px; border: 1px solid var(--border-color); border-radius: 6px; cursor: pointer;">
                            <input type="radio" name="paymentMethod" value="Credit / Debit Card">
                            <div>
                                <div style="font-size: 14px; font-weight: 700;">Credit / Debit Card (Visa, Mastercard, RuPay)</div>
                                <div style="font-size: 12px; color: var(--text-muted);">Safe &amp; encrypted card transactions</div>
                            </div>
                        </label>

                        <label style="display: flex; align-items: center; gap: 12px; padding: 14px; border: 1px solid var(--border-color); border-radius: 6px; cursor: pointer;">
                            <input type="radio" name="paymentMethod" value="Net Banking">
                            <div>
                                <div style="font-size: 14px; font-weight: 700;">Net Banking</div>
                                <div style="font-size: 12px; color: var(--text-muted);">All major Indian banks supported</div>
                            </div>
                        </label>

                        <label style="display: flex; align-items: center; gap: 12px; padding: 14px; border: 1px solid var(--border-color); border-radius: 6px; cursor: pointer;">
                            <input type="radio" name="paymentMethod" value="Cash on Delivery (COD)">
                            <div>
                                <div style="font-size: 14px; font-weight: 700;">Cash on Delivery (COD)</div>
                                <div style="font-size: 12px; color: var(--text-muted);">Pay cash or UPI at the doorstep</div>
                            </div>
                        </label>
                    </div>
                </div>
            </div>

            <!-- Right: Order Summary -->
            <div>
                <div class="price-summary-card">
                    <h3 class="summary-title">ORDER SUMMARY</h3>

                    <div class="summary-row">
                        <span>Items in Bag</span>
                        <span>${cart.itemCount}</span>
                    </div>

                    <div class="summary-row">
                        <span>Total MRP</span>
                        <span>&#8377;${cart.totalMRP}</span>
                    </div>

                    <div class="summary-row">
                        <span>Bag Discount</span>
                        <span class="discount-text">- &#8377;${cart.totalDiscount}</span>
                    </div>

                    <div class="summary-row">
                        <span>Delivery Charges</span>
                        <span style="color: var(--success); font-weight: 700;">FREE</span>
                    </div>

                    <div class="summary-row total-payable">
                        <span>Total Payable</span>
                        <span>&#8377;${cart.totalAmount}</span>
                    </div>

                    <button type="submit" class="btn-place-order">
                        CONFIRM &amp; PLACE ORDER
                    </button>
                </div>
            </div>
        </div>
    </form>
</div>

<jsp:include page="footer.jsp" />
