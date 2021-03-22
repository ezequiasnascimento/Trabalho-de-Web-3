from app import db


class Carro(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  modelo = db.  Column(db.String(64), index=True)
  cor = db.Column(db.String(20), index=True)
  ano = db.Column(db.Integer(), index=True)



  comentarios = db.relationship('Comentario', backref='autor', lazy='dynamic')


  def __repr__(self):
    return '<Carro {} ({})>'.format(self.modelo, self.ano)