// Animaciones simples placeholder
document.addEventListener('DOMContentLoaded', function(){
  const els = document.querySelectorAll('.tabla tbody tr');
  els.forEach((el, idx)=> el.style.transition = 'background .3s ease');
});