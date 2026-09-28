package com.ecommerce.dao;

import com.ecommerce.model.Category;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

public class CategoryDAO {
    private static final Logger LOGGER = Logger.getLogger(CategoryDAO.class.getName());

    public List<Category> getAllActiveCategories() {
        List<Category> categories = new ArrayList<>();
        String sql = "SELECT * FROM categories WHERE is_active = TRUE ORDER BY category_id ASC";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {

            while (rs.next()) {
                categories.add(extractCategory(rs));
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching active categories", e);
        }
        return categories;
    }

    public Category getCategoryById(int categoryId) {
        String sql = "SELECT * FROM categories WHERE category_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, categoryId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return extractCategory(rs);
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching category by ID: " + categoryId, e);
        }
        return null;
    }

    private Category extractCategory(ResultSet rs) throws SQLException {
        Category cat = new Category();
        cat.setCategoryId(rs.getInt("category_id"));
        cat.setCategoryName(rs.getString("category_name"));
        cat.setDescription(rs.getString("description"));
        cat.setActive(rs.getBoolean("is_active"));
        return cat;
    }
}
