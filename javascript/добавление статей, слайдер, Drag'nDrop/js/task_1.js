const slider = document.querySelector(".slider");
const bar = document.querySelector(".bar");

slider.onmousedown = (event) => {
  /* Определяем координату x мыши на ползунке */
  let shiftX = event.clientX - slider.getBoundingClientRect().left;

  document.addEventListener("mousemove", onMouseMove);
  document.addEventListener("mouseup", onMouseUp);

  function onMouseMove(event) {
    let newLeft = event.clientX - shiftX - bar.getBoundingClientRect().left;

    if (newLeft < 0) {
      newLeft = 0;
    }

    let rightEdge = bar.offsetWidth - slider.offsetWidth;

    if (newLeft > rightEdge) {
      newLeft = rightEdge;
    }

    slider.style.left = newLeft + "px";
  }

  function onMouseUp() {
    document.removeEventListener("mouseup", onMouseUp);
    document.removeEventListener("mousemove", onMouseMove);
  }
};

slider.ondragstart = () => {
  return false;
};
