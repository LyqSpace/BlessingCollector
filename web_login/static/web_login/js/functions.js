var GET;

function event_login_form(form_obj) {
    $.post({
        url: "user_login/",
        data: {
            "email": $("#email").val(),
            "token": $("#token").val()
        },
        success: function(ret_data) {
            console.log(ret_data);
            if (ret_data["status"] == "SUCCESS") {
                Cookies.set("email", $("#email").val(), {expires: 30});
                Cookies.set("fullname", ret_data["fullname"], {expires: 30});
                Cookies.set("token", $("#token").val(), {expires: 30});
                location.href = "/";
            } else {
                $.alert(ret_data['message']);
            }
        },
        error: function(ret_data) {
            $.alert("登录失败！");
        }
    });

    return false;

}

$(document).ready(function() {
    ajax_setup();
    GET = url_get();

    Cookies.remove("email");
    Cookies.remove("token");
    Cookies.set("fullname", "游客");

    set_greeting();

});