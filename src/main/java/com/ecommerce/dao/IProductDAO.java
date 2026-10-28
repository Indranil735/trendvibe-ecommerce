package com.ecommerce.dao;

import com.ecommerce.model.Product;
import com.ecommerce.model.ProductSize;

import java.util.List;

/**
 * IProductDAO - Interface defining persistence contracts for Product operations.
 */
public interface IProductDAO {
    List<Product> getAllActiveProducts();
    List<Product> getProductsByCategory(int categoryId);
    Product getProductById(int productId);
    List<Product> searchProducts(String query, Integer categoryId, String size, String sort);
    List<ProductSize> getProductSizes(int productId);
}
