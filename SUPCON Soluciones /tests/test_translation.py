import pytest
from playwright.sync_api import Page, expect

# Import prohibited terms to check against visible UI text
from verificar_catalogo import PROHIBITED_TERMS

def test_header_text_is_spanish(page: Page, server_url: str):
    """Test that the main header text is in Spanish and contains no English."""
    page.goto(server_url)
    header_text = page.locator("#header-title").text_content()
    assert "Catálogo" in header_text
    assert "Dispositivos" in header_text
    assert "Campo" in header_text
    assert "Catalog" not in header_text
    assert "Devices" not in header_text

def test_search_labels_and_placeholder_are_spanish(page: Page, server_url: str):
    """Test that the search bar labels and placeholders are in Spanish."""
    page.goto(server_url)
    label_text = page.locator('label[for="search-input"]').text_content()
    placeholder_text = page.locator("#search-input").get_attribute("placeholder")
    
    assert "Buscar por nombre" in label_text
    assert "Escriba el nombre" in placeholder_text
    assert "Search" not in label_text
    assert "type" not in placeholder_text.lower()

def test_filter_labels_are_spanish(page: Page, server_url: str):
    """Test that the labels for advanced filters are in Spanish."""
    page.goto(server_url)
    
    size_label = page.locator('label[for="filter-size"]').text_content()
    pressure_label = page.locator('label[for="filter-pressure"]').text_content()
    leakage_label = page.locator('label[for="filter-leakage"]').text_content()
    
    assert "Diámetro Nominal" in size_label
    assert "Presión Máxima" in pressure_label
    assert "Clase de Fuga" in leakage_label
    
    assert "diameter" not in size_label.lower()
    assert "pressure" not in pressure_label.lower()
    assert "leakage" not in leakage_label.lower()

def test_quote_modal_labels_are_spanish(page: Page, server_url: str):
    """Test that all label texts in the quote modal form are in Spanish."""
    page.goto(server_url)
    page.locator(".product-card .quote-btn").first.click()
    
    modal_title = page.locator("#modal-title").text_content()
    name_label = page.locator('label[for="client-name"]').text_content()
    email_label = page.locator('label[for="client-email"]').text_content()
    qty_label = page.locator('label[for="quote-qty"]').text_content()
    comments_label = page.locator('label[for="quote-comments"]').text_content()
    submit_btn = page.locator("#submit-quote").text_content()
    
    assert "Solicitud de Cotización" in modal_title
    assert "Nombre Completo" in name_label
    assert "Correo Electrónico" in email_label
    assert "Cantidad Requerida" in qty_label
    assert "Comentarios Adicionales" in comments_label
    assert "Enviar Cotización" in submit_btn
    
    assert "name" not in name_label.lower()
    assert "email" not in email_label.lower()
    assert "quantity" not in qty_label.lower()
    assert "submit" not in submit_btn.lower()

def test_no_prohibited_english_terms_visible_in_grid(page: Page, server_url: str):
    """Test that none of the prohibited English terms are rendered inside the product grid."""
    page.goto(server_url)
    page.wait_for_selector(".product-card")
    
    grid_text = page.locator("#product-grid").text_content().lower()
    
    for term in PROHIBITED_TERMS:
        # Ignore "class" if it is checked, but let's check:
        # "class" is in PROHIBITED_TERMS. But we use "Clase IV", which does not contain "class".
        # So "class" in "clase iv" is False.
        # "leakage", "pressure rating", etc. should not be in the product text.
        assert term not in grid_text, f"Found prohibited English term '{term}' in product grid text."
