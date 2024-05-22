class ExtendedDate extends Date {
  constructor(someDay, now, leap, next) {
    super();
    this.someDay = someDay;
    this.now = now;
    this.leap = leap;
    this.next = next;
  }

  outputDate() {
    this.someDay = new Date(2021, 10, 24);
    alert(this.someDay);
  }

  checkDate() {
    this.now = new Date();
    let isDay;
    console.log(this.someDay.getTime());
    if (this.someDay.getTime() >= this.now.getTime()) {
      alert("Этот день еще не наступил!");
      isDay = true;
    } else {
      alert("Этот день уже прошел");
      isDay = false;
    }
    console.log(isDay);
    return isDay;
  }

  checkLeapYear() {
    this.leap = new Date(1996, 0, 1);

    if (this.leap.getFullYear() % 4 === 0) {
      alert("Этот год високосный");
    } else {
      alert("Этот год  не високосный");
    }

    console.log(this.leap);
  }

  nextDate() {
    this.next = new Date();
    this.next.setDate(this.next.getDate() + 1);
    alert("следующая дата: " + this.next);
  }
}

const extendedDate = new ExtendedDate();
extendedDate.outputDate();
extendedDate.checkDate();
extendedDate.checkLeapYear();
extendedDate.nextDate();
