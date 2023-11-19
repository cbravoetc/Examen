from flask import Flask, render_template, request

app = Flask(__name__)


# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')


# Página del ejercicio 1
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


# Ruta para procesar el ejercicio 1
@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    tarros = int(request.form['tarros'])

    precio_tarro = 9000
    total_sin_descuento = precio_tarro * tarros

    descuento = 0
    if edad >= 18 and edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25

    descuento_aplicado = total_sin_descuento * descuento
    total_con_descuento = total_sin_descuento - descuento_aplicado

    total_sin_descuento = "${:.2f}".format(total_sin_descuento)
    descuento_aplicado = "${:.2f}".format(descuento_aplicado)
    total_con_descuento = "${:.2f}".format(total_con_descuento)


    return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                           descuento_aplicado=descuento_aplicado, total_con_descuento=total_con_descuento)

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    username = request.form['username']
    password = request.form['password']
    mensaje = ''

    if username == 'juan' and password == 'admin':
        mensaje =  f'Bienvenido administrador {username}'
    elif username == 'pepe' and password == 'user':
        mensaje =  f'Bienvenido usuario {username}'
    else:
        mensaje =  'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)