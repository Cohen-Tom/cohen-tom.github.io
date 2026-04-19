import subprocess
import os

ROOT = r"C:\Users\Tom_Le_BG\Desktop\Projets_Sites\cohen-tom.github.io"

def main(commit_message=None):
    print("📦 Ajout des fichiers...")
    # Plus besoin de syntaxe complexe ou d'exclusion manuelle !
    # Git lira automatiquement ton .gitignore et n'ajoutera que ce qui est autorisé.
    subprocess.run('git add .') 

    print("📝 Commit...")
    
    if not commit_message:
        commit_message = "Mise à jour automatique"  # Message de commit par défaut
    subprocess.run(f'git commit -m "{commit_message}"')

if __name__ == "__main__":
    main()