// Featured Projects Interactive Carousel with GSAP
// Assumes GSAP is loaded in the page

document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.project-carousel');
    const projects = document.querySelectorAll('.project-carousel .project');
    let activeIndex = 0;

    // Set initial state
    function setActive(idx) {
        projects.forEach((proj, i) => {
            if (i === idx) {
                proj.classList.add('active');
                gsap.to(proj, {scale: 1.12, zIndex: 2, duration: 0.5, boxShadow: '0 8px 40px rgba(0,0,0,0.18)'});
            } else {
                proj.classList.remove('active');
                gsap.to(proj, {scale: 1, zIndex: 1, duration: 0.5, boxShadow: '0 2px 8px rgba(0,0,0,0.10)'});
            }
        });
        activeIndex = idx;
        updateDots(idx);
    }

    // Dots logic
    const dots = document.querySelectorAll('.mobile-carousel-indicators .carousel-dot');
    function updateDots(idx) {
        dots.forEach((dot, i) => {
            if (i === idx) dot.classList.add('active');
            else dot.classList.remove('active');
        });
    }

    // IntersectionObserver to detect visible project (for scroll/swipe)
    if ('IntersectionObserver' in window && projects.length > 1) {
        const carousel = document.querySelector('.project-carousel');
        let lastVisible = 0;
        const observer = new window.IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const idx = Array.from(projects).indexOf(entry.target);
                    if (idx !== lastVisible) {
                        setActive(idx);
                        lastVisible = idx;
                    }
                }
            });
        }, {
            root: carousel,
            threshold: 0.6
        });
        projects.forEach(proj => observer.observe(proj));
    }

    projects.forEach((proj, idx) => {
        // Hover effect (scale up on hover, return if not active)
        proj.addEventListener('mouseenter', () => {
            if (activeIndex !== idx) {
                gsap.to(proj, {scale: 1.08, zIndex: 2, duration: 0.3, boxShadow: '0 6px 24px rgba(0,0,0,0.14)'});
            }
        });
        proj.addEventListener('mouseleave', () => {
            if (activeIndex !== idx) {
                gsap.to(proj, {scale: 1, zIndex: 1, duration: 0.3, boxShadow: '0 2px 8px rgba(0,0,0,0.10)'});
            }
        });
        // Click to activate
        proj.addEventListener('click', () => setActive(idx));
    });
    // Set initial active
    setActive(activeIndex);
});
