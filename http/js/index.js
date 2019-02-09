function go() {
    var text = $("#usr").val();
    if (!isEmpty(text)) {
        var url = "info.html?q=" + text;
        $(location).attr('href', url);
    }
}

function keypress() {
    var text = $("#usr").val();
    var btn = $("#go_btn");
    if (isEmpty(text) && !btn.hasClass("disabled")) {
        btn.toggleClass("disabled");
    } else if (!isEmpty(text) && btn.hasClass("disabled")){
        btn.toggleClass("disabled");
    }
}

function isEmpty(str) {
    return (!str || str.isEmpty());
}
String.prototype.isEmpty = function() {
    return (this.length === 0 || !this.trim());
};

window.onload = function() {
    keypress();
}