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

        // Update background position with enhanced movement
        const currentPos = getComputedStyle(body).backgroundPosition.split(',')[0];
        const yPos = parseInt(currentPos.split(' ')[1]) || 0;
        const newYPos = yPos + (direction * scrollDiff);

        // Apply new position only to the texture layer
        body.style.backgroundPosition = `center ${newYPos}px, center center`;

        lastScrollY = currentScrollY;
    }, { passive: true });
});