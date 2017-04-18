var GET;

function event_add_birthday_form(form_obj) {
    $.post({
        url: "add_birthday/",
        data: {
            "year": $("#year").val(),
        },
        success: function(ret_data) {
            if (ret_data["status"] == "AUTH_FAIL") {
                location.href = '/login/';
            } else if (ret_data["status"] == "SUCCESS") {
                $("#div_event_list_unit").html(ret_data["content"]);
                $.alert("批量添加生日祝福事件成功！");
            } else {
                $.alert(ret_data["message"]);
            }
        },
        error: function(ret_data) {
            $.alert("批量添加生日祝福事件失败！");
        }
    });

    return false;
}

function event_select_old_user_form(form_obj) {
    $.get({
        url: "select_old_user/",
        data: {
            "email": $("#select_user").val(),
        },
        success: function(ret_data) {
            if (ret_data["status"] == "AUTH_FAIL") {
                location.href = '/login/';
            } else if (ret_data["status"] == "SUCCESS") {
                $("#user_profile").html(ret_data["user_profile"]);
            } else {
                $.alert(ret_data["message"]);
            }
        },
        error: function(ret_data) {
            $.alert("查询用户失败！");
        }
    });

    return false;
}

function event_user_info_form(form_obj) {
    $.post({
        url: "update_user_info/",
        data: {
            "field": $("#field").val(),
            "value": $("#value").val(),
            "email": $("#select_email").html()
        },
        success: function(ret_data) {
            if (ret_data["status"] == "AUTH_FAIL") {
                location.href = '/login/';
            } else if (ret_data["status"] == "SUCCESS") {
                $.alert(ret_data["message"]);
            } else {
                $.alert(ret_data["message"]);
            }
        },
        error: function(ret_data) {
            $.alert("更新用户信息失败！");
        }
    });

    return false;
}

$(document).ready(function() {
    ajax_setup();
    GET = url_get();
});