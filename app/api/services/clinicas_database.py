from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session


URL = 'URL_DA_SUA_BASE_DE_DADOS_AQUI'


engine = create_engine(URL,
                       pool_pre_ping=True,
                       pool_size=5,
                       max_overflow=10
                       )

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

class DatabaseService:
    def __init__(self, Model):
        self.db = SessionLocal()
        self.Model = Model

    def get_all(self):
        return self.db.query(self.Model).all()
    
    def post(self, dados):
        novo = self.Model(**dados)
        self.db.add(novo)
        self.db.commit()
        self.db.refresh(novo)
        return novo
    
    def update(self, id, dados):
        item = self.db.query(self.Model).filter(self.Model.id == id).first()

        if not item:
            return None
        
        for campo, valor in dados.items():
            if valor is not None and hasattr(self.Model, campo):
                setattr(item, campo, valor)
        self.db.commit()
        self.db.refresh(item)
        return item
    
    def delete(self, id):
        item = self.db.query(self.Model).filter(self.Model.id == id).first()

        if not item:
            return None
        
        self.db.delete(item)
        self.db.commit()
        return item
