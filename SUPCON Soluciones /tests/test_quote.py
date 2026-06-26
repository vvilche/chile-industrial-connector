import re
import pytest
from playwright.sync_api import Page, expect

def test_modal_initially_hidden(page: Page, server_url: str):
    """Test that the quote request modal is hidden when page is first loaded."""
    page.goto(server_url)
    modal = page.locator("#quote-modal")
    expect(modal).to_have_class(re.compile("hidden"))

def test_open_modal_populates_product_name(page: Page, server_url: str):
    """Test that clicking 'Solicitar Cotización' opens the modal and displays the selected product."""
    page.goto(server_url)
    page.wait_for_selector(".product-card")
    
    first_card = page.locator(".product-card").first
    prod_name = first_card.locator("h3").text_content()
    first_card.locator(".quote-btn").click()
    
    modal = page.locator("#quote-modal")
    expect(modal).not_to_have_class(re.compile("hidden"))
    
    product_input = page.locator("#quote-product-name")
    expect(product_input).to_have_value(prod_name)
    expect(product_input).to_have_attribute("readonly", "")

def test_close_modal_via_close_button(page: Page, server_url: str):
    """Test that clicking the close (X) button closes the modal."""
    page.goto(server_url)
    page.locator(".product-card .quote-btn").first.click()
    
    modal = page.locator("#quote-modal")
    expect(modal).not_to_have_class(re.compile("hidden"))
    
    page.click("#close-modal")
    expect(modal).to_have_class(re.compile("hidden"))

def test_close_modal_via_cancel_button(page: Page, server_url: str):
    """Test that clicking the Cancelar button closes the modal."""
    page.goto(server_url)
    page.locator(".product-card .quote-btn").first.click()
    
    modal = page.locator("#quote-modal")
    expect(modal).not_to_have_class(re.compile("hidden"))
    
    page.click("#cancel-quote")
    expect(modal).to_have_class(re.compile("hidden"))

def test_submit_quote_success(page: Page, server_url: str):
    """Test successful submission of a quotation request showing the success message."""
    page.goto(server_url)
    page.locator(".product-card .quote-btn").first.click()
    
    # Fill in the form fields
    page.fill("#client-name", "Juan Pérez")
    page.fill("#client-email", "juan.perez@empresa.cl")
    page.fill("#quote-qty", "5")
    page.fill("#quote-comments", "Requerimos calibración para alta presión.")
    
    # Submit form
    page.click('#submit-quote')
    
    # Check that success message is shown
    success_msg = page.locator("#quote-success-message")
    expect(success_msg).to_be_visible()
    expect(success_msg).to_have_text("¡Cotización enviada con éxito! Nos pondremos en contacto a la brevedad.")

def test_submit_quote_form_validation(page: Page, server_url: str):
    """Test that required fields block form submission when empty."""
    page.goto(server_url)
    page.locator(".product-card .quote-btn").first.click()
    
    # Leave client-name and client-email blank and try to submit
    page.fill("#client-name", "")
    page.fill("#client-email", "")
    
    # Use trigger submit via click (browser validation should trigger or custom)
    page.click('#submit-quote')
    
    # Success message must NOT be visible
    success_msg = page.locator("#quote-success-message")
    expect(success_msg).to_have_class(re.compile("hidden"))
