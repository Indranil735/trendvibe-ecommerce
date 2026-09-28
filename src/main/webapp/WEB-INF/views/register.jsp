<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div class="auth-wrapper" style="max-width: 480px;">
    <div class="auth-header">
        <h2 style="font-size: 22px; font-weight: 900; margin-bottom: 6px;">Sign Up to TrendVibe</h2>
        <p style="font-size: 13px; opacity: 0.9;">Join the India's most loved fashion &amp; beauty community</p>
    </div>

    <div class="auth-body">
        <c:if test="${not empty errorMessage}">
            <div style="background: #ffebee; color: var(--danger); padding: 12px 14px; border-radius: 6px; font-size: 13px; font-weight: 700; margin-bottom: 18px;">
                ✕ ${errorMessage}
            </div>
        </c:if>

        <form action="${pageContext.request.contextPath}/register" method="POST">
            <div class="form-group">
                <label for="fullName">Full Name *</label>
                <input type="text" id="fullName" name="fullName" value="${fullName}" placeholder="Enter full name" required>
            </div>

            <div class="form-group">
                <label for="email">Email Address *</label>
                <input type="email" id="email" name="email" value="${email}" placeholder="name@example.com" required>
            </div>

            <div class="form-group">
                <label for="phone">Mobile Number</label>
                <input type="tel" id="phone" name="phone" value="${phone}" placeholder="10-digit mobile number">
            </div>

            <div class="form-group">
                <label for="password">Choose Password *</label>
                <input type="password" id="password" name="password" placeholder="Minimum 6 characters" required>
            </div>

            <div class="form-group">
                <label for="gender">Gender</label>
                <select id="gender" name="gender">
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>
            </div>

            <div class="form-group">
                <label for="address">Delivery Address</label>
                <textarea id="address" name="address" rows="2" placeholder="House/Flat, Street, City, State, PIN">${address}</textarea>
            </div>

            <button type="submit" class="btn-submit-auth">CREATE ACCOUNT</button>

            <div style="margin-top: 24px; text-align: center; font-size: 13px; color: var(--text-muted);">
                Already have an account? 
                <a href="${pageContext.request.contextPath}/login" style="color: var(--primary); font-weight: 800;">
                    LOGIN
                </a>
            </div>
        </form>
    </div>
</div>

<jsp:include page="footer.jsp" />
