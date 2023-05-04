from pymongo import MongoClient

import password as password_verify

# Crear una conexión con la base de datos MongoDB
client = MongoClient('mongodb+srv://lillanez:41Jj11WdEqNZrJfU@excelencia.e0mptog.mongodb.net/?retryWrites=true&w=majority')

# Obtener una referencia a la base de datos 'excelencia'
db = client['excelencia']

# Obtener una referencia a la colección 'users'
users_collection = db['users']


def verify_user(username, password):  
  # Recuperar un solo documento de la colección
  doc_user = users_collection.find_one({'user': username})
  if doc_user is None:
    print('Usuario no encontrado')
    return False
  else:
    hashed_password = doc_user['password']
    pass_is_ok = password_verify.verificar(password, hashed_password)
    if pass_is_ok:
      print('Login correcto!')
      return True
    else:
      print('Login INCORRECTO!')
      return False
  