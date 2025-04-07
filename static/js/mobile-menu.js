document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.querySelector('.toggle-nav-btn');
    const navbarLinks = document.querySelector('.navbar-links');
    const menuIcon = toggleButton.querySelector('img');

    // Store the base paths for the icons
    const menuIconPath = '/static/assets/images/navbar/menu.png';
    const closeIconPath = '/static/assets/images/navbar/close.png';

    toggleButton.addEventListener('click', function () {
        navbarLinks.classList.toggle('active');
        toggleButton.classList.toggle('active');

        if (navbarLinks.classList.contains('active')) {
            menuIcon.src = closeIconPath;
        } else {
            menuIcon.src = menuIconPath;
        }
    });

    const navLinks = document.querySelectorAll('.navbar-links .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navbarLinks.classList.remove('active');
            toggleButton.classList.remove('active');
            menuIcon.src = menuIconPath;
        });
    });
}); 