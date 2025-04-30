// imageValidation.js

document.addEventListener("DOMContentLoaded", function () {
  const pictureInput = document.getElementById("id_picture");
  if (pictureInput) {
    pictureInput.addEventListener("change", function (event) {
      const file = event.target.files[0];
      if (file && file.size > 2 * 1024 * 1024) {
        // 5 MB
        alert("The image file is too large. Maximum size allowed is 5 MB.");
        event.target.value = ""; // Clear the input
      }
    });
  }
});
