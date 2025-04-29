document.addEventListener("DOMContentLoaded", () => {
  const favicon = document.getElementById("favicon");
  const lightIcon = favicon.getAttribute("data-light");
  const darkIcon = favicon.getAttribute("data-dark");

  function updateFavicon() {
    const newHref = document.documentElement.classList.contains("dark")
      ? darkIcon
      : lightIcon;

    // Only update if the href has changed
    if (favicon.href !== location.origin + newHref) {
      // Fade out favicon
      favicon.style.opacity = "0";

      setTimeout(() => {
        favicon.href = newHref;
        favicon.style.opacity = "1"; // Fade back in
      }, 10); // Small delay, CSS transition handles the animation
    }
  }

  updateFavicon(); // Call once at start

  const observer = new MutationObserver(updateFavicon);
  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["class"],
  });
});
