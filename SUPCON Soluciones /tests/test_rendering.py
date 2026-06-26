import re
import pytest
from playwright.sync_api import Page, expect

def test_page_title(page: Page, server_url: str):
    """Test that the page title is correct and in Spanish."""
    page.goto(server_url)
    expect(page).to_have_title("Catálogo de Dispositivos de Campo SUPCON")

def test_header_rendering(page: Page, server_url: str):
    """Test that the header elements render correctly."""
    page.goto(server_url)
    header_title = page.locator("#header-title")
    expect(header_title).to_be_visible()
    expect(header_title).to_have_text("Catálogo de Dispositivos de Campo SUPCON")

def test_initial_product_load_count(page: Page, server_url: str):
    """Test that all 15 products are loaded and displayed initially."""
    page.goto(server_url)
    # Wait for the product cards to load
    page.wait_for_selector(".product-card")
    product_cards = page.locator(".product-card")
    expect(product_cards).to_have_count(15)

def test_product_card_details(page: Page, server_url: str):
    """Test that a product card contains all expected structural fields."""
    page.goto(server_url)
    page.wait_for_selector(".product-card")
    
    # Check the first product card
    first_card = page.locator(".product-card").first
    expect(first_card.locator("h3")).to_be_visible()
    expect(first_card.locator(".cat-badge")).to_be_visible()
    expect(first_card.locator(".desc")).to_be_visible()
    expect(first_card.locator(".features")).to_be_visible()
    expect(first_card.locator(".specs")).to_be_visible()
    expect(first_card.locator(".certs")).to_be_visible()
    expect(first_card.locator(".quote-btn")).to_be_visible()

def test_theme_toggle_behavior(page: Page, server_url: str):
    """Test that the theme toggle changes the HTML class between light and dark."""
    page.goto(server_url)
    html_element = page.locator("html")
    
    # Initially should be light or no dark class
    expect(html_element).to_have_class(re.compile("light"))
    expect(html_element).not_to_have_class(re.compile("dark"))
    
    # Toggle theme
    page.click("#theme-toggle")
    expect(html_element).to_have_class(re.compile("dark"))
    expect(html_element).not_to_have_class(re.compile("light"))
    
    # Toggle back
    page.click("#theme-toggle")
    expect(html_element).to_have_class(re.compile("light"))
    expect(html_element).not_to_have_class(re.compile("dark"))

def test_product_count_badge_rendering(page: Page, server_url: str):
    """Test that the count badge renders the correct initial text."""
    page.goto(server_url)
    count_badge = page.locator("#product-count")
    expect(count_badge).to_have_text("Mostrando 15 productos")
