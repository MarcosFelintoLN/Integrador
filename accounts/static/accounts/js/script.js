let menu = document.querySelector('#menu-icon');
let navbar = document = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('bx-bx');
    navbar.classList.toggle('open');
}
const header = document.querySelector("header");

window.addEventListener("scroll", function() {
    header.classList.toggle("navbar", window.scrollY > 0);

})