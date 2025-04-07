document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.querySelector('.toggle-nav-btn');
    const navbarLinks = document.querySelector('.navbar-links');

    toggleButton.addEventListener('click', function () {
        navbarLinks.classList.toggle('active');
    });
}); 