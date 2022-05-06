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


// Ajout des placeholder
let title = document.querySelector("#id_title_ad");
let price = document.querySelector("#id_price_ad");
let description = document.querySelector("#id_description_ad"); 
let number_of_piece = document.querySelector("#id_number_of_piece"); 
let number_phone = document.querySelector("#id_number_phone"); 

title.setAttribute("placeholder", "Titre");
price.setAttribute("placeholder", "Prix");
description.setAttribute("placeholder", "Description");
number_of_piece.setAttribute("placeholder", "Nombre(s) de piéce(s)");
number_phone.setAttribute("placeholder", "Numéro de téléphone");

let element_hide_1 = document.evaluate('/html/body/main/div[1]/form/p[5]/text()[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.textContent = "";
let element_hide_2 = document.evaluate('/html/body/main/div[1]/form/p[5]/text()[3]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.textContent = "";


