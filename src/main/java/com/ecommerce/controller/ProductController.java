package com.ecommerce.controller;

import com.ecommerce.dao.CategoryDAO;
import com.ecommerce.dao.ProductDAO;
import com.ecommerce.model.Category;
import com.ecommerce.model.Product;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.List;

@WebServlet(name = "ProductController", urlPatterns = {"/home", "/products", "/product-details", ""})
public class ProductController extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private ProductDAO productDAO;
    private CategoryDAO categoryDAO;

    @Override
    public void init() {
        productDAO = new ProductDAO();
        categoryDAO = new CategoryDAO();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String servletPath = request.getServletPath();

        // Pass categories to all product views for the navigation bar
        List<Category> categories = categoryDAO.getAllActiveCategories();
        request.setAttribute("categories", categories);

        if ("/product-details".equals(servletPath)) {
            handleProductDetails(request, response);
        } else if ("/products".equals(servletPath)) {
            handleProductListing(request, response);
        } else {
            // Default: /home or root
            handleHome(request, response);
        }
    }

    private void handleHome(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        List<Product> products = productDAO.getAllActiveProducts();
        request.setAttribute("products", products);
        request.getRequestDispatcher("/WEB-INF/views/home.jsp").forward(request, response);
    }

    private void handleProductListing(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String query = request.getParameter("q");
        String categoryIdParam = request.getParameter("category");
        String size = request.getParameter("size");
        String sort = request.getParameter("sort");

        Integer categoryId = null;
        if (categoryIdParam != null && !categoryIdParam.trim().isEmpty()) {
            try {
                categoryId = Integer.parseInt(categoryIdParam.trim());
            } catch (NumberFormatException ignored) {}
        }

        List<Product> products = productDAO.searchProducts(query, categoryId, size, sort);
        request.setAttribute("products", products);
        request.setAttribute("selectedCategory", categoryId);
        request.setAttribute("selectedSize", size);
        request.setAttribute("selectedSort", sort);
        request.setAttribute("searchQuery", query);

        request.getRequestDispatcher("/WEB-INF/views/products.jsp").forward(request, response);
    }

    private void handleProductDetails(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String idParam = request.getParameter("id");
        if (idParam == null || idParam.trim().isEmpty()) {
            response.sendRedirect(request.getContextPath() + "/home");
            return;
        }

        try {
            int productId = Integer.parseInt(idParam.trim());
            Product product = productDAO.getProductById(productId);

            if (product == null) {
                response.sendRedirect(request.getContextPath() + "/home");
                return;
            }

            // Related products from same category
            List<Product> related = productDAO.getProductsByCategory(product.getCategoryId());
            // Remove current product from related list
            related.removeIf(p -> p.getProductId() == productId);

            request.setAttribute("product", product);
            request.setAttribute("relatedProducts", related);
            request.getRequestDispatcher("/WEB-INF/views/product-details.jsp").forward(request, response);

        } catch (NumberFormatException e) {
            response.sendRedirect(request.getContextPath() + "/home");
        }
    }
}
