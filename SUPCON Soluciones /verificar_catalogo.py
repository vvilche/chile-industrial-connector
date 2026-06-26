import sys
import json
import os
import re

# File path
JSON_PATH = "productos.json"

# List of prohibited English terms (checked case-insensitively)
PROHIBITED_TERMS = [
    "zero leakage",
    "fugitive emission",
    "globe control valve",
    "ball control valve",
    "ball valve",
    "butterfly valve",
    "pressure transmitter",
    "flowmeter",
    "level transmitter",
    "safety barrier",
    "calibrator",
    "positioner",
    "control system",
    "equal percentage",
    "linear",
    "quick opening",
    "double eccentric",
    "triple-offset",
    "bubble tight",
    "leakage",
    "accuracy",
    "stability",
    "capacity",
    "range",
    "repeatability",
    "beam angle",
    "blind area",
    "drift",
    "signal",
    "abrasion",
    "wear",
    "modularization",
    "cutting",
    "sealing",
    "torque",
    "fire safe",
    "class",
    "pressure rating",
    "nominal diameter",
    "features",
    "specifications",
    "certificates",
    "slurry",
    "erosion",
    "coking",
    "anti-cavitation",
    "anti-scouring",
    "rangeability",
    "flow capacity",
    "friction"
]

def check_text_for_english(text, path_str):
    if not isinstance(text, str):
        return []
    
    violations = []
    # Check each prohibited term
    for term in PROHIBITED_TERMS:
        # Match as word or part of word to be very strict
        if term in text.lower():
            # Exclude false positives or standard abbreviations if they occur inside words
            # But the requirement is "Audits that no English terms exist in the main text fields."
            # So let's report the violation.
            violations.append((path_str, term, text))
    return violations

def audit_product(prod):
    violations = []
    prod_id = prod.get("id", "unknown")
    
    # Audit name
    violations.extend(check_text_for_english(prod.get("name", ""), f"{prod_id}.name"))
    
    # Audit description
    violations.extend(check_text_for_english(prod.get("description", ""), f"{prod_id}.description"))
    
    # Audit features
    for idx, feat in enumerate(prod.get("features", [])):
        violations.extend(check_text_for_english(feat, f"{prod_id}.features[{idx}]"))
        
    # Audit specifications
    specs = prod.get("specifications", {})
    if isinstance(specs, dict):
        for s_key, s_val in specs.items():
            violations.extend(check_text_for_english(s_key, f"{prod_id}.specifications.key({s_key})"))
            violations.extend(check_text_for_english(str(s_val), f"{prod_id}.specifications.value({s_key})"))
            
    # Audit certificates
    certs = prod.get("certificates", [])
    for idx, cert in enumerate(certs):
        violations.extend(check_text_for_english(cert, f"{prod_id}.certificates[{idx}]"))
        
    return violations

def main():
    print("Starting verification of productos.json...")
    
    if not os.path.exists(JSON_PATH):
        print(f"ERROR: {JSON_PATH} does not exist!")
        sys.exit(1)
        
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            products = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to parse {JSON_PATH}: {e}")
        sys.exit(1)
        
    print(f"Loaded {len(products)} products.")
    
    # 1. Check product count (must be at least 15)
    if len(products) < 15:
        print(f"ERROR: Product count ({len(products)}) is less than the required 15!")
        sys.exit(1)
    else:
        print(f"SUCCESS: Product count is {len(products)} (>= 15).")
        
    # 2. Check category distribution (must have at least 4 categories)
    categories = set()
    for prod in products:
        cat = prod.get("category")
        if cat:
            categories.add(cat)
            
    print(f"Found categories: {categories}")
    if len(categories) < 4:
        print(f"ERROR: Category count ({len(categories)}) is less than the required 4!")
        sys.exit(1)
    else:
        print(f"SUCCESS: Found {len(categories)} categories (>= 4).")
        
    # 3. Audit for English terms
    all_violations = []
    for prod in products:
        violations = audit_product(prod)
        all_violations.extend(violations)
        
    if all_violations:
        print(f"\nERROR: Found {len(all_violations)} English term violations in main text fields:")
        for path_str, term, text in all_violations[:20]: # show first 20
            print(f" - Field: {path_str}")
            print(f"   Prohibited Term: '{term}'")
            print(f"   Found In: '{text}'")
        if len(all_violations) > 20:
            print(f" ... and {len(all_violations) - 20} more violations.")
        sys.exit(1)
    else:
        print("SUCCESS: No English term violations found in the main text fields.")
        print("\nAll verification checks passed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
