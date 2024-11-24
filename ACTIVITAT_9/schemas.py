# Funció que converteix un usuari individual en un diccionari.
def user_schema(user) -> dict:
    return {"Id": user[0], # Assigna l'identificador de l'usuari.
            "nom": user[1], # Assigna el nom de l'usuari.
            "cognom": user[2], # Assigna el cognom de l'usuari.
            }

# Funció que converteix una llista d'usuaris en una llista de diccionaris.
def users_schema(users) -> dict:
    return [user_schema(user) for user in users]