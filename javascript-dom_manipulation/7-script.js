#!/usr/bin/node
const ulMovies = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      ulMovies.appendChild(li);
    });
  });
