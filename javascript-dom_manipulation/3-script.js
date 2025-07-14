#!/usr/bin/node
const button = document.querySelector('#toggle_header');
const modif = document.querySelector('header');

button.addEventListener('click', function () {
  if (modif.classList.contains('red')) {
    modif.classList.remove('red');
    modif.classList.add('green');
  } else {
    modif.classList.remove('green');
    modif.classList.add('red');
  }
});
