$(document).ready(function(){
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
        $.each(data.results, function(index, movie){
            var movieTitle = movie.title;            
            $('#list_movies').append('<li>' + movieTitle + '</li>');
        });
    });
});
