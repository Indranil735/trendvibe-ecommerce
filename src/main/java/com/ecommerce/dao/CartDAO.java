package com.ecommerce.dao;

import com.ecommerce.model.Cart;
import com.ecommerce.model.CartItem;
import com.ecommerce.model.Product;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

public class CartDAO {
    private static final Logger LOGGER = Logger.getLogger(CartDAO.class.getName());

    public Cart getOrCreateCart(int userId) {
        String selectSql = "SELECT cart_id, user_id, created_at, updated_at FROM cart WHERE user_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(selectSql)) {

            ps.setInt(1, userId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    Cart cart = new Cart();
                    cart.setCartId(rs.getInt("cart_id"));
                    cart.setUserId(rs.getInt("user_id"));
                    cart.setCreatedAt(rs.getTimestamp("created_at"));
                    cart.setUpdatedAt(rs.getTimestamp("updated_at"));
                    return cart;
                }
            }

            // Create new cart if none exists
            String insertSql = "INSERT INTO cart (user_id) VALUES (?)";
            try (PreparedStatement insertPs = conn.prepareStatement(insertSql, Statement.RETURN_GENERATED_KEYS)) {
                insertPs.setInt(1, userId);
                insertPs.executeUpdate();
                try (ResultSet genRs = insertPs.getGeneratedKeys()) {
                    if (genRs.next()) {
                        Cart newCart = new Cart();
                        newCart.setCartId(genRs.getInt(1));
                        newCart.setUserId(userId);
                        return newCart;
                    }
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error in getOrCreateCart for user: " + userId, e);
        }
        return null;
    }

    public Cart getCartWithItems(int userId) {
        Cart cart = getOrCreateCart(userId);
        if (cart == null) {
            return null;
        }

        List<CartItem> items = new ArrayList<>();
        String sql = "SELECT ci.*, p.product_name, p.image_url, p.discount_percent, p.category_id " +
                     "FROM cart_items ci " +
                     "JOIN products p ON ci.product_id = p.product_id " +
                     "WHERE ci.cart_id = ? ORDER BY ci.cart_item_id DESC";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, cart.getCartId());
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    CartItem item = new CartItem();
                    item.setCartItemId(rs.getInt("cart_item_id"));
                    item.setCartId(rs.getInt("cart_id"));
                    item.setProductId(rs.getInt("product_id"));
                    item.setSizeLabel(rs.getString("size_label"));
                    item.setQuantity(rs.getInt("quantity"));
                    item.setUnitPrice(rs.getDouble("unit_price"));
                    item.setAddedAt(rs.getTimestamp("added_at"));

                    Product p = new Product();
                    p.setProductId(item.getProductId());
                    p.setProductName(rs.getString("product_name"));
                    p.setImageUrl(rs.getString("image_url"));
                    p.setDiscountPercent(rs.getDouble("discount_percent"));
                    p.setFinalPrice(item.getUnitPrice());
                    item.setProduct(p);

                    items.add(item);
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching cart items for cart: " + cart.getCartId(), e);
        }

        cart.setItems(items);
        return cart;
    }

    public boolean addItemToCart(int cartId, int productId, String sizeLabel, int quantity, double unitPrice) {
        // Check if the item already exists with the same size in the cart
        String checkSql = "SELECT cart_item_id, quantity FROM cart_items WHERE cart_id = ? AND product_id = ? AND size_label = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement checkPs = conn.prepareStatement(checkSql)) {

            checkPs.setInt(1, cartId);
            checkPs.setInt(2, productId);
            checkPs.setString(3, sizeLabel);

            try (ResultSet rs = checkPs.executeQuery()) {
                if (rs.next()) {
                    int existingId = rs.getInt("cart_item_id");
                    int existingQty = rs.getInt("quantity");
                    return updateItemQuantity(existingId, existingQty + quantity);
                }
            }

            // Insert new cart item
            String insertSql = "INSERT INTO cart_items (cart_id, product_id, size_label, quantity, unit_price) VALUES (?, ?, ?, ?, ?)";
            try (PreparedStatement insertPs = conn.prepareStatement(insertSql)) {
                insertPs.setInt(1, cartId);
                insertPs.setInt(2, productId);
                insertPs.setString(3, sizeLabel);
                insertPs.setInt(4, quantity);
                insertPs.setDouble(5, unitPrice);
                return insertPs.executeUpdate() > 0;
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error adding item to cart", e);
        }
        return false;
    }

    public boolean updateItemQuantity(int cartItemId, int quantity) {
        if (quantity <= 0) {
            return removeItem(cartItemId);
        }

        String sql = "UPDATE cart_items SET quantity = ? WHERE cart_item_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, quantity);
            ps.setInt(2, cartItemId);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error updating cart item quantity: " + cartItemId, e);
        }
        return false;
    }

    public boolean removeItem(int cartItemId) {
        String sql = "DELETE FROM cart_items WHERE cart_item_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, cartItemId);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error removing cart item: " + cartItemId, e);
        }
        return false;
    }

    public boolean clearCart(int cartId) {
        String sql = "DELETE FROM cart_items WHERE cart_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, cartId);
            ps.executeUpdate();
            return true;
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error clearing cart: " + cartId, e);
        }
        return false;
    }
}
