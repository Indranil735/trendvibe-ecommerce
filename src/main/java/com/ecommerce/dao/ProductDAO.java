package com.ecommerce.dao;

import com.ecommerce.model.Product;
import com.ecommerce.model.ProductSize;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

public class ProductDAO {
    private static final Logger LOGGER = Logger.getLogger(ProductDAO.class.getName());

    public List<Product> getAllActiveProducts() {
        List<Product> list = new ArrayList<>();
        String sql = "SELECT p.*, c.category_name FROM products p " +
                     "JOIN categories c ON p.category_id = c.category_id " +
                     "WHERE p.is_active = TRUE ORDER BY p.product_id ASC";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {

            while (rs.next()) {
                Product p = extractProduct(rs);
                p.setSizes(getProductSizes(p.getProductId()));
                list.add(p);
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching active products", e);
        }
        return list;
    }

    public List<Product> getProductsByCategory(int categoryId) {
        List<Product> list = new ArrayList<>();
        String sql = "SELECT p.*, c.category_name FROM products p " +
                     "JOIN categories c ON p.category_id = c.category_id " +
                     "WHERE p.category_id = ? AND p.is_active = TRUE ORDER BY p.product_id ASC";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, categoryId);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    Product p = extractProduct(rs);
                    p.setSizes(getProductSizes(p.getProductId()));
                    list.add(p);
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching products for category: " + categoryId, e);
        }
        return list;
    }

    public Product getProductById(int productId) {
        String sql = "SELECT p.*, c.category_name FROM products p " +
                     "JOIN categories c ON p.category_id = c.category_id " +
                     "WHERE p.product_id = ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, productId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    Product p = extractProduct(rs);
                    p.setSizes(getProductSizes(p.getProductId()));
                    return p;
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching product by ID: " + productId, e);
        }
        return null;
    }

    public List<Product> searchProducts(String query, Integer categoryId, String size, String sortBy) {
        List<Product> list = new ArrayList<>();
        StringBuilder sql = new StringBuilder(
            "SELECT DISTINCT p.*, c.category_name FROM products p " +
            "JOIN categories c ON p.category_id = c.category_id " +
            "LEFT JOIN product_sizes ps ON p.product_id = ps.product_id " +
            "WHERE p.is_active = TRUE "
        );

        List<Object> params = new ArrayList<>();

        if (query != null && !query.trim().isEmpty()) {
            sql.append("AND (LOWER(p.product_name) LIKE ? OR LOWER(p.description) LIKE ? OR LOWER(c.category_name) LIKE ?) ");
            String q = "%" + query.trim().toLowerCase() + "%";
            params.add(q);
            params.add(q);
            params.add(q);
        }

        if (categoryId != null && categoryId > 0) {
            sql.append("AND p.category_id = ? ");
            params.add(categoryId);
        }

        if (size != null && !size.trim().isEmpty()) {
            sql.append("AND ps.size_label = ? AND ps.is_available = TRUE ");
            params.add(size.trim());
        }

        if ("discount".equalsIgnoreCase(sortBy)) {
            sql.append("ORDER BY p.discount_percent DESC ");
        } else if ("newest".equalsIgnoreCase(sortBy)) {
            sql.append("ORDER BY p.product_id DESC ");
        } else {
            sql.append("ORDER BY p.product_id ASC ");
        }

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql.toString())) {

            for (int i = 0; i < params.size(); i++) {
                ps.setObject(i + 1, params.get(i));
            }

            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    Product p = extractProduct(rs);
                    p.setSizes(getProductSizes(p.getProductId()));
                    list.add(p);
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error executing product search", e);
        }
        return list;
    }

    public List<ProductSize> getProductSizes(int productId) {
        List<ProductSize> sizes = new ArrayList<>();
        String sql = "SELECT * FROM product_sizes WHERE product_id = ? AND is_available = TRUE ORDER BY product_size_id ASC";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, productId);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    ProductSize size = new ProductSize();
                    size.setProductSizeId(rs.getInt("product_size_id"));
                    size.setProductId(rs.getInt("product_id"));
                    size.setSizeLabel(rs.getString("size_label"));
                    size.setStockQuantity(rs.getInt("stock_quantity"));
                    size.setSkuCode(rs.getString("sku_code"));
                    size.setAvailable(rs.getBoolean("is_available"));
                    sizes.add(size);
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching product sizes for product: " + productId, e);
        }
        return sizes;
    }

    public boolean decrementSizeStock(int productId, String sizeLabel, int qty) {
        String sql = "UPDATE product_sizes SET stock_quantity = GREATEST(0, stock_quantity - ?) " +
                     "WHERE product_id = ? AND size_label = ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, qty);
            ps.setInt(2, productId);
            ps.setString(3, sizeLabel);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error decrementing size stock", e);
        }
        return false;
    }

    private Product extractProduct(ResultSet rs) throws SQLException {
        Product p = new Product();
        p.setProductId(rs.getInt("product_id"));
        p.setCategoryId(rs.getInt("category_id"));
        p.setProductName(rs.getString("product_name"));
        p.setDescription(rs.getString("description"));
        p.setDiscountPercent(rs.getDouble("discount_percent"));
        p.setImageUrl(rs.getString("image_url"));
        p.setActive(rs.getBoolean("is_active"));
        try {
            p.setCategoryName(rs.getString("category_name"));
        } catch (SQLException ignored) {}
        try {
            p.setCreatedAt(rs.getTimestamp("created_at"));
        } catch (SQLException ignored) {}
        p.calculatePrices();
        return p;
    }
}
