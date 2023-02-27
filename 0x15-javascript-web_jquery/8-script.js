$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, response) {
  const movieListOfDict = data.results;
  let myList = "";
  for (let i = 0; i < movieListOfDict.length; i++) {
    myList += "<li>" + movieListOfDict[i].title + "</li>";
  }
$('UL#list_movies').html(myList);
});
