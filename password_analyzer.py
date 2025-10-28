import re
from colorama import Fore, Style, init

init(autoreset=True)

def check_strength(pwd: str) -> str:
    score = 0
    feedback = []
    
    #Palabras comunes
    common = ["123", "password", "admin", "administrator", "admin", "123456"]
    if any(word in pwd.lower() for word in common):
        feedback.append("Evita palabras comunes.")
        score -= 1
        
    
    #Longitud
    if len(pwd) >= 8:
        score += 1
    else:
        feedback.append("Usa al menos 8 caracteres.")
        
    
    #Mayusculas
    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        feedback.append("Incluye letas mayúsculas.")
        
    
    #Minusculas
    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        feedback.append("Incluye letas minúsculas.")
        
    
    #Numeros
    if re.search(r"[0-9]", pwd):
        score += 1
    else:
        feedback.append("Agrega números.")


    #Simbolos
    if  re.search(r"[¡!@#$%^&*(),.¿?\":{}|<>]", pwd):
        score += 1
    else:
        feedback.append("Utiliza al menos un simbolo.")
        
    
    #Feedback
    if score <= 2:
        return Fore.RED + "Contraseña INSEGURA \n" + "\n".join(feedback)
    if score == 3 or score == 4:
        return Fore.YELLOW + "Contraseña ACEPTABLE \n" + "\n".join(feedback) 
    else:
        return Fore.GREEN + "Contraseña SEGURA"
    

if __name__ == "__main__":    
    print(Fore.CYAN + "=== Analizador de seguridad de contraseñas ===")
    user_pwd = str(input("Introduce tu contraseña: "))
    print("\n" + check_strength(user_pwd))
