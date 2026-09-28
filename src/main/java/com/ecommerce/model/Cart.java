package com.ecommerce.model;

import java.io.Serializable;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

public class Cart implements Serializable {
    private static final long serialVersionUID = 1L;

    private int cartId;
    private int userId;
    private Timestamp createdAt;
    private Timestamp updatedAt;

    private List<CartItem> items = new ArrayList<>();

    public Cart() {}

    public Cart(int cartId, int userId) {
        this.cartId = cartId;
        this.userId = userId;
    }

    public int getItemCount() {
        int count = 0;
        for (CartItem item : items) {
            count += item.getQuantity();
        }
        return count;
    }

    public double getTotalAmount() {
        double total = 0.0;
        for (CartItem item : items) {
            total += item.getSubtotal();
        }
        return Math.round(total * 100.0) / 100.0;
    }

    public double getTotalMRP() {
        double mrp = 0.0;
        for (CartItem item : items) {
            double itemBase = (item.getProduct() != null && item.getProduct().getBasePrice() > 0)
                    ? item.getProduct().getBasePrice()
                    : item.getUnitPrice() * 1.5;
            mrp += itemBase * item.getQuantity();
        }
        return Math.round(mrp * 100.0) / 100.0;
    }

    public double getTotalDiscount() {
        double diff = getTotalMRP() - getTotalAmount();
        return diff > 0 ? Math.round(diff * 100.0) / 100.0 : 0.0;
    }

    public int getCartId() {
        return cartId;
    }

    public void setCartId(int cartId) {
        this.cartId = cartId;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public Timestamp getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Timestamp createdAt) {
        this.createdAt = createdAt;
    }

    public Timestamp getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(Timestamp updatedAt) {
        this.updatedAt = updatedAt;
    }

    public List<CartItem> getItems() {
        return items;
    }

    public void setItems(List<CartItem> items) {
        this.items = items;
    }
}
