let check = [
  {
    nameProduct: "Apples",
    amount: 10,
    price: 100,
  },
  {
    nameProduct: "tomatoes",
    amount: 7,
    price: 80,
  },
  {
    nameProduct: "strawberry",
    amount: 15,
    price: 320,
  },
  {
    nameProduct: "potatoes",
    amount: 9,
    price: 60,
  },
];

function output(arr) {
  alert(JSON.stringify(arr));
}

function totalSum(arr) {
  let sumTotal = 0;
  arr.forEach((item) => {
    sumTotal += item.amount * item.price;
  });
  alert("Общая стоимость: " + sumTotal);
}

function mostExpensive(arr) {
  let max = 0;
  let index = 0;
  arr.forEach((item) => {
    sumTotal = item.amount * item.price;
    if (max < sumTotal) {
      max = sumTotal;
      index = arr.indexOf(item);
    }
  });
  alert("Самая дорогая покупка: " + JSON.stringify(arr[index]));
}

function averageValue(arr) {
  let sum = 0;
  arr.forEach((item) => {
    sum += item.price;
  });
  alert("Средняя стоимость одного товара: " + JSON.stringify(sum / arr.length));
  return sum / arr.length;
}

output(check);
totalSum(check);
mostExpensive(check);
averageValue(check);
