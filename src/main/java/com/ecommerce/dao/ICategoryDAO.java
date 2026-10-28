package com.ecommerce.dao;

import com.ecommerce.model.Category;

import java.util.List;

/**
 * ICategoryDAO - Interface defining persistence contracts for Category operations.
 */
public interface ICategoryDAO {
    List<Category> getAllActiveCategories();
    Category getCategoryById(int categoryId);
}
