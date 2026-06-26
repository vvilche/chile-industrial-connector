import pytest
from playwright.sync_api import Page, expect

def test_search_by_partial_name(page: Page, server_url: str):
    """Test searching with partial keyword 'globo' matches the 4 globe valves."""
    page.goto(server_url)
    search_input = page.locator("#search-input")
    search_input.fill("globo")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(4)
    expect(page.locator("#product-count")).to_have_text("Mostrando 4 productos")

def test_search_exact_match(page: Page, server_url: str):
    """Test searching with a highly specific term returns the exact single product."""
    page.goto(server_url)
    search_input = page.locator("#search-input")
    search_input.fill("criogénica")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(1)
    expect(product_cards.first.locator("h3")).to_have_text("Válvula de globo criogénica modelo VG2")

def test_search_with_whitespace_trimming(page: Page, server_url: str):
    """Test that leading/trailing whitespaces in search inputs are trimmed."""
    page.goto(server_url)
    search_input = page.locator("#search-input")
    search_input.fill("   bola   ")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(4)

def test_search_no_results(page: Page, server_url: str):
    """Test that searching for a non-existent item shows a friendly message and 0 count."""
    page.goto(server_url)
    search_input = page.locator("#search-input")
    search_input.fill("inexistente-12345")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(0)
    expect(page.locator("#product-count")).to_have_text("Mostrando 0 productos")
    
    no_results_msg = page.locator("#no-products-message")
    expect(no_results_msg).to_be_visible()
    expect(no_results_msg).to_have_text("No se encontraron productos que coincidan con los filtros.")

def test_search_clear_restores_products(page: Page, server_url: str):
    """Test that clearing the search input displays the full list of products again."""
    page.goto(server_url)
    search_input = page.locator("#search-input")
    search_input.fill("wafer")
    expect(page.locator(".product-card")).to_have_count(1)
    
    search_input.fill("")
    expect(page.locator(".product-card")).to_have_count(15)

def test_search_combined_with_category(page: Page, server_url: str):
    """Test search functionality in combination with active category tabs."""
    page.goto(server_url)
    # Filter by Válvulas de Globo first
    page.click('button[data-category="Válvulas de Globo"]')
    expect(page.locator(".product-card")).to_have_count(4)
    
    # Search for model 'VG1' inside Válvulas de Globo
    search_input = page.locator("#search-input")
    search_input.fill("VG1")
    expect(page.locator(".product-card")).to_have_count(1)
    expect(page.locator(".product-card").first.locator("h3")).to_have_text("Válvula de globo para control de fluidos modelo VG1")
    
    # Search for model 'VB1' (which is Válvula de Bola) while in Válvulas de Globo should yield 0
    search_input.fill("VB1")
    expect(page.locator(".product-card")).to_have_count(0)
