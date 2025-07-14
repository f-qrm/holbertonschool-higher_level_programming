#!/usr/bin/node
const button = document.querySelector('#update_header');
const remplace = document.querySelector('header');

button.addEventListener('click', function () {
  remplace.textContent = 'New Header!!!';
});
