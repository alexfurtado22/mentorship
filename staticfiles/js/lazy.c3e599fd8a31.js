document.addEventListener("DOMContentLoaded", () => {
  const lazyImages = document.querySelectorAll("img.lazy-image");

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target;
        const fullSrc = img.getAttribute("data-src");

        if (fullSrc) {
          const newImg = new Image();
          newImg.src = fullSrc;

          newImg.onload = () => {
            img.src = fullSrc;
            img.classList.remove("blur", "opacity-60"); // Remove blur and opacity on load
            img.classList.add("opacity-100"); // Apply full opacity
            img.classList.add("transition-all"); // Ensure the transition happens smoothly
            img.classList.add("loaded"); // Add the 'loaded' class after image has loaded
          };

          observer.unobserve(img); // Stop observing after the image is loaded
        }
      }
    });
  });

  lazyImages.forEach((img) => {
    img.classList.add("opacity-60", "blur-[40px]"); // Initially set opacity and blur
    observer.observe(img); // Start observing the images
  });
});
