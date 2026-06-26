import os
import sys
import json
import subprocess
import pytest

# Add project root to path so we can import verificar_catalogo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import verificar_catalogo

def test_check_text_for_english_detects_prohibited_terms():
    """Test that check_text_for_english detects prohibited English terms."""
    # Test with direct prohibited term
    violations = verificar_catalogo.check_text_for_english("This is a globe control valve.", "test.field")
    assert len(violations) == 1
    assert violations[0][1] == "globe control valve"
    
    # Test case insensitivity
    violations2 = verificar_catalogo.check_text_for_english("ZERO LEAKAGE expected", "test.field")
    assert len(violations2) == 1
    assert violations2[0][1] == "zero leakage"

def test_check_text_for_english_ignores_valid_spanish():
    """Test that check_text_for_english does not flag valid Spanish technical terms."""
    clean_texts = [
        "Válvula de control tipo globo de asiento simple",
        "Estanqueidad de burbuja clase VI",
        "Transmisor de presión inteligente",
        "Rango de medición de caudal",
        "Par de torsión del actuador"
    ]
    for text in clean_texts:
        violations = verificar_catalogo.check_text_for_english(text, "test.field")
        assert len(violations) == 0, f"False positive flag for: {text}"

def test_audit_product_detects_nested_english_terms():
    """Test that audit_product scans all fields including features and specifications."""
    bad_product = {
        "id": "test-prod",
        "name": "Válvula de control",
        "category": "Válvulas de Globo",
        "description": "Una válvula normal",
        "features": [
            "Fácil instalación",
            "Double eccentric design" # "double eccentric" is prohibited
        ],
        "specifications": {
            "diámetro_nominal": "DN50",
            "leakage": "Clase VI" # "leakage" is prohibited
        },
        "certificates": ["CE"]
    }
    
    violations = verificar_catalogo.audit_product(bad_product)
    assert len(violations) >= 2
    violation_fields = [v[0] for v in violations]
    assert "test-prod.features[1]" in violation_fields
    assert "test-prod.specifications.key(leakage)" in violation_fields

def test_verification_script_success():
    """Test that running verificar_catalogo.py on the current valid products.json exits with 0."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    script_path = os.path.join(project_root, "verificar_catalogo.py")
    
    # Execute the script
    result = subprocess.run([sys.executable, script_path], cwd=project_root, capture_output=True, text=True)
    assert result.returncode == 0
    assert "All verification checks passed successfully!" in result.stdout

def test_verification_script_fails_missing_file(tmp_path):
    """Test that the script fails and exits with 1 when productos.json is missing."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    script_path = os.path.join(project_root, "verificar_catalogo.py")
    
    # Run in a temp directory where productos.json does not exist
    result = subprocess.run([sys.executable, script_path], cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 1
    assert "ERROR: productos.json does not exist!" in result.stdout

def test_verification_script_fails_under_15_products(tmp_path):
    """Test that the script fails if productos.json has fewer than 15 products."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    script_path = os.path.join(project_root, "verificar_catalogo.py")
    
    # Write a temporary productos.json with only 2 products
    temp_products = [
        {
            "id": "valvula-1",
            "name": "Válvula A",
            "category": "Válvulas de Globo",
            "description": "Una",
            "features": [],
            "specifications": {},
            "certificates": []
        },
        {
            "id": "valvula-2",
            "name": "Válvula B",
            "category": "Válvulas de Bola",
            "description": "Dos",
            "features": [],
            "specifications": {},
            "certificates": []
        }
    ]
    
    with open(tmp_path / "productos.json", "w", encoding="utf-8") as f:
        json.dump(temp_products, f)
        
    result = subprocess.run([sys.executable, script_path], cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 1
    assert "ERROR: Product count" in result.stdout
