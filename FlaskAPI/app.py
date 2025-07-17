from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, ToDo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --- AUTH ROUTES ---

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists'}), 400
    user = User()
    user.username = data['username']
    user.password = data['password']
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        login_user(user)
        return jsonify({'message': 'Logged in'})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out'})

# --- TODO ROUTES ---

@app.route('/api/todos', methods=['GET'])
@login_required
def get_todos():
    todos = ToDo.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': t.id, 'title': t.title, 'done': t.done} for t in todos])

@app.route('/api/todos', methods=['POST'])
@login_required
def add_todo():
    data = request.json
    todo = ToDo(title=data['title'], user_id=current_user.id)
    db.session.add(todo)
    db.session.commit()
    return jsonify({'message': 'Todo added'}), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
@login_required
def update_todo(todo_id):
    todo = ToDo.query.get_or_404(todo_id)
    if todo.user_id != current_user.id:
        return jsonify({'message': 'Not authorized'}), 403
    data = request.json
    todo.title = data.get('title', todo.title)
    todo.done = data.get('done', todo.done)
    db.session.commit()
    return jsonify({'message': 'Todo updated'})

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
@login_required
def delete_todo(todo_id):
    todo = ToDo.query.get_or_404(todo_id)
    if todo.user_id != current_user.id:
        return jsonify({'message': 'Not authorized'}), 403
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)