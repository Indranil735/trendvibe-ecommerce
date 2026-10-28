package com.ecommerce.dao;

import com.ecommerce.model.Cart;

/**
 * ICartDAO - Interface defining persistence contracts for Shopping Cart operations.
 */
public interface ICartDAO {
    Cart getOrCreateCart(int userId);
    Cart getCartWithItems(int userId);
    boolean addItemToCart(int cartId, int productId, String sizeLabel, int quantity, double unitPrice);
    boolean updateItemQuantity(int cartItemId, int quantity);
    boolean removeItem(int cartItemId);
    boolean clearCart(int cartId);
}
