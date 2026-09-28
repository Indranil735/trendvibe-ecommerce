package com.ecommerce.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * DBConnection - Centralized JDBC connection manager for MySQL database.
 * Reads configuration from System properties, Environment variables, or defaults.
 */
public class DBConnection {
    private static final Logger LOGGER = Logger.getLogger(DBConnection.class.getName());

    private static final String DEFAULT_HOST = "localhost";
    private static final String DEFAULT_PORT = "3306";
    private static final String DEFAULT_DB = "ecommerce_db";
    private static final String DEFAULT_USER = "root";
    private static final String DEFAULT_PASSWORD = "root"; // can also be blank or custom

    static {
        try {
            // Load MySQL JDBC driver (supports modern CJ and legacy driver)
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            try {
                Class.forName("com.mysql.jdbc.Driver");
            } catch (ClassNotFoundException ex) {
                LOGGER.log(Level.SEVERE, "MySQL JDBC Driver not found in classpath", ex);
            }
        }
    }

    public static Connection getConnection() throws SQLException {
        String host = getPropertyOrEnv("DB_HOST", DEFAULT_HOST);
        String port = getPropertyOrEnv("DB_PORT", DEFAULT_PORT);
        String dbName = getPropertyOrEnv("DB_NAME", DEFAULT_DB);
        String user = getPropertyOrEnv("DB_USER", DEFAULT_USER);
        String password = getPropertyOrEnv("DB_PASSWORD", DEFAULT_PASSWORD);

        String url = String.format(
            "jdbc:mysql://%s:%s/%s?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC&characterEncoding=UTF-8",
            host, port, dbName
        );

        try {
            return DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            // Retry with empty password if root fails (common on local Mac homebrew MySQL)
            if ("root".equals(password)) {
                try {
                    return DriverManager.getConnection(url, user, "");
                } catch (SQLException ignored) {
                    // Fall back to throwing original exception
                }
            }
            LOGGER.log(Level.SEVERE, "Failed to connect to MySQL database at " + url, e);
            throw e;
        }
    }

    private static String getPropertyOrEnv(String key, String defaultValue) {
        String val = System.getProperty(key);
        if (val != null && !val.trim().isEmpty()) {
            return val.trim();
        }
        val = System.getenv(key);
        if (val != null && !val.trim().isEmpty()) {
            return val.trim();
        }
        return defaultValue;
    }

    public static void closeConnection(Connection conn) {
        if (conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                LOGGER.log(Level.WARNING, "Error closing connection", e);
            }
        }
    }
}
