$(document).keypress( function(event) {

    if( event.which === 13 && event.ctrlKey ) {
        selection = window.getSelection();
        if(selection.isCollapsed) {
            return;
        }
        if(selection.toString().length > parseInt($("#id_mistype").attr("maxlength"))) {
            alert("Выделено слишком много текста.");
            return;
        }

        r = selection.getRangeAt(0);
        _1 = document.createRange();
        _1.setStartBefore(r.startContainer.ownerDocument.body);
        _1.setEnd(r.startContainer, r.startOffset);
        pre = _1.toString().replace(/\s\s+/g, ' ');
        _2 = document.createRange();
        _2.setStart(r.endContainer, r.endOffset);
        _2.setEndAfter(r.endContainer.ownerDocument.body);
        suf = _2.toString().replace(/\s\s+/g, ' ');
        pre = pre.substring(pre.length - parseInt($("#id_before").attr("maxlength")));
        suf = suf.substring(0, parseInt($("#id_after").attr("maxlength")));

        $("#mistype-before").text(pre);
        $("#mistype-mistype").text(selection);
        $("#mistype-after").text(suf);

        form = $("#mistype-form");
        form.find("input[name='url']").val(window.location.href);

        form.find("input[name='before']").val(pre);
        form.find("input[name='mistype']").val(selection);
        form.find("input[name='after']").val(suf);

        $("#mistype-div").show();
        form.find("input[name='comment']").focus();
    }

});

$("#mistype-form").submit(function(e) {
    form = $("#mistype-form");

    $.ajax({
           type: "POST",
           url: form.attr("action"),
           data: form.serialize(),
           success: function(data)
           {
               alert("Спасибо за найденную неточность!");
               $("#mistype-div").hide();
           },
           error: function(data)
           {
               alert("Что-то пошло не так. Попробуйте ещё раз или сообщите администратору.");
           }
         });

    e.preventDefault();
});

$("#id_cancel").click(function(e) {
    $("#mistype-div").hide();
});