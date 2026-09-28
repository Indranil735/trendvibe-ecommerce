package com.ecommerce.controller;

import com.ecommerce.dao.UserDAO;
import com.ecommerce.model.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

@WebServlet(name = "RegisterController", urlPatterns = {"/register"})
public class RegisterController extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private UserDAO userDAO;

    @Override
    public void init() {
        userDAO = new UserDAO();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session != null && session.getAttribute("user") != null) {
            response.sendRedirect(request.getContextPath() + "/home");
            return;
        }
        request.getRequestDispatcher("/WEB-INF/views/register.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String fullName = request.getParameter("fullName");
        String email = request.getParameter("email");
        String phone = request.getParameter("phone");
        String password = request.getParameter("password");
        String gender = request.getParameter("gender");
        String address = request.getParameter("address");

        if (fullName == null || email == null || password == null ||
            fullName.trim().isEmpty() || email.trim().isEmpty() || password.trim().isEmpty()) {
            request.setAttribute("errorMessage", "Full name, email, and password are required.");
            request.getRequestDispatcher("/WEB-INF/views/register.jsp").forward(request, response);
            return;
        }

        if (userDAO.emailExists(email.trim())) {
            request.setAttribute("errorMessage", "An account with this email address already exists. Please login.");
            request.setAttribute("fullName", fullName);
            request.setAttribute("phone", phone);
            request.setAttribute("gender", gender);
            request.setAttribute("address", address);
            request.getRequestDispatcher("/WEB-INF/views/register.jsp").forward(request, response);
            return;
        }

        User newUser = new User();
        newUser.setFullName(fullName.trim());
        newUser.setEmail(email.trim());
        newUser.setPhone(phone != null ? phone.trim() : "");
        newUser.setPassword(password.trim());
        newUser.setGender(gender != null ? gender.trim() : "Not Specified");
        newUser.setAddress(address != null ? address.trim() : "");

        boolean success = userDAO.registerUser(newUser);
        if (success) {
            HttpSession session = request.getSession(true);
            session.setAttribute("user", newUser);
            response.sendRedirect(request.getContextPath() + "/home?registered=true");
        } else {
            request.setAttribute("errorMessage", "Registration failed due to a system error. Please try again.");
            request.getRequestDispatcher("/WEB-INF/views/register.jsp").forward(request, response);
        }
    }
}
