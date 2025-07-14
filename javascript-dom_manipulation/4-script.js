#!/usr/bin/node
const button = document.querySelector('#add_item');
const listAdd = document.querySelector('.my_list');

button.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  listAdd.appendChild(newItem);
});
