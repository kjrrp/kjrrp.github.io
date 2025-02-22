// Initializes a single-image carousel (mono carousel)
function initMonoCarousel(carouselContainer) {
    const carouselImages = carouselContainer.querySelectorAll('.mono-carousel-images img');
    let currentIndex = 0;

    function showImage(index) {
        if (!carouselImages.length) return;

        carouselImages.forEach((img, i) => img.classList.toggle('active', i === index));
    }

    showImage(currentIndex);
}

// Handle clicks outside the carousel to close it
function handleClickOutside(event, carouselContainer) {
    if (!event.target.classList.contains('trigger-image')) {
        carouselContainer.classList.add('hidden');
    }
}

// Initialize all carousels and set up trigger images
function initializeCarousels() {

    document.querySelectorAll('.mono-carousel-container').forEach(carouselContainer => {
        const carouselId = carouselContainer.id;
        const triggerImage = document.querySelector(`.trigger-image[data-carousel="${carouselId}"]`);

        if (!triggerImage) return;

        initMonoCarousel(carouselContainer);

        triggerImage.addEventListener('click', () => {
            carouselContainer.classList.remove('hidden');
            if (!carouselContainer.querySelector('.mono-carousel-images img.active')) {
                carouselContainer.querySelector('.mono-carousel-images img')?.classList.add('active');
            }
        });

        document.addEventListener('click', (event) => handleClickOutside(event, carouselContainer));
    });
}

// Initialize all carousels on the page
initializeCarousels();
