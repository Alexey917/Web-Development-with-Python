const auto = {
  manufacturer: "tesla",
  model: "model X",
  yearOfIssue: 2015,
  averageSpeed: "125 km/h",
};

const info = () => {
  alert(
    "Производитель: " +
      auto.manufacturer +
      "\n" +
      "Модель: " +
      auto.model +
      "\n" +
      "Год выпуска: " +
      auto.yearOfIssue +
      "\n" +
      "Средняя скорость: " +
      auto.averageSpeed +
      "\n"
  );
};

const calcutateTime = (distance) => {
  distance = +prompt("Укажите расстояние", "");
  let time = distance / parseInt(auto.averageSpeed);

  for (let i = 1; i < time; i++) {
    if (i % 4 == 0) {
      time++; //каждые 4 часа добавляем 1 час перерыва
    }
  }
  alert(time);
  return time;
};

info();
calcutateTime();
