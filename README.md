# AURA — Java JSP, JDBC & MySQL E-Commerce Web Application

A full-stack, minimalist E-Commerce web application built with **HTML5, CSS3, JavaScript, Java Servlets, JSP (with JSTL), JDBC, and MySQL**, designed to run smoothly in **Eclipse IDE for Enterprise Java and Web Developers** with **Apache Tomcat 10+**.

---

## 🏗️ Architecture & Technology Stack

| Layer | Technologies Used |
|---|---|
| **Frontend** | HTML5, Modern Vanilla CSS3 (Custom Design System), Vanilla JavaScript |
| **View Layer** | JSP (JavaServer Pages), Jakarta JSTL (Core & Formatting Tags) |
| **Controller & Routing** | Java Servlets (`jakarta.servlet.*`), Servlet Filters (`AuthFilter`) |
| **Data Access Layer** | JDBC (Java Database Connectivity) with `PreparedStatement` |
| **Database** | MySQL 8.0+ (`ecommerce_db`) |
| **Build & Dependencies**| Apache Maven (`pom.xml`) |
| **Target IDE & Server** | Eclipse IDE for Enterprise Java / Apache Tomcat 10+ |

---

## 📁 Project Structure

```text
ecommerce-app/
├── pom.xml                               # Maven project configuration & dependencies
├── schema.sql                            # MySQL database tables & seed data
├── README.md                             # Setup & execution guide
├── uploads/                              # Directory for uploaded product images
└── src/
    └── main/
        ├── java/
        │   └── com/ecommerce/
        │       ├── model/                # User, Product, CartItem, Order
        │       ├── dao/                  # DBConnection, UserDAO, ProductDAO, OrderDAO
        │       ├── filter/               # AuthFilter (Route protection for admin/user)
        │       └── servlet/              # AuthServlet, ProductServlet, CartServlet, AdminServlet, ImageServlet
        └── webapp/
            ├── WEB-INF/
            │   └── web.xml               # Deployment descriptor & servlet mappings
            ├── css/
            │   └── style.css             # Responsive typography, components, and layout
            ├── js/
            │   └── main.js               # Client-side validation & interactivity
            ├── images/                   # Fallback sample product assets
            └── views/
                ├── header.jsp            # Common header & navigation
                ├── footer.jsp            # Common footer
                ├── index.jsp             # Catalog listing & search/filter
                ├── product-detail.jsp    # Single product view & Add to Cart
                ├── login.jsp             # User login form
                ├── register.jsp          # User registration form
                ├── cart.jsp              # Shopping cart & checkout form
                ├── orders.jsp            # Order confirmation & past history
                └── admin/
                    ├── dashboard.jsp     # Inventory management table
                    └── add-product.jsp   # Add product form with image upload
```

---

## 🚀 Step-by-Step Setup Guide in Eclipse IDE

### Step 1: Set Up MySQL Database
1. Open **MySQL Workbench** or your MySQL command-line client.
2. Open and execute [`schema.sql`](./schema.sql):
   ```sql
   SOURCE /path/to/ecommerce-app/schema.sql;
   ```
   Or copy-paste the contents of `schema.sql` into MySQL Workbench and run the script.
3. This creates the `ecommerce_db` database and seeds initial users and products.

### Step 2: Configure Database Credentials
Open [`src/main/java/com/ecommerce/dao/DBConnection.java`](./src/main/java/com/ecommerce/dao/DBConnection.java) and set your MySQL username and password:
```java
private static final String URL = "jdbc:mysql://localhost:3306/ecommerce_db?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true";
private static final String USER = "root";       // Your MySQL username
private static final String PASSWORD = "your_password"; // Your MySQL password
```

### Step 3: Import Project into Eclipse IDE
1. Launch **Eclipse IDE for Enterprise Java and Web Developers**.
2. Click **File** > **Import...**
3. Select **Maven** > **Existing Maven Projects** and click **Next**.
4. In **Root Directory**, click **Browse...** and select the `ecommerce-app` directory:
   `/Users/somaindra/.gemini/antigravity/scratch/ecommerce-app`
5. Click **Finish**. Eclipse will automatically resolve all Maven dependencies (`jakarta.servlet-api`, `jstl`, `mysql-connector-j`).

### Step 4: Configure Apache Tomcat 10 in Eclipse
1. In the **Servers** tab at the bottom of Eclipse:
   - Click the link *"No servers are available. Click this link to create a new server..."* (or right-click > **New** > **Server**).
2. Select **Apache** > **Tomcat v10.0 Server** (or v10.1).
3. Specify your local Tomcat installation directory and click **Next**.
4. Select `ecommerce-app` from the left list and click **Add >** to add it to the server.
5. Click **Finish**.

### Step 5: Run and Test the Application
1. Right-click on the `ecommerce-app` project in the Project Explorer.
2. Select **Run As** > **Run on Server**.
3. Choose your configured Tomcat 10 server and click **Finish**.
4. Open your browser and navigate to:
   ```
   http://localhost:8080/ecommerce-app/products
   ```

---

## 🔑 Default Accounts

| Role | Username | Password | Privileges |
|---|---|---|---|
| **Admin** | `admin` | `admin123` | Full access to Admin Panel, product catalog management, add/delete items |
| **Customer** | `john` | `customer123` | Browse catalog, add to cart, checkout, view order history |

---

## ✨ Features

- **Storefront & Catalog**:
  - Clean, responsive grid layout.
  - Search by product keyword and filter by category chips.
  - Product detail pages with price formatting and descriptions.
- **Cart & Checkout**:
  - Session-based shopping cart with real-time quantity modifiers and item removal.
  - Shipping address collection and order placement.
- **Order Management**:
  - Track order details, status, timestamps, and line-item breakdown in "My Orders".
- **Admin Dashboard**:
  - Secure admin area protected by `AuthFilter`.
  - Add new products with file upload handling (`@MultipartConfig`).
  - Delete existing products with automatic file cleanup.
- **Security & Session Management**:
  - Session-based user authentication.
  - Role-based authorization filter restricting administrative routes.
