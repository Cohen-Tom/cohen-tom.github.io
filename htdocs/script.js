// Fonction générique de pagination
function createPagination({
    containerSelector, // Sélecteur du conteneur (ex: "#projets")
    itemSelector,      // Sélecteur des éléments à paginer (ex: ".projet")
    prevBtnId,         // ID du bouton "Précédent"
    nextBtnId,         // ID du bouton "Suivant"
    countId,           // ID de l’élément qui affiche le total
    perPage = 3        // Nombre d’éléments affichés par page (3 par défaut)
}) {

    // Sélectionne tous les éléments à paginer dans le conteneur
    const items = document.querySelectorAll(`${containerSelector} ${itemSelector}`);

    // Récupère les boutons de navigation
    const prevBtn = document.getElementById(prevBtnId);
    const nextBtn = document.getElementById(nextBtnId);

    // Index de la page actuelle (0 = première page)
    let currentPage = 0;

    // Affiche le nombre total d’éléments (si un ID est fourni)
    if (countId) {
        document.getElementById(countId).textContent = `(${items.length})`;
    }

    // Fonction qui met à jour l’affichage des éléments
    function show() {
        // Parcourt tous les éléments avec leur index
        items.forEach((item, index) => {

            // Supprime la classe "visible" pour réinitialiser l’animation
            item.classList.remove("visible");

            // Vérifie si l’élément appartient à la page actuelle
            if (
                index >= currentPage * perPage &&
                index < (currentPage + 1) * perPage
            ) {
                // Affiche l’élément
                item.style.display = "block";

                // Petit délai pour déclencher correctement l’animation CSS
                setTimeout(() => {
                    item.classList.add("visible");
                }, 50);

            } else {
                // Cache les éléments hors de la page actuelle
                item.style.display = "none";
            }
        });

        // Désactive le bouton "Précédent" si on est sur la première page
        prevBtn.disabled = currentPage === 0;

        // Désactive le bouton "Suivant" si on est sur la dernière page
        nextBtn.disabled = (currentPage + 1) * perPage >= items.length;
    }

    // Quand on clique sur "Précédent"
    prevBtn.addEventListener("click", () => {
        currentPage--; // On recule d’une page
        show();        // On met à jour l’affichage
    });

    // Quand on clique sur "Suivant"
    nextBtn.addEventListener("click", () => {
        currentPage++; // On avance d’une page
        show();        // On met à jour l’affichage
    });

    // Affiche les éléments dès le chargement
    show();
}


//Pagination pour les projets
createPagination({
    containerSelector: "#projets",  // Section des projets
    itemSelector: ".projet",        // Chaque projet
    prevBtnId: "prev",              // Bouton précédent
    nextBtnId: "next",              // Bouton suivant
    countId: "project-count",       // Affichage du nombre total
    perPage: 3                      // 3 projets par page
});


//Pagination pour les cours
createPagination({
    containerSelector: "#cours",    // Section des cours
    itemSelector: "._cours_",       // Chaque cours
    prevBtnId: "prevLessons",       // Bouton précédent (différent)
    nextBtnId: "nextLessons",       // Bouton suivant (différent)
    countId: "Lesson-count",        // Affichage du nombre total
    perPage: 3                      // 3 cours par page
});