import os
import re
import pytest

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def test_index_html_exists():
    index_path = os.path.join(REPO_DIR, "index.html")
    assert os.path.exists(index_path)

def test_all_linked_simulations_exist():
    index_path = os.path.join(REPO_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    links = set(re.findall(r'href="([^"#]+\.html)"', content))
    assert len(links) > 0

    for link in links:
        target = os.path.join(REPO_DIR, link)
        assert os.path.isfile(target), f"Linked simulation file {link} is missing on disk"

def test_html_structure_and_canvas():
    html_files = [f for f in os.listdir(REPO_DIR) if f.endswith(".html")]
    assert len(html_files) >= 14

    for html_file in html_files:
        path = os.path.join(REPO_DIR, html_file)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        assert "<!DOCTYPE html>" in content or "<!doctype html>" in content.lower(), f"{html_file} missing DOCTYPE"
        assert "<html" in content, f"{html_file} missing <html> tag"
        assert "</html>" in content, f"{html_file} missing </html> tag"
        assert "<body" in content, f"{html_file} missing <body> tag"
        assert "</body>" in content, f"{html_file} missing </body> tag"
