// ? For the Jungle Parallax Effect
let text = document.getElementById("text");
let leaf = document.getElementById("leaf");
let hill1 = document.getElementById("hill1");
let hill4 = document.getElementById("hill4");
let hill5 = document.getElementById("hill5");

window.addEventListener("scroll", function () {
  let value = window.scrollY;

  text.style.marginTop = value * 2.5 + "px";
  leaf.style.top = value * -1.5 + "px";
  leaf.style.left = value * 1.5 + "px";
  hill5.style.left = value * 1.5 + "px";
  hill4.style.left = value * -1.5 + "px";
  hill1.style.top = value * 1 + "px";
});

// ? For ScrollReveal JS
// Common reveal options to create reveal animations
ScrollReveal({
  reset: true,
  distance: "60px",
  duration: 1250,
  delay: 200,
});

// Target elements and specify options to create reveal animations
ScrollReveal().reveal(".main-title, .section-title", {
  delay: 250,
  origin: "left",
});
ScrollReveal().reveal(".sec-01 .image, .info", {
  delay: 300,
  origin: "bottom",
});
ScrollReveal().reveal(".text-box", {
  delay: 350,
  origin: "right",
});
ScrollReveal().reveal(".media-icons i, .cards .card", {
  delay: 250,
  origin: "bottom",
  interval: 100,
});
ScrollReveal().reveal(".sec-02 .image, .sec-03 .image", {
  delay: 250,
  origin: "top",
});
ScrollReveal().reveal(".media-info li", {
  delay: 250,
  origin: "left",
  interval: 100,
});
