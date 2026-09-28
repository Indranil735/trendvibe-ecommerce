package com.ecommerce.controller;

import com.ecommerce.dao.CartDAO;
import com.ecommerce.dao.CategoryDAO;
import com.ecommerce.dao.ProductDAO;
import com.ecommerce.model.Cart;
import com.ecommerce.model.Product;
import com.ecommerce.model.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

@WebServlet(name = "CartController", urlPatterns = {"/cart", "/cart/add", "/cart/update", "/cart/remove"})
public class CartController extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private CartDAO cartDAO;
    private ProductDAO productDAO;
    private CategoryDAO categoryDAO;

    @Override
    public void init() {
        cartDAO = new CartDAO();
        productDAO = new ProductDAO();
        categoryDAO = new CategoryDAO();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String path = request.getServletPath();
        if ("/cart/remove".equals(path)) {
            handleRemove(request, response);
            return;
        }

        request.setAttribute("categories", categoryDAO.getAllActiveCategories());
        int userId = getEffectiveUserId(request);

        Cart cart = cartDAO.getCartWithItems(userId);
        request.setAttribute("cart", cart);
        request.getRequestDispatcher("/WEB-INF/views/cart.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String path = request.getServletPath();

        if ("/cart/add".equals(path)) {
            handleAdd(request, response);
        } else if ("/cart/update".equals(path)) {
            handleUpdate(request, response);
        } else if ("/cart/remove".equals(path)) {
            handleRemove(request, response);
        } else {
            doGet(request, response);
        }
    }

    private void handleAdd(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        int userId = getEffectiveUserId(request);
        String productIdParam = request.getParameter("productId");
        String sizeLabel = request.getParameter("sizeLabel");
        String quantityParam = request.getParameter("quantity");

        if (productIdParam == null || sizeLabel == null || sizeLabel.trim().isEmpty()) {
            response.sendRedirect(request.getContextPath() + "/home?error=invalid_selection");
            return;
        }

        try {
            int productId = Integer.parseInt(productIdParam.trim());
            int quantity = quantityParam != null ? Math.max(1, Integer.parseInt(quantityParam.trim())) : 1;

            Product product = productDAO.getProductById(productId);
            if (product != null) {
                Cart cart = cartDAO.getOrCreateCart(userId);
                if (cart != null) {
                    cartDAO.addItemToCart(cart.getCartId(), productId, sizeLabel.trim(), quantity, product.getFinalPrice());
                }
            }
        } catch (NumberFormatException ignored) {}

        String returnUrl = request.getParameter("returnUrl");
        if (returnUrl != null && !returnUrl.trim().isEmpty()) {
            response.sendRedirect(returnUrl);
        } else {
            response.sendRedirect(request.getContextPath() + "/cart");
        }
    }

    private void handleUpdate(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        String cartItemIdParam = request.getParameter("cartItemId");
        String quantityParam = request.getParameter("quantity");

        if (cartItemIdParam != null && quantityParam != null) {
            try {
                int cartItemId = Integer.parseInt(cartItemIdParam.trim());
                int quantity = Integer.parseInt(quantityParam.trim());
                cartDAO.updateItemQuantity(cartItemId, quantity);
            } catch (NumberFormatException ignored) {}
        }

        response.sendRedirect(request.getContextPath() + "/cart");
    }

    private void handleRemove(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        String cartItemIdParam = request.getParameter("cartItemId");
        if (cartItemIdParam != null) {
            try {
                int cartItemId = Integer.parseInt(cartItemIdParam.trim());
                cartDAO.removeItem(cartItemId);
            } catch (NumberFormatException ignored) {}
        }

        response.sendRedirect(request.getContextPath() + "/cart");
    }

    private int getEffectiveUserId(HttpServletRequest request) {
        HttpSession session = request.getSession(true);
        User user = (User) session.getAttribute("user");
        if (user != null) {
            return user.getUserId();
        }
        // Guest user session fallback ID
        Integer guestId = (Integer) session.getAttribute("guestUserId");
        if (guestId == null) {
            guestId = 1; // Default to demo user 1
            session.setAttribute("guestUserId", guestId);
        }
        return guestId;
    }
}
