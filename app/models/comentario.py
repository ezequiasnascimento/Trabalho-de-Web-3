from app import db
from datetime import datetime


class Comentario(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  nome_usuario = db.Column(db.String(60))
  corpo = db.Column(db.String(93))
  nota = db.Column(db.Integer())




  
  carro_id = db.Column(db.Integer(), db.ForeignKey('carro.id'))
  usuario_id = db.Column(db.Integer(), db.ForeignKey('usuario.id'))


  def __repr__(self):
    return '<Avaliação {}>'.format(self.nota)