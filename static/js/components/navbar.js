function initializeNavbar() {
    const toggleNavButton = document.querySelector('.toggle-nav-btn');
    const navbarLinks = document.querySelector('.navbar-links');
    const menuIcon = toggleNavButton.querySelector('img');

    if (!toggleNavButton || !navbarLinks || !menuIcon) {
        console.error('Required elements not found');
        return;
    }

    let isMenuOpen = false;

    toggleNavButton.addEventListener('click', () => {
        isMenuOpen = !isMenuOpen;

        if (isMenuOpen) {
            menuIcon.src = '/static/assets/images/navbar/close.png';
            navbarLinks.classList.add('active');
            toggleNavButton.classList.add('active');
        } else {
            menuIcon.src = '/static/assets/images/navbar/hamburger.png';
            navbarLinks.classList.remove('active');
            toggleNavButton.classList.remove('active');
        }
    });
}

// Initialize when script loads
document.addEventListener('DOMContentLoaded', initializeNavbar);