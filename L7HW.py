#Napiš program, který bude pracovat s informacemi o uživatelském účtu: username, age, email
#Vytvoř následující funkce:

#is_adult: Funkce ověří zda je uživatel dospělý
def adult(age):
    return age >=18
#is_name_valid: Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé
def name(user):
    return len(user) >= 4
#create_user:
#Funkce vytvoří slovník reprezentujícího uživatele.


def create_user(username, age, email):
    # Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
    if not name(username):
        return {
            "success":False,
            "error": "Uzivatel. jmeno min. 4 znak."
        }
    if not adult(age):
        return {
            "success": False,
            "error": "Musis +18."
        }
    # Pokud je vše v pořádku, create_user vrátí následující slovník:
    return{
        "success": True,
        "user": {
            "username":username,
            "age":age,
            "email":email
        }
    }

def print_user_info(result):
    if result["success"]:
        user = result["user"]
        print(f"Uživatel: {user['username']}")
        print(f"Věk: {user['age']}")
        print(f"Email: {user['email']}")
        print("--------------------")
    else:
        print("Chyba:", result["error"])
        print("--------------------")

"""{
"success": True,
"user": {"username": "...", "age": ..., "email": "..."}
}
 Pokud validace selže, create_user vrátí:
{
"success": False,
"error": "Chybová zpráva..."
}
"""

#print_user_info: Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření

#Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu.

users = [
    create_user("AAAA", 21, "1@1.cz"),
    create_user("B", 22, "2@2.cz"),
    create_user("CCCC", 3, "3@3.cz"),
    create_user("DDDD", 24, "4@4.cz")
]

#Nakonec vytvořené uživatele vytiskni pomocí cyklu a metody print_user_info.

for user in users:
    print_user_info(user)