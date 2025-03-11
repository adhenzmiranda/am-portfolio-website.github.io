import gsap from 'gsap';

// If you need specific plugins, import them individually
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { Flip } from 'gsap/Flip';

// Register plugins
gsap.registerPlugin(ScrollTrigger, Flip);

// Get your elements
const hamburgerBtn = document.querySelector('.open-sidebar-button');
const closeBtn = document.querySelector('.close-sidebar-button');
const navMenu = document.querySelector('.navbar-links');

// Set initial state
gsap.set(navMenu, {
    y: '100vh',
    opacity: 0,
    visibility: 'hidden'
});

// Toggle menu function
function toggleMenu(isOpen) {
    if (isOpen) {
        gsap.to(navMenu, {
            y: '0',
            opacity: 1,
            visibility: 'visible',
            duration: 0.5,
            ease: 'power2.out'
        });
        hamburgerBtn.style.display = 'none';
        closeBtn.style.display = 'block';
    } else {
        gsap.to(navMenu, {
            y: '100vh',
            opacity: 0,
            visibility: 'hidden',
            duration: 0.5,
            ease: 'power2.in'
        });
        hamburgerBtn.style.display = 'block';
        closeBtn.style.display = 'none';
    }
}

// Event listeners
hamburgerBtn.addEventListener('click', () => toggleMenu(true));
closeBtn.addEventListener('click', () => toggleMenu(false));