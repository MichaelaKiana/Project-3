const body = document.body;
const btn = document.querySelectorAll('.button')[0];

btn.addEventListener('mouseenter', () => {
	body.classList.add('hover');
});

btn.addEventListener('mouseleave', () => {
	body.classList.remove('hover');
});