# TrendVibe Atelier — Enterprise Java Full Stack E-Commerce Platform

A production-grade, full-stack E-Commerce web application developed strictly using the **Java Full Stack Architecture**:
- **Backend**: Java 21, Jakarta EE 10, Apache Tomcat 10.1, Java Servlets, JSP (JavaServer Pages), JSTL, and JDBC
- **Database**: MySQL 8.0 (`ecommerce_db`) with PreparedStatement security, connection pooling, and ACID transaction rollback
- **Frontend**: Responsive HTML5, CSS3 Luxury Design System, Vanilla JavaScript, and dynamic JSTL rendering
- **IDE**: Eclipse IDE for Enterprise Java and Web Developers (2024+)

---

## 🏛️ Project Architecture (MVC Pattern)

TrendVibe Atelier adheres strictly to the **Model-View-Controller (MVC)** design pattern and **SOLID** principles:

```
[ Browser / Client ]
        │  (HTTP GET/POST)
        ▼
[ Apache Tomcat 10.1 Container ]
        │  (web.xml URL Routing)
        ▼
[ Controller Layer: Java Servlets ]  <───> [ Session Management: HttpSession ]
  • ProductController (/home, /products, /product-details)
  • CartController (/cart, /cart/add, /cart/update, /cart/remove)
  • CheckoutController (/checkout, /checkout/place-order, /my-orders)
  • LoginController (/login) & RegisterController (/register)
  • ProfileController (/profile) & LogoutController (/logout)
        │
        ▼  (Calls Interface Contracts)
[ Data Access Layer: DAO Pattern ]
  • Interfaces: IUserDAO, IProductDAO, ICategoryDAO, ICartDAO, IOrderDAO
  • Implementations: UserDAO, ProductDAO, CategoryDAO, CartDAO, OrderDAO
  • DBConnection: Centralized JDBC Manager (DriverManager + UTF-8 + Auto-Reconnect)
        │
        ▼  (PreparedStatement SQL)
[ Relational Database: MySQL 8.0 (ecommerce_db) ]
  • Tables: users, categories, products, product_sizes, cart, cart_items, orders, order_items
        │
        ▼  (Maps ResultSet to POJOs)
[ Model Layer: POJOs ]
  • User, Product, ProductSize, Category, Cart, CartItem, Order, OrderItem
        │
        ▼  (request.setAttribute() + RequestDispatcher.forward())
[ View Layer: JSP + JSTL + Expression Language ]
  • Securely protected inside /WEB-INF/views/
  • home.jsp, products.jsp, product-details.jsp, cart.jsp, checkout.jsp, orders.jsp, etc.
```

---

## 🛠️ Technology Stack Breakdown

| Layer | Technologies & Tools |
| :--- | :--- |
| **Backend Language** | **Java (JDK 21 / JavaSE-21)** |
| **Web Container / Server** | **Apache Tomcat 10.1.36** |
| **Enterprise Framework** | **Jakarta EE 10 (Servlets, JSP, JSTL 2.0)** |
| **Database & Persistence** | **MySQL 8.0, JDBC (Java Database Connectivity), MySQL Connector/J 8.3.0** |
| **Architecture Patterns** | **MVC (Model-View-Controller), DAO Pattern, Singleton (DBConnection)** |
| **Frontend** | **HTML5, CSS3 (Luxury Atelier Design System), Vanilla JavaScript** |
| **Security** | **PreparedStatement (SQL Injection immunity), /WEB-INF/ protected views, Session Authentication** |
| **Build & Tooling** | **Apache Maven (`pom.xml`), Eclipse IDE for Enterprise Java** |

---

## 💾 Database Setup (MySQL)

1. Open Terminal or MySQL Workbench:
   ```bash
   mysql -u root -p
   ```
2. Run the database schema and sample data scripts included in the project:
   ```sql
   CREATE DATABASE IF NOT EXISTS ecommerce_db;
   USE ecommerce_db;
   ```
3. Import the schema and dataset:
   ```bash
   mysql -u root -p ecommerce_db < schema.sql
   mysql -u root -p ecommerce_db < sample_data.sql
   ```
4. Verify tables:
   - `users` (3 seed accounts: admin, customer, premium customer)
   - `categories` (5 departments: Men Fashion, Women Ethnic, Beauty, Footwear, Accessories)
   - `products` (27 curated catalog items)
   - `product_sizes` (inventory per size variant S, M, L, XL)
   - `cart` and `cart_items`
   - `orders` and `order_items`

---

## 💻 Running the Project in Eclipse IDE

1. **Import into Eclipse**:
   - Open **Eclipse IDE for Enterprise Java and Web Developers**.
   - Go to **File** → **Import...** → **General** → **Existing Projects into Workspace**.
   - Select root directory: `/Users/somaindra/Desktop/ecommerce-app` (or workspace folder).
   - Click **Finish**.

2. **Target Apache Tomcat 10.1**:
   - Right-click project → **Properties** → **Targeted Runtimes** → check **Apache Tomcat v10.1** → **Apply and Close**.

3. **Run on Server**:
   - Right-click `ecommerce-app` → **Run As** → **Run on Server**.
   - Select **Tomcat v10.1 Server at localhost** → Click **Finish**.
   - Browser opens automatically at: `http://localhost:8080/ecommerce-app/home`.

---

## 🌐 Live Storefront & Candidate Interview Material

- **Live Storefront Demo**: [https://indranil735.github.io/trendvibe-ecommerce/](https://indranil735.github.io/trendvibe-ecommerce/)
- **Candidate Interview Master Guide (PDF)**: Located on your Desktop at `TrendVibe_Project_Complete_Interview_Master_Guide.pdf`

---

## 📄 License & Attribution

Designed and developed by **Soma Indranil** as a production-grade Java Full Stack Portfolio Project.
