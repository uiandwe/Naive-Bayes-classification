$(function(){
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
                    str = json.data[0];
                    $("#word_decision").append("<h3>"+str+"</h3>");
                    str1 = ""
                    word_list = json.data[1];
                    for(var i in word_list){
                        str1 += "<span class='word_token'><span><strong>"+word_list[i][0]+"</strong></span><span>["+word_list[i][1]+"]</span></span>"
                    }
                    $("#word_decision").append("<div >"+str1+"</div>");
                    str = json.data[2]
                    $("#word_decision").append("<div >"+str+"</div>");
                    console.log(json.data);
                }
            },
            error : function(b1, b2, b3) {
                alert(json.message);
            }
        });

    });

});