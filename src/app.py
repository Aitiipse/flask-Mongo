from ast import Delete
from config import *
from persona import Persona
from flask import Flask, render_template, request,redirect, url_for

con_db = conexion()
app = Flask(__name__)


@app.route('/')
def index():
    personas = con_db['Personas']
    personasregistradas=personas.find()
    
    return render_template("index.html", personas=personasregistradas)

    # nombre= request.form['nombre']
    # apellido= request.form['apellido']
    # telefono= request.form['email']

@app.route('/index')
def pindex():
    personas = con_db['Personas']
    personasregistradas=personas.find()
    
    return render_template("index.html", personas=personasregistradas)

@app.route('/editar')
def peditar():
    personas = con_db['Personas']
    personasregistradas=personas.find()
    
    return render_template("editar.html", personas=personasregistradas)

# @app.route('/buscar')
# def peditar():
#     personas = con_db['Personas']
#     personasregistradas=personas.find()
    
#     return render_template("buscar.html", personas=personasregistradas)

@app.route('/eliminar')
def peliminar():
    personas = con_db['Personas']
    personasregistradas=personas.find()
    
    return render_template("eliminar.html", personas=personasregistradas)

@app.route('/lista')
def plista():
    personas = con_db['Personas']
    personasregistradas=personas.find()
    return render_template("lista.html", personas=personasregistradas)

@app.route('/guardar_user', methods = ['POST']) 
def agregarPersona():
    personas = con_db['Personas']
    nombre= request.form['nombre']
    apellido= request.form['apellido']
    telefono= request.form['telefono']

    if nombre and apellido and telefono:
        persona= Persona(nombre,apellido,telefono)
        personas.insert_one(persona.formato_doc())
        return redirect(url_for('index'))
    else:
        return "Error"   
    
    

@app.route('/eliminar_persona/<string:nombre_persona>')
def eliminar (nombre_persona):
    personas = con_db['Personas']
    personas.delete_one({ 'nombre': nombre_persona})
    print(personas)
    return redirect(url_for('peliminar'))
    
    
@app.route('/editar_persona/<string:nombre_persona>', methods=['POST'])
def editar (nombre_persona):
    personas = con_db['Personas']
    nombre= request.form['nombre']
    apellido= request.form['apellido']
    telefono= request.form['telefono']
    
    if nombre and apellido and telefono:
        personas.update_one({'nombre':nombre_persona},{'$set':{'nombre':nombre, 'apellido':apellido,'telefono':telefono}})
        return redirect(url_for('peditar'))
    else:
        return "error"

# @app.route('/buscar_persona/<string:nombre_persona>', methods=['GET'])
# def editar (nombre_persona):
#     personas = con_db['Personas']
#     nombre= request.form['nombre']
#     apellido= request.form['apellido']
#     telefono= request.form['telefono']
    
#     if nombre and apellido and telefono:
#         personas.update_one({'nombre':nombre_persona},{'$set':{'nombre':nombre, 'apellido':apellido,'telefono':telefono}})
#         return redirect(url_for('peditar'))
#     else:
#         return "error"


if __name__== '__main__':
    app.run(debug=True, port=8000)
