import bcrypt

def codificar(password):
  password = password.encode('utf-8')
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password, salt)
  return hashed_password

def verificar(password, hashed_password):
  password = password.encode('utf-8')
  hashed_password = hashed_password.encode('utf-8')
  if bcrypt.checkpw(password, hashed_password):
    return True
  else:
    return False
  