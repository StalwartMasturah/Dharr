document.addEventListener("DOMContentLoaded", function () {
  // Account card toggle
  const accountLink = document.getElementById('account-link');
  const accountCard = document.getElementById('account-card');

  if (accountLink && accountCard) {
    accountLink.addEventListener('click', function(e) {
      e.preventDefault();
      accountCard.style.display = (accountCard.style.display === 'block') ? 'none' : 'block';
    });

    // Hide card if clicked outside
    document.addEventListener('click', function(e) {
      if (!accountCard.contains(e.target) && !accountLink.contains(e.target)) {
        accountCard.style.display = 'none';
      }
    });
  }

  // Modal logic
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
