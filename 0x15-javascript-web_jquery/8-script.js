// fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (i, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
  // for (let i = 0; i < data.results.length; i++) {
  //   $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  // }
});
