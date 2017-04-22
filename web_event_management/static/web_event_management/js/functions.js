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
                $.alert(ret_data["message"]);
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

function event_add_event_form(form_obj) {
    if ($("#user1").val() == "NULL") {
        $.alert("用户 1 必选");
        return false;
    }

    $.post({
        url: "add_event/",
        data: {
            "DESCRIPTION": $("#description").val(),
            "HAPPEN_DATE": $("#happen_date").val(),
            "USER1": $("#user1").val(),
            "USER2": $("#user2").val(),
            "USER3": $("#user3").val(),
            "email": $("#select_email").html()
        },
        success: function(ret_data) {
            if (ret_data["status"] == "AUTH_FAIL") {
                location.href = '/login/';
            } else if (ret_data["status"] == "SUCCESS") {
                $("#div_event_list_unit").html(ret_data["content"]);
                $.alert(ret_data["message"]);
            } else {
                $("#div_event_list_unit").html(ret_data["content"]);
                $.alert(ret_data["message"]);
            }
        },
        error: function(ret_data) {
            $.alert("添加单个祝福事件失败！");
        }
    });

    return false;
}

function post_delete_event(event_id) {
    $.post({
        url: "delete_event/",
        data: {
            "EVENT_ID": event_id
        },
        success: function(ret_data) {
            if (ret_data["status"] == "AUTH_FAIL") {
                location.href = '/login/';
            } else if (ret_data["status"] == "SUCCESS") {
                $("#div_event_list_unit").html(ret_data["content"]);
                $.alert(ret_data["message"]);
            } else {
                $("#div_event_list_unit").html(ret_data["content"]);
                $.alert(ret_data["message"]);
            }
        },
        error: function(ret_data) {
            $.alert("删除祝福事件失败！");
        }
    });
}

function delete_event(event_obj) {

    var event_id = $(event_obj).attr("id");

    $.confirm({
        title: "删除祝福事件",
        content: "请确认，删除后将清空所有人对该事件的祝福。",
        autoClose: "取消|8000",
        animation: "RotateY",
        closeAnimation: "RotateX",
        buttons: {
            确认删除: {
                btnClass: "btn-primary",
                action: function() {
                    post_delete_event(event_id);
                }
            },
            取消: {
            }
        }
    });
}

$(document).ready(function() {
    ajax_setup();
    GET = url_get();
});