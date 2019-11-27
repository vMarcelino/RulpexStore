from . import dbapp as models
#print('imported')
#print('making adapter')
Base = models.Model
Column = models.Column
Integer = models.Integer
Float = models.Float
String = models.String
DateTime = models.DateTime
relationship = models.relationship
ForeignKey = models.ForeignKey

#print('adapter done')

#print('creating classes')


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cpf = Column(String)
    email = Column(String)
    address = Column(String)
    password = Column(String)
    salt = Column(String)


class Catalog(Base):
    __tablename__ = 'Catalog'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    owner_id = Column(Integer, ForeignKey('User.id'), nullable=False)

    owner = relationship("User", backref='Catalogs')


class Item(Base):
    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    value = Column(Float, nullable=False)
    image = Column(String)
    catalog_id = Column(Integer, ForeignKey('Catalog.id'))

    catalog = relationship("Catalog", backref='items')


class Transaction(Base):
    __tablename__ = 'Transaction'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('Item.id'))
    user_id = Column(Integer, ForeignKey('User.id'))

    item = relationship("Item", backref='buyers')
    user = relationship("User", backref='items_bought')


def generate_base():
    from . import helpers
    print('generating base')
    models.create_all()
    session = models.session
    salt = helpers.generate_cryptographically_random_string(8)
    hashed_password = helpers.hash_with_salt('admin', salt)
    admin = User(name='admin', password=hashed_password, salt=salt)
    catalogo_camisetas = Catalog(name='Camisetas', owner=admin)
    to_add = [admin, catalogo_camisetas]
    session.add_all(to_add)
    session.commit()
