import sqlite3
from flask import Flask, render_template, abort, request, url_for, redirect
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', title='Sistema de Gestión de Alumnos')

@app.route('/alumnos', methods=['GET'])
def get_all_alumnos():
    conn = get_db_connection()
    alumnos = conn.execute('SELECT * FROM alumnos').fetchall()
    conn.close()
    return render_template('students.html', title='Lista de Estudiantes', alumnos=alumnos)

@app.route('/alumnos/<int:alumno_id>', methods=['GET'])
def get_alumno(alumno_id):
    conn = get_db_connection()
    alumno = conn.execute('SELECT * FROM alumnos WHERE id = ?', (alumno_id,)).fetchone()
    conn.close()
    if alumno is None:
        abort(404)
    return render_template('students.html', alumno=alumno)

@app.route('/alumnos/create', methods=['GET', 'POST'])
def create_alumno():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = True if request.form.get('aprobado') == 'true' else False
        nota = float(request.form['nota'])
        fecha = request.form['fecha']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha) VALUES (?, ?, ?, ?, ?)',
                    (nombre, apellido, aprobado, nota, fecha))
        conn.commit()
        conn.close()
        return redirect(url_for('get_all_alumnos'))

    return render_template('alumno/create.html')

@app.route('/alumnos/edit/<int:alumno_id>', methods=['GET', 'POST'])
def edit_alumno(alumno_id):
    conn = get_db_connection()
    alumno = conn.execute('SELECT * FROM alumnos WHERE id = ?', (alumno_id,)).fetchone()
    
    if alumno is None:
        conn.close()
        abort(404)
        
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = True if request.form.get('aprobado') == 'true' else False
        nota = float(request.form['nota'])
        fecha = request.form['fecha']

        conn.execute('UPDATE alumnos SET nombre = ?, apellido = ?, aprobado = ?, nota = ?, fecha = ? WHERE id = ?',
                    (nombre, apellido, aprobado, nota, fecha, alumno_id))
        conn.commit()
        conn.close()
        return redirect(url_for('get_all_alumnos'))

    conn.close()
    return render_template('alumno/edit.html', alumno=alumno)

@app.route('/alumnos/delete/<int:alumno_id>', methods=['POST'])
def delete_alumno(alumno_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM alumnos WHERE id = ?', (alumno_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('get_all_alumnos'))

if __name__ == '__main__':
    app.run(debug=True)