// Hide loading screen as soon as possible
window.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loadingScreen');
    if (loadingScreen) {
        loadingScreen.classList.add('fade-out');
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 500);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu functionality
const mobileMenu = document.getElementById('mobile-menu');
const navMenu = document.querySelector('.nav-menu');

mobileMenu.addEventListener('click', () => {
    mobileMenu.classList.toggle('active');
    navMenu.classList.toggle('active');
});

    // Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
            });
        }
    });
});

    // Scroll to top button
    const scrollToTopButton = document.querySelector('.scroll-to-top');
    if (scrollToTopButton) {
window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                scrollToTopButton.classList.add('visible');
    } else {
                scrollToTopButton.classList.remove('visible');
            }
        });

        scrollToTopButton.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Fade in animation for elements
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('appear');
                observer.unobserve(entry.target);
        }
    });
}, observerOptions);

    document.querySelectorAll('.service-card, .feature-item, .contact-method-card').forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });

    // Accordion for service cards on homepage
    document.querySelectorAll('.service-card .service-card-header').forEach(header => {
        header.addEventListener('click', function(e) {
            e.stopPropagation();

            const card = this.closest('.service-card');
            const content = card.querySelector('.service-card-content');
            const wasActive = card.classList.contains('active');

            // Close all other cards
            document.querySelectorAll('.service-card').forEach(c => {
                if (c !== card) {
                    c.classList.remove('active');
                    c.querySelector('.service-card-content').style.maxHeight = null;
                }
            });

            // Toggle current card
            if (wasActive) {
                card.classList.remove('active');
                content.style.maxHeight = null;
            } else {
                card.classList.add('active');
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });

    const header = document.querySelector('.header');
    const backToTopBtn = document.querySelector('.back-to-top-btn');

    window.addEventListener('scroll', () => {
        // Sticky header
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // Back to top button
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    });

    // Smooth scroll for back to top
    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Dropdown/accordion for services section
    document.querySelectorAll('.category-header').forEach(header => {
        header.addEventListener('click', function() {
            const category = header.parentElement;
            const services = category.querySelector('.category-services');
            const arrow = header.querySelector('.dropdown-arrow');
            const isActive = header.classList.contains('active');
            
            // Close all others
            document.querySelectorAll('.category-header').forEach(h => {
                h.classList.remove('active');
                h.parentElement.classList.remove('expanded');
                h.parentElement.querySelector('.category-services').classList.remove('active');
                h.querySelector('.dropdown-arrow').classList.remove('active');
            });

            // Toggle current
            if (!isActive) {
                header.classList.add('active');
                category.classList.add('expanded');
                services.classList.add('active');
                arrow.classList.add('active');
            }
        });
    });
});