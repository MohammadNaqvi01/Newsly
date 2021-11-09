alert("g")


$(document).ready(function(){

alert("booo")





//To show otp part of form after clicking on next
    $("#send").click(function(){
     
       alert("Clicked")
        
        $.ajax({
            type:POST,
            url:'/verification/',
            data:{
                send:'Resend'
            }
        })
        
        
        
         });





 });


