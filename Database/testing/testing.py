import unittest
import os
import sys
import inspect
db_dir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
print('path is', db_dir)
sys.path.insert(0, db_dir)
from db_init import *
import TYPICAL_REQUESTS

class WrappedRequestsTest(unittest.TestCase):    
    def tearDown(self) -> None:
        alch.session.rollback()
    
    def test_provider_of_product(self):
        self.assertEqual(TYPICAL_REQUESTS.provider_of_product(Products.by_name('Ноутбук FCNPZ')), Providers.by_name('Handsome Company'))
        self.assertEqual(TYPICAL_REQUESTS.provider_of_product(Products.by_name('Флагман P1')), Providers.by_name('TurnipDisagreeable Technologies'))
        self.assertEqual(TYPICAL_REQUESTS.provider_of_product(Products.by_name('Салфетки для техники IGUU')), Providers.by_name('EnergeticPumpkin'))
    
    def test_products_from_city(self):
        l = TYPICAL_REQUESTS.products_from_city(Cities.by_name('Вашингтон'))
        self.assertCountEqual(l, [Products.by_name('Флагман P1')])
        l = TYPICAL_REQUESTS.products_from_city(Cities.by_name('Лондон'))
        self.assertCountEqual(l, [])
        l = TYPICAL_REQUESTS.products_from_city(Cities.by_name('Варшава'))
        self.assertCountEqual(l, [])
        l = TYPICAL_REQUESTS.products_from_city(Cities.by_name('Саратов'))
        self.assertCountEqual(l, [Products.by_name('Колонки DarkEJK'), Products.by_name('Аккумулятор NY150'),\
            Products.by_name('Смартфон CheerfulP94N'), Products.by_name('Мышь 9M')])
    
    def test_recent_buyers(self):
        l = TYPICAL_REQUESTS.recent_buyers(datetime.date.fromisoformat('2022-01-17'))
        self.assertCountEqual(l, [Users.by_name_surname('Тимур', 'Пономарёв'), Users.by_name_surname('Максим', 'Королёв')])
        l = TYPICAL_REQUESTS.recent_buyers(datetime.date.fromisoformat('2022-01-18'))
        self.assertCountEqual(l, [Users.by_name_surname('Тимур', 'Пономарёв')])
        l = TYPICAL_REQUESTS.recent_buyers(datetime.date.fromisoformat('2077-11-23'))
        self.assertCountEqual(l, [])
    
    def test_favorite_of_user(self):
        self.assertEqual(TYPICAL_REQUESTS.favorite_of_user(Users.by_name_surname('Владимир', 'Фомичёв')), [Products.by_name('Процессор JSM')])
        self.assertEqual(TYPICAL_REQUESTS.favorite_of_user(Users.by_name_surname('Марк', 'Антонов')), [Products.by_name('Ноутбук FCNPZ')])
    
    def test_country_of_provider(self):
        self.assertEqual(TYPICAL_REQUESTS.country_of_provider(Providers.by_name('WatermelonApricot')), Countries.by_name('Россия'))
        self.assertEqual(TYPICAL_REQUESTS.country_of_provider(Providers.by_name('PeaCherry')), Countries.by_name('Канада'))
    
    def test_last_supply_of_product(self):
        self.assertEqual(TYPICAL_REQUESTS.last_supply_of_product(Products.by_name('Флагман 1O47')), datetime.date.fromisoformat('2021-04-15'))
        self.assertEqual(TYPICAL_REQUESTS.last_supply_of_product(Products.by_name('Мышь ConceitedJF9G')), datetime.date.fromisoformat('2019-10-23'))
    
    def test_add_user(self):
        alch.session.add(Users(name = 'Вася', surname = 'Пупкин', password = 'somethingincredible43252543', birth_date = datetime.date(1234, 4, 1),\
            sign_up_date = datetime.date(2000, 6, 15)))
        self.assertEqual(Users.by_name_surname('Вася', 'Пупкин').password, 'somethingincredible43252543')
        self.assertEqual(Users.by_name_surname('Вася', 'Пупкин').email, None)
    
    def test_delete_user(self):
        alch.session.delete(Users.query.get(118))
        self.assertIsNone(Users.by_name_surname('Элина', 'Кабанова'))

if __name__=='__main__':
    unittest.main()