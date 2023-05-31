$.get('https://swapi.co/api/people/5/?format=json', function (char_name) {
  $('DIV#character').text(char_name.name);
});
