const createColorForm = document.querySelector(".create-color");
const allColors = document.querySelector(".all-colors");
const bg = document.getElementsByClassName("color");
let index = 0;

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
 }

 displayForm();
 const saveButton = document.querySelector(".form-button");
 const firstInput = document.querySelector(".first-input");
 const secondInput = document.querySelector(".second-input");
 const errorLabel = document.querySelector(".error-label");
 const erLabel = document.querySelector(".er-label");
 const select = document.querySelector(".select");
 let arrNameColor = ["yellowgreen", "darkcyan", "orangered"];
 
 let displayPalette = () => {
  // const bg = document.getElementsByClassName("color");
  for(let i = 0; i < bg.length; i++) {
    if(i === index) {
      allColors.innerHTML += `
      <div class="color">
        <div class="color-content">
          <p class="text-name">${firstInput.value}</p>
          <p class="text-type">${select.value}</p>
          <p class="text-code">${secondInput.value}</p>
        </div>
      </div>
      `;
      i = bg.length-1;
      if(select.value === "RGB") bg[i].style.backgroundColor = `rgb(${secondInput.value})`;
      if(select.value === "RGBA") bg[i].style.backgroundColor = `rgba(${secondInput.value})`;
      if(select.value === "HEX") bg[i].style.backgroundColor = secondInput.value;
    }
  }
 }

 saveButton.addEventListener("click", (event) => {
  event.preventDefault();
  if(firstInput.value === "" || secondInput.value === "") {
    if(firstInput.value === "") errorLabel.textContent = "Заполните поле!";
    if(secondInput.value === "") erLabel.textContent = "Заполните поле!";
    return false;
  }
  
  errorLabel.style.display ="none";
  erLabel.style.display ="none";
  //[.,\/#!$%\^&\*;:{}=\-_`~()\+@\[\]?\\\|]+
  if(!(/^[a-z]+$/gi.test(firstInput.value))) {
    errorLabel.style.display ="block";
    errorLabel.textContent = "Только буквы!";
    return false;
  }

  
  arrNameColor.push(firstInput.value);
  console.log(arrNameColor);
  for(let i = 0; i < arrNameColor.length; i++) {
    for(let j=i; j < arrNameColor.length; j++) {
      if(arrNameColor.length === 1) break;
      if(j === i) continue;
      if(arrNameColor[j].toUpperCase() === arrNameColor[i].toUpperCase()) {
        errorLabel.style.display ="block";
        errorLabel.textContent = "Такое имя уже есть!";
        arrNameColor.pop(firstInput.value);
        return false;
      }
    }
  }

  let regRgb = /^([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])$/g;
  if(select.value === "RGB") {
    if(!(secondInput.value.match(regRgb))) {
      erLabel.style.display ="block";
      erLabel.textContent = "[0-255],[0-255],[0-255]!";
      arrNameColor.pop(firstInput.value);
      return false;
    }
  }

  let regRgba = /^([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([1-9]||[1-9][0-9]||[1-2][0-9][0-9]||2[0-5][0-9])[,]([0-1]||0\.[1-9])$/g;
  if(select.value === "RGBA") {
    if(!(secondInput.value.match(regRgba))) {
      erLabel.style.display ="block";
      erLabel.textContent = "[0-255],[0-255],[0-255],[0-1]";
      arrNameColor.pop(firstInput.value);
      return false;
    }
  }

  let regHex = /^#[a-f0-9]{6}$/gi;
  if(select.value === "HEX") {
    if(!(secondInput.value.match(regHex))) {
      erLabel.style.display ="block";
      erLabel.textContent = "шестнадцатеричные цифры";
      arrNameColor.pop(firstInput.value);
      return false;
    }
  }
  
  displayPalette();
  
  index++;
  createColorForm.reset();

  function setCookie(name, value, options = {}) {
    value = JSON.stringify(bg);
    console.log(value)

    options = {
      path: '/',
      // при необходимости добавьте другие значения по умолчанию
      ...options
    };
  
    if (options.expires instanceof Date) {
      options.expires = options.expires.toUTCString();
    }
  
    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);
  
    for (let optionKey in options) {
      updatedCookie += "; " + optionKey;
      let optionValue = options[optionKey];
      if (optionValue !== true) {
        updatedCookie += "=" + optionValue;
      }
    }
  
    document.cookie = updatedCookie;
    if(options["max-age"] > 21600) {
      function deleteCookie(name) {
        setCookie(name, "", {
          
          'max-age': -1
        })
      }
    
      deleteCookie("user");
    }
  }
  
  // Пример использования:
  setCookie('user', `${bg}`, {secure: true, 'max-age': 21600});
  // document.cookie = "user=Alexey; max-age=21600";
  // alert(document.cookie);
  console.log(typeof JSON.stringify(bg));
 })

 function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}
 
 getCookie('user');

 

 
