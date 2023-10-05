from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 이 부분 추가
db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


@app.route('/create', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' in data:
        new_item = Item(name=data['name'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item created successfully"}), 201
    else:
        return jsonify({"error": "Name is required"}), 400
    
@app.route('/read', methods=['GET'])
def get_items():
    items = Item.query.all()
    item_list = [{"id": item.id, "name": item.name} for item in items]
    return jsonify(item_list), 200    


@app.route('/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get(item_id)
    if item:
        item.name = data['name']
        db.session.commit()
        return jsonify({"message": "Item updated successfully"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404
    


@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item deleted successfully"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
# @app.route('/users')
# def users():
#     # users 데이터를 Json 형식으로 반환한다
#     return {"members": [{"id":1, "name":"yuhyeon"}, {"id":2,"name":"mango"}]}

# if __name__ == "__main__":
#     app.run(debug = True)