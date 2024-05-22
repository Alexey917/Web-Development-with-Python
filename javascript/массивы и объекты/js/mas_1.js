let shoppingList = [
  {
    nameProduct: "Apples",
    amount: 10,
    bought: true,
  },
  {
    nameProduct: "tomatoes",
    amount: 7,
    bought: false,
  },
  {
    nameProduct: "strawberry",
    amount: 15,
    bought: true,
  },
  {
    nameProduct: "potatoes",
    amount: 9,
    bought: false,
  },
];

function output(arr) {
  let outputArr = arr.sort((item) => {
    if (item.bought) return 1;
    else return -1;
  });

  alert(JSON.stringify(outputArr));
}

function add(arr) {
  arr.push({
    nameProduct: "bread",
    amount: 1,
    bought: true,
  });
  console.log(arr.length);
}

function buy(arr, name) {
  let change = arr.filter((item) => {
    if (item.nameProduct === name) {
      item.bought = true;
    }
    return item;
  });

  console.log(change);
}

output(shoppingList);
add(shoppingList);
buy(shoppingList, "tomatoes");
