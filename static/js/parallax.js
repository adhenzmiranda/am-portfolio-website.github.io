document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    let lastScrollY = window.scrollY;

    window.addEventListener('scroll', () => {
        // Get scroll direction and amount
        const currentScrollY = window.scrollY;
        const direction = currentScrollY > lastScrollY ? 1 : -1;
        
        // Adjust this value to change parallax speed (0.1 = subtle, 0.4 = medium, 0.8 = dramatic)
        const parallaxSpeed = 2.0;
        const scrollDiff = Math.abs(currentScrollY - lastScrollY) * parallaxSpeed;

        // Update parallax Y position using CSS variable
        const currentParallaxY = parseInt(getComputedStyle(body).getPropertyValue('--parallax-y')) || 0;
        const newYPos = currentParallaxY + (direction * scrollDiff);
        body.style.setProperty('--parallax-y', `${newYPos}px`);

        lastScrollY = currentScrollY;
    }, { passive: true });
});