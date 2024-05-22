const links = document.querySelectorAll(".link");

links.forEach((item) => {
  item.parentNode.style.marginTop = "15px";
  item.style.fontFamily = "Arial";
  let attr = item.getAttribute("href");
  if (attr.includes("http://") || attr.includes("https://")) {
    item.style.textDecorationStyle = "dashed";
  } else {
    item.style.textDecoration = "none";
  }
});
