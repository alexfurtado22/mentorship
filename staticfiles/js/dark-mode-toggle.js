document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("dark-mode-toggle");
  const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");
  const currentMode = document.documentElement.classList.contains("dark")
    ? "dark"
    : "light";

  // Check if the dark mode cookie is set
  const darkModeCookie = document.cookie
    .split("; ")
    .find((row) => row.startsWith("dark_mode="));

  // Apply dark mode based on the cookie
  if (darkModeCookie && darkModeCookie.split("=")[1] === "true") {
    document.documentElement.classList.add("dark");
    if (moonIcon && sunIcon) {
      moonIcon.style.display = "none"; // Hide moon icon when dark mode is active
      sunIcon.style.display = "block"; // Show sun icon when dark mode is active
    }
  }

  // Toggle dark mode and set the cookie
  if (toggleButton) {
    toggleButton.addEventListener("click", () => {
      const isDarkMode = document.documentElement.classList.toggle("dark");
      document.cookie = `dark_mode=${isDarkMode}; path=/; max-age=31536000`; // Set cookie for one year

      // Toggle the icons
      if (moonIcon && sunIcon) {
        if (isDarkMode) {
          moonIcon.style.display = "none";
          sunIcon.style.display = "block";
        } else {
          moonIcon.style.display = "block";
          sunIcon.style.display = "none";
        }
      }
    });
  }
});
