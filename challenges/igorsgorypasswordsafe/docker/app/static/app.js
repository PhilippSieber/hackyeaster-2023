$(document).ready(function () {
    console.log("Application is running")

    $(".copypassword").click(function (obj) {
        if (obj.target.id.startsWith("copypassword_")) {
            id = obj.target.id.split("_")[1];
            $.get("/get/" + id, function (data, status) {
                if (status == "success") {
                    navigator.clipboard.writeText(data);
                }
            });
        }
    });

    $(document).ready(function(){
        setInterval(flashingEyes,1000);
     });
     function flashingEyes(){
        $("#eyes").fadeIn(400).delay(200).fadeOut(400);
     }
     
});
