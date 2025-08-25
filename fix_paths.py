import re

def fix_html(input_file="export/index.html", output_file="export/index.html"):
    with open(input_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove localhost URLs like http://localhost:52241/
    html = re.sub(r"https?://localhost:\d+/", "", html)

    # Fix absolute paths like /libs/... → libs/...
    html = re.sub(r'"/+libs/', '"libs/', html)
    html = re.sub(r'"/+assets/', '"assets/', html)

    # Optionally, do the same for CSS/JS references
    html = re.sub(r'"/+my_theme.css', '"my_theme.css', html)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Fixed HTML saved to {output_file}")

if __name__ == "__main__":
    fix_html()
