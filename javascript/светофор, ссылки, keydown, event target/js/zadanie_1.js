//первое задание
const input = document.querySelector(".input");

input.addEventListener("keydown", (event) => {
  if (event.key >= 0 && event.key <= 9) {
    event.preventDefault();
  }
});
