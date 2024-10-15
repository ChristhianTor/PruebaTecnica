from flask import Flask, request, jsonify
from models import db, Product

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta simple para verificar que todo funciona
@app.route('/')
def home():
    return "¡Hola, Flask está funcionando!"

# Iniciar la aplicación solo si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)


# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Vincular la base de datos con la aplicación Flask
db.init_app(app)

@app.route('/db')
def Visudb():
    return "¡Base de datos conectada correctamente!"

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()  # Obtener el cuerpo de la solicitud en formato JSON

    # Crear un nuevo objeto de tipo Product usando los datos recibidos
    new_product = Product(name=data['name'], price=data['price'])

    # Agregar el nuevo producto a la sesión de la base de datos
    db.session.add(new_product)

    # Confirmar los cambios y guardarlos en la base de datos
    db.session.commit()

    # Devolver una respuesta indicando que el producto fue creado
    return jsonify({'message': 'Producto creado con éxito'}), 201


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()  # Obtener todos los productos

    # Convertir cada producto a un diccionario
    result = [
        {'id': p.id, 'name': p.name, 'price': p.price} for p in products
    ]

    return jsonify(result), 200  # Devolver la lista de productos en formato JSON


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)  # Buscar el producto por ID o devolver 404

    # Devolver los datos del producto en formato JSON
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 200


@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)  # Buscar el producto por ID
    data = request.get_json()  # Obtener los nuevos datos en JSON

    # Actualizar los atributos del producto
    product.name = data.get('name', product.name)  # Si no se envía 'name', se mantiene el actual
    product.price = data.get('price', product.price)  # Igual con 'price'

    # Guardar los cambios en la base de datos
    db.session.commit()

    return jsonify({'message': 'Producto actualizado con éxito'}), 200


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)  # Buscar el producto por ID

    # Eliminar el producto de la base de datos
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Producto eliminado con éxito'}), 200
