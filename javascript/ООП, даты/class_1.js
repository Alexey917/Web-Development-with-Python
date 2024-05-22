class Circle {
  constructor(radius) {
    this.radius = radius;
  }

  get getRadius() {
    return this.radius;
  }

  set getRadius(value) {
    this.radius = value;
  }

  square() {
    let square = Math.PI * (this.radius * this.radius);
    return square;
  }

  lengthCircle() {
    let length = Math.PI * 2 * this.radius;
    return length;
  }
}

let circle = new Circle(4);
console.log(circle.square());
console.log(circle.lengthCircle());
console.log((circle.radius = 7));
console.log(circle.square());
console.log(circle.lengthCircle());
