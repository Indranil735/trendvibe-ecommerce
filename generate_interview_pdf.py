# generate_interview_pdf.py
import sys
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
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
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "TrendVibe E-Commerce Platform — Technical Architecture & Interview Guide")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
        
        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 40, page_text)
        self.drawString(54, 40, "Confidential — Prepared for Technical Pair Programming & Placement Interviews")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 52, 558, 52)
        self.restoreState()

def build_pdf(filename="TrendVibe_Project_Interview_Guide.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#1e293b"),
        alignment=TA_LEFT
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#ff3f6c"),
        alignment=TA_LEFT
    )

    meta_style = ParagraphStyle(
        'CoverMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#475569")
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#ff3f6c"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#0f172a"),
        backColor=colors.HexColor("#f1f5f9"),
        borderPadding=6,
        spaceAfter=6,
        keepWithNext=True
    )

    qa_q_style = ParagraphStyle(
        'QA_Question',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#1e293b"),
        spaceBefore=8,
        spaceAfter=2,
        keepWithNext=True
    )

    qa_a_style = ParagraphStyle(
        'QA_Answer',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155"),
        spaceAfter=8,
        alignment=TA_JUSTIFY
    )

    story = []

    # ================= COVER / HEADER =================
    story.append(Spacer(1, 10))
    story.append(Paragraph("TRENDVIBE E-COMMERCE PLATFORM", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Pin-to-Pin System Architecture, Class Design &amp; Master Technical Interview Guide", title_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#ff3f6c"), spaceBefore=2, spaceAfter=12))

    story.append(Paragraph("<b>Tech Stack:</b> Java, Jakarta EE (Servlets &amp; JSP), JDBC, MySQL 8.0, Apache Tomcat 10+, HTML5, CSS3, JavaScript, Eclipse IDE", meta_style))
    story.append(Paragraph("<b>Reference Models:</b> Myntra, Ajio, Nykaa (Fashion, Multi-Size Footwear &amp; Beauty Cosmetics)", meta_style))
    story.append(Paragraph("<b>Author / Engineer:</b> Indranil Soma | Portfolio &amp; Campus Recruitment Specification", meta_style))
    story.append(Spacer(1, 14))

    # ================= SECTION 1: ARCHITECTURE OVERVIEW =================
    story.append(Paragraph("1. High-Level Enterprise Architecture &amp; Request Lifecycle", h1_style))
    story.append(Paragraph(
        "TrendVibe is engineered around the industry-standard <b>Model-View-Controller (MVC)</b> and <b>Data Access Object (DAO)</b> architecture. "
        "This strictly decouples presentations, routing logic, business validation, and database queries for enterprise maintainability.",
        body_style
    ))

    arch_flow_text = """[Client Web / Mobile Browser]
      &darr; (HTTP Requests / Form Submission / JSON)
[Apache Tomcat 10+ Web Server] &rarr; [web.xml Deployment Descriptor]
      &darr;
[Controller Layer (Jakarta Servlets)]
  &bull; ProductController (/home, /products, /product-details)
  &bull; CartController (/cart, /cart/add, /cart/update, /cart/remove)
  &bull; CheckoutController (/checkout, /checkout/place-order, /my-orders)
  &bull; LoginController / RegisterController (/login, /register)
      &darr;
[DAO Layer (Data Access Objects &amp; JDBC)]
  &bull; DBConnection (Connection Pool &amp; Driver Manager)
  &bull; ProductDAO, CartDAO, OrderDAO, UserDAO, CategoryDAO
      &darr; (Atomic SQL Queries &amp; PreparedStatements)
[MySQL Relational Database (ecommerce_db)]
  &bull; 8 Normalized Tables with Foreign Keys, Cascades &amp; Indexing"""
    story.append(Paragraph(arch_flow_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))

    story.append(Paragraph(
        "<b>What is the 'Main File' in this application?</b><br/>"
        "Unlike standalone C/Java programs that execute from <code>public static void main(String[] args)</code>, "
        "an enterprise Jakarta EE web application contains <b>four primary architectural entry points</b>:<br/>"
        "1. <b>Configuration Entry Point (<code>web.xml</code>):</b> Located in <code>WEB-INF/web.xml</code>. This is the very first file Tomcat reads to register servlets, URL patterns, session timeouts, and the welcome list.<br/>"
        "2. <b>Web Request Entry Point (<code>index.jsp</code>):</b> The root welcome file that intercepts incoming traffic (<code>/</code>) and forwards to <code>/home</code>.<br/>"
        "3. <b>Primary Controller Entry Point (<code>ProductController.java</code>):</b> Dispatches home catalog feeds, category sorting, and product detail views.<br/>"
        "4. <b>Primary Database Entry Point (<code>DBConnection.java</code>):</b> Centralizes JDBC connection creation to MySQL.",
        body_style
    ))

    story.append(Spacer(1, 10))

    # ================= SECTION 2: PIN-TO-PIN CLASS CREATION =================
    story.append(Paragraph("2. Pin-to-Pin Class Creation &amp; Object-Oriented Hierarchy", h1_style))
    story.append(Paragraph(
        "To satisfy the design blueprint, the application is divided into three Java packages under <code>com.ecommerce</code>:",
        body_style
    ))

    # Table of Classes
    class_table_data = [
        [Paragraph("<b>Package / Layer</b>", meta_style), Paragraph("<b>Class Name</b>", meta_style), Paragraph("<b>Responsibility &amp; Core Methods</b>", meta_style)],
        [
            Paragraph("<code>com.ecommerce.model</code>", meta_style),
            Paragraph("<b>User, Product, Category, ProductSize, Order, OrderItem, Cart, CartItem</b>", meta_style),
            Paragraph("JavaBeans (POJOs) implementing <code>Serializable</code>. Encapsulates private fields with getters/setters and calculated pricing methods.", meta_style)
        ],
        [
            Paragraph("<code>com.ecommerce.dao</code>", meta_style),
            Paragraph("<b>DBConnection</b>", meta_style),
            Paragraph("Thread-safe connection provider. Loads <code>com.mysql.cj.jdbc.Driver</code>, reads environment variables (Host, Port, User, Password) with failover.", meta_style)
        ],
        [
            Paragraph("<code>com.ecommerce.dao</code>", meta_style),
            Paragraph("<b>ProductDAO, CartDAO, OrderDAO, UserDAO, CategoryDAO</b>", meta_style),
            Paragraph("Executes prepared statements, converts <code>ResultSet</code> rows into domain model objects, manages batch insertions, and runs atomic SQL updates.", meta_style)
        ],
        [
            Paragraph("<code>com.ecommerce.controller</code>", meta_style),
            Paragraph("<b>ProductController, CartController, CheckoutController, etc.</b>", meta_style),
            Paragraph("Extends <code>HttpServlet</code>. Overrides <code>doGet()</code> and <code>doPost()</code>. Sanitizes input, verifies session state, and forwards to JSP views.", meta_style)
        ]
    ]

    t = Table(class_table_data, colWidths=[110, 140, 254])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    # ================= SECTION 3: INVENTORY MANAGEMENT =================
    story.append(Paragraph("3. Multi-Size Inventory Management &amp; Concurrency Control", h1_style))
    story.append(Paragraph(
        "A major challenge in fashion e-commerce (such as Myntra, Ajio, and Nykaa) is tracking stock across multiple variations "
        "(sizes like S, M, L, XL, or shoe sizes UK 7, UK 8). Storing stock on the product level fails because size 'M' may be sold out while size 'XL' remains available.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Relational Schema Implementation:</b><br/>"
        "We maintain a dedicated <code>product_sizes</code> table with a composite key logic: <code>product_id (FK)</code>, <code>size_label</code>, <code>stock_quantity</code>, and unique <code>sku_code</code>. "
        "Every cart item links specifically to a <code>(product_id, size_label)</code> pair.",
        body_style
    ))

    story.append(Paragraph("How to Prevent Overselling During Flash Sales (Concurrency &amp; Locking):", h2_style))
    story.append(Paragraph(
        "When 100 users try to buy the last 2 units of a Nike sneaker simultaneously, naive code causes race conditions (dirty reads and overselling). "
        "In our application, we handle this through <b>ACID-compliant Database Transactions</b>:",
        body_style
    ))

    sql_code = """// Atomic Stock Decrement within a Transaction (OrderDAO.java)
connection.setAutoCommit(false); // Begin ACID Transaction

String stockSql = "UPDATE product_sizes "
                + "SET stock_quantity = stock_quantity - ? "
                + "WHERE product_id = ? AND size_label = ? "
                + "AND stock_quantity >= ?"; // Guard Condition!

try (PreparedStatement ps = connection.prepareStatement(stockSql)) {
    ps.setInt(1, item.getQuantity());
    ps.setInt(2, item.getProductId());
    ps.setString(3, item.getSizeLabel());
    ps.setInt(4, item.getQuantity()); // Must have at least this amount

    int rowsAffected = ps.executeUpdate();
    if (rowsAffected == 0) {
        // Stock was insufficient! Abort checkout.
        connection.rollback();
        throw new OutOfStockException("Size " + item.getSizeLabel() + " is sold out!");
    }
}
connection.commit(); // Successfully updated and locked"""
    story.append(Paragraph(sql_code.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))

    story.append(Paragraph(
        "<b>Pessimistic Locking vs. Optimistic Locking:</b><br/>"
        "&bull; <b>Pessimistic Locking (<code>SELECT ... FOR UPDATE</code>):</b> Acquires an exclusive row lock at the database level. No other transaction can read or write that row until the transaction commits. Ideal for high-contention flash sales.<br/>"
        "&bull; <b>Optimistic Locking (Version Column):</b> Each row has a <code>version INT</code>. Updates only succeed if <code>WHERE version = current_version</code>. If another buyer updated first, a <code>StaleObjectStateException</code> is thrown and the user retries.",
        body_style
    ))

    story.append(PageBreak())

    # ================= SECTION 4: 25+ INTERVIEW QUESTIONS & ANSWERS =================
    story.append(Paragraph("4. Top 25 Technical Interview Questions &amp; High-Scoring Answers", h1_style))
    story.append(Paragraph(
        "The following questions are specifically tailored to this project and represent what top recruiters and senior engineers ask in Java, E-Commerce, and System Design interviews:",
        body_style
    ))

    qas = [
        (
            "Q1. Walk me through the architecture of your e-commerce project.",
            "I developed TrendVibe, an enterprise fashion and cosmetics e-commerce platform inspired by Myntra and Nykaa. It follows the MVC and DAO architectural patterns. The View layer utilizes responsive HTML5, CSS3, and JSP with JSTL. The Controller layer uses Jakarta EE Servlets mapped via web.xml to handle requests and manage HTTP sessions. The Model layer consists of serializable JavaBeans, while the DAO layer executes parameterized JDBC queries against a normalized 8-table MySQL database. I deployed the web application on Apache Tomcat 10+."
        ),
        (
            "Q2. Why did you choose the DAO pattern instead of writing SQL queries directly inside Servlets?",
            "Writing SQL queries in Servlets violates the Single Responsibility Principle and couples web request handling with database access. The DAO pattern abstracts and encapsulates all database interactions. If we decide to migrate from MySQL to PostgreSQL, or adopt an ORM like Hibernate, we only modify the DAO implementation classes without changing a single line of servlet or controller code."
        ),
        (
            "Q3. How do you prevent SQL Injection attacks in your application?",
            "We strictly use <code>PreparedStatement</code> with parameterized placeholders (<code>?</code>) instead of string concatenation in raw SQL statements. PreparedStatements pre-compile the SQL statement on the database server. User input is treated strictly as literal data rather than executable SQL code, entirely neutralizing injection attempts."
        ),
        (
            "Q4. How does the shopping cart work for guest users vs. authenticated users?",
            "When an unauthenticated guest user adds an item to their bag, the cart is maintained in their HTTP session (<code>session.getAttribute(\"cart\")</code>). Once the user logs in or registers, the session cart items are merged into the persistent MySQL <code>cart</code> and <code>cart_items</code> tables associated with their unique <code>user_id</code>. This ensures their selections are never lost across devices."
        ),
        (
            "Q5. How do you manage database connections efficiently? What happens under high load?",
            "Instead of opening and closing a physical connection on every HTTP request—which is expensive due to TCP handshake and authentication overhead—we utilize connection pooling via <code>DBConnection</code>. We reuse pre-established database connections from the pool. In high-traffic scenarios, Tomcat's JNDI DataSource maintains an active pool (e.g. 20-50 connections), drastically lowering response latency."
        ),
        (
            "Q6. How does your system handle multi-size inventory (e.g. Shirts with S, M, L, XL)?",
            "We designed a normalized one-to-many relationship: <code>products (1) &rarr; product_sizes (N)</code>. Each size entry holds its own <code>size_label</code>, <code>stock_quantity</code>, and unique <code>sku_code</code>. This allows us to display real-time stock availability per size, alert users when a specific size has 'Only 2 units left', and disable sold-out sizes dynamically in the UI."
        ),
        (
            "Q7. Explain how an order checkout transaction works and how you guarantee ACID properties.",
            "Checkout involves multiple database operations: inserting into <code>orders</code>, inserting multiple rows into <code>order_items</code>, decrementing stock in <code>product_sizes</code>, and clearing <code>cart_items</code>. We invoke <code>connection.setAutoCommit(false)</code> to begin an atomic transaction. If any item is out of stock or an error occurs, we execute <code>connection.rollback()</code>, guaranteeing that stock is never deducted without an order being created. If all succeed, <code>connection.commit()</code> commits the changes."
        ),
        (
            "Q8. How did you ensure the website is 100% mobile-responsive for smartphones?",
            "I used a mobile-first CSS architecture. For viewports under 768px, the product grid automatically formats into a native-feeling 2-column layout (<code>grid-template-columns: repeat(2, 1fr)</code>) with 4:5 fashion aspect ratios. We also implemented a slide-out drawer menu, horizontally scrolling category chips, and a native app bottom navigation bar with iOS safe-area inset support."
        ),
        (
            "Q9. What is the difference between <code>forward()</code> and <code>sendRedirect()</code>?",
            "<code>RequestDispatcher.forward()</code> happens entirely on the server-side: Tomcat forwards the request and response objects to another resource (like a JSP view) without the client knowing, keeping the original URL in the address bar. <code>HttpServletResponse.sendRedirect()</code> sends an HTTP 302 redirect header to the client browser, forcing it to initiate a new GET request to the new URL. We use forward for rendering views and sendRedirect after successful POST actions (Post/Redirect/Get pattern to prevent duplicate form submissions)."
        ),
        (
            "Q10. What is the Servlet Lifecycle?",
            "Tomcat manages the servlet lifecycle through three core methods: 1. <code>init(ServletConfig config)</code>: called once when the servlet is first loaded into memory. 2. <code>service(HttpServletRequest req, HttpServletResponse res)</code>: called on every client request, which delegates to <code>doGet()</code>, <code>doPost()</code>, etc., across worker threads. 3. <code>destroy()</code>: called once when the server shuts down or the application is undeployed to release resources."
        ),
        (
            "Q11. Are Servlets thread-safe?",
            "No. Tomcat creates a single instance of each servlet and executes concurrent requests on separate threads using the same instance. Therefore, instance variables inside a servlet are shared across all users and threads, leading to race conditions. To ensure thread safety, servlets must be stateless: all request-specific data must be stored in local method variables, request attributes, or session attributes."
        ),
        (
            "Q12. What indexes did you create in MySQL and why?",
            "We added B-Tree indexes on high-frequency query columns: <code>category_id</code> on <code>products</code>, <code>product_id</code> on <code>product_sizes</code>, <code>user_id</code> on <code>orders</code>, and <code>cart_id</code> on <code>cart_items</code>. Without indexing, MySQL performs full table scans (O(N) complexity). With indexes, lookup time is reduced to O(log N), allowing instant catalog filtering and cart retrieval."
        ),
        (
            "Q13. How would you scale this platform to handle 1 Million daily active users?",
            "I would implement horizontal scaling and caching: 1. Place an Nginx reverse proxy / load balancer in front of multiple Tomcat nodes. 2. Use Redis as a distributed in-memory cache for product catalog queries and session storage. 3. Configure MySQL Master-Slave replication (writes to Master, reads distributed across Read Replicas). 4. Offload static media (images, CSS, JS) to a Content Delivery Network (CDN) like AWS CloudFront or Cloudflare."
        ),
        (
            "Q14. How did you structure your Git repository and deployment workflow?",
            "The project uses standard Git branching. The <code>main</code> branch contains the complete production-ready Jakarta EE and Maven source code for Eclipse IDE. We automated continuous deployment by publishing an interactive, live client-side application to the <code>gh-pages</code> branch on GitHub Pages, giving recruiters instant access without local server setup."
        )
    ]

    for q, a in qas:
        story.append(Paragraph(q, qa_q_style))
        story.append(Paragraph(a, qa_a_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF: {filename}")

if __name__ == "__main__":
    build_pdf()
