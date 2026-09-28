<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div class="auth-wrapper">
    <div class="auth-header">
        <h2 style="font-size: 22px; font-weight: 900; margin-bottom: 6px;">Login to TrendVibe</h2>
        <p style="font-size: 13px; opacity: 0.9;">Access your Orders, Bag and Wishlist</p>
    </div>

    <div class="auth-body">
        <c:if test="${not empty errorMessage}">
            <div style="background: #ffebee; color: var(--danger); padding: 12px 14px; border-radius: 6px; font-size: 13px; font-weight: 700; margin-bottom: 18px;">
                ✕ ${errorMessage}
            </div>
        </c:if>

        <form action="${pageContext.request.contextPath}/login" method="POST">
            <input type="hidden" name="redirect" value="${param.redirect}">

            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" value="${enteredEmail != null ? enteredEmail : 'indranil@example.com'}" placeholder="Enter your email" required>
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" value="password123" placeholder="Enter password" required>
            </div>

            <button type="submit" class="btn-submit-auth">LOGIN</button>

            <!-- Demo helper card -->
            <div style="margin-top: 16px; background: var(--bg-light); border-radius: 6px; padding: 10px; font-size: 12px; color: var(--text-muted);">
                💡 <strong>Demo Credentials:</strong><br>
                Email: <code>indranil@example.com</code> | Password: <code>password123</code>
            </div>

            <div style="margin-top: 24px; text-align: center; font-size: 13px; color: var(--text-muted);">
                New to TrendVibe? 
                <a href="${pageContext.request.contextPath}/register" style="color: var(--primary); font-weight: 800;">
                    CREATE ACCOUNT
                </a>
            </div>
        </form>
    </div>
</div>

<jsp:include page="footer.jsp" />
