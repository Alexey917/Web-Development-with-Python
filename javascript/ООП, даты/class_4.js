const tbody = document.getElementById("tbody");

class Employee {
  constructor(arr = []) {
    this.arr = arr;
  }
}

class EmTable extends Employee {
  constructor(arr = []) {
    super(arr);
  }

  getHtml() {
    for (let i = 0; i < this.arr.length; i++) {
      tbody.innerHTML += `
      <tr>
        <td style="border: 1px solid black">${i + 1}</td>
        <td style="border: 1px solid black">${this.arr[i]}</td>
      </tr>
    `;
    }
  }
}

class StyleEmpTable extends EmTable {
  constructor(arr, strStyle) {
    super(arr);
    strStyle = "font-size: 18px; color: blue; text-align: center";
    this.strStyle = strStyle;
  }

  getStyles() {
    return this.strStyle;
  }

  getHtml() {
    for (let i = 0; i < this.arr.length; i++) {
      tbody.innerHTML += `
      <tr>
        <td style="border: 1px solid black; ${this.getStyles()}">
          ${i + 1}
        </td>
        <td style="border: 1px solid black; ${this.getStyles()}">
          ${this.arr[i]}
        </td>
      </tr>
    `;
    }
  }
}

/* вывод результата задания 1 со звездочкой */
// const emTable = new EmTable(["Николай", "Петр", "Афанасий", "Григорий"]);
// emTable.getHtml();

/* вывод результата задания 2 со звездочкой */
const styleEmpTable = new StyleEmpTable(
  ["Николай", "Петр", "Афанасий", "Григорий"],
  "font-size: 18px; color: blue; text-align: center"
);
styleEmpTable.getHtml();
