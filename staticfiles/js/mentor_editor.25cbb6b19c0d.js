document.addEventListener("DOMContentLoaded", () => {
  const textarea = document.getElementById("id_content");
  if (!textarea) return;

  const wrapper = document.createElement("div");
  textarea.style.display = "none";
  textarea.parentNode.insertBefore(wrapper, textarea);

  const editor = new toastui.Editor({
    el: wrapper,
    height: "400px",
    initialEditType: "markdown",
    previewStyle: "vertical",
    initialValue: textarea.value,
    toolbarItems: [
      ["heading", "bold", "italic", "strike"],
      ["hr", "quote"],
      ["ul", "ol", "task"],
      ["table"],
      ["scrollSync"],
    ],
  });

  textarea.closest("form").addEventListener("submit", () => {
    textarea.value = editor.getHTML();
  });
});
