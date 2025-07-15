from flask import Flask, render_template, request, redirect, url_for

from config import Config
from models import Employee, db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

# Create DB tables once
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    employees = Employee.query.all()
    return render_template('home.html')

# @app.route('/listemp')
# def listemp():
#     employees = Employee.query.all()
#     return render_template('listemp.html', employees=employees)


@app.route('/listemp')
def listemp():
    query = Employee.query

    # Search by name or department
    search = request.args.get('search')
    if search:
        query = query.filter(
            (Employee.name.ilike(f'%{search}%')) |
            (Employee.department.ilike(f'%{search}%'))
        )

    # Filter by department
    dept = request.args.get('department')
    if dept and dept != "All":
        query = query.filter(Employee.department == dept)

    # Filter by salary range
    min_salary = request.args.get('min_salary')
    max_salary = request.args.get('max_salary')
    if min_salary:
        query = query.filter(Employee.salary >= float(min_salary))
    if max_salary:
        query = query.filter(Employee.salary <= float(max_salary))

    employees = query.all()

    # Get distinct departments for dropdown
    departments = [d[0] for d in db.session.query(Employee.department).distinct()]

    return render_template('listemp.html', employees=employees, departments=departments)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        dept = request.form['department']
        salary = float(request.form['salary'])

        new_emp = Employee(name=name, department=dept, salary=salary)
        db.session.add(new_emp)
        db.session.commit()
        return redirect(url_for('listemp'))
    return render_template('create.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    emp = Employee.query.get_or_404(id)
    if request.method == 'POST':
        emp.name = request.form['name']
        emp.department = request.form['department']
        emp.salary = float(request.form['salary'])

        db.session.commit()
        return redirect(url_for('listemp'))
    return render_template('edit.html', emp=emp)

@app.route('/delete/<int:id>')
def delete(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('listemp'))

if __name__ == '__main__':
    app.run()
