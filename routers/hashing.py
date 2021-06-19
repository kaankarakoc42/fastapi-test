from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

algorithm = "HS256"
secret = "secret"
expiration_time = 30

class Hash:
      def createHash(data):
          return pwd_context.hash(data)

      def verify(string,hashedString):
          return pwd_context.verify(string,hashedString)

      def encodeJWT(token:dict):
          return jwt.encode(token,secret,algorithm=algorithm)

      def decodeJWT(token):
          return jwt.decode(token,secret,algorithms=algorithm)
