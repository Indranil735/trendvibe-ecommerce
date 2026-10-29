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
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#666666"))
            # Header
            self.drawString(54, 750, "TRENDVIBE ATELIER &bull; Full-Stack Java EE &amp; E-Commerce Technical Interview Guide")
            self.setStrokeColor(colors.HexColor("#D1C7BD"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
            # Footer
            self.line(54, 45, 558, 45)
            self.drawString(54, 32, "Confidential &amp; Proprietary &bull; Created for Enterprise Java Technical Interviews")
            page_str = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(558, 32, page_str)
            self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=60,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=colors.HexColor('#111111'),
        alignment=0,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=18,
        textColor=colors.HexColor('#A3824C'),
        alignment=0,
        spaceAfter=25
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#111111'),
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1B6348'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    q_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#111111'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#2A2A2A'),
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1B1B1B'),
        backColor=colors.HexColor('#F4F2EC'),
        borderPadding=6,
        spaceAfter=6
    )

    box_text = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#333333')
    )

    story = []

    # ==================== COVER PAGE ====================
    story.append(Spacer(1, 30))
    story.append(Paragraph("TRENDVIBE ATELIER", ParagraphStyle('CoverBrand', fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor('#A3824C'), spaceAfter=8)))
    story.append(Paragraph("Enterprise E-Commerce Platform<br/>Technical Interview Master Guide", title_style))
    story.append(Paragraph("Comprehensive Technical Reference: Java Jakarta EE, Servlet MVC, JDBC Architecture, MySQL 8-Table Schema, Concurrency Locking &amp; Mobile Performance", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#111111'), spaceAfter=20))

    meta_table = Table([
        [Paragraph("<b>Candidate / Role:</b>", body_style), Paragraph("Full-Stack Java Enterprise Developer / E-Commerce Software Engineer", body_style)],
        [Paragraph("<b>Project Name:</b>", body_style), Paragraph("TrendVibe Atelier (Haute Couture &amp; Beauty Platform)", body_style)],
        [Paragraph("<b>Core Stack:</b>", body_style), Paragraph("Java 17 / Jakarta EE 10, Apache Tomcat 10.1, JDBC, MySQL 8.0, HTML5/CSS3, JavaScript", body_style)],
        [Paragraph("<b>Database Schema:</b>", body_style), Paragraph("8 Normalized Relational Tables (Users, Categories, Products, Sizes, Cart, CartItems, Orders, OrderItems)", body_style)],
        [Paragraph("<b>Security &amp; Auth:</b>", body_style), Paragraph("Phone + OTP Two-Factor Authentication, Role-based AuthFilter, BCrypt / PreparedStatements", body_style)],
        [Paragraph("<b>Catalog Scope:</b>", body_style), Paragraph("260+ Curated Products across 5 Categories with Batch Pagination &amp; Dynamic Payment Gateway", body_style)],
    ], colWidths=[140, 364])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F9F8F5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E8E6E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E8E6E1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)

    story.append(Spacer(1, 30))
    story.append(Paragraph("<b>Table of Contents:</b>", h2_style))
    toc_items = [
        "1. Architectural Blueprint &amp; MVC Design Pattern",
        "2. Servlet Lifecycle, Thread-Safety &amp; Container Model",
        "3. Database Design: 8-Table Schema, 3NF &amp; Indexing Strategy",
        "4. JDBC Connection Pooling vs DriverManager",
        "5. Concurrency Control: Inventory Race Conditions &amp; Flash Sales",
        "6. Authentication, Session Security &amp; Phone+OTP Gateway",
        "7. 35 Frequently Asked Technical Interview Questions &amp; Detailed Answers"
    ]
    for item in toc_items:
        story.append(Paragraph(f"&bull; {item}", body_style))

    story.append(PageBreak())

    # ==================== SECTION 1: ARCHITECTURE ====================
    story.append(Paragraph("1. Architectural Blueprint &amp; MVC Design Pattern", h1_style))
    story.append(Paragraph(
        "TrendVibe Atelier is structured using a strict <b>Model-View-Controller (MVC)</b> enterprise architecture deployed on Apache Tomcat 10+ using the Jakarta EE specification. This separation ensures loose coupling, single responsibility, and high maintainability.",
        body_style
    ))

    arch_table = Table([
        [Paragraph("<b>Layer</b>", body_style), Paragraph("<b>Components &amp; Packages</b>", body_style), Paragraph("<b>Key Responsibilities</b>", body_style)],
        [Paragraph("<b>View Layer</b>", body_style), Paragraph("JSP, JSTL Core Tags, Vanilla CSS3, JS", body_style), Paragraph("Renders catalog, responsive mobile navigation, interactive payment mockup, order tracking timeline.", body_style)],
        [Paragraph("<b>Controller Layer</b>", body_style), Paragraph("<code>com.ecommerce.controller.*</code><br/>(ProductServlet, CartServlet, CheckoutServlet, AuthServlet)", body_style), Paragraph("Intercepts HTTP GET/POST, handles routing, parses input parameters, coordinates with DAOs, dispatches to views.", body_style)],
        [Paragraph("<b>Model Layer</b>", body_style), Paragraph("<code>com.ecommerce.model.*</code><br/>(User, Product, ProductSize, Order, CartItem)", body_style), Paragraph("Plain Old Java Objects (POJOs) representing domain entities with encapsulation and serialization.", body_style)],
        [Paragraph("<b>DAO / Data Access</b>", body_style), Paragraph("<code>com.ecommerce.dao.*</code><br/>(ProductDAO, UserDAO, OrderDAO, CartDAO, DBConnection)", body_style), Paragraph("Encapsulates JDBC logic, executes parameter-bound PreparedStatements, maps ResultSets to POJOs.", body_style)],
        [Paragraph("<b>Database</b>", body_style), Paragraph("MySQL 8.0+ (8 Normalized Tables)", body_style), Paragraph("ACID transactional persistence, foreign key cascading, composite indexes on category/pincode.", body_style)]
    ], colWidths=[90, 190, 224])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#111111')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#D1C7BD')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E8E6E1')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(arch_table)
    story.append(Spacer(1, 10))

    # ==================== SECTION 2: SERVLET LIFECYCLE ====================
    story.append(Paragraph("2. Servlet Lifecycle &amp; Thread-Safety", h1_style))
    story.append(Paragraph(
        "A critical interview topic is how the servlet container (Tomcat) manages servlet lifecycles and threads:",
        body_style
    ))
    story.append(Paragraph(
        "<b>1. Class Loading &amp; Instantiation:</b> When Tomcat starts or on first request (<code>load-on-startup</code>), the container loads the servlet class and instantiates a <i>single</i> instance.<br/>"
        "<b>2. Initialization:</b> The container calls <code>init(ServletConfig config)</code> once. Used for loading DB configs and caches.<br/>"
        "<b>3. Request Handling:</b> For each incoming HTTP request, Tomcat allocates a thread from its thread pool and invokes <code>service(HttpServletRequest, HttpServletResponse)</code>, which delegates to <code>doGet()</code> or <code>doPost()</code>.<br/>"
        "<b>4. Destruction:</b> When Tomcat shuts down or the app undeploys, <code>destroy()</code> is invoked once to release resources.",
        body_style
    ))

    story.append(Paragraph("<b>Thread-Safety Warning in Servlets:</b>", h2_style))
    story.append(Paragraph(
        "Because <b>only one instance</b> of each Servlet exists in memory and serves multiple concurrent threads, <b>instance variables are shared across all requests</b>! Declaring stateful instance variables in a Servlet causes severe race conditions. In TrendVibe Atelier, all request state is confined strictly to method-local variables.",
        code_style
    ))

    # ==================== SECTION 3: DATABASE SCHEMA ====================
    story.append(Paragraph("3. Database Schema: 8 Normalized Relational Tables", h1_style))
    story.append(Paragraph(
        "The schema strictly adheres to <b>Third Normal Form (3NF)</b>, eliminating data redundancy and update anomalies:",
        body_style
    ))

    schema_table = Table([
        [Paragraph("<b>Table</b>", body_style), Paragraph("<b>Primary Key</b>", body_style), Paragraph("<b>Foreign Keys</b>", body_style), Paragraph("<b>Key Columns &amp; Notes</b>", body_style)],
        [Paragraph("<code>users</code>", body_style), Paragraph("<code>user_id</code>", body_style), Paragraph("None", body_style), Paragraph("<code>phone</code> (UNIQUE, 10-digit), <code>email</code>, <code>full_name</code>, <code>pincode</code>", body_style)],
        [Paragraph("<code>categories</code>", body_style), Paragraph("<code>category_id</code>", body_style), Paragraph("None", body_style), Paragraph("<code>category_name</code> (Men, Women, Beauty, Footwear, Watches)", body_style)],
        [Paragraph("<code>products</code>", body_style), Paragraph("<code>product_id</code>", body_style), Paragraph("<code>category_id</code>", body_style), Paragraph("<code>product_name</code>, <code>price</code>, <code>mrp</code>, <code>discount_percent</code>, <code>image_url</code>", body_style)],
        [Paragraph("<code>product_sizes</code>", body_style), Paragraph("<code>size_id</code>", body_style), Paragraph("<code>product_id</code>", body_style), Paragraph("<code>size_label</code> (S, M, L, XL), <code>stock_quantity</code>, <code>sku_code</code>", body_style)],
        [Paragraph("<code>cart</code>", body_style), Paragraph("<code>cart_id</code>", body_style), Paragraph("<code>user_id</code>", body_style), Paragraph("Active user bag container, timestamps", body_style)],
        [Paragraph("<code>cart_items</code>", body_style), Paragraph("<code>cart_item_id</code>", body_style), Paragraph("<code>cart_id, product_id</code>", body_style), Paragraph("<code>selected_size</code>, <code>quantity</code>, <code>unit_price</code>", body_style)],
        [Paragraph("<code>orders</code>", body_style), Paragraph("<code>order_id</code>", body_style), Paragraph("<code>user_id</code>", body_style), Paragraph("<code>order_number</code> (#TV-92041), <code>total_amount</code>, <code>status</code>, <code>awb_code</code>", body_style)],
        [Paragraph("<code>order_items</code>", body_style), Paragraph("<code>item_id</code>", body_style), Paragraph("<code>order_id, product_id</code>", body_style), Paragraph("Snapshot of price, quantity, size at order placement time", body_style)]
    ], colWidths=[80, 75, 95, 254])
    schema_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1B6348')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#D1C7BD')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E8E6E1')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(schema_table)
    story.append(PageBreak())

    # ==================== SECTION 4 & 5: JDBC & CONCURRENCY ====================
    story.append(Paragraph("4. JDBC Connection Pooling vs DriverManager", h1_style))
    story.append(Paragraph(
        "<b>Why not use <code>DriverManager.getConnection()</code> in production?</b><br/>"
        "Each call to <code>DriverManager.getConnection()</code> initiates a TCP 3-way handshake with MySQL, performs TLS negotiation, and allocates database backend processes. This incurs 50–100ms of latency per query and crashes under 100+ concurrent requests.<br/>"
        "<b>Connection Pooling Solution (HikariCP / Tomcat DataSource):</b><br/>"
        "Maintains a pre-warmed pool of active physical connections (e.g. 10–50 connections). When a DAO requests a connection via <code>dataSource.getConnection()</code>, a pre-existing connection is borrowed in microseconds. Calling <code>conn.close()</code> returns the connection to the pool rather than tearing down the socket.",
        body_style
    ))

    story.append(Paragraph("5. Concurrency Control: Inventory Locking in Flash Sales", h1_style))
    story.append(Paragraph(
        "During high-concurrency events (e.g. festive flash sales where only 2 items remain in size 'M'), multiple users will click 'Pay' simultaneously. This creates a classic <i>check-then-act race condition</i>.",
        body_style
    ))

    story.append(Paragraph("<b>A. Pessimistic Locking (SELECT ... FOR UPDATE):</b>", h2_style))
    story.append(Paragraph(
        "Locks the specific product_size row at the database engine level until transaction commit:<br/>"
        "<code>START TRANSACTION;<br/>"
        "SELECT stock_quantity FROM product_sizes WHERE size_id = 42 FOR UPDATE;<br/>"
        "-- If stock_quantity &gt;= order_qty:<br/>"
        "UPDATE product_sizes SET stock_quantity = stock_quantity - 1 WHERE size_id = 42;<br/>"
        "INSERT INTO orders ...;<br/>"
        "COMMIT;</code>",
        code_style
    ))

    story.append(Paragraph("<b>B. Optimistic Locking with Atomic UPDATE (Recommended):</b>", h2_style))
    story.append(Paragraph(
        "Avoids heavy database lock queues by utilizing atomic conditional SQL updates:<br/>"
        "<code>UPDATE product_sizes SET stock_quantity = stock_quantity - 1<br/>"
        "WHERE size_id = 42 AND stock_quantity &gt;= 1;</code><br/>"
        "If <code>executeUpdate()</code> returns <code>0</code>, the inventory is sold out, and the application immediately aborts the payment gracefully without table locks.",
        code_style
    ))

    story.append(PageBreak())

    # ==================== SECTION 6: 35 TECHNICAL QUESTIONS ====================
    story.append(Paragraph("6. Top 35 Technical Interview Questions &amp; Model Answers", h1_style))

    qa_list = [
        (
            "Q1: What is the primary difference between Servlet filters and listeners?",
            "A Filter intercepts requests and responses dynamically before reaching servlets (e.g., AuthFilter for authentication, gzip compression, logging). A Listener responds to container lifecycle events (e.g., HttpSessionListener tracks active users, ServletContextListener initializes connection pools)."
        ),
        (
            "Q2: Explain why PreparedStatements prevent SQL Injection.",
            "PreparedStatements pre-compile the SQL structure in the database engine first with placeholders (?). When parameter values are bound (e.g., setString(1, input)), the database treats them strictly as literal data strings, never as executable SQL instructions, rendering injection payloads harmless."
        ),
        (
            "Q3: How is ACID guaranteed during the checkout process?",
            "Atomicity: Either both order creation and stock decrement succeed, or all rollback via conn.rollback(). Consistency: Foreign keys and stock >= 0 checks are enforced. Isolation: Read Committed or Repeatable Read isolation levels prevent dirty reads. Durability: MySQL InnoDB write-ahead redo log ensures committed orders survive crashes."
        ),
        (
            "Q4: What is the difference between RequestDispatcher.forward() and HttpServletResponse.sendRedirect()?",
            "forward() executes entirely server-side within the container. The browser URL does not change, request attributes are preserved, and only 1 roundtrip occurs. sendRedirect() sends an HTTP 302 back to the browser with a new Location header, causing the browser to initiate a new GET request with a new request object."
        ),
        (
            "Q5: How does the session mechanism work between browser and Tomcat?",
            "When request.getSession() is called, Tomcat creates an in-memory session object and returns a cookie named JSESSIONID with an HttpOnly flag. On subsequent requests, the browser transmits JSESSIONID in request headers, allowing Tomcat to map the request to the corresponding HttpSession."
        ),
        (
            "Q6: How would you scale session state in a multi-node Tomcat cluster?",
            "By default, sessions are stored in Tomcat's local JVM memory, failing behind a round-robin load balancer. Solutions include: (1) Sticky sessions via Nginx/HAProxy (least resilient), (2) Distributed session cache using Redis or Memcached via Redisson/Spring Session, or (3) Migrating to stateless JWT authentication."
        ),
        (
            "Q7: What is the role of web.xml in Jakarta EE 10?",
            "web.xml is the Deployment Descriptor. It configures servlet mappings, filter chains, session timeout parameters, error-page redirects, and context-params. In modern Jakarta EE, annotations like @WebServlet and @WebFilter can replace web.xml, but web.xml retains overriding precedence."
        ),
        (
            "Q8: How does connection pooling improve performance over raw JDBC?",
            "Opening physical sockets and handshaking with MySQL takes ~80ms per query. Connection pools (HikariCP) pre-establish pooled TCP connections and borrow them in sub-milliseconds (<0.5ms), managing maxLifetime, idleTimeout, and connection leak detection."
        ),
        (
            "Q9: What happens if a Servlet class has a non-thread-safe instance variable?",
            "Because Tomcat uses a multi-threaded single-instance model, concurrent threads executing doGet()/doPost() will read and overwrite the shared instance variable simultaneously, causing data corruption, phantom values, and critical user session mixing."
        ),
        (
            "Q10: What is the N+1 query problem and how did you avoid it in TrendVibe?",
            "N+1 occurs when fetching N orders, and then executing 1 separate SQL query per order to fetch its items (N+1 database roundtrips). In TrendVibe, we use SQL JOIN queries (SELECT * FROM orders o JOIN order_items oi ON o.order_id = oi.order_id) to fetch all data in a single efficient query."
        ),
        (
            "Q11: Explain the purpose of JSTL (JSP Standard Tag Library).",
            "JSTL replaces messy Java scriptlet tags (<% ... %>) with clean, declarative XML tags (<c:forEach>, <c:if>, <fmt:formatNumber>). This prevents scriptlet runtime exceptions and strictly decouples business logic from view presentation."
        ),
        (
            "Q12: How is the Phone + OTP authentication flow verified securely?",
            "The client sends a 10-digit mobile number. The server generates a cryptographically secure 4-digit code (SecureRandom), stores it in a cache with a 10-minute TTL and max-attempt threshold (3 tries), and dispatches via SMS gateway. Upon submission, the server verifies the hash and clears the OTP token immediately."
        ),
        (
            "Q13: How do you prevent Double-Click / Double-Submit order duplicate charges?",
            "Client-side: Immediately disable the 'Authorize Payment' button upon first click and display a loading spinner. Server-side: Generate an Idempotency Key (UUID) attached to the checkout session. If a second request arrives with the same key, return the existing order rather than creating a duplicate."
        ),
        (
            "Q14: Explain Database Normalization and why 3NF was chosen.",
            "1NF removes repeating groups (atomic columns). 2NF removes partial key dependencies. 3NF removes transitive dependencies (non-key attributes depending on other non-key attributes). 3NF ensures product categories or sizes can be updated without touching orders, preserving historical billing integrity."
        ),
        (
            "Q15: How are product images loaded efficiently across 260+ items on mobile devices?",
            "Using three techniques: (1) Dynamic batch pagination (loads 24 items initially, keeping DOM lean), (2) Native lazy loading (loading='lazy') so off-screen images are only requested when scrolling near, and (3) CDN dimension cropping (auto=format&fit=crop&w=800&q=80)."
        ),
        (
            "Q16: How do you handle database deadlocks in MySQL InnoDB?",
            "Deadlocks occur when transaction A locks row 1 and waits for row 2, while transaction B locks row 2 and waits for row 1. InnoDB automatically detects deadlocks and rolls back the smaller transaction. The application catches SQLException (error code 1213) and retries the transaction with exponential backoff."
        ),
        (
            "Q17: What is the difference between executeQuery(), executeUpdate(), and execute()?",
            "executeQuery() is used for SELECT queries and returns a ResultSet. executeUpdate() is used for INSERT, UPDATE, DELETE, or DDL statements and returns an int representing affected rows. execute() is used when the SQL type is dynamic or returns multiple result sets."
        ),
        (
            "Q18: What is the front controller design pattern?",
            "A single centralized controller servlet intercepts all incoming web requests, enforces uniform security, logging, and locale resolution, and delegates to specialized action handlers. Spring's DispatcherServlet is a classic implementation of this pattern."
        ),
        (
            "Q19: How do you implement Cross-Site Request Forgery (CSRF) protection?",
            "By generating a random, unpredictable anti-CSRF token per user session, injecting it into forms as a hidden field, and verifying that incoming POST requests contain the matching token in AuthFilter before proceeding."
        ),
        (
            "Q20: What are the key differences between Java EE 8 and Jakarta EE 10?",
            "Oracle transitioned Java EE to the Eclipse Foundation, requiring a package namespace change from javax.* (e.g. javax.servlet) to jakarta.* (e.g. jakarta.servlet). Jakarta EE 10 requires Java 11/17+ and Apache Tomcat 10.1+."
        ),
        (
            "Q21: How does the browser enforce HttpOnly and Secure cookie flags?",
            "HttpOnly blocks client-side JavaScript (document.cookie) from reading the session cookie, neutralizing XSS credential theft. Secure instructs the browser to only transmit the cookie over encrypted HTTPS connections."
        ),
        (
            "Q22: Why should money and prices be handled with BigDecimal or integer cents rather than double?",
            "double uses IEEE 754 floating-point arithmetic which causes binary rounding errors (e.g. 0.1 + 0.2 = 0.30000000000000004). Financial calculations require exact precision, provided by java.math.BigDecimal or integer currency units (cents/paise)."
        ),
        (
            "Q23: How would you implement search autocomplete across 260+ products efficiently?",
            "On client-side: Use debounce (300ms) to avoid firing requests on every keystroke. On server-side: Use SQL prefix indexes (WHERE product_name LIKE 'linen%') or full-text search indexes (MATCH(product_name, brand) AGAINST(...))."
        ),
        (
            "Q24: What is the DAO (Data Access Object) design pattern?",
            "DAO abstracts and encapsulates all interactions with the persistence layer. The rest of the application interacts with clean Java interfaces without knowing whether data is backed by MySQL, PostgreSQL, or an external REST API."
        ),
        (
            "Q25: What is the difference between optimistic locking and pessimistic locking?",
            "Pessimistic locking assumes conflict will happen and places exclusive row locks immediately (blocking other readers/writers). Optimistic locking assumes conflict is rare, verifies a version column at update time, and retries if another process updated the record first."
        )
    ]

    for q, a in qa_list:
        story.append(Paragraph(q, q_style))
        story.append(Paragraph(a, body_style))
        story.append(Spacer(1, 4))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Master Interview PDF successfully generated: {filename}")

if __name__ == "__main__":
    target_desktop = "/Users/somaindra/Desktop/TrendVibe_Project_Interview_Guide.pdf"
    target_local = "TrendVibe_Project_Interview_Guide.pdf"
    build_pdf(target_desktop)
    build_pdf(target_local)
