


$(function(){
//        $("form[method=post]").submit(function(e){
//        e.preventDefault();
//        var $form = $(this);
//        var successReturnUrl = $form.attr("data-success-return-url");
//        var errorReturnUrl = $form.attr("data-error-return-url");
//
//        $form.ajaxSubmit({
//            type : 'post',
//            dataType : 'json',
//            iframe : true,
//            target : '#hidden-iframe',
//            success : function(json) {
//                if(json.status=="success") {
//                    var message = $form.attr("data-success-message");
//                    if (typeof message !== typeof undefined && message !== false) {
//                        if(message) {
//                            alert(message);
//                        }
//                    }
//                    else {
//                        alert(json.message);
//                    }
//
//                    if(successReturnUrl) {
//                        location.href = successReturnUrl;
//                    }
//                    else {
//                        location.reload(true);
//                    }
//                }
//                else {
//                    alert(json.message);
//
//                    if(errorReturnUrl) {
//                        location.href = errorReturnUrl;
//                    }
//                    else {
//
//                        if(json.data) {
//                            $form.find("[name="+json.data+"]").focus();
//                        }
//
//                    }
//                }
//            },
//            error : function(data) {
//                //alert("error");
//
//
//
//            },
//            complete : function(data) {
//
//            }
//        });
//
//    });

    $("#sentence_btn").on("click", function(e){

        var $sentence = $(document).find("#sentence").val();
        $.ajax({
            async : false,
            url : "/",
            data : "sentence="+$sentence,
            dataType : "json",
            type: "post",
            success : function(json) {
                json = json.results;
                if(json.data) {

                }
            },
            error : function(b1, b2, b3) {
                alert(json.message);
            }
        });

    });


});