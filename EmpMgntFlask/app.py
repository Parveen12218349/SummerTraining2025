from flask import Flask, render_template, request, redirect, url_for

from config import Config
from decorators import login_required, admin_required
from models import Employee, db, User

app = Flask(__name__)

app.secret_key='SECRETKEY'

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
@login_required
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
@admin_required
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
@admin_required
def delete(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('listemp'))


@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    total_employees = Employee.query.count()
    avg_salary = db.session.query(db.func.avg(Employee.salary)).scalar()
    max_salary = db.session.query(db.func.max(Employee.salary)).scalar()
    min_salary = db.session.query(db.func.min(Employee.salary)).scalar()

    dept_counts = db.session.query(Employee.department, db.func.count(Employee.id)) \
                            .group_by(Employee.department).all()

    recent_employees = Employee.query.order_by(Employee.id.desc()).limit(5).all()

    return render_template('dashboard.html',
                           total=total_employees,
                           avg=round(avg_salary or 0, 2),
                           max_salary=max_salary,
                           min_salary=min_salary,
                           dept_counts=dept_counts,
                           recent_employees=recent_employees)


from flask import session, flash, redirect, url_for, request, render_template

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            session['user_id'] = user.id
            flash("Logged in successfully.")
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out.")
    return redirect(url_for('login'))

@app.route('/create-admin')
@admin_required
def create_admin():
    admin = User(username='admin', is_admin=True)
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    return "Admin created!"


if __name__ == '__main__':
    app.run()
