const blockMessage = document.querySelector(".block-message");
const forForm = document.querySelector(".for-form");
const forMessage = document.querySelector(".for-message");
const headerMessage = document.createElement("div");
const message = document.createElement("p");
const form = document.createElement("form");
const user = document.createElement("p");
const date = document.createElement("p");

blockMessage.appendChild(headerMessage);
blockMessage.appendChild(message);
forForm.appendChild(form);
headerMessage.appendChild(user);
headerMessage.appendChild(date);

form.classList.add("form");
headerMessage.classList.add("header-wrapper");
user.classList.add("user");
date.classList.add("date");

form.innerHTML = `
  <legend class="form-title">Add new message:</legend>
  <label for="name">Your name</label>
  <input class="form-input" type="text" name="name" required>
  <label for="message">Your message</label>
  <textarea class="textarea-input" name="message" required></textarea>
  <button type="submit" class="form-button">Send</button>
`;

const formInput = document.querySelector(".form-input");
const textareaInput = document.querySelector(".textarea-input");
const formButton = document.querySelector(".form-button");

const messages = [];

formButton.addEventListener("click", (event) => {
  event.preventDefault();
  forMessage.innerHTML = "";

  if (formInput.value === "" || textareaInput.value === "") {
    alert("Заполните пустые поля!");
    return false;
  }

  let obj = {
    name: formInput.value,
    date: currentDate(),
    text: textareaInput.value,
  };

  messages.push(obj);

  messages.forEach((item) => {
    forMessage.innerHTML += `
        <div class="header-wrapper">
          <p class="user">${item.name}</p>
          <p class="date">${item.date}</p>
        </div>

        <p class="message">${item.text}</p>
      `;
  });
  form.reset();
});

function currentDate() {
  let now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth();
  const day = now.getDate();
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();

  let date;
  let monthWithoutZero = `${hours}:${minutes}:${seconds}  ${day}.${
    month + 1
  }.${year}`;
  let monthWithtZero = `${hours}:${minutes}:${seconds}  ${day}.0${
    month + 1
  }.${year}`;
  let hourWithtZero = `0${hours}:${minutes}:${seconds}  ${day}.${
    month + 1
  }.${year}`;
  let minutesWithtZero = `${hours}:0${minutes}:${seconds} ${day}.${
    month + 1
  }.${year}`;

  let secondesWithZero = `${hours}:${minutes}:0${seconds} ${day}.${
    month + 1
  }.${year}`;

  if (seconds < 9) {
    date = secondesWithZero;
  }
  if (minutes < 9) {
    date = minutesWithtZero;
  } 
  if (hours < 9) {
    date = hourWithtZero;
  } 
  if (month < 9) {
    date = monthWithtZero;
  } 

  return date;
}
