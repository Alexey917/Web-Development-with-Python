const gallery = document.querySelector(".gallery");
// console.log(gallery);
const buttonNext = document.querySelector(".next");
const buttonPrev = document.querySelector(".prev");

// console.log(buttonNext);
// console.log(buttonPrev);

const pictures = [
  "img/picture_1.jpg",
  "img/picture_2.jpg",
  "img/picture_3.jpg",
  "img/picture_4.jpg",
  "img/picture_5.jpg",
];

function flipGallery() {
  let i = 0;
  gallery.innerHTML = `
      <img src="${pictures[i]}" class="img" alt="картинка">
    `;
  buttonPrev.style.visibility = "hidden";

  buttonPrev.onclick = (event) => {
    if (i > 0) {
      i--;
      console.log(i);
      buttonNext.style.visibility = "visible";
    }

    if (i === 0) {
      buttonPrev.style.visibility = "hidden";
    }

    gallery.innerHTML = `
      <img src="${pictures[i]}" class="img" alt="картинка">
    `;
    console.log("prev");
  };

  buttonNext.onclick = (event) => {
    if (i < pictures.length - 1) {
      i++;
      console.log(i);
      buttonPrev.style.visibility = "visible";
    }

    if (i === 4) {
      buttonNext.style.visibility = "hidden";
    }

    gallery.innerHTML = `
      <img src="${pictures[i]}" class="img" alt="картинка">
    `;
    console.log("next");
  };
}

flipGallery();
