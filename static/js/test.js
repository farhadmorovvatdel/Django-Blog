$(document).ready(function() {
    $('#btn').click(function () {
        var name = $('#name').val();
        var family = $('#family').val();
        var person={name:name, family:family}
        $.ajax({
            method: 'POST',
            url:'http://127.0.0.1:8000/test' ,
            data:person,
            success: function (data) {
               alert(data)
            }
        })
    })
})

