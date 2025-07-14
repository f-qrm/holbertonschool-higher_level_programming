#!/usr/bin/node
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
const element = document.querySelector('#hello');

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    element.textContent = data.hello;
  })
  .catch(error => {
    console.error('Failed to load API:', error);
  });
