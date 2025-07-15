#!/bin/usr/node
const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');
redHeader.addEventListener('click', function () {
  header.style.color = '#FF0000';
});
