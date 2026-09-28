package com.ecommerce.model;

import java.io.Serializable;
import java.sql.Timestamp;

public class CartItem implements Serializable {
    private static final long serialVersionUID = 1L;

    private int cartItemId;
    private int cartId;
    private int productId;
    private String sizeLabel;
    private int quantity;
    private double unitPrice;
    private Timestamp addedAt;

    // Associated product for UI rendering
    private Product product;

    public CartItem() {}

    public CartItem(int cartItemId, int cartId, int productId, String sizeLabel, int quantity, double unitPrice) {
        this.cartItemId = cartItemId;
        this.cartId = cartId;
        this.productId = productId;
        this.sizeLabel = sizeLabel;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    public double getSubtotal() {
        return Math.round((this.unitPrice * this.quantity) * 100.0) / 100.0;
    }

    public int getCartItemId() {
        return cartItemId;
    }

    public void setCartItemId(int cartItemId) {
        this.cartItemId = cartItemId;
    }

    public int getCartId() {
        return cartId;
    }

    public void setCartId(int cartId) {
        this.cartId = cartId;
    }

    public int getProductId() {
        return productId;
    }

    public void setProductId(int productId) {
        this.productId = productId;
    }

    public String getSizeLabel() {
        return sizeLabel;
    }

    public void setSizeLabel(String sizeLabel) {
        this.sizeLabel = sizeLabel;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public double getUnitPrice() {
        return unitPrice;
    }

    public void setUnitPrice(double unitPrice) {
        this.unitPrice = unitPrice;
    }

    public Timestamp getAddedAt() {
        return addedAt;
    }

    public void setAddedAt(Timestamp addedAt) {
        this.addedAt = addedAt;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }
}
