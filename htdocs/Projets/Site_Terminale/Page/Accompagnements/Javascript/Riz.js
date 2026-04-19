//Change le fond en sombre ou clair, au choix
var couleur_fond = "antiquewhite"
function fond(){
    if(couleur_fond=="antiquewhite"){
        couleur_fond = "262121";
        $("body").css("background-color", "#262121")
    } 
    else {
        $("body").css("background-color", "antiquewhite")
        couleur_fond="antiquewhite";
    }
}

//Rajoute 1 au compteur de baquette
function plus_un(){
    var valeur_actuelle = parseInt($("#Compteur").html());
    valeur_actuelle++;
    $("#Compteur").html(valeur_actuelle)
}

//Enlève 1 au compteur de baquette
function moins_un(){
    var valeur_actuelle = parseInt($("#Compteur").html());
    valeur_actuelle = valeur_actuelle - 1;
    $("#Compteur").html(valeur_actuelle)
}