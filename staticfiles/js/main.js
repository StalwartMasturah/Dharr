document.getElementById('account-link').addEventListener('click', function(e) {
  e.preventDefault();
  const card = document.getElementById('account-card');
  card.style.display = (card.style.display === 'block') ? 'none' : 'block';
});

// Optional: hide card if clicked outside
document.addEventListener('click', function(e) {
  const card = document.getElementById('account-card');
  const link = document.getElementById('account-link');

  if (!card.contains(e.target) && !link.contains(e.target)) {
    card.style.display = 'none';
  }
});

