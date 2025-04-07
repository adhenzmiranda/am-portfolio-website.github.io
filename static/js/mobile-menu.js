document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.querySelector('.toggle-nav-btn');
    const navbarLinks = document.querySelector('.navbar-links');
    const menuIcon = toggleButton.querySelector('img');

    toggleButton.addEventListener('click', function () {
        navbarLinks.classList.toggle('active');
        toggleButton.classList.toggle('active');

        if (navbarLinks.classList.contains('active')) {
            menuIcon.src = "{% static 'assets/images/navbar/close.png' %}";
        } else {
            menuIcon.src = "{% static 'assets/images/navbar/menu.png' %}";
        }
    });

    const navLinks = document.querySelectorAll('.navbar-links .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navbarLinks.classList.remove('active');
            toggleButton.classList.remove('active');
            menuIcon.src = "{% static 'assets/images/navbar/menu.png' %}";
        });
    });
}); 