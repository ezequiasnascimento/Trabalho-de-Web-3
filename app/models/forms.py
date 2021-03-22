from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class DeleteForm(FlaskForm):
  submit = SubmitField('Confirmar Exclusão')

class ComentarioForm(FlaskForm):
  
  nota = IntegerField('Nota', validators=[DataRequired()])
  corpo = StringField('Descrição', widget=TextArea(), validators=[DataRequired()])
  
  submit = SubmitField('Enviar')



class LoginForm(FlaskForm):
    nome_usuario = StringField('Nome de Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    nome_usuario = StringField('Nome de Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])

    submit = SubmitField('Enviar')


