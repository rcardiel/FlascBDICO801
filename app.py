from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate #agegar referencia de migracion
from config import DevelopmentConfig
import forms

from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate=Migrate(app, db) #inicializar migracion
csrf = CSRFProtect(app)


@app.route("/",methods=["GET","POST"])
@app.route("/index")
def index():
    create_alumno=forms.UserForm(request.form)
    #select * alumnos alumnos
    alumno=Alumnos.query.all()
    return render_template("index.html", form=create_alumno, alumno=alumno)




@app.route("/usuarios",methods=["GET","POST"])
def usuario():
    mat=0
    nom=''
    apa=''
    ama=''
    edad=0
    email=''
    usuarios_clas=forms.UserForm(request.form)
    if request.method=='POST':
        mat=usuarios_clas.matricula.data
        nom=usuarios_clas.nombre.data
        apa=usuarios_clas.apaterno.data
        ama=usuarios_clas.amaterno.data
        edad=usuarios_clas.edad.data
        email=usuarios_clas.correo.data
    
    return render_template('usuarios.html',form=usuarios_clas,mat=mat,
                           nom=nom,apa=apa,ama=ama,edad=edad,email=email)

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
