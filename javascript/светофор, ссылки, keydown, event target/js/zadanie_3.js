const books = document.querySelector("#books");

let singleSelected = (li) => {
  let selected = document.querySelectorAll(".selected");
  selected.forEach((item) => {
    item.classList.remove("selected");
  });
  li.classList.add("selected");
};

books.addEventListener("click", (event) => {
  if (event.target.tagName !== "LI") {
    return;
  } else {
    singleSelected(event.target);
  }
});
