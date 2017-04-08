function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function ajax_setup() {
    var csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function url_get() {
    var query = window.location.href.split("?");
    var get_array = new Array();
    if (query.length > 1) {
        var buffer = query[1].split("&");
        for (var i = 0; i < buffer.length; i++) {
            var temp = buffer[i].split("=");
            get_array[temp[0]] = temp[1];
        }
    }
    return get_array;
}

function set_greeting() {
    var date = new Date();
    var hour = date.getHours();
    var greeting = "";

    if (hour >= 6 && hour < 11) {
        greeting = "早上好！";
    } else if (hour >= 11 && hour < 13) {
        greeting = "中午好！";
    } else if (hour >= 13 && hour < 18) {
        greeting = "下午好！";
    } else if (hour >= 18 && hour < 23) {
        greeting = "晚上好！";
    } else {
        greeting = "夜深了，繁忙的一天还没有结束吗:) ";
    }

    var fullname = Cookies.get("fullname");
    greeting = greeting + fullname;

    $("#greeting").html(greeting);
}

$(document).ready(function() {
    set_greeting();
});