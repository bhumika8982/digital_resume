// =========================================
// DOM ELEMENTS
// =========================================
const themeToggleBtn = document.getElementById('theme-toggle');
const body = document.body;
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const navLinksItems = document.querySelectorAll('.nav-link');
const navbar = document.querySelector('.navbar');

// =========================================
// THEME TOGGLE (DARK/LIGHT MODE)
// =========================================
// Check for saved user preference, if any, on load of the website
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    body.classList.remove('light-mode', 'dark-mode');
    body.classList.add(currentTheme);
    updateThemeIcon();
}

// Event listener for theme toggle button
themeToggleBtn.addEventListener('click', () => {
    if (body.classList.contains('light-mode')) {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark-mode');
    } else {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
        localStorage.setItem('theme', 'light-mode');
    }
    updateThemeIcon();
});

// Update the icon based on the current theme
function updateThemeIcon() {
    const icon = themeToggleBtn.querySelector('i');
    if (body.classList.contains('dark-mode')) {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    } else {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
    }
}

// =========================================
// MOBILE NAVIGATION
// =========================================
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
});

// Close mobile menu when a link is clicked
navLinksItems.forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    });
});

// =========================================
// NAVBAR SCROLL EFFECT
// =========================================
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// =========================================
// ACTIVE NAV LINK ON SCROLL
// =========================================
const sections = document.querySelectorAll('section');

window.addEventListener('scroll', () => {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= (sectionTop - 150)) {
            current = section.getAttribute('id');
        }
    });

    navLinksItems.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// =========================================
// SCROLL REVEAL ANIMATIONS
// =========================================
function reveal() {
    const reveals = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');
    
    for (let i = 0; i < reveals.length; i++) {
        const windowHeight = window.innerHeight;
        const elementTop = reveals[i].getBoundingClientRect().top;
        const elementVisible = 100; // Trigger threshold
        
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add('active');
        }
    }
}

// Initial check
reveal();

// Check on scroll
window.addEventListener('scroll', reveal);

// =========================================
// CONTACT FORM SUBMISSION
// =========================================
const contactForm = document.querySelector('.contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const subject = document.getElementById('subject').value;
        const message = document.getElementById('message').value;
        
        const submitBtn = contactForm.querySelector('.submit-btn');
        const originalBtnText = submitBtn.innerHTML;
        submitBtn.innerHTML = 'Sending... <i class="fas fa-spinner fa-spin"></i>';
        submitBtn.disabled = true;

        try {
            const response = await fetch('/api/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, email, subject, message }),
            });

            const data = await response.json();

            if (response.ok) {
                alert('Success: ' + data.message);
                contactForm.reset();
            } else {
                let errorMsg = data.detail;
                if (Array.isArray(errorMsg)) {
                    errorMsg = errorMsg.map(err => err.msg).join(', ');
                }
                alert('Error: ' + (errorMsg || 'Something went wrong.'));
            }
        } catch (error) {
            console.error('Error submitting form:', error);
            alert('Error connecting to the server. Make sure the backend is running.');
        } finally {
            submitBtn.innerHTML = originalBtnText;
            submitBtn.disabled = false;
        }
    });
}
