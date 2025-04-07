document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.querySelector('.toggle-nav-btn');
    const navbarLinks = document.querySelector('.navbar-links');
    const menuIcon = toggleButton.querySelector('img');

    // Store the base paths for the icons with cache-busting
    const menuIconPath = `/static/assets/images/navbar/menu.png?v=${Date.now()}`;
    const closeIconPath = `/static/assets/images/navbar/close.png?v=${Date.now()}`;

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