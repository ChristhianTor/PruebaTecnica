from flask_sqlalchemy import SQLAlchemy

# Inicializar la base de datos SQLAlchemy (sin crearla aún)
db = SQLAlchemy()

# Definir el modelo de Producto como ejemplo
class Product(db.Model):

    __tablename__ = 'products'  # Nombre de la tabla en la base de datos
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
