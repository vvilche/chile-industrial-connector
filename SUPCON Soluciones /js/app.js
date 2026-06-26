document.addEventListener("DOMContentLoaded", () => {
  let allProducts = [];
  let currentCategory = "Todos";
  let searchQuery = "";
  let sizeFilter = "Todos";
  let pressureFilter = "Todos";
  let leakageFilter = "Todos";

  // Elements
  const productGrid = document.getElementById("product-grid");
  const productCount = document.getElementById("product-count");
  const noProductsMessage = document.getElementById("no-products-message");
  const searchInput = document.getElementById("search-input");
  const categoryNavContainer = document.getElementById("category-nav-container");
  const filterSize = document.getElementById("filter-size");
  const filterPressure = document.getElementById("filter-pressure");
  const filterLeakage = document.getElementById("filter-leakage");
  const themeToggle = document.getElementById("theme-toggle");

  // Modal elements
  const quoteModal = document.getElementById("quote-modal");
  const closeModal = document.getElementById("close-modal");
  const cancelQuote = document.getElementById("cancel-quote");
  const quoteForm = document.getElementById("quote-form");
  const quoteProductName = document.getElementById("quote-product-name");
  const quoteSuccessMessage = document.getElementById("quote-success-message");
  const clientName = document.getElementById("client-name");
  const clientEmail = document.getElementById("client-email");
  const quoteQty = document.getElementById("quote-qty");
  const quoteComments = document.getElementById("quote-comments");

  // Initialize
  init();

  async function init() {
    setupEventListeners();
    await loadProducts();
  }

  function setupEventListeners() {
    // Search
    searchInput.addEventListener("input", (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      renderProducts();
    });

    // Category navigation
    categoryNavContainer.addEventListener("click", (e) => {
      const btn = e.target.closest(".cat-btn");
      if (!btn) return;

      // Update active style
      categoryNavContainer.querySelectorAll(".cat-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      currentCategory = btn.getAttribute("data-category");
      renderProducts();
    });

    // Advanced filters
    filterSize.addEventListener("change", (e) => {
      sizeFilter = e.target.value;
      renderProducts();
    });

    filterPressure.addEventListener("change", (e) => {
      pressureFilter = e.target.value;
      renderProducts();
    });

    filterLeakage.addEventListener("change", (e) => {
      leakageFilter = e.target.value;
      renderProducts();
    });

    // Theme toggle
    themeToggle.addEventListener("click", () => {
      const html = document.documentElement;
      if (html.classList.contains("dark")) {
        html.classList.remove("dark");
        html.classList.add("light");
      } else {
        html.classList.remove("light");
        html.classList.add("dark");
      }
    });

    // Modal close
    closeModal.addEventListener("click", hideModal);
    cancelQuote.addEventListener("click", hideModal);
    
    // Modal submit
    quoteForm.addEventListener("submit", (e) => {
      e.preventDefault();
      
      // Basic validation check
      if (!clientName.value.trim() || !clientEmail.value.trim() || !quoteQty.value) {
        alert("Por favor complete todos los campos obligatorios.");
        return;
      }

      // Show success message and hide form fields (except title and success message)
      quoteForm.classList.add("hidden");
      quoteSuccessMessage.classList.remove("hidden");

      // Auto close after 2 seconds
      setTimeout(() => {
        hideModal();
      }, 2000);
    });
  }

  async function loadProducts() {
    try {
      if (typeof SUPCON_PRODUCTS !== "undefined") {
        allProducts = SUPCON_PRODUCTS;
      } else {
        const response = await fetch("productos.json");
        if (!response.ok) {
          throw new Error("No se pudo cargar productos.json");
        }
        allProducts = await response.json();
      }
      renderProducts();
    } catch (error) {
      console.error(error);
      if (noProductsMessage) {
        noProductsMessage.textContent = "Error al cargar los productos. Por favor, reintente más tarde.";
      }
    }
  }

  function renderProducts() {
    // Filter
    const filtered = allProducts.filter(prod => {
      // Category
      if (currentCategory !== "Todos" && prod.category !== currentCategory) {
        return false;
      }

      // Search Query
      if (searchQuery && !prod.name.toLowerCase().includes(searchQuery)) {
        return false;
      }

      // Size
      if (sizeFilter !== "Todos") {
        const dNominal = prod.specifications && (prod.specifications.diámetro_nominal || prod.specifications.diámetro);
        if (dNominal !== sizeFilter) {
          return false;
        }
      }

      // Pressure
      if (pressureFilter !== "Todos") {
        const pMax = prod.specifications && (prod.specifications.presión_máxima || prod.specifications.presión_rating);
        if (pMax !== pressureFilter) {
          return false;
        }
      }

      // Leakage
      if (leakageFilter !== "Todos") {
        const fAsiento = prod.specifications && prod.specifications.fuga_asiento;
        if (fAsiento !== leakageFilter) {
          return false;
        }
      }

      return true;
    });

    // Update count
    productCount.textContent = `Mostrando ${filtered.length} producto${filtered.length === 1 ? "" : "s"}`;

    // Render
    if (filtered.length === 0) {
      productGrid.innerHTML = "";
      if (noProductsMessage) {
        noProductsMessage.textContent = "No se encontraron productos que coincidan con los filtros.";
        noProductsMessage.classList.remove("hidden");
      }
      return;
    }

    if (noProductsMessage) {
      noProductsMessage.classList.add("hidden");
    }

    productGrid.innerHTML = filtered.map(prod => {
      const featuresLi = (prod.features || []).map(f => `<li>${f}</li>`).join("");
      const certsSpan = (prod.certificates || []).map(c => `<span>${c}</span>`).join("");
      
      // Generate specifications list
      let specsHtml = "";
      if (prod.specifications) {
        specsHtml = Object.entries(prod.specifications)
          .map(([key, val]) => `<div><strong>${key.replace("_", " ")}:</strong> ${val}</div>`)
          .join("");
      }

      return `
        <div class="product-card" data-id="${prod.id}">
          <div>
            <span class="cat-badge">${prod.category}</span>
            <h3>${prod.name}</h3>
            <p class="desc">${prod.description}</p>
            <h4 class="text-sm font-semibold mt-2 mb-1">Características:</h4>
            <ul class="features">${featuresLi}</ul>
            <h4 class="text-sm font-semibold mt-2 mb-1">Especificaciones:</h4>
            <div class="specs">${specsHtml}</div>
            <h4 class="text-sm font-semibold mt-2 mb-1">Certificados:</h4>
            <div class="certs">${certsSpan}</div>
          </div>
          <button class="quote-btn mt-4" data-name="${prod.name}">Solicitar Cotización</button>
        </div>
      `;
    }).join("");

    // Add event listeners to quote buttons
    productGrid.querySelectorAll(".quote-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const name = btn.getAttribute("data-name");
        showModal(name);
      });
    });
  }

  function showModal(productName) {
    quoteProductName.value = productName;
    // Reset form fields
    quoteForm.reset();
    quoteForm.classList.remove("hidden");
    quoteSuccessMessage.classList.add("hidden");
    quoteModal.classList.remove("hidden");
  }

  function hideModal() {
    quoteModal.classList.add("hidden");
  }
});
