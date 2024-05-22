const createColorForm = document.querySelector(".create-color");
const allColors = document.querySelector(".all-colors");
const bg = document.getElementsByClassName("color");
let index = 0;

colorsCollection = [
  {
    color: "YELLOWGREEN",
    select: "RGB",
    code: "154, 205, 50",
  },

  {
    color: "DARKCYAN",
    select: "RGBA",
    code: "0, 139, 139, 1",
  },

  {
    color: "ORANGERED",
    select: "HEX",
    code: "#FF4500",
  },
];

let displayForm = () => {
  createColorForm.innerHTML = `
  <legend class="form-legend">Create new color</legend>

  <div class="first-input-group">
    <label class="label-style" for="name-color">Color:</label>
    <label class="error-label" for="name-color"></label>
    <input class="input-style first-input" type="text" id="name-color">
  </div>

  <select class="input-style select">
    <option vaue="RGB">RGB</option>
    <option vaue="RGBA">RGBA</option>
    <option vaue="HEX">HEX</option>
  </select>

  <div class="second-input-group">
    <label class="label-style" for="code-color">Code:</label>
    <label class="er-label" for="name-color"></label>
    <input class="input-style second-input items-input" type="text" id="code-color">
  </div>
  <button class="form-button">Save</button>
  `;
};

displayForm();
const saveButton = document.querySelector(".form-button");
const firstInput = document.querySelector(".first-input");
const secondInput = document.querySelector(".second-input");
const errorLabel = document.querySelector(".error-label");
const erLabel = document.querySelector(".er-label");
const select = document.querySelector(".select");

let displayPalette = () => {
  // const bg = document.getElementsByClassName("color");
  for (let i = 0; i < colorsCollection.length; i++) {
    if (i === index) {
      allColors.innerHTML += `
      <div class="color">
        <div class="color-content">
          <p class="text-name">${firstInput.value}</p>
          <p class="text-type">${select.value}</p>
          <p class="text-code">${secondInput.value}</p>
        </div>
      </div>
      `;
      i = colorsCollection.length - 1;

      if (select.value === "RGB")
        bg[i].style.backgroundColor = `rgb(${secondInput.value})`;
      if (select.value === "RGBA")
        bg[i].style.backgroundColor = `rgba(${secondInput.value})`;
      if (select.value === "HEX")
        bg[i].style.backgroundColor = secondInput.value;
    }
  }
};

saveButton.addEventListener("click", (event) => {
  event.preventDefault();
  if (firstInput.value === "" || secondInput.value === "") {
    if (firstInput.value === "") errorLabel.textContent = "Заполните поле!";
    if (secondInput.value === "") erLabel.textContent = "Заполните поле!";
    return false;
  }

  errorLabel.style.display = "none";
  erLabel.style.display = "none";
  //[.,\/#!$%\^&\*;:{}=\-_`~()\+@\[\]?\\\|]+
  if (!/^[a-z]+$/gi.test(firstInput.value)) {
    errorLabel.style.display = "block";
    errorLabel.textContent = "Только буквы!";
    return false;
  }

  let obj = {
    color: firstInput.value,
    select: select.value,
    code: secondInput.value,
  };

  colorsCollection.push(obj);
  console.log(colorsCollection);
  for (let i = 0; i < colorsCollection.length; i++) {
    for (let j = i; j < colorsCollection.length; j++) {
      if (colorsCollection.length === 1) break;
      if (j === i) continue;
      if (
        colorsCollection[j].color.toUpperCase() ===
        colorsCollection[i].color.toUpperCase()
      ) {
        errorLabel.style.display = "block";
        errorLabel.textContent = "Такое имя уже есть!";
        colorsCollection.pop(obj);
        return false;
      }
    }
  }

  let regRgb =
    /^([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])$/g;
  if (select.value === "RGB") {
    if (!secondInput.value.match(regRgb)) {
      erLabel.style.display = "block";
      erLabel.textContent = "[0-255],[0-255],[0-255]!";
      colorsCollection.pop(obj);
      return false;
    }
  }

  let regRgba =
    /^([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([0-1]||0\.[1-9])$/g;
  if (select.value === "RGBA") {
    if (!secondInput.value.match(regRgba)) {
      erLabel.style.display = "block";
      erLabel.textContent = "[0-255],[0-255],[0-255],[0-1]";
      colorsCollection.pop(obj);
      return false;
    }
  }

  let regHex = /^#[a-f0-9]{6}$/gi;
  if (select.value === "HEX") {
    if (!secondInput.value.match(regHex)) {
      erLabel.style.display = "block";
      erLabel.textContent = "шестнадцатеричные цифры";
      colorsCollection.pop(obj);
      return false;
    }
  }

  displayPalette();
  index++;
  createColorForm.reset();

  function setCookie(name, value, options = {}) {
    // value = JSON.stringify(value);
    console.log(value);

    options = {
      path: "/",
      // при необходимости добавьте другие значения по умолчанию
      ...options,
    };

    if (options.expires instanceof Date) {
      options.expires = options.expires.toUTCString();
    }

    let updatedCookie =
      encodeURIComponent(name) + "=" + encodeURIComponent(value);

    for (let optionKey in options) {
      updatedCookie += "; " + optionKey;
      let optionValue = options[optionKey];
      if (optionValue !== true) {
        updatedCookie += "=" + optionValue;
      }
    }

    document.cookie = updatedCookie;
    if (options["max-age"] > 300) {
      function deleteCookie(name) {
        setCookie(name, "", {
          "max-age": -1,
        });
      }

      deleteCookie("user");
    }
  }

  // Пример использования:
  setCookie("user", `${JSON.stringify(colorsCollection)}`, {
    secure: true,
    "max-age": 300,
  });
});

function getCookie(name) {
  let matches = document.cookie.match(
    new RegExp(
      "(?:^|; )" +
        name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, "\\$1") +
        "=([^;]*)"
    )
  );
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

if (document.cookie.indexOf("user") == 0) {
  console.log("Куки есть");

  let resultCookie = JSON.parse(getCookie("user"));
  console.log(resultCookie);
  console.log(colorsCollection);
  for (let i = 0; i < resultCookie.length; i++) {
    if (JSON.stringify(colorsCollection[i]) !== JSON.stringify(resultCookie[i]))
      colorsCollection.push(resultCookie[i]);
  }
  console.log(colorsCollection.length);

  /* Чтобы не дублироовать созданые в HTML цвета */
  for (let i = 3; i < resultCookie.length; i++) {
    allColors.innerHTML += `
      <div class="color">
        <div class="color-content">
          <p class="text-name">${resultCookie[i].color}</p>
          <p class="text-type">${resultCookie[i].select}</p>
          <p class="text-code">${resultCookie[i].code}</p>
        </div>
      </div>
    `;
    // i = colorsCollection.length-1;
    if (resultCookie[i].select === "RGB")
      bg[i].style.backgroundColor = `rgb(${resultCookie[i].code})`;
    if (resultCookie[i].select === "RGBA")
      bg[i].style.backgroundColor = `rgba(${resultCookie[i].code})`;
    if (resultCookie[i].select === "HEX")
      bg[i].style.backgroundColor = resultCookie[i].code;
  }
} else {
  console.log("Куки нет");
}
