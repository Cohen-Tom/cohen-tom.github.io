// Sélectionne tous les éléments ayant la classe "projet" dans la section #projets
const projects = document.querySelectorAll("#projets .projet");
// Récupère le bouton "Précédent" via son id
const prevBtn = document.getElementById("prev");
// Récupère le bouton "Suivant" via son id
const nextBtn = document.getElementById("next");
// Compte le nombre total de projets présents dans la page
const projectCount = document.querySelectorAll("#projets .projet").length;
// Définit le nombre maximum de projets affichés par page
const projectsPerPage = 3;
// Stocke l’index de la page actuelle (0 = première page)
let currentPage = 0;


// Affiche le nombre total de projets à côté du titre "Mes Projets"
document.getElementById("project-count").textContent = `(${projectCount})`;


// Fonction qui gère l’affichage des projets selon la page courante
function showProjects() {
    // Parcourt tous les projets avec leur index
    projects.forEach((project, index) => {
        // Supprime la classe "visible" pour réinitialiser l’animation
        project.classList.remove("visible");
        // Vérifie si le projet appartient à la page actuelle
        if (
            index >= currentPage * projectsPerPage &&
            index < (currentPage + 1) * projectsPerPage
        ) {
            // Rend le projet visible dans le flux HTML
            project.style.display = "block";
            // Petit délai pour permettre au navigateur d’appliquer le display
            // avant d’ajouter la classe (nécessaire pour déclencher l’animation)
            setTimeout(() => {
                project.classList.add("visible");
            }, 50);
        } else {
            // Cache les projets qui ne sont pas sur la page actuelle
            project.style.display = "none";
        }
    });

    // Désactive le bouton "Précédent" si on est sur la première page
    prevBtn.disabled = currentPage === 0;
    // Désactive le bouton "Suivant" si on est sur la dernière page
    nextBtn.disabled =
        (currentPage + 1) * projectsPerPage >= projects.length;
}

// Événement déclenché lors du clic sur le bouton "Précédent"
prevBtn.addEventListener("click", () => {
    // Recule d’une page
    currentPage--;
    // Met à jour l’affichage des projets
    showProjects();
});

// Événement déclenché lors du clic sur le bouton "Suivant"
nextBtn.addEventListener("click", () => {
    // Avance d’une page
    currentPage++;
    // Met à jour l’affichage des projets
    showProjects();
});

// Affiche les projets dès le chargement de la page
showProjects();