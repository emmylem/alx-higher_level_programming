$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (char_name) {
  $('DIV#hello').text(char_name.hello);
});
