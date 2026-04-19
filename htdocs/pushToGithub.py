import subprocess
import os
import sys

# Chemin absolu vers la racine de ton repo
ROOT = r"C:\Users\Tom_Le_BG\Desktop\Projets_Sites\cohen-tom.github.io"

def run_git(cmd):
    """Exécute une commande shell et affiche l'erreur si elle échoue."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Erreur lors de : {cmd}")
        print(f"Détail : {result.stderr}")
    else:
        print(f"✅ Succès : {cmd}")
    return result

def main(commit_message=None):
    # 1. On se déplace IMPÉRATIVEMENT dans le dossier du projet
    if not os.path.exists(ROOT):
        print(f"❌ Le dossier {ROOT} n'existe pas !")
        return
    
    os.chdir(ROOT)
    print(f"📂 Dossier actuel : {os.getcwd()}")

    print("📦 Ajout des fichiers...")
    # Git utilise ton .gitignore automatiquement ici
    run_git('git add .')

    print("📝 Commit...")
    if not commit_message:
        commit_message = "Mise à jour automatique"
    
    run_git(f'git commit -m "{commit_message}"')

    print("🚀 Push vers GitHub...")
    run_git("git push")

if __name__ == "__main__":
    # Permet de passer un message de commit en argument : python script.py "Mon message"
    msg = sys.argv[1] if len(sys.argv) > 1 else None
    main(msg)