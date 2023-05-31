$.get('https://swapi.co/api/films/?format=json', function (char_name) {
  $('UL#list_movies').append(char_name.results.map(movie => `<li>${movie.title}</li>`));
});
