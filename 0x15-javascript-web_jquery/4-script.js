$("DIV#toggle_header").click(function() {
  if ($("HEADER").hasClass("green")) {
    $("HEADER").removeClass("green");
    $("HEADER").toggleClass("red");
  } else {
    $("HEADER").removeClass("red");
    $("HEADER").toggleClass("green");
  }
});
