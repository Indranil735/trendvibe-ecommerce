import glob

jsp_files = glob.glob('src/main/webapp/**/*.jsp', recursive=True)
count = 0
for jsp in jsp_files:
    with open(jsp, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content
    # Replace > 0 with gt 0 inside ${...}
    new_content = new_content.replace('cart.itemCount > 0', 'cart.itemCount gt 0')
    new_content = new_content.replace('.discountPercent > 0', '.discountPercent gt 0')
    new_content = new_content.replace('quantity <= 1', 'quantity le 1')
    new_content = new_content.replace('quantity < 1', 'quantity lt 1')
    if new_content != content:
        with open(jsp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed EL operators in {jsp}')
        count += 1

print(f'Completed fixing {count} JSP files.')
