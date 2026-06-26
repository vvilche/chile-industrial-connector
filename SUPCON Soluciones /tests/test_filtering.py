import pytest
from playwright.sync_api import Page, expect

def test_filter_by_size(page: Page, server_url: str):
    """Test filtering by nominal diameter (DN50) returns matching products."""
    page.goto(server_url)
    page.select_option("#filter-size", "DN50")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(2)
    
    # Verify specs contain DN50
    for i in range(2):
        expect(product_cards.nth(i).locator(".specs")).to_contain_text("DN50")

def test_filter_by_pressure(page: Page, server_url: str):
    """Test filtering by maximum pressure (PN40) returns matching products."""
    page.goto(server_url)
    page.select_option("#filter-pressure", "PN40")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(3)
    
    for i in range(3):
        expect(product_cards.nth(i).locator(".specs")).to_contain_text("PN40")

def test_filter_by_seat_leakage(page: Page, server_url: str):
    """Test filtering by seat leakage class ('Cero fugas') returns matching products."""
    page.goto(server_url)
    page.select_option("#filter-leakage", "Cero fugas")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(4)
    
    for i in range(4):
        expect(product_cards.nth(i).locator(".specs")).to_contain_text("Cero fugas")

def test_combined_advanced_filters(page: Page, server_url: str):
    """Test combining multiple advanced filter criteria (Size DN80 + Pressure PN25 + Leakage Clase V)."""
    page.goto(server_url)
    page.select_option("#filter-size", "DN80")
    page.select_option("#filter-pressure", "PN25")
    page.select_option("#filter-leakage", "Clase V")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(1)
    expect(product_cards.first.locator("h3")).to_have_text("Válvula de globo criogénica modelo VG2")

def test_reset_filters_individually(page: Page, server_url: str):
    """Test resetting an active filter back to 'Todos' restores the other products."""
    page.goto(server_url)
    # Select size DN100
    page.select_option("#filter-size", "DN100")
    expect(page.locator(".product-card")).to_have_count(1)
    
    # Reset size to Todos
    page.select_option("#filter-size", "Todos")
    expect(page.locator(".product-card")).to_have_count(15)

def test_no_matching_combined_filters(page: Page, server_url: str):
    """Test when no product matches the combination of selected criteria."""
    page.goto(server_url)
    # Size DN300 and Pressure PN10
    page.select_option("#filter-size", "DN300")
    page.select_option("#filter-pressure", "PN10")
    
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(0)
    expect(page.locator("#product-count")).to_have_text("Mostrando 0 productos")
