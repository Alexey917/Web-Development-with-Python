const fraction = {
  numerator: +prompt("Введите числитель для первой дроби", ""),
  denominator: +prompt("Введите знаменатель для первой дроби", ""),
};

function sum(obj) {
  return obj.numerator + obj.denominator;
}

function subtraction(obj) {
  return obj.numerator - obj.denominator;
}

function multiplication(obj) {
  return obj.numerator * obj.denominator;
}

function division(obj) {
  return obj.numerator / obj.denominator;
}

function fractionReduction(obj) {
  let max;
  if (obj.numerator > obj.denominator) {
    max = obj.numerator;
  } else {
    max = obj.denominator;
  }

  for (let i = 2; i < max; i++) {
    while (obj.numerator % i === 0 && obj.denominator % i === 0) {
      obj.numerator /= i;
      obj.denominator /= i;
    }
  }

  return String(obj.numerator + "\n" + "\u2013" + "\n" + obj.denominator);
}

alert(sum(fraction));
alert(subtraction(fraction));
alert(multiplication(fraction));
alert(division(fraction));
alert(fractionReduction(fraction));
