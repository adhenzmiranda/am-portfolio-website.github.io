document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const carousel = document.querySelector('.project-carousel');
    const projects = Array.from(carousel.querySelectorAll('.project'));
    const leftArrow = document.querySelector('.a-left');
    const rightArrow = document.querySelector('.a-right');

    // Guard clause if no projects
    if (projects.length === 0) return;

    let currentIndex = 0;

    // Function to update active project
    function updateActiveProject(newIndex, shouldScroll = true) {
        // Remove active class from all projects
        projects.forEach(p => p.classList.remove('active'));
        
        // Update current index
        currentIndex = newIndex;
        
        // Add active class to new current project
        projects[currentIndex].classList.add('active');

        // Only scroll if shouldScroll is true (for click events)
        if (shouldScroll) {
            const activeProject = projects[currentIndex];
            activeProject.scrollIntoView({
                behavior: 'smooth',
                block: 'nearest',
                inline: 'center'
            });
        }

        // Update dots if they exist
        updateDots();
    }

    // Function to update mobile dots
    function updateDots() {
        const dots = document.querySelectorAll('.carousel-dot');
        if (dots.length > 0) {
            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === currentIndex);
            });
        }
    }

    // Initialize first project as active without scrolling
    updateActiveProject(0, false);

    // Add click event listeners
    if (leftArrow) {
        leftArrow.addEventListener('click', () => {
            if (currentIndex > 0) {
                updateActiveProject(currentIndex - 1, true);
            }
        });
    }

    if (rightArrow) {
        rightArrow.addEventListener('click', () => {
            if (currentIndex < projects.length - 1) {
                updateActiveProject(currentIndex + 1, true);
            }
        });
    }

    // Add keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft' && currentIndex > 0) {
            updateActiveProject(currentIndex - 1, true);
        } else if (e.key === 'ArrowRight' && currentIndex < projects.length - 1) {
            updateActiveProject(currentIndex + 1, true);
        }
    });

    console.log('Carousel initialized with', projects.length, 'projects');
});