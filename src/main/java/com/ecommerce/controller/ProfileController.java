package com.ecommerce.controller;

import com.ecommerce.dao.CategoryDAO;
import com.ecommerce.dao.UserDAO;
import com.ecommerce.model.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

@WebServlet(name = "ProfileController", urlPatterns = {"/profile"})
public class ProfileController extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private UserDAO userDAO;
    private CategoryDAO categoryDAO;

    @Override
    public void init() {
        userDAO = new UserDAO();
        categoryDAO = new CategoryDAO();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect(request.getContextPath() + "/login?redirect=" + request.getContextPath() + "/profile");
            return;
        }

        User user = (User) session.getAttribute("user");
        User freshUser = userDAO.getUserById(user.getUserId());
        if (freshUser != null) {
            session.setAttribute("user", freshUser);
        }

        request.setAttribute("categories", categoryDAO.getAllActiveCategories());
        request.getRequestDispatcher("/WEB-INF/views/profile.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect(request.getContextPath() + "/login");
            return;
        }

        User user = (User) session.getAttribute("user");
        String fullName = request.getParameter("fullName");
        String phone = request.getParameter("phone");
        String gender = request.getParameter("gender");
        String address = request.getParameter("address");

        if (fullName != null && !fullName.trim().isEmpty()) {
            user.setFullName(fullName.trim());
        }
        user.setPhone(phone != null ? phone.trim() : "");
        user.setGender(gender != null ? gender.trim() : "Not Specified");
        user.setAddress(address != null ? address.trim() : "");

        boolean updated = userDAO.updateUser(user);
        if (updated) {
            session.setAttribute("user", user);
            request.setAttribute("successMessage", "Profile updated successfully!");
        } else {
            request.setAttribute("errorMessage", "Failed to update profile. Please try again.");
        }

        request.setAttribute("categories", categoryDAO.getAllActiveCategories());
        request.getRequestDispatcher("/WEB-INF/views/profile.jsp").forward(request, response);
    }
}
