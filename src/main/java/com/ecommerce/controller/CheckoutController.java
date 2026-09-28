package com.ecommerce.controller;

import com.ecommerce.dao.CartDAO;
import com.ecommerce.dao.CategoryDAO;
import com.ecommerce.dao.OrderDAO;
import com.ecommerce.model.Cart;
import com.ecommerce.model.Order;
import com.ecommerce.model.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
import java.util.List;

@WebServlet(name = "CheckoutController", urlPatterns = {
    "/checkout", "/checkout/place-order", "/order-success", "/my-orders", "/order-details"
})
public class CheckoutController extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private CartDAO cartDAO;
    private OrderDAO orderDAO;
    private CategoryDAO categoryDAO;

    @Override
    public void init() {
        cartDAO = new CartDAO();
        orderDAO = new OrderDAO();
        categoryDAO = new CategoryDAO();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String path = request.getServletPath();
        request.setAttribute("categories", categoryDAO.getAllActiveCategories());

        if ("/order-success".equals(path)) {
            handleOrderSuccess(request, response);
        } else if ("/my-orders".equals(path)) {
            handleMyOrders(request, response);
        } else if ("/order-details".equals(path)) {
            handleOrderDetails(request, response);
        } else {
            handleCheckoutPage(request, response);
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String path = request.getServletPath();

        if ("/checkout/place-order".equals(path)) {
            handlePlaceOrder(request, response);
        } else {
            doGet(request, response);
        }
    }

    private void handleCheckoutPage(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession(true);
        User user = (User) session.getAttribute("user");

        int userId = (user != null) ? user.getUserId() : 1;
        Cart cart = cartDAO.getCartWithItems(userId);

        if (cart == null || cart.getItems() == null || cart.getItems().isEmpty()) {
            response.sendRedirect(request.getContextPath() + "/cart?error=empty_cart");
            return;
        }

        request.setAttribute("cart", cart);
        request.setAttribute("user", user);
        request.getRequestDispatcher("/WEB-INF/views/checkout.jsp").forward(request, response);
    }

    private void handlePlaceOrder(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        HttpSession session = request.getSession(true);
        User user = (User) session.getAttribute("user");
        int userId = (user != null) ? user.getUserId() : 1;

        String deliveryAddress = request.getParameter("deliveryAddress");
        String paymentMethod = request.getParameter("paymentMethod");

        if (deliveryAddress == null || deliveryAddress.trim().isEmpty()) {
            deliveryAddress = (user != null && user.getAddress() != null)
                ? user.getAddress()
                : "Flat 402, Green Valley Apts, Bangalore - 560001";
        }

        if (paymentMethod == null || paymentMethod.trim().isEmpty()) {
            paymentMethod = "Cash on Delivery (COD)";
        }

        Order order = orderDAO.createOrderFromCart(userId, deliveryAddress.trim(), paymentMethod.trim());

        if (order != null) {
            response.sendRedirect(request.getContextPath() + "/order-success?orderId=" + order.getOrderId());
        } else {
            response.sendRedirect(request.getContextPath() + "/checkout?error=failed");
        }
    }

    private void handleOrderSuccess(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String orderIdParam = request.getParameter("orderId");
        HttpSession session = request.getSession(true);
        User user = (User) session.getAttribute("user");
        int userId = (user != null) ? user.getUserId() : 1;

        if (orderIdParam != null) {
            try {
                int orderId = Integer.parseInt(orderIdParam.trim());
                Order order = orderDAO.getOrderById(orderId, userId);
                request.setAttribute("order", order);
            } catch (NumberFormatException ignored) {}
        }

        request.getRequestDispatcher("/WEB-INF/views/order-success.jsp").forward(request, response);
    }

    private void handleMyOrders(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession(true);
        User user = (User) session.getAttribute("user");
        int userId = (user != null) ? user.getUserId() : 1;

        List<Order> orders = orderDAO.getOrdersByUser(userId);
        request.setAttribute("orders", orders);
        request.getRequestDispatcher("/WEB-INF/views/orders.jsp").forward(request, response);
    }

    private void handleOrderDetails(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String orderIdParam = request.getParameter("id");
        HttpSession session = request.getSession(true);
        User user = (User) session.getAttribute("user");
        int userId = (user != null) ? user.getUserId() : 1;

        if (orderIdParam != null) {
            try {
                int orderId = Integer.parseInt(orderIdParam.trim());
                Order order = orderDAO.getOrderById(orderId, userId);
                request.setAttribute("order", order);
            } catch (NumberFormatException ignored) {}
        }

        request.getRequestDispatcher("/WEB-INF/views/order-details.jsp").forward(request, response);
    }
}
