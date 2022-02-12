from app.app_init import *

class Cities(alch.Model):
    id = alch.Column(alch.Integer, primary_key = True)
    name = alch.Column(alch.String(20), nullable = False)
    country_id = alch.Column(alch.Integer, alch.ForeignKey('countries.id'), nullable = False)
    country = alch.relationship('Countries', backref = alch.backref('cities', lazy = False))

    def __repr__(self) -> str:
        return f'{self.name} city'
    
    def by_name(name: str):
        '''finds city or returns None'''
        for x in Cities.query.filter_by(name = name):
            return x
        return None

class Countries(alch.Model):
    id = alch.Column(alch.Integer, primary_key = True)
    name = alch.Column(alch.String(20), nullable = False, unique = True)

    def __repr__(self) -> str:
        return f'{self.name} country'
    
    def by_name(name: str):
        '''finds country or returns None'''
        for x in Countries.query.filter_by(name = name):
            return x
        return None

class Producers(alch.Model):
    id = alch.Column(alch.Integer, primary_key = True)
    name = alch.Column(alch.String(50), nullable = False, unique = True)
    city_id = alch.Column(alch.Integer, alch.ForeignKey('cities.id'), nullable = False)
    city = alch.relationship('Cities', backref = alch.backref('producers', lazy = False))

    def __repr__(self) -> str:
        return f'{self.name} producer'
    
    def by_name(name: str):
        '''finds producer or returns None'''
        for x in Producers.query.filter_by(name = name):
            return x
        return None

class Products(alch.Model):
    id = alch.Column(alch.Integer, primary_key = True)
    name = alch.Column(alch.String(50), nullable = False, unique = True)
    amount = alch.Column(alch.Integer, nullable = False)
    price = alch.Column(alch.Float, nullable = False)
    discount = alch.Column(alch.Float, nullable = False)
    producer_id = alch.Column(alch.Integer, alch.ForeignKey('producers.id'), nullable = False)
    producer = alch.relationship('Producers', backref = alch.backref('products', lazy = False))
    provider_id = alch.Column(alch.Integer, alch.ForeignKey('providers.id'), nullable = False)
    provider = alch.relationship('Providers', backref = alch.backref('products', lazy = False))
    image_link = alch.Column(alch.String(80))
    
    def __repr__(self) -> str:
        return f'{self.name} product'
    
    def by_name(name: str):
        '''finds product or returns None'''
        for x in Products.query.filter_by(name = name):
            return x
        return None

class Providers(alch.Model):
    id = alch.Column(alch.Integer, primary_key = True)
    name = alch.Column(alch.String(50), nullable = False, unique = True)
    city_id = alch.Column(alch.Integer, alch.ForeignKey('cities.id'), nullable = False)
    city = alch.relationship('Cities', backref = alch.backref('providers', lazy = False))

    def __repr__(self) -> str:
        return f'{self.name} provider'
    
    def by_name(name: str):
        '''finds provider or returns None'''
        for x in Providers.query.filter_by(name = name):
            return x
        return None

class Purchases(alch.Model):
    id = alch.Column(alch.Integer, primary_key = True)
    user_id = alch.Column(alch.Integer, alch.ForeignKey('users.id'), nullable = False)
    user = alch.relationship('Users', backref = alch.backref('purchases', lazy = False))
    product_id = alch.Column(alch.Integer, alch.ForeignKey('products.id'), nullable = False)
    product = alch.relationship('Products', backref = alch.backref('purchases', lazy = False))
    amount = alch.Column(alch.Integer, nullable = False)
    price = alch.Column(alch.Float, nullable = False)
    discount = alch.Column(alch.Float, nullable = False)
    date = alch.Column(alch.Date, nullable = False)
    
    def __repr__(self) -> str:
        return f'{self.user} purchased {self.product} x{self.amount} at {self.date}'

class Supplies(alch.Model):
    id = alch.Column(alch.Integer, primary_key = True)
    product_id = alch.Column(alch.Integer, alch.ForeignKey('products.id'), nullable = False)
    product = alch.relationship('Products', backref = alch.backref('supplies', lazy = False))
    amount = alch.Column(alch.Integer, nullable = False)
    date = alch.Column(alch.Date, nullable = False)

    def __repr__(self) -> str:
        return f'delivered {self.product} x{self.amount} at {self.date}'

class Users(alch.Model):
    id = alch.Column(alch.Integer, primary_key = True)
    email = alch.Column(alch.String(80), unique = True)
    phone = alch.Column(alch.String(80), unique = True)
    password = alch.Column(alch.String(80), nullable = False)
    name = alch.Column(alch.String(80), nullable = False)
    surname = alch.Column(alch.String(80), nullable = False)
    birth_date = alch.Column(alch.Date, nullable = False)
    sign_up_date = alch.Column(alch.Date, nullable = False)

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} {self.email}'
    
    def by_name_surname(name, surname: str):
        '''finds user or returns None'''
        for x in Users.query.filter_by(name = name, surname = surname):
            return x
        return None

print('ORM models included')
