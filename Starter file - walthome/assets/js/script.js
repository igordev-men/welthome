const header = document.querySelector('.header'); 
const navToggleBtn = document.querySelector('.nav-toggle-btn'); 
const navbar = document.querySelector('.navbar'); 
navToggleBtn.addEventListener('click', () => {
  header.classList.toggle('active');
  navbar.classList.toggle('active');
});
