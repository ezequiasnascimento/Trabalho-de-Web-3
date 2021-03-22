from app import db
from werkzeug.security import check_password_hash, generate_password_hash


class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60))
    nome_usuario = db.Column(db.String(60))
    senha_hash = db.Column(db.String(180))

    comentarios = db.relationship('Comentario', backref='escritor', lazy='dynamic')


   


    def adicionar_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)



   
    @property
    def is_authenticated(self):
        return True  
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
  
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<Usuario {}>".format(self.nome_usuario)


