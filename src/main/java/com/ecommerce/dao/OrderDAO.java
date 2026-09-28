package com.ecommerce.dao;

import com.ecommerce.model.Cart;
import com.ecommerce.model.CartItem;
import com.ecommerce.model.Order;
import com.ecommerce.model.OrderItem;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

public class OrderDAO {
    private static final Logger LOGGER = Logger.getLogger(OrderDAO.class.getName());

    public Order createOrderFromCart(int userId, String deliveryAddress, String paymentMethod) {
        CartDAO cartDAO = new CartDAO();
        Cart cart = cartDAO.getCartWithItems(userId);

        if (cart == null || cart.getItems() == null || cart.getItems().isEmpty()) {
            LOGGER.warning("Cannot create order: Cart is empty for user " + userId);
            return null;
        }

        Connection conn = null;
        try {
            conn = DBConnection.getConnection();
            conn.setAutoCommit(false); // Begin transaction

            double totalAmount = cart.getTotalAmount();

            // 1. Insert into orders table
            String orderSql = "INSERT INTO orders (user_id, total_amount, payment_method, order_status, delivery_address) " +
                              "VALUES (?, ?, ?, 'Placed', ?)";
            int orderId = 0;
            try (PreparedStatement orderPs = conn.prepareStatement(orderSql, Statement.RETURN_GENERATED_KEYS)) {
                orderPs.setInt(1, userId);
                orderPs.setDouble(2, totalAmount);
                orderPs.setString(3, paymentMethod);
                orderPs.setString(4, deliveryAddress);
                orderPs.executeUpdate();

                try (ResultSet rs = orderPs.getGeneratedKeys()) {
                    if (rs.next()) {
                        orderId = rs.getInt(1);
                    }
                }
            }

            if (orderId == 0) {
                conn.rollback();
                return null;
            }

            // 2. Insert items into order_items table and update stock
            String itemSql = "INSERT INTO order_items (order_id, product_id, product_name, quantity, unit_price, subtotal, size_label) " +
                             "VALUES (?, ?, ?, ?, ?, ?, ?)";
            String stockSql = "UPDATE product_sizes SET stock_quantity = GREATEST(0, stock_quantity - ?) " +
                              "WHERE product_id = ? AND size_label = ?";

            try (PreparedStatement itemPs = conn.prepareStatement(itemSql);
                 PreparedStatement stockPs = conn.prepareStatement(stockSql)) {

                for (CartItem ci : cart.getItems()) {
                    String pName = (ci.getProduct() != null) ? ci.getProduct().getProductName() : "Product #" + ci.getProductId();
                    itemPs.setInt(1, orderId);
                    itemPs.setInt(2, ci.getProductId());
                    itemPs.setString(3, pName);
                    itemPs.setInt(4, ci.getQuantity());
                    itemPs.setDouble(5, ci.getUnitPrice());
                    itemPs.setDouble(6, ci.getSubtotal());
                    itemPs.setString(7, ci.getSizeLabel());
                    itemPs.addBatch();

                    stockPs.setInt(1, ci.getQuantity());
                    stockPs.setInt(2, ci.getProductId());
                    stockPs.setString(3, ci.getSizeLabel());
                    stockPs.addBatch();
                }

                itemPs.executeBatch();
                stockPs.executeBatch();
            }

            // 3. Clear cart items
            String clearCartSql = "DELETE FROM cart_items WHERE cart_id = ?";
            try (PreparedStatement clearPs = conn.prepareStatement(clearCartSql)) {
                clearPs.setInt(1, cart.getCartId());
                clearPs.executeUpdate();
            }

            conn.commit(); // Transaction successful!

            Order order = new Order();
            order.setOrderId(orderId);
            order.setUserId(userId);
            order.setTotalAmount(totalAmount);
            order.setPaymentMethod(paymentMethod);
            order.setOrderStatus("Placed");
            order.setDeliveryAddress(deliveryAddress);
            order.setOrderDate(new Timestamp(System.currentTimeMillis()));

            return order;

        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Transaction failed while creating order for user: " + userId, e);
            if (conn != null) {
                try {
                    conn.rollback();
                } catch (SQLException ex) {
                    LOGGER.log(Level.SEVERE, "Failed rollback", ex);
                }
            }
        } finally {
            if (conn != null) {
                try {
                    conn.setAutoCommit(true);
                    conn.close();
                } catch (SQLException ignored) {}
            }
        }
        return null;
    }

    public List<Order> getOrdersByUser(int userId) {
        List<Order> orders = new ArrayList<>();
        String sql = "SELECT * FROM orders WHERE user_id = ? ORDER BY order_id DESC";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, userId);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    Order order = extractOrder(rs);
                    order.setOrderItems(getOrderItems(order.getOrderId()));
                    orders.add(order);
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching orders for user: " + userId, e);
        }
        return orders;
    }

    public Order getOrderById(int orderId, int userId) {
        String sql = "SELECT * FROM orders WHERE order_id = ? AND user_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, orderId);
            ps.setInt(2, userId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    Order order = extractOrder(rs);
                    order.setOrderItems(getOrderItems(orderId));
                    return order;
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching order by ID: " + orderId, e);
        }
        return null;
    }

    public List<OrderItem> getOrderItems(int orderId) {
        List<OrderItem> items = new ArrayList<>();
        String sql = "SELECT oi.*, p.image_url FROM order_items oi " +
                     "LEFT JOIN products p ON oi.product_id = p.product_id " +
                     "WHERE oi.order_id = ? ORDER BY oi.order_item_id ASC";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, orderId);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    OrderItem item = new OrderItem();
                    item.setOrderItemId(rs.getInt("order_item_id"));
                    item.setOrderId(rs.getInt("order_id"));
                    item.setProductId(rs.getInt("product_id"));
                    item.setProductName(rs.getString("product_name"));
                    item.setQuantity(rs.getInt("quantity"));
                    item.setUnitPrice(rs.getDouble("unit_price"));
                    item.setSubtotal(rs.getDouble("subtotal"));
                    item.setSizeLabel(rs.getString("size_label"));
                    item.setImageUrl(rs.getString("image_url"));
                    items.add(item);
                }
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error fetching order items for order: " + orderId, e);
        }
        return items;
    }

    private Order extractOrder(ResultSet rs) throws SQLException {
        Order order = new Order();
        order.setOrderId(rs.getInt("order_id"));
        order.setUserId(rs.getInt("user_id"));
        order.setOrderDate(rs.getTimestamp("order_date"));
        order.setTotalAmount(rs.getDouble("total_amount"));
        order.setPaymentMethod(rs.getString("payment_method"));
        order.setOrderStatus(rs.getString("order_status"));
        order.setDeliveryAddress(rs.getString("delivery_address"));
        return order;
    }
}
