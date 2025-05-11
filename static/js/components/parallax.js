document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    let lastScrollY = window.scrollY;
    const parallaxSpeed = 0.4; // Increased from 0.15 to 0.4 for more obvious effect

    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        const yOffset = currentScrollY * parallaxSpeed;
        
        // Move texture layer more dramatically
        body.style.backgroundPosition = `center ${yOffset}px, center center`;
        
        lastScrollY = currentScrollY;
    }, { passive: true });
});