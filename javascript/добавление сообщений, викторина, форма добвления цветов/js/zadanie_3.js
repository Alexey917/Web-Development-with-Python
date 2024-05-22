const colorWrapper = document.querySelector(".color-wrapper");
const formAddColor = document.querySelector(".form-add-color");
const blockColor = document.querySelector(".color");
let index = 0;
 
function dispalyForm() {
  formAddColor.innerHTML = `
    <label class="label-r" for="inputR">R</label>
    <input class="input-r input-range"  id="inputR">

    <label class="label-g" for="inputG">G</label>
    <input class="input-g input-range"  id="inputG">

    <label class="label-b" for="inputB">B</label>
    <input class="input-b input-range"  id="inputB">

    <button class="add-color">Add color</button>
  `;
}

function displayPalette() {
  let newColor = document.createElement("div");
  colorWrapper.appendChild(newColor);
  let newBg = document.createElement("div");
  newColor.appendChild(newBg);
  let text = document.createElement("p");
  newColor.appendChild(text);

  newColor.classList.add("color");
  newBg.classList.add("bg");
  text.classList.add("text");

  const bg = document.querySelectorAll(".bg");

  for(let i = 0; i < bg.length; i++) {
    if(i === index) {
      bg[i].style.backgroundColor = `rgb(${inputR.value}, ${inputG.value}, ${inputB.value})`;
    }
  }

  text.textContent = `RGB (${inputR.value}, ${inputG.value}, ${inputB.value})`;
}

dispalyForm();

const inputR = document.querySelector(".input-r");
const inputG = document.querySelector(".input-g");
const inputB = document.querySelector(".input-b");
const addColor = document.querySelector(".add-color");

function inputRange() {
  const inputRange = document.querySelectorAll(".input-range");
  inputRange.forEach((item) => {
    item.addEventListener("input", () => {
      item.value = item.value.replace(/^\D|([2-9][5-9][6-9]|[2-9][6-9][0-9]|[3-9][0-9][0-9])$/gi, "").substring(0,3)

      // let regexp = /^\D|([2-9][5-9][6-9])$/g;
      // if(regexp.test(item.value)) {
      //   item.value = "";
      //   alert("Введите число от 0 до 255: ")
      // }
      //(?=.*iphone)(?=.*16gb) пример двух условий
      // item.value = item.value.match(/^(?=^.{1,3}$)\d+$/g);
      // if(!(item.value > 0 && item.value < 255)) {
      //   item.value = "";
      //   alert("Введите число от 0 до 255: ")
      // }
    })
  })
}

inputRange();

addColor.addEventListener("click", (event) => {
  event.preventDefault();
  if (inputR.value === "" || inputG.value === "" || inputB.value === "")
    return false;
  index++;
  displayPalette();
  formAddColor.reset();
  
});
