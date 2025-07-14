#!/usr/bin/node
const charElement = document.querySelector('#character');
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(apiUrl)
  .then(response => {
    return response.json();
  })
  .then(data => {
    charElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
