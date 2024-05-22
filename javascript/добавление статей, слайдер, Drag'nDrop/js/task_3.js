const article = document.querySelector(".article");
const formComment = document.createElement("form");
// console.log(formComment);
formComment.classList.add("form");
formComment.innerHTML = `
  <h4 class="leave-comment">Leave you comment</h4>
  <label for="name">Name</label>
  <input class="form-input" type="text" name="name" required>
  <label for="comment">Comment</label>
  <textarea class="add-comment" name="comment" required></textarea>
  <button type="sumbit" class="form-button">Add comment</button>
`;
article.append(formComment);

const formInput = document.querySelector(".form-input");
const commentBlock = document.querySelector(".comment");
const button = document.querySelector(".form-button");
const textComment = document.querySelector(".add-comment");

button.addEventListener("click", (event) => {
  event.preventDefault();
  commentBlock.innerHTML += `
    <h4 class="user">${formInput.value}</h4>
    <p class="date">${currentDate()}</p>
    <p class="text-comment">${textComment.value}</p>
  `;
  if (formInput.value === "" || textComment.value === "") {
    alert("Заполните пустые поля!");
    return false;
  }
  formComment.reset();
});

function currentDate() {
  let now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth();
  const day = now.getDate();
  let date;
  let monthWithoutZero = `${day}.${month + 1}.${year}`;
  let monthWithtZero = `${day}.0${month + 1}.${year}`;
  if (month < 9) date = monthWithtZero;
  else date = monthWithoutZero;
  return date;
}
