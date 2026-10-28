package com.ecommerce.dao;

import com.ecommerce.model.Order;
import com.ecommerce.model.OrderItem;

import java.util.List;

/**
 * IOrderDAO - Interface defining persistence contracts for Order transactions.
 */
public interface IOrderDAO {
    Order createOrderFromCart(int userId, String deliveryAddress, String paymentMethod);
    List<Order> getOrdersByUser(int userId);
    List<Order> getOrdersByUserId(int userId);
    Order getOrderById(int orderId);
    Order getOrderById(int orderId, int userId);
    List<OrderItem> getOrderItems(int orderId);
    boolean updateOrderStatus(int orderId, String status);
}
