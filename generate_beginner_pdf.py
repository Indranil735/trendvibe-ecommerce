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
            self.drawString(54, 752, "TRENDVIBE ATELIER &bull; SIMPLE &amp; COMPLETE BEGINNER'S PROJECT GUIDE")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#777777"))
            self.drawRightString(558, 752, "FROM SCRATCH INTERVIEW PREP")
            self.setStrokeColor(colors.HexColor("#D1C7BD"))
            self.setLineWidth(0.6)
            self.line(54, 744, 558, 744)
            
            # Footer
            self.line(54, 45, 558, 45)
            self.drawString(54, 32, "TrendVibe Atelier &bull; Simple Words, Clear Explanations &amp; Real-Life Analogies")
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

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#1A1A1A"),
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#6B5E4F"),
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#111111"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=colors.HexColor("#8C6E3B"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#2C2C2C"),
        spaceAfter=5
    )

    q_style = ParagraphStyle(
        'Question_Style',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor("#111827"),
        spaceBefore=8,
        spaceAfter=2,
        keepWithNext=True
    )

    a_style = ParagraphStyle(
        'Answer_Style',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#374151"),
        spaceAfter=6
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
        borderPadding=5,
        spaceBefore=3,
        spaceAfter=5
    )

    box_style = ParagraphStyle(
        'BoxText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#1A1A1A")
    )

    story = []

    # Title & Banner
    story.append(Paragraph("TRENDVIBE ATELIER", title_style))
    story.append(Paragraph("Complete Project &amp; Code Guide &bull; Explained in Simple Everyday English", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#8C6E3B"), spaceAfter=10))

    meta_data = [
        [
            Paragraph("<b>Target Audience:</b> Complete Beginners &amp; Interview Candidates", box_style),
            Paragraph("<b>Live Website:</b> https://indranil735.github.io/trendvibe-ecommerce/", box_style)
        ],
        [
            Paragraph("<b>Architecture:</b> 3-Tier MVC (Servlets, JDBC, MySQL, HTML5/ES6)", box_style),
            Paragraph("<b>Core Features:</b> 535 Products, Phone+Password Auth, Quick View Drawer", box_style)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[250, 254])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F9F8F6")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#D8CFC4")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5DFD7")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    # Section 1
    story.append(Paragraph("1. What Is This Project? (The 1-Minute Explanation)", h1_style))
    story.append(Paragraph(
        "<b>TrendVibe Atelier</b> is a modern, luxury online shopping store (like Myntra, Zara, or Amazon).<br/>"
        "Here is what happens when someone visits the store:<br/>"
        "&bull; <b>Browse 535 Products:</b> Men's tailored shirts, trousers, Women's silk sarees &amp; dresses, botanical skincare serums, luxury leather footwear, and watches.<br/>"
        "&bull; <b>Quick View &amp; Size Selection:</b> Clicking any product opens a smooth popup showing high-res pictures, details, size buttons (S, M, L, XL), and a 6-digit Pincode delivery estimator.<br/>"
        "&bull; <b>Phone + Password Sign In:</b> No complicated SMS OTP codes! Customers sign in using their 10-digit mobile number and password.<br/>"
        "&bull; <b>Shopping Bag &amp; Checkout:</b> Customers add items to their bag, view their order summary, enter delivery address, pick payment mode (UPI, Card, Cash on Delivery), and receive an instant order confirmation.",
        body_style
    ))

    # Section 2: The Restaurant Analogy
    story.append(Paragraph("2. The Big Picture: The Restaurant Analogy", h1_style))
    story.append(Paragraph(
        "To easily understand the whole system, compare it to a real-life restaurant:",
        body_style
    ))
    analogy_data = [
        [Paragraph("<b>Component</b>", box_style), Paragraph("<b>Restaurant Part</b>", box_style), Paragraph("<b>What It Does</b>", box_style)],
        [
            Paragraph("<b>Frontend (HTML/CSS/JS)</b>", box_style),
            Paragraph("<b>The Dining Room &amp; Menu Card</b>", box_style),
            Paragraph("The visual display. The customer sees beautiful photos, prices, and buttons to click.", box_style)
        ],
        [
            Paragraph("<b>Servlets (Controllers)</b>", box_style),
            Paragraph("<b>The Waiter &amp; Receptionist</b>", box_style),
            Paragraph("Listens to what the customer wants ('Sign In' or 'Buy this Shirt') and takes that order to the back.", box_style)
        ],
        [
            Paragraph("<b>DAO (Data Access Object)</b>", box_style),
            Paragraph("<b>The Kitchen Chef</b>", box_style),
            Paragraph("Knows exactly how to talk to MySQL, write SQL queries, fetch clothes, and deduct stock.", box_style)
        ],
        [
            Paragraph("<b>Model Classes (POJOs)</b>", box_style),
            Paragraph("<b>The Serving Tray / Dish</b>", box_style),
            Paragraph("The clean paper form holding the data (Product name, price, user name) while passing between layers.", box_style)
        ],
        [
            Paragraph("<b>Database (MySQL)</b>", box_style),
            Paragraph("<b>The Refrigerator &amp; Pantry</b>", box_style),
            Paragraph("The safe permanent storage where all accounts, products, and order receipts are locked.", box_style)
        ]
    ]
    t_analogy = Table(analogy_data, colWidths=[120, 140, 244])
    t_analogy.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EFECE6")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#D1C7BD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5DFD7")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_analogy)
    story.append(Spacer(1, 10))

    # Section 3: Model Classes
    story.append(Paragraph("3. Model Classes Explained (What Are They?)", h1_style))
    story.append(Paragraph(
        "A <b>Model class</b> in Java is simply a digital form or blueprint that holds data in memory. "
        "Each variable is <code>private</code> (encapsulation) with public <code>get...()</code> and <code>set...()</code> methods:",
        body_style
    ))
    models_summary = [
        ("User.java", "Holds human customer data: userId, fullName, email, phone (for login), password, address, and pincode."),
        ("Product.java", "Holds catalog item data: productId, productName, brand, basePrice (MRP), discountPercent, finalPrice, and imageUrl."),
        ("ProductSize.java", "Holds inventory variations: sizeLabel ('M', 'L', '42mm'), stockQuantity (e.g. 15 left), and isAvailable."),
        ("Category.java", "Holds store departments: categoryId (1), categoryName ('Tailored Shirts')."),
        ("Cart.java & CartItem.java", "Holds shopping bag contents: list of CartItems, with helper calculations for total items, total MRP, and final payable amount."),
        ("Order.java & OrderItem.java", "Holds confirmed purchases: Order has orderId, orderDate, totalAmount, status. OrderItem saves the unit_price permanently at the moment of checkout.")
    ]
    for m_name, m_desc in models_summary:
        story.append(Paragraph(f"&bull; <b><code>{m_name}</code></b>: {m_desc}", body_style))
    story.append(Spacer(1, 10))

    # Section 4: DBConnection & DAOs
    story.append(Paragraph("4. DBConnection &amp; The DAO Pattern (How Java Talks to MySQL)", h1_style))
    story.append(Paragraph(
        "&bull; <b><code>DBConnection.java</code></b>: Think of this like picking up a telephone. It loads the MySQL driver (<code>Class.forName(\"com.mysql.cj.jdbc.Driver\")</code>), dials the database address (<code>jdbc:mysql://localhost:3306/ecommerce_db</code>), provides the username ('root') and password, and returns an active <code>Connection</code> object.<br/>"
        "&bull; <b>Interface vs. Implementation Class</b>:<br/>"
        "&nbsp;&nbsp;- <b>Interface (e.g. <code>IProductDAO</code>)</b>: The Menu of promises ('I promise there is a method <code>getAllActiveProducts()</code>').<br/>"
        "&nbsp;&nbsp;- <b>Class (e.g. <code>ProductDAO</code>)</b>: The actual Chef who executes <code>PreparedStatement ps = conn.prepareStatement(sql)</code>, iterates the <code>ResultSet</code>, and builds the products list.<br/>"
        "&bull; <b>Atomic Transactions in <code>OrderDAO</code></b>:<br/>"
        "When placing an order, we run: 1) Insert into orders, 2) Insert into order_items, 3) Deduct stock, 4) Clear cart. All 4 steps must succeed together using <code>conn.commit()</code>. If anything fails, <code>conn.rollback()</code> undoes everything like an ATM returning your card without taking your money.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Section 5: Top 10 Interview Q&A
    story.append(Paragraph("5. Top 10 Interview Questions &amp; Word-for-Word Answers", h1_style))
    qa_data = [
        ("1. What is the architecture of your project?",
         "My project uses a 3-tier MVC (Model-View-Controller) architecture. The View is HTML5/CSS/JavaScript. The Controller is Java Servlets. The Model is Java POJO classes. For data persistence, I used the DAO pattern with JDBC to communicate with MySQL."),
        ("2. Why use PreparedStatement over Statement?",
         "PreparedStatement uses parameter placeholders (?) and pre-compiles the SQL query. This completely prevents SQL Injection attacks and runs faster because the database caches the compiled query execution plan."),
        ("3. What is a DAO?",
         "DAO stands for Data Access Object. It isolates database operations from business logic. Servlets do not write raw SQL; instead, they call DAO methods like userDAO.loginUser(), keeping the codebase clean and modular."),
        ("4. How does customer login and session work?",
         "The user submits their phone number and password. The LoginController verifies credentials via UserDAO. If correct, the User object is saved in HttpSession. Tomcat gives the browser a JSESSIONID cookie to keep the customer logged in."),
        ("5. How do you prevent two customers from buying the last shirt?",
         "I use database transactions with row-level pessimistic locking (SELECT ... FOR UPDATE). The second user waits until the first user's order commits. The second query then sees zero stock and safely rolls back without overselling."),
        ("6. What is Third Normal Form (3NF)?",
         "3NF means every piece of data is stored in only one place and depends strictly on the primary key. This eliminates duplicate data and prevents update/delete anomalies."),
        ("7. Why store unit_price inside order_items if products table has it?",
         "To preserve the historical purchase price. If a product's price changes next month in the catalog, past order receipts and invoices must always show the exact price the customer paid on that day."),
        ("8. How did you fix broken or blurred images on the website?",
         "I removed invalid 404 image IDs, used verified high-density fashion photography, and added a JavaScript onerror fallback handler that automatically swaps any failed image to a high-res category photo so no broken icon appears."),
        ("9. Why did you use Phone Number + Password instead of SMS OTP?",
         "SMS OTP relies on third-party SMS networks, causing latency, delivery failures, and recurring fees. Phone + Password provides instant, zero-delay login that is fully testable and secured with password hashing."),
        ("10. Where is your project hosted?",
         "The code is stored in GitHub repository 'Indranil735/trendvibe-ecommerce', and the interactive web application is deployed live on GitHub Pages at https://indranil735.github.io/trendvibe-ecommerce/.")
    ]
    for q, a in qa_data:
        story.append(Paragraph(f"<b>{q}</b>", q_style))
        story.append(Paragraph(a, a_style))

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Beginner PDF generated successfully:", filename)

if __name__ == "__main__":
    out_desktop = "/Users/somaindra/Desktop/TrendVibe_Beginner_Friendly_Project_Guide.pdf"
    build_pdf(out_desktop)
    build_pdf("TrendVibe_Beginner_Friendly_Project_Guide.pdf")
