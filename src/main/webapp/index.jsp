<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    // Forward directly to ProductController (/home)
    response.sendRedirect(request.getContextPath() + "/home");
%>
