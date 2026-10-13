with open("generate_ultimate_interview_pdf.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix unescaped HTML characters in Q&A
text = text.replace("stock_quantity >= 0", "stock_quantity &gt;= 0")
text = text.replace("replacing `<` with `&lt;`, `>` with `&gt;`", "replacing &lt; with &amp;lt;, &gt; with &amp;gt;")
text = text.replace("injecting `<script>` tags", "injecting &lt;script&gt; tags")

with open("generate_ultimate_interview_pdf.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Replacement complete")
