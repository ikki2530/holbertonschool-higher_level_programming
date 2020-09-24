// fetches and replaces the name of this URL
$(function (){
  cont = $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: function(data) {
      $("DIV#character").text(data.name);
    }
  });
});
