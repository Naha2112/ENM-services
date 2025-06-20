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

    // Simple portfolio loading
    loadSimplePortfolio();
    
    // Refresh portfolio every 30 seconds
    setInterval(loadSimplePortfolio, 30000);

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

    const modal = document.getElementById('portfolioModal');
    const modalClose = document.getElementById('portfolioModalClose');
    if (modal && modalClose) {
        modalClose.addEventListener('click', hidePortfolioModal);
        modal.addEventListener('click', function(e) {
            if (e.target === modal) hidePortfolioModal();
        });
        document.addEventListener('keydown', function(e) {
            if (modal.style.display === 'flex' && (e.key === 'Escape' || e.key === ' ')) {
                hidePortfolioModal();
            }
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

// Simple function to load and display portfolio images
async function loadSimplePortfolio() {
    try {
        const response = await fetch('/api/images');
        if (!response.ok) {
            console.log('No images endpoint available');
            return;
        }
        
        let images = await response.json();
        // Handle both {images: [...]} and [...] formats
        if (Array.isArray(images.images)) {
            images = images.images.map(img =>
                typeof img === 'string' ? `images/${img}` : `images/${img.filename}`
            );
        } else if (Array.isArray(images)) {
            images = images.map(img =>
                typeof img === 'string' ? img : `images/${img.filename}`
            );
        } else {
            images = [];
        }
        // Filter out logo files
        images = images.filter(imgPath => !/logo\.(png|jpg|jpeg|gif|webp)$/i.test(imgPath));
        
        const portfolioGrid = document.getElementById('portfolioGrid');
        if (!portfolioGrid) return;
        
        // Clear existing content
        portfolioGrid.innerHTML = '';
        
        if (images.length === 0) {
            // Show empty state
            portfolioGrid.innerHTML = `
                <div class="portfolio-empty-state">
                    <i class="fas fa-images"></i>
                    <h3>Upload your work photos in the admin panel</h3>
                    <p>Photos will appear here once uploaded</p>
                </div>
            `;
            return;
        }
        
        // Add each image to the grid
        images.forEach(imagePath => {
            const imageDiv = document.createElement('div');
            imageDiv.className = 'portfolio-image';
            
            imageDiv.innerHTML = `
                <img src="${imagePath}" alt="Portfolio work" loading="lazy" 
                     onerror="this.parentElement.innerHTML='<div style=&quot;padding:2rem;text-align:center;color:#999;&quot;><i class=&quot;fas fa-image&quot;></i><br>Image not found</div>'">
            `;
            
            // Add click-to-expand (lightbox)
            imageDiv.addEventListener('click', function() {
                showPortfolioModal(imagePath);
            });
            
            portfolioGrid.appendChild(imageDiv);
        });
        
    } catch (error) {
        console.error('Error loading portfolio:', error);
        const portfolioGrid = document.getElementById('portfolioGrid');
        if (portfolioGrid) {
            portfolioGrid.innerHTML = `
                <div class="portfolio-empty-state">
                    <i class="fas fa-images"></i>
                    <h3>Upload your work photos in the admin panel</h3>
                    <p>Photos will appear here once uploaded</p>
                </div>
            `;
        }
    }
}

// Lightbox/modal logic for portfolio images
function showPortfolioModal(imgSrc) {
    const modal = document.getElementById('portfolioModal');
    const modalImg = document.getElementById('portfolioModalImg');
    if (!modal || !modalImg) return;
    modalImg.src = imgSrc;
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function hidePortfolioModal() {
    const modal = document.getElementById('portfolioModal');
    if (!modal) return;
    modal.style.display = 'none';
    document.body.style.overflow = '';
}

// Always hide the lightbox on page load
window.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('lightbox');
    if (lightbox) lightbox.style.display = 'none';
});