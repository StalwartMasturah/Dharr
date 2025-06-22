document.addEventListener("DOMContentLoaded", function () {
  // Account card toggle
  const accountLink = document.getElementById('account-link');
  const accountCard = document.getElementById('account-card');

  if (accountLink && accountCard) {
    accountLink.addEventListener('click', function(e) {
      e.preventDefault();
      accountCard.style.display = (accountCard.style.display === 'block') ? 'none' : 'block';
    });

    document.addEventListener('click', function(e) {
      if (!accountCard.contains(e.target) && !accountLink.contains(e.target)) {
        accountCard.style.display = 'none';
      }
    });
  }


    // Quick View Modal
  const quickViewModal = document.getElementById("quickViewModal");
  const quickViewImage = document.getElementById("quickViewImage");
  const quickViewClose = document.getElementById("quickViewClose");

  if (quickViewModal && quickViewImage && quickViewClose) {
    document.querySelectorAll(".quick-view-btn").forEach(button => {
      
      button.addEventListener("click", function (e) {
        e.preventDefault();
        const imageUrl = this.getAttribute("data-image-url");
          quickViewModal.style.display = "block";
          quickViewImage.src = imageUrl;
        
      });
    });

    quickViewClose.addEventListener("click", () => {
      quickViewModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
      if (event.target === quickViewModal) {
        quickViewModal.style.display = "none";
      }
    });
  }

  // Info Modal logic
  const modal = document.getElementById("customModal");
  const modalTitle = document.getElementById("modalProductName");
  const modalDetails = document.getElementById("modalProductDetails");
  const closeBtn = document.querySelector(".custom-close");

  if (modal && modalTitle && modalDetails && closeBtn) {
    document.querySelectorAll(".info-btn").forEach(button => {
      button.addEventListener("click", function (e) {
        e.preventDefault();
        const name = this.getAttribute("data-product-name");
        const details = this.getAttribute("data-product-details");
   
        modalTitle.textContent = name;
        modalDetails.textContent = details;
        modal.style.display = "block";
      });
    });

    closeBtn.addEventListener("click", () => {
      modal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    });
  }
});   
 // Function to handle the "Add to Cart" button click
 function addToCart(productId) {
  // Simulate adding to cart
  console.log(`Product ${productId} added to cart!`);
  alert(`Product ${productId} added to cart!`);

}




 
