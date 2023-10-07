from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/flask_db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# 데이터베이스 테이블 생성
with app.app_context():
    db.create_all()

# Create - 데이터 생성
@app.route('/create', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' in data:
        new_item = Item(name=data['name'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item created successfully'}), 201
    else:
        return jsonify({'error': 'Name is required'}), 400

# Read - 데이터 조회
@app.route('/read', methods=['GET'])
def get_all_items():
    items = Item.query.all()
    item_list = [{'id': item.id, 'name': item.name} for item in items]
    return jsonify(item_list)

# Update - 데이터 수정
@app.route('/update/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    if 'name' in data:
        item.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Item updated successfully'}), 200
    else:
        return jsonify({'error': 'Name is required'}), 400
    
# Delete - 데이터 삭제
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)