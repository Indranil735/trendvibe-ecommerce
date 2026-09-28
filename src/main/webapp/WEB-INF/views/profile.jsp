<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="header.jsp" />

<div style="max-width: 680px; margin: 20px auto; background: #fff; border: 1px solid var(--border-color); border-radius: 12px; padding: 36px; box-shadow: var(--shadow-sm);">
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--border-color);">
        <div style="width: 56px; height: 56px; border-radius: 28px; background: var(--primary-light); color: var(--primary); font-size: 24px; font-weight: 900; display: flex; align-items: center; justify-content: center;">
            👤
        </div>
        <div>
            <h2 style="font-size: 20px; font-weight: 800; color: var(--dark);">${user != null ? user.fullName : 'My Profile'}</h2>
            <p style="font-size: 13px; color: var(--text-muted);">${user != null ? user.email : ''}</p>
        </div>
    </div>

    <c:if test="${not empty successMessage}">
        <div style="background: #e6f7f3; color: var(--success); padding: 12px 16px; border-radius: 6px; font-size: 13px; font-weight: 700; margin-bottom: 20px;">
            ✓ ${successMessage}
        </div>
    </c:if>

    <c:if test="${not empty errorMessage}">
        <div style="background: #ffebee; color: var(--danger); padding: 12px 16px; border-radius: 6px; font-size: 13px; font-weight: 700; margin-bottom: 20px;">
            ✕ ${errorMessage}
        </div>
    </c:if>

    <form action="${pageContext.request.contextPath}/profile" method="POST">
        <div class="form-group">
            <label for="fullName">Full Name</label>
            <input type="text" id="fullName" name="fullName" value="${user != null ? user.fullName : ''}" required>
        </div>

        <div class="form-group">
            <label for="email">Email Address (Registered)</label>
            <input type="email" id="email" value="${user != null ? user.email : ''}" disabled style="background: #f7f7f8; cursor: not-allowed;">
        </div>

        <div class="form-group">
            <label for="phone">Mobile Number</label>
            <input type="tel" id="phone" name="phone" value="${user != null ? user.phone : ''}" placeholder="10-digit mobile number">
        </div>

        <div class="form-group">
            <label for="gender">Gender</label>
            <select id="gender" name="gender">
                <option value="Male" ${user != null && user.gender == 'Male' ? 'selected' : ''}>Male</option>
                <option value="Female" ${user != null && user.gender == 'Female' ? 'selected' : ''}>Female</option>
                <option value="Other" ${user != null && user.gender == 'Other' ? 'selected' : ''}>Other</option>
            </select>
        </div>

        <div class="form-group">
            <label for="address">Default Shipping Address</label>
            <textarea id="address" name="address" rows="3" placeholder="Apartment / Flat, Street, City, State, PIN">${user != null ? user.address : ''}</textarea>
        </div>

        <button type="submit" class="btn-submit-auth">SAVE PROFILE DETAILS</button>
    </form>
</div>

<jsp:include page="footer.jsp" />
