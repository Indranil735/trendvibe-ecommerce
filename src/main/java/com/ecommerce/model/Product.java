package com.ecommerce.model;

import java.io.Serializable;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

public class Product implements Serializable {
    private static final long serialVersionUID = 1L;

    private int productId;
    private int categoryId;
    private String productName;
    private String description;
    private double discountPercent;
    private String imageUrl;
    private boolean isActive;
    private Timestamp createdAt;

    // Derived / UI fields
    private String categoryName;
    private double basePrice = 1499.00; // Base MRP default
    private double finalPrice;
    private List<ProductSize> sizes = new ArrayList<>();

    public Product() {}

    public Product(int productId, int categoryId, String productName, String description,
                   double discountPercent, String imageUrl, boolean isActive) {
        this.productId = productId;
        this.categoryId = categoryId;
        this.productName = productName;
        this.description = description;
        this.discountPercent = discountPercent;
        this.imageUrl = imageUrl;
        this.isActive = isActive;
        calculatePrices();
    }

    public void calculatePrices() {
        if (this.basePrice <= 0) {
            this.basePrice = 1499.00;
        }
        if (discountPercent > 0) {
            this.finalPrice = Math.round((basePrice * (1.0 - (discountPercent / 100.0))) * 100.0) / 100.0;
        } else {
            this.finalPrice = this.basePrice;
        }
    }

    public int getProductId() {
        return productId;
    }

    public void setProductId(int productId) {
        this.productId = productId;
    }

    public int getCategoryId() {
        return categoryId;
    }

    public void setCategoryId(int categoryId) {
        this.categoryId = categoryId;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public double getDiscountPercent() {
        return discountPercent;
    }

    public void setDiscountPercent(double discountPercent) {
        this.discountPercent = discountPercent;
        calculatePrices();
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }

    public boolean isActive() {
        return isActive;
    }

    public void setActive(boolean active) {
        isActive = active;
    }

    public Timestamp getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Timestamp createdAt) {
        this.createdAt = createdAt;
    }

    public String getCategoryName() {
        return categoryName;
    }

    public void setCategoryName(String categoryName) {
        this.categoryName = categoryName;
    }

    public double getBasePrice() {
        return basePrice;
    }

    public void setBasePrice(double basePrice) {
        this.basePrice = basePrice;
        calculatePrices();
    }

    public double getFinalPrice() {
        if (finalPrice <= 0) {
            calculatePrices();
        }
        return finalPrice;
    }

    public void setFinalPrice(double finalPrice) {
        this.finalPrice = finalPrice;
    }

    public List<ProductSize> getSizes() {
        return sizes;
    }

    public void setSizes(List<ProductSize> sizes) {
        this.sizes = sizes;
    }
}
