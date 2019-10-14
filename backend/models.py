from backend import dbapp as models
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
    name = Column(String)
    cpf = Column(String)
    email = Column(String)
    address = Column(String)
    password = Column(String)
    salt = Column(String)


class Catalog(Base):
    __tablename__ = 'Catalog'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    owner_id = Column(Integer, ForeignKey('User.id'), nullable=False)

    owner = relationship("User", backref='Catalogs')


class Item(Base):
    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    description = Column(String)
    value = Column(Float, nullable=False)
    image = Column(String)
    catalog_id = Column(Integer, ForeignKey('Catalog.id'))

    catalog = relationship("Catalog", backref='items')


def generate_base():
    print('generating base')
    session = models.session
    admin = User(name='admin', password='admin')
    catalogo_camisetas = Catalog(name='Camisetas', owner=admin)
    to_add = [admin, catalogo_camisetas]
    session.add_all(to_add)
    session.commit()
