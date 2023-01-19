from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def return_session():
    CONN = "sqlite:///preject01.db"
    engine =  create_engine(CONN, echo = True)
    Session = sessionmaker(bind=engine)
    return Session()


class ControllerRegister():
    @classmethod
    def check_data(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        return 1

    @classmethod
    def register(cla, nome, email, senha):
        session = return_session()
        user = session.query(Pessoa).filter(Pessoa.email == email).all()

        if len(user) > 0:
            return 5
        data_check = cls.check_data(nome, email, senha)

        if data_check != 1:
            return data_check
        
        try:
            senha = hashlib.sha256(senha)

        except:
            pass

senha = "minha segha"
print(hashlib.sha256(senha.encode()).hexdigest())