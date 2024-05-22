//второе задание
const trafficLight = document.querySelectorAll(".circle");
const buttonTrafficLight = document.querySelector(".button");

// console.log(trafficLight);

let counter = 0;

buttonTrafficLight.addEventListener("click", () => {
  // console.log("click");

  counter++;
  for (let i = 0; i < trafficLight.length; i++) {
    if (counter === 1 && i === 0) {
      trafficLight[i].style.backgroundColor = "red";
    } else if (counter === 2 && i === 1) {
      trafficLight[i].style.backgroundColor = "yellow";
      trafficLight[i - 1].style.backgroundColor = "grey";
    } else if (counter === 3 && i === 2) {
      trafficLight[i].style.backgroundColor = "green";
      trafficLight[i - 1].style.backgroundColor = "grey";
    } else if (counter > 3 && i === 2) {
      trafficLight[i].style.backgroundColor = "grey";
      trafficLight[i - 2].style.backgroundColor = "red";
      counter = 1;
      i = 0;
    }
  }
});
