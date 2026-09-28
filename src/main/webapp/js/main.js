/**
 * TrendVibe E-Commerce Frontend Scripts (Myntra / Ajio / Nykaa features)
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Highlight active navigation category link
    const currentUrl = window.location.href;
    document.querySelectorAll('nav.main-nav a').forEach(link => {
        if (link.href === currentUrl) {
            link.classList.add('active');
        }
    });

    // 2. Size selector pill click interaction
    const sizeRadios = document.querySelectorAll('.size-radio');
    sizeRadios.forEach(radio => {
        radio.addEventListener('change', () => {
            document.querySelectorAll('.size-btn').forEach(btn => btn.style.borderColor = '');
        });
    });

    // 3. Add to bag validation
    const addToCartForm = document.getElementById('addToCartForm');
    if (addToCartForm) {
        addToCartForm.addEventListener('submit', (e) => {
            const selectedSize = addToCartForm.querySelector('input[name="sizeLabel"]:checked');
            if (!selectedSize) {
                e.preventDefault();
                alert('Please select a size before adding to Bag!');
            }
        });
    }

    // 4. URL query toast / alert handlers
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('registered') === 'true') {
        showToast('🎉 Welcome to TrendVibe! Your account was successfully created.');
    }
    if (urlParams.get('loggedout') === 'true') {
        showToast('👋 You have been successfully logged out.');
    }
    if (urlParams.get('error') === 'empty_cart') {
        showToast('⚠️ Your bag is empty. Please add items to checkout.');
    }
});

/**
 * Modern floating toast notification
 */
function showToast(message) {
    let toast = document.createElement('div');
    toast.style.position = 'fixed';
    toast.style.bottom = '24px';
    toast.style.right = '24px';
    toast.style.backgroundColor = '#282c3f';
    toast.style.color = '#ffffff';
    toast.style.padding = '14px 24px';
    toast.style.borderRadius = '8px';
    toast.style.boxShadow = '0 8px 24px rgba(0,0,0,0.2)';
    toast.style.fontSize = '14px';
    toast.style.fontWeight = '700';
    toast.style.zIndex = '9999';
    toast.style.transition = 'all 0.3s ease';
    toast.textContent = message;

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}
