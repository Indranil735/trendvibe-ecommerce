package com.ecommerce.dao;

import com.ecommerce.model.User;

/**
 * IUserDAO - Interface defining persistence contracts for User operations.
 */
public interface IUserDAO {
    boolean registerUser(User user);
    User loginUser(String email, String password);
    User getUserById(int userId);
    boolean emailExists(String email);
    boolean updateUser(User user);
}
