class Css {
  constructor(name) {
    this.name = name;
    this.styles = [
      {
        ["font - size"]: "14px",
        ["font - weight"]: 900,
        ["text - decoration"]: "underline",
      },

      {
        ["font - size"]: "16px",
        ["font - weight"]: 400,
        ["text - decoration"]: "none",
      },

      {
        ["font - size"]: "20px",
        ["font - weight"]: 600,
        ["text - decoration"]: "line-through",
      },
    ];
  }

  getCss() {
    const str = JSON.stringify(this.styles);
    console.log(str);
    return str;
  }

  addCss(obj) {
    this.styles.push(obj);
    console.log(this.styles);
  }

  deleteCss(obj) {
    let del = this.styles.filter(
      (item) => JSON.stringify(item) !== JSON.stringify(obj)
    );
    console.log(del);
  }
}

const css = new Css("text-style");
console.log(css.name);
css.addCss({
  ["font - size"]: "26px",
  ["font - weight"]: 700,
  ["text - decoration"]: "overline",
});

css.deleteCss({
  ["font - size"]: "16px",
  ["font - weight"]: 400,
  ["text - decoration"]: "none",
});

css.getCss();
