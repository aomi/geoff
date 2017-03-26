//connect to server
var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function () {
    socket.emit('my event', {data: 'I\'m connected!'});
});

$(document).ready(function () {
    var key_up;
    var key_down;
    var key_leff;
    var key_right;
    $(document).keydown(function (event) {
        if (!is_Down) {
            socket.emit('key_command', {data: event.keyCode});
            is_Down = true;
        }
    })
    $(document).keyup(function (event) {
        socket.emit('keyup', {data: event.keyCode});
        is_Down = false;
    })

    $("#refresh").click(function () {
         $.get("http://" + document.domain + ":" + location.port + "/sensor/all", function (data, status) {
            console.log('new data requested')
        });
        $.get("http://" + document.domain + ":" + location.port + "/sensor/air_temp", function (data, status) {
            $("#air_temp").text(data);
        });
        $.get("http://" + document.domain + ":" + location.port + "/sensor/water_temp", function (data, status) {
            $("#water_temp").text(data);
        });
        $.get("http://" + document.domain + ":" + location.port + "/sensor/ph", function (data, status) {
            $("#ph").text(data);
        });
        $.get("http://" + document.domain + ":" + location.port + "/sensor/pressure", function (data, status) {
            $("#pressure").text(data)
        });
        $.get("http://" + document.domain + ":" + location.port + "/sensor/humidity", function (data, status) {
            $("#humidity").text(data)
        });
    });
})