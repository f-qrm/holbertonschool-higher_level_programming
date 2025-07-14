#!/usr/bin/node
const button = document.querySelector('#red_header');
const addClass = document.querySelector('header');

button.addEventListener('click', function () {
  addClass.classList.add('red');
});
