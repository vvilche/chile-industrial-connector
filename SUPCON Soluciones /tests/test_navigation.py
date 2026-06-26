import pytest
from playwright.sync_api import Page, expect

def test_category_buttons_visibility(page: Page, server_url: str):
    """Test that all category selection buttons are visible with correct Spanish names."""
    page.goto(server_url)
    category_buttons = page.locator("#category-nav-container .cat-btn")
    expect(category_buttons).to_have_count(5)
    
    expected_categories = [
        "Todos",
        "Válvulas de Globo",
        "Válvulas de Bola",
        "Válvulas de Mariposa",
        "Otros Instrumentos"
    ]
    for idx, category in enumerate(expected_categories):
        expect(category_buttons.nth(idx)).to_have_text(category)

def test_navigate_to_valvulas_globo(page: Page, server_url: str):
    """Test that selecting 'Válvulas de Globo' displays exactly 4 products."""
    page.goto(server_url)
    page.click('button[data-category="Válvulas de Globo"]')
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(4)
    expect(page.locator("#product-count")).to_have_text("Mostrando 4 productos")
    
    # Check that all visible cards belong to this category
    for i in range(4):
        expect(product_cards.nth(i).locator(".cat-badge")).to_have_text("Válvulas de Globo")

def test_navigate_to_valvulas_bola(page: Page, server_url: str):
    """Test that selecting 'Válvulas de Bola' displays exactly 4 products."""
    page.goto(server_url)
    page.click('button[data-category="Válvulas de Bola"]')
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(4)
    expect(page.locator("#product-count")).to_have_text("Mostrando 4 productos")
    
    for i in range(4):
        expect(product_cards.nth(i).locator(".cat-badge")).to_have_text("Válvulas de Bola")

def test_navigate_to_valvulas_mariposa(page: Page, server_url: str):
    """Test that selecting 'Válvulas de Mariposa' displays exactly 4 products."""
    page.goto(server_url)
    page.click('button[data-category="Válvulas de Mariposa"]')
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(4)
    expect(page.locator("#product-count")).to_have_text("Mostrando 4 productos")
    
    for i in range(4):
        expect(product_cards.nth(i).locator(".cat-badge")).to_have_text("Válvulas de Mariposa")

def test_navigate_to_otros_instrumentos(page: Page, server_url: str):
    """Test that selecting 'Otros Instrumentos' displays exactly 3 products."""
    page.goto(server_url)
    page.click('button[data-category="Otros Instrumentos"]')
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(3)
    expect(page.locator("#product-count")).to_have_text("Mostrando 3 productos")
    
    for i in range(3):
        expect(product_cards.nth(i).locator(".cat-badge")).to_have_text("Otros Instrumentos")

def test_navigate_back_to_todos(page: Page, server_url: str):
    """Test that selecting 'Todos' resets the category filter and displays all 15 products."""
    page.goto(server_url)
    # First select a subcategory
    page.click('button[data-category="Otros Instrumentos"]')
    expect(page.locator(".product-card")).to_have_count(3)
    
    # Then click Todos
    page.click('button[data-category="Todos"]')
    expect(page.locator(".product-card")).to_have_count(15)
    expect(page.locator("#product-count")).to_have_text("Mostrando 15 productos")
Approved.
