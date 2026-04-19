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

//Rajoute 1 au spam clique
function plus_un(){
    var valeur_actuelle = parseInt($("#Compteur").html());
    valeur_actuelle++;
    $("#Compteur").html(valeur_actuelle)
}

//Rajoute 1000 au crédit(s)
function plus_1000(){
    var valeur_actuelle = parseInt($("#Credit").html());
    valeur_actuelle= valeur_actuelle + 1000 +" Cr";
    $("#Credit").html(valeur_actuelle)
}

//Réduit de moitié les crédits
function moins_moitie() {
    var valeur_actuelle = parseInt($("#Credit").html());
    valeur_actuelle= valeur_actuelle / 2 +" Cr";
    $("#Credit").html(valeur_actuelle)
}