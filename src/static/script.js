// Abre e fecha menu mobile

const menuMobile = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

menuMobile.addEventListener('click',() =>{ //função callback
    menuMobile.classList.toggle('bi-list')
    ? menuMobile.classList.replace('bi-list','bi-x') //IF ternário
    : menuMobile.classList.replace('bi-x','bi-list');
    body.classList.toggle('menu-nav-active');
});