const menu = document.getElementById('myLinks');
const icon = document.getElementById('menu-icon');

function myFunction() {

    const isOpen = menu.classList.toggle('active');

    icon.textContent = isOpen ? '✕' : '☰';
}

document.querySelector('.icon').addEventListener('click', function(event) {
    event.stopPropagation();
});

menu.addEventListener('click', function(event) {
    event.stopPropagation();
});

document.addEventListener('click', function() {
    menu.classList.remove('active');
    icon.textContent = '☰';
});

menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        menu.classList.remove('active');
        icon.textContent = '☰';
    });
});