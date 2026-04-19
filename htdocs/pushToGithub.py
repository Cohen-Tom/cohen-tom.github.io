import subprocess
import os

ROOT = r"C:\Users\Tom_Le_BG\Desktop\Projets_Sites\cohen-tom.github.io\htdocs"

def run(cmd):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Erreur : {cmd}")
        exit()

def main(commit_message=None):
    # 📦 Aller dans le repo
    os.chdir(ROOT)

    # 📝 Message commit
    if commit_message is None:
        commit_message = "update automatique"

    print("📦 Ajout des fichiers...")

    # ✅ Ajouter tout SAUF AI_Whatsapp
    run('git add . ":!AI_Whatsapp"')

    # ✅ Ajouter UNIQUEMENT Website
    run('git add AI_Whatsapp/Website')

    print("📝 Commit...")

    run(f'git commit -m "{commit_message}"')

    print("🚀 Push...")

    run("git push")

    print("✅ Terminé !")

if __name__ == "__main__":
    main()