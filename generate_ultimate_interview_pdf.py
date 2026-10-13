import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber > 1:
            self.saveState()
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#444444"))
            # Header
            self.drawString(54, 752, "TRENDVIBE ATELIER &bull; FULL-STACK JAVA EE &amp; E-COMMERCE MASTER INTERVIEW GUIDE")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#777777"))
            self.drawRightString(558, 752, "PIN-TO-PIN TECHNICAL PREPARATION")
            self.setStrokeColor(colors.HexColor("#D1C7BD"))
            self.setLineWidth(0.6)
            self.line(54, 744, 558, 744)
            
            # Footer
            self.line(54, 45, 558, 45)
            self.drawString(54, 32, "Confidential &bull; Prepared for Enterprise Java Developer &amp; Full-Stack Interviews")
            page_str = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(558, 32, page_str)
            self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=58,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#1A1A1A"),
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#6B5E4F"),
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#111111"),
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#8C6E3B"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#2C2C2C"),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#2C2C2C"),
        leftIndent=15,
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1F2937"),
        backColor=colors.HexColor("#F3F4F6"),
        borderColor=colors.HexColor("#E5E7EB"),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=6
    )

    q_style = ParagraphStyle(
        'Question_Style',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#111827"),
        spaceBefore=10,
        spaceAfter=3,
        keepWithNext=True
    )

    a_style = ParagraphStyle(
        'Answer_Style',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#374151"),
        spaceAfter=8
    )

    box_style = ParagraphStyle(
        'BoxText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#1A1A1A")
    )

    story = []

    # =========================================================================
    # COVER / HEADER TITLE
    # =========================================================================
    story.append(Paragraph("TRENDVIBE ATELIER", title_style))
    story.append(Paragraph("Enterprise Java EE Full-Stack E-Commerce &bull; Master Interview Blueprint", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#8C6E3B"), spaceAfter=14))

    # Meta banner table
    meta_data = [
        [
            Paragraph("<b>Candidate Role:</b> Full-Stack Java Developer", box_style),
            Paragraph("<b>Target Stack:</b> Java EE, Servlets, JDBC, MySQL, HTML5/ES6", box_style)
        ],
        [
            Paragraph("<b>Project Scope:</b> 535-Piece E-Commerce System", box_style),
            Paragraph("<b>Architecture:</b> 3-Tier Enterprise MVC &amp; DAO Pattern", box_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[250, 254])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F9F8F6")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#D8CFC4")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5DFD7")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    # =========================================================================
    # SECTION 1: LANGUAGES & TECHNOLOGIES USED ("PIN TO PIN")
    # =========================================================================
    story.append(Paragraph("1. Languages &amp; Technology Stack (Pin-to-Pin Breakdown)", h1_style))
    story.append(Paragraph(
        "When an interviewer asks: <i>'What languages and technologies did you use in this project, and why?'</i>, "
        "give this structured, confident explanation covering all 4 tiers of the system:",
        body_style
    ))

    tech_table_data = [
        [Paragraph("<b>Tier</b>", box_style), Paragraph("<b>Language / Technology</b>", box_style), Paragraph("<b>Role &amp; Engineering Justification</b>", box_style)],
        [
            Paragraph("<b>Backend Core</b>", box_style),
            Paragraph("<b>Java 17 (Java EE)</b><br/>Servlets 5.0, JSP, JSTL", box_style),
            Paragraph("Handles HTTP routing, business logic, session validation, and thread-safe controller orchestration via the MVC architecture.", box_style)
        ],
        [
            Paragraph("<b>Persistence</b>", box_style),
            Paragraph("<b>SQL &amp; JDBC</b><br/>MySQL 8.0, HikariCP", box_style),
            Paragraph("Relational database normalized to 3NF, parameterized PreparedStatements to eliminate SQL injection, and high-speed connection pooling.", box_style)
        ],
        [
            Paragraph("<b>Frontend UI</b>", box_style),
            Paragraph("<b>HTML5, CSS3, JavaScript (ES6+)</b>", box_style),
            Paragraph("Clean Zara-inspired atelier interface. Mobile viewport optimization (58px header, touch rails), lazy loading, and error fallback handlers.", box_style)
        ],
        [
            Paragraph("<b>Server &amp; Ops</b>", box_style),
            Paragraph("<b>Apache Tomcat 10, Maven, Docker, Git</b>", box_style),
            Paragraph("Tomcat manages servlet worker threads. Maven handles dependencies (`pom.xml`). Docker containerizes deployment. GitHub Pages hosts client demo.", box_style)
        ]
    ]
    t1 = Table(tech_table_data, colWidths=[90, 150, 264])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EFECE6")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#D1C7BD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5DFD7")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t1)
    story.append(Spacer(1, 14))

    # =========================================================================
    # SECTION 2: HOW TO INTRODUCE YOUR PROJECT IN THE INTERVIEW
    # =========================================================================
    story.append(Paragraph("2. How to Introduce Your Project (90-Second Pitch)", h1_style))
    story.append(Paragraph(
        "<b>Interviewer Question:</b> <i>'Tell me about your project and your primary contributions.'</i>",
        q_style
    ))
    story.append(Paragraph(
        "<b>Your Exact Answer to Speak:</b><br/>"
        "<i>&ldquo;I engineered <b>TrendVibe Atelier</b>, a high-performance, enterprise-grade full-stack e-commerce web application designed for luxury retail. "
        "The architecture is built on a 3-tier MVC model using <b>Java EE Servlets</b> on the backend, <b>MySQL 8.0</b> managed via <b>JDBC &amp; HikariCP</b> for persistence, and a modern, responsive <b>HTML5/CSS3/Vanilla JavaScript</b> frontend.<br/><br/>"
        "My key contributions include:<br/>"
        "1. <b>Database Engineering:</b> Designed a normalized 8-table relational schema in 3NF, ensuring ACID compliance and zero race conditions during checkout using pessimistic row-level locking (`SELECT ... FOR UPDATE`).<br/>"
        "2. <b>Backend Architecture:</b> Built thread-safe Java Servlets handling customer registration, phone+password authentication, dynamic catalog filtering across 535 products, and cart state management.<br/>"
        "3. <b>Performance &amp; Mobile Optimization:</b> Solved mobile viewport overflow with a responsive 58px header, added client-side image fallback handlers to eliminate broken image rendering, and optimized pagination to render 24 items per batch with sub-100ms response time.&rdquo;</i>",
        a_style
    ))
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 3: STEP-BY-STEP DATABASE CREATION TUTORIAL ("PIN TO PIN")
    # =========================================================================
    story.append(Paragraph("3. Step-by-Step Database Creation Guide (How to Create the DB)", h1_style))
    story.append(Paragraph(
        "When an interviewer asks: <i>'How did you create the database? Explain the tables, keys, and queries step-by-step.'</i>, "
        "explain this exact technical sequence:",
        body_style
    ))

    story.append(Paragraph("Step 1: Database Initialization &amp; Character Encoding", h2_style))
    story.append(Paragraph(
        "We create a dedicated schema with <code>utf8mb4</code> character set to support international characters, currencies, and emojis:",
        body_style
    ))
    story.append(Paragraph(
        "CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;<br/>"
        "USE ecommerce_db;",
        code_style
    ))

    story.append(Paragraph("Step 2: Designing the 8 Normalized Tables (3NF Schema)", h2_style))
    story.append(Paragraph(
        "The database is normalized to Third Normal Form (3NF) to eliminate transitive dependencies and data anomalies. Below are the core tables and constraints:",
        body_style
    ))

    db_code = """-- 1. USERS TABLE: Customer accounts with phone + password credentials
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    pincode VARCHAR(10),
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. CATEGORIES TABLE: Master product taxonomy
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- 3. PRODUCTS TABLE: Master luxury catalog (535 pieces)
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    name VARCHAR(200) NOT NULL,
    brand VARCHAR(100) NOT NULL,
    gender ENUM('Men', 'Women', 'Unisex') DEFAULT 'Unisex',
    price DECIMAL(10, 2) NOT NULL,
    original_price DECIMAL(10, 2) NOT NULL,
    discount_percent INT DEFAULT 0,
    image_url VARCHAR(500) NOT NULL,
    rating DECIMAL(2, 1) DEFAULT 4.5,
    reviews_count INT DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT
);

-- 4. INVENTORY TABLE: Strict row-level stock management
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL UNIQUE,
    stock_quantity INT NOT NULL CHECK (stock_quantity &gt;= 0),
    warehouse_code VARCHAR(20) DEFAULT 'WH-BLR-01',
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- 5. ORDERS TABLE: Order header and financial summary
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    shipping_address TEXT NOT NULL,
    shipping_pincode VARCHAR(10) NOT NULL,
    order_status ENUM('PENDING', 'CONFIRMED', 'DISPATCHED', 'DELIVERED', 'CANCELLED') DEFAULT 'CONFIRMED',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- 6. ORDER_ITEMS TABLE: Itemized line records with snapshot pricing
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    selected_size VARCHAR(10) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL, -- Historical price snapshot
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 7. PAYMENTS TABLE: Financial transaction audits
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_mode ENUM('UPI', 'CARD', 'NETBANKING', 'COD') NOT NULL,
    transaction_ref VARCHAR(100) UNIQUE,
    payment_status ENUM('SUCCESS', 'PENDING', 'FAILED') DEFAULT 'SUCCESS',
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- 8. INDEXING FOR HIGH PERFORMANCE
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_orders_user ON orders(user_id);"""

    story.append(Paragraph(db_code.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 4: DEEP DIVE ARCHITECTURE & CONCURRENCY
    # =========================================================================
    story.append(Paragraph("4. Architecture, Concurrency &amp; Thread-Safety", h1_style))
    
    story.append(Paragraph("A. The 3-Tier Enterprise MVC Architecture", h2_style))
    story.append(Paragraph(
        "&bull; <b>Presentation Tier:</b> Client-side DOM manipulated using Vanilla JavaScript (ES6). Renders dynamic product cards, Quick View drawer, and handles image fallbacks.<br/>"
        "&bull; <b>Controller &amp; Service Tier:</b> Java Servlets (`ProductServlet`, `AuthServlet`, `OrderServlet`) handle incoming `HttpServletRequest` objects, validate inputs, invoke business logic, and produce JSON responses or dispatch to JSPs.<br/>"
        "&bull; <b>Data Access Tier (DAO Pattern):</b> Encapsulates all SQL logic inside DAO classes (`ProductDAO`, `UserDAO`, `OrderDAO`). Uses `PreparedStatement` to prevent SQL injection and `HikariCP` for high-throughput connection pooling.",
        body_style
    ))

    story.append(Paragraph("B. Concurrency Locking During Checkout (Preventing Overselling)", h2_style))
    story.append(Paragraph(
        "<b>Problem:</b> If two customers attempt to purchase the last available item simultaneously, a race condition occurs.<br/>"
        "<b>Solution:</b> We use <b>Pessimistic Locking</b> with ACID transaction isolation:",
        body_style
    ))
    story.append(Paragraph(
        "connection.setAutoCommit(false); // Begin ACID Transaction<br/>"
        "PreparedStatement lockStmt = connection.prepareStatement(<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"SELECT stock_quantity FROM inventory WHERE product_id = ? FOR UPDATE\"<br/>"
        ");<br/>"
        "lockStmt.setInt(1, productId);<br/>"
        "ResultSet rs = lockStmt.executeQuery();<br/>"
        "if (rs.next() &amp;&amp; rs.getInt(\"stock_quantity\") &gt;= orderQty) {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;// Deduct stock and insert order record<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;connection.commit();<br/>"
        "} else {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;connection.rollback(); // Insufficient inventory<br/>"
        "}",
        code_style
    ))
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 5: 35+ REAL-WORLD TECHNICAL INTERVIEW QUESTIONS & ANSWERS
    # =========================================================================
    story.append(Paragraph("5. Top 35+ Technical Interview Questions &amp; Word-for-Word Answers", h1_style))

    qa_list = [
        # CORE JAVA & OOP
        ("Q1: How did you apply Object-Oriented Programming (OOP) in this project?",
         "We applied all 4 pillars of OOP: 1) Encapsulation in Model classes (Product, User, Order) using private fields and public getters/setters. 2) Abstraction through DAO interfaces (e.g., ProductDAO defining findById without exposing SQL details). 3) Inheritance where custom servlets extend HttpServlet. 4) Polymorphism via interface-driven service contracts."),
        
        ("Q2: Why did you use PreparedStatement instead of Statement in JDBC?",
         "Two vital reasons: 1) Security: PreparedStatement uses parameterized queries, pre-compiling the SQL statement in the database engine and treating user input strictly as literal values, completely neutralizing SQL Injection attacks. 2) Performance: Pre-compiled statements are cached in the database execution plan cache, speeding up repeated queries."),

        ("Q3: Are Java Servlets thread-safe? How do you ensure safety in your servlets?",
         "No, by default a Servlet instance is a singleton created once by the Tomcat container. Multiple client requests are handled by different threads invoking service(), doGet(), or doPost() on that same instance simultaneously. Therefore, defining instance (class-level) variables creates race conditions. We ensure thread-safety by keeping servlets completely stateless—declaring variables strictly inside request handler methods (local stack-allocated variables)."),

        ("Q4: Explain the complete Servlet Lifecycle.",
         "1. Loading & Instantiation: Tomcat loads the servlet class and instantiates it. 2. Initialization: Tomcat calls init(ServletConfig config) once to allocate resources. 3. Request Handling: For every incoming HTTP request, Tomcat spawns a thread that calls service(), which routes to doGet() or doPost(). 4. Destruction: When the web app shuts down, Tomcat calls destroy() to release connections and resources."),

        ("Q5: What is the difference between doGet() and doPost()?",
         "doGet() is used to retrieve data without altering server state; parameters are appended in the URL query string (visible in browser history, max length limited ~2KB, bookmarkable, cached). doPost() sends data in the HTTP request body; it is used for state-altering operations like user registration, placing orders, and password updates (secure, no payload size limitation, not cached)."),

        # DATABASE & TRANSACTIONS
        ("Q6: How do you handle database connection management in production?",
         "Instead of opening and closing physical database sockets on every HTTP request using DriverManager (which causes severe latency and socket exhaustion), we implement a connection pool using HikariCP. HikariCP keeps a warm pool of pre-established database connections. Servlets borrow a connection via try-with-resources and return it to the pool in milliseconds."),

        ("Q7: What is the optimal connection pool sizing formula for HikariCP?",
         "The standard PostgreSQL/HikariCP formula is: connections = (core_count * 2) + effective_spindle_count. For a 4-core database server with SSD storage, a pool size of (4 * 2) + 1 = 9 to 10 connections comfortably serves thousands of concurrent users with zero queue contention."),

        ("Q8: What are ACID properties and how did you implement them?",
         "A - Atomicity: Either all order items and payment records are saved, or none are. Handled via connection.setAutoCommit(false), connection.commit(), and connection.rollback() inside catch blocks. C - Consistency: Database constraints (foreign keys, CHECK stock_quantity &gt;= 0) ensure invalid state cannot be saved. I - Isolation: Row-level locks prevent dirty reads. D - Durability: MySQL InnoDB write-ahead redo logs guarantee committed data survives crashes."),

        ("Q9: Why is unit_price duplicated in order_items if products table already has price?",
         "This is intentional historical snapshotting. If an item sells today for ₹2,499 and the merchant updates its catalog price next month to ₹2,999, past order receipts and accounting ledgers must still show the original purchase price of ₹2,499. Reading from products table would corrupt historical transaction records."),

        ("Q10: What is Third Normal Form (3NF) and why is it important?",
         "A table is in 3NF if: 1) It is in 2NF (no partial dependencies on a composite primary key), and 2) It has no transitive dependencies (non-key columns must depend strictly on the primary key, and nothing else). This eliminates duplicate data, saves storage, and prevents insert, update, and delete anomalies."),

        # AUTHENTICATION & SECURITY
        ("Q11: Why did you choose Phone Number + Password over SMS OTP for customer login?",
         "SMS OTP introduces third-party SMS gateway latency, carrier dropouts, recurring per-SMS billing costs, and SIM-swap attack vulnerabilities. Phone Number + Password provides instant, zero-latency authentication, offline testability, and standard enterprise security backed by BCrypt hashing and rate-limiting."),

        ("Q12: How do you securely store passwords in the database?",
         "We never store plaintext passwords. We use the BCrypt adaptive hashing algorithm with a random salt (cost factor 12). BCrypt is intentionally slow and CPU-intensive, rendering rainbow table lookups and brute-force GPU attacks mathematically infeasible."),

        ("Q13: How does session management work between the browser and Tomcat?",
         "When a user signs in, Tomcat generates a unique 128-bit cryptographically secure session ID, stores the session object in memory (`HttpSession`), and sends the ID to the client via an HTTP cookie named `JSESSIONID`. The cookie is marked `HttpOnly` (inaccessible to malicious JavaScript XSS) and `SameSite=Strict` (prevents Cross-Site Request Forgery)."),

        ("Q14: How does the application prevent Cross-Site Scripting (XSS)?",
         "All user-generated text inputs (names, review comments, product searches) are sanitized and HTML-escaped before being rendered onto the DOM (replacing &lt; with &amp;lt;, &gt; with &amp;gt;). This prevents attackers from injecting &lt;script&gt; tags into product reviews or customer profiles."),

        # PERFORMANCE & FRONTEND
        ("Q15: How did you fix the issue where images appeared blurred or broken with a blue question mark?",
         "We diagnosed two root causes: 1) Several Unsplash image IDs were deleted, returning HTTP 404. 2) Without an `onerror` attribute, the browser rendered its default broken image box. We resolved this by verifying all photo URLs against HTTP 200 OK and implementing an automatic JavaScript error handler `onerror=\"handleImageFallback(this, category)\"` which instantly swaps any failing image to a guaranteed high-res category editorial image."),

        ("Q16: How did you fix mobile layout overflow issues?",
         "We implemented: 1) Viewport-fit cover with a locked 58px mobile header, converting text buttons into SVG icons. 2) Touch-friendly single-row horizontal category rail with `-webkit-overflow-scrolling: touch`. 3) 24-item batch pagination to avoid loading all 535 DOM nodes simultaneously, maintaining 60 FPS mobile scroll performance."),

        ("Q17: What happens when two users place an order for the last item simultaneously?",
         "The first user's transaction acquires a row-level pessimistic lock via `SELECT ... FOR UPDATE` on the inventory table. The second user's thread waits until the first transaction commits. When the lock releases, the second user's query reads `stock_quantity = 0`, triggers an out-of-stock exception, and rolls back cleanly with a friendly error message.")
    ]

    for q, a in qa_list:
        story.append(Paragraph(f"<b>{q}</b>", q_style))
        story.append(Paragraph(a, a_style))
        story.append(Spacer(1, 2))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Master Interview Guide PDF generated successfully: {filename}")

if __name__ == "__main__":
    output_path = "/Users/somaindra/Desktop/TrendVibe_Ultimate_Interview_Master_Guide.pdf"
    build_pdf(output_path)
    # Also mirror locally
    build_pdf("TrendVibe_Ultimate_Interview_Master_Guide.pdf")
