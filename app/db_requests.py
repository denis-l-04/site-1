import datetime
from app.ORM_models import *

#Поставщик для товара product
def provider_of_product(product: Products) -> Providers:
    return product.provider

#Товары, произведённые в городе city
def products_from_city(city: Cities) -> list:
    return list(filter(lambda x: x.producer.city == city, Products.query.all()))

#Пользователи, купившие последний товар не раньше даты date
def recent_buyers(date: datetime.date) -> list:
    buyers = set()
    for p in Purchases.query.all():
        if p.date >= date:
            buyers.add(p.user)
    return list(buyers)

#Товары, купленные пользователем user наибольшее число раз, либо пустой список, если их нет
def favorite_of_user(user: Users) -> list:
    goods_am = dict()
    for p in Purchases.query.filter_by(user = user):
        if p.product_id in goods_am:
            goods_am[p.product_id] += p.amount
        else:
            goods_am[p.product_id] = p.amount
    
    max_am = max(goods_am.values())
    fav = list()
    for key, value in goods_am.items():
        if value == max_am:
            fav.append(Products.query.get(key))
    goods_am.clear()
    return fav


#Страна поставщика provider
def country_of_provider(provider: Providers) -> Countries:
    return provider.city.country

#Дата последней поставки товара product или None при отсутствии поставок
def last_supply_of_product(product: Products):
    mxd = None
    for s in Supplies.query.filter_by(product = product):
        if mxd == None or mxd < s.date:
            mxd = s.date
    return mxd

print('database typical requests included')
