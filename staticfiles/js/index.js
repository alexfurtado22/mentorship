document.addEventListener("alpine:init", () => {
  Alpine.data("mentorCreate", () => ({
    name: "",
    company: "",
  }));
  Alpine.data("togglePassword", () => ({
    show: false,
  }));
});
