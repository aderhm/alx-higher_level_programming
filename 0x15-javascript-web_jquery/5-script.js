$(document).ready(function(){
    $('#add_item').click(function(){
        let newItem = $('<li>Item</li>');        
        $('.my_list').append(newItem);
    });
});
