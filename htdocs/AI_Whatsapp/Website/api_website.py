import time
from xml.dom.expatbuilder import Rejecter



def getHtmlInfo(log_content:list[str])->list[tuple[str, str, str, str]]:
    """Sépare les lignes de log en éléments HTML.

    Args:
        log_content (list[str]): La liste des lignes de log : [hh:mm:ss | index-balise-attribute | message, hh:mm:ss | index-balise-attribute | message, ...]

    Returns:
        list[tuple[str, str, str]]: La liste des éléments HTML formatés : [(index, balise, attribute, message), (index, balise, attribute, message), ...]
    """
    
    html_info = []
    for line in log_content:
        line = line.strip("\n") # Supprime les caractères de nouvelle ligne à la fin de la ligne
        time, balise_detail, message = line.split("|") # Sépare la ligne en parties : [hh:mm:ss, index-balise-attribute, message]
        
        index, balise, attribute = balise_detail.split("-") # Sépare la partie index-balise-attribute en éléments : [index, balise, attribute]
        html_info.append((index, balise, attribute, message))
    return html_info

def OpenLog(url:str)->list[str]:
    with open(url, "r") as f:
        log_content = f.readlines() # Enregistre le contenu du fichier dans ce format : ["Ligne 1", "Ligne 2", ...]
    return log_content

def createBalise(log_line:list[tuple[str, str, str, str]])-> list[tuple[str, str, str, str]]:
    """ Crée un titre html à partir d'une ligne de log.
    
    Args:
        log_line (list[tuple[str, str, str]]): La ligne de log à transformer en titre : [(index, balise, attribute, message), (index, balise, attribute, message), ...]
        
    Returns:
        list[tuple[str, str, str, str]]: Une balise html formatée. exemple : [(<index>, <balise attribute>, <message>, <\\balise_end>), ...]
    """
    
    html_balises = []
    for index, balise, attribute, message in log_line:
        if attribute == "None": # Si l'attribut est "None", on ne l'inclut pas dans la balise
            balise_attribute = f"<{balise}>"
        else:
            balise_attribute = f"<{balise} {attribute}>"
        balise_end = fr"</{balise}>"
        html_balises.append((index, balise_attribute, message, balise_end))
    
    return html_balises


if __name__ == "__main__":
    log_content = OpenLog("htdocs\\AI_Whatsapp\\Website\\Logs_test\\api_fun.txt")
    html_info = getHtmlInfo(log_content)
    print("info html non traitées:", html_info)
    
    html_balises = createBalise(html_info)
    print("balises html traitées:", html_balises)