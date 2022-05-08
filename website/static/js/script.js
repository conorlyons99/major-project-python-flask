window.addEventListener("scroll", reveal);

function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var revealtop = reveals[i].getBoundingClientRect().top;
    var revealpoint = 150;

    if (revealtop < windowHeight - revealpoint) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}

var query =
  "https://api.themoviedb.org/3/search/movie?api_key=1be15b756b9925a237ddd16fd977e807&query=" +
  name;
$.ajax({
  type: "GET",
  url: query,
  success: function (recs) {
    var a = JSON.stringify(recs);
    //alert(a);
    var rslt = JSON.parse(a);
    var pp = rslt.results[0].poster_path;
    document.getElementById("searchedImage").src =
      "https://image.tmdb.org/t/p/w500" + pp;
    var movieId = rslt.results[0].id;
  },
  error: function () {
    //alert("error");
  },
});
