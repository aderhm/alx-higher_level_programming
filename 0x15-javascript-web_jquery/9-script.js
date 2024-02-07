$(document).ready(function(){
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data){
        var helloTranslation = data.hello;        
        $('#hello').text(helloTranslation);
    });
});
