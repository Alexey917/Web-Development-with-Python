const test = document.querySelector(".test");
const wrapper = document.querySelector(".test-wrapper");

const questions = [
  {
    title: "How many letters are there in the word 'Hello'",
    answers: {
      firstAnswer: 5,
      secondAnswer: 2,
    },
  },

  {
    title: "How many letters are there in the word 'World'",
    answers: {
      firstAnswer: 4,
      secondAnswer: 5,
    },
  },
];

const rightAnswers = [
  questions[0].answers.firstAnswer,
  questions[1].answers.secondAnswer,
];

let counterRightAnswers = 0;

function playTest() {
  let index = 0;

  function displayTest() {
    test.innerHTML += `
      ${questions[index].title}
      <label class="firstLabel" for="first">
        ${questions[index].answers.firstAnswer}
        <input class="first-input" type="radio" name="${questions[index].title}" value="${questions[index].answers.firstAnswer}" id="first">
          </label>
          
      <label class="secondLabel" for="second">
        ${questions[index].answers.secondAnswer}
        <input class="second-input" type="radio" name="${questions[index].title}" value="${questions[index].answers.secondAnswer}" id="second">
      </label>          
  `;
    wrapper.appendChild(test);
  }

  displayTest();

  const firstInput = document.querySelector(".first-input");
  const secondInput = document.querySelector(".second-input");
  const firstLabel = document.querySelector(".firstLabel");
  const secondLabel = document.querySelector(".secondLabel");
  const nextButton = document.querySelector(".next-button");
  const finishButton = document.querySelector(".finish-button");

  finishButton.style.display = "none";

  nextButton.addEventListener("click", () => {
    if (firstInput.checked === true || secondInput.checked === true) {
      if (
        (rightAnswers[index] === parseInt(firstInput.value) &&
          firstInput.checked) ||
        (rightAnswers[index] === parseInt(secondInput.value) &&
          secondInput.checked)
      ) {
        counterRightAnswers++;
      }
      test.innerHTML = "";
      index++;

      displayTest();
      finishButton.style.display = "block";
      nextButton.style.display = "none";
    }

    test.addEventListener("click", (event) => {
      if (event.target.classList.contains("first-input")) {
        firstInput.checked = true;
        secondInput.checked = false;
      }

      if (event.target.classList.contains("second-input")) {
        secondInput.checked = true;
        firstInput.checked = false;
      }
    });
  });

  finishButton.addEventListener("click", () => {
    finishButton.style.display = "none";

    firstInput.setAttribute("value", questions[index].answers.firstAnswer);
    secondInput.setAttribute("value", questions[index].answers.secondAnswer);
    firstInput.setAttribute("name", questions[index].title);
    secondInput.setAttribute("name", questions[index].title);
    firstInput.setAttribute("id", "third");
    secondInput.setAttribute("id", "fourth");
    firstLabel.setAttribute("for", "third");
    secondLabel.setAttribute("for", "fourth");

    if (
      (rightAnswers[index] === parseInt(firstInput.value) &&
        firstInput.checked) ||
      (rightAnswers[index] === parseInt(secondInput.value) &&
        secondInput.checked)
    ) {
      counterRightAnswers++;
    }
    test.innerHTML = `
      <p class="test-result">Result: ${counterRightAnswers} correct answers to ${questions.length} questions</p>
      `;
  });
}

playTest();
