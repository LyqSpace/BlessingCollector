var GET;

function save_blessing(obj) {
    var event_id = $(obj).attr("id");

    $.post({
        url: "save_blessing/",
        data: {
            "BLESSING": $("#blessing_"+event_id).val(),
            "EVENT_ID": event_id
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
            $.alert("保存祝福失败！");
        }
    });

    return false;
}

$(document).ready(function() {
    ajax_setup();
    GET = url_get();
});