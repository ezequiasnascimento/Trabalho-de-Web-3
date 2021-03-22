from app import app
from flask import request, render_template, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from app.models.forms import ComentarioForm, LoginForm, CadastroForm, DeleteForm
from app.models.carro import Carro
from app.models.usuario import Usuario
from app.models.comentario import Comentario

from app import db, login

from werkzeug.urls import url_parse


@login.user_loader
def load_user(id):
    return Usuario.query.filter_by(id=id).first()

@app.route("/")
@app.route("/carros")
@login_required
def carros():

    carros = Carro.query.all()
    return render_template("carros.html", carros=carros)


@app.route("/comentarios/<int:id>/novo", methods=['GET', 'POST'])
@login_required
def novo_comentario(id):
    form = ComentarioForm()
    carro = Carro.query.get(id)
    usuario = Usuario.query.get(current_user.get_id())
 

    if form.validate_on_submit():
        c = Comentario(nome_usuario=current_user.nome_usuario,
                       corpo=form.corpo.data,
                       autor=carro,
                       escritor=usuario,
                       nota=form.nota.data)
        db.session.add(c)
        db.session.commit()
        return redirect(url_for("carros"))
    return render_template("comentario_novo.html", form=form)


@app.route("/comentarios/<int:id>", methods=['GET', 'POST'])
@login_required
def comentarios(id):
    carro = Carro.query.get(id)
    print(carro)
    comentarios = carro.comentarios
    print(comentarios)
    return render_template("comentarios.html", comentarios=comentarios, id=id)

@app.route("/comentarios/<int:id>/<int:id2>/editar", methods=['GET', 'POST'])
@login_required
def editar_comentario(id, id2):
  form = ComentarioForm()
  comentario = Comentario.query.get(id2)
  if comentario is None:
    return abort(404)
  if form.validate_on_submit():
    comentario.nota = form.nota.data
    comentario.corpo = form.corpo.data
    db.session.commit()
    return redirect(url_for("comentarios", id=id))
  return render_template("comentario_editar.html", form=form, comentario=comentario)

@app.route("/comentarios/<int:id>/<int:id2>", methods=['GET', 'POST'])
@login_required
def excluir_comentario(id, id2):
  form = DeleteForm()
  comentario = Comentario.query.get(id2)
  if comentario is None:
    return abort(404)
  if form.validate_on_submit():
    db.session.delete(comentario)
    db.session.commit()
    return redirect(url_for("comentarios", id=id))
  return render_template("comentario_excluir.html", form=form, comentario=comentario)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Seja bem-vindo!")

        return redirect(url_for('carros'))

    form = LoginForm()

    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(
            nome_usuario=form.nome_usuario.data).first()
        if usuario is None or not usuario.verificar_senha(form.senha.data):
         
            flash("Dados Invalidos")
        else:
            login_user(usuario)
            flash("Usuário Valido")

            next_page = request.args.get('next')

            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('carros')
            return redirect(next_page)

    return render_template('login.html', form=form)


@app.route("/cadastro", methods=['GET', 'POST'])
def signup():
    form = CadastroForm()
    if form.validate_on_submit():
        u = Usuario(
            nome=form.nome.data,
            nome_usuario=form.nome_usuario.data)
        u.adicionar_senha(form.senha.data)

        confirma = Usuario.query.filter_by(nome_usuario= form.nome_usuario.data).first()

        if (confirma == None):
            db.session.add(u)
            db.session.commit()
            flash("Conta Criada")
            return redirect(url_for('login'))

        else:
            flash("Conta existente! Faça login")

    return render_template('cadastro.html', form=form)


@app.route("/sair", methods=['GET', 'POST'])
@login_required
def sair():
    logout_user()
    flash("Usuário Saiu")
    return redirect(url_for("login"))


@app.route("/add/<k>", methods=['GET', 'POST'])
def add(k):

    f = Carro(modelo='Fusca Italic', cor="Azul", ano="2002")
    db.session.add(f)
    db.session.commit()
    return 'ok'

@app.errorhandler(404)
def not_found_error(error):
  return render_template("erro.html", cod_erro=404, desc_erro="Página não encontrada!"), 404

@app.errorhandler(500)
def internal_error(error):
  db.session.rollback()
  return render_template("erro.html", cod_erro=500, desc_erro="Erro interno do servidor!"), 500