$(function () {
    $('#btn').click(function () {
        // alert('abc')
        $.ajax({
            type: 'get',
            url: '/myapp/studentsinfo/',
            dataType: 'json',
            success:function (data, status) {
                console.log(data)
                var d = data.data;
                for (var i =1; i < d.length; i++) {
                    document.write('<p>' + d[i][0] + '---'+ d[i][1] + '</p>');
                }
            }

        })
    });
});