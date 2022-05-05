let logo_user = document.querySelector(".logo_user");
div_hide_user = document.querySelector(".div_hide_user")
container_logo_user = document.querySelector(".container_logo_user")

n = 0
logo_user.addEventListener("click", function(){
    if (n % 2 == 0){
        div_hide_user.style.visibility = "visible"
    } 
    else {
        div_hide_user.style.visibility = "hidden"
    }
    n += 1
});


