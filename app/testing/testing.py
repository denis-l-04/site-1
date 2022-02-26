import tempfile
import unittest
import os
import sys
import datetime
from shutil import copyfile
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'..\\..\\..\\'))
from app import app_obj, alch, db_requests
from app.ORM_models import *
from config import BASE_DIR


class WrappedRequestsTest(unittest.TestCase):
    def setUp(self) -> None:
        '''
        with open(BASE_DIR+'/app/testing/testing.db', 'rb') as src_f:
            with open(BASE_DIR+'/app/testing/temp.db', 'wb') as dst_f:
        '''
        copyfile(BASE_DIR+'\\app\\testing\\testing.db', BASE_DIR+'\\app\\testing\\temp.db')
        self.db_fd, app_obj.config["DATABASE"] = tempfile.mkstemp()
        app_obj.config["TESTING"] = True
        self.client = app_obj.test_client()
        alch.create_all()

    def tearDown(self) -> None:
        os.close(self.db_fd)
        os.unlink(app_obj.config["DATABASE"])
    
    def test_provider_of_product(self):
        self.assertEqual(db_requests.provider_of_product(product_by_name('Ноутбук FCNPZ')), provider_by_name('Handsome Company'))
        self.assertEqual(db_requests.provider_of_product(product_by_name('Флагман P1')), provider_by_name('TurnipDisagreeable Technologies'))
        self.assertEqual(db_requests.provider_of_product(product_by_name('Салфетки для техники IGUU')), provider_by_name('EnergeticPumpkin'))
    
    def test_products_from_city(self):
        l = db_requests.products_from_city(city_by_name('Вашингтон'))
        self.assertCountEqual(l, [product_by_name('Флагман P1')])
        l = db_requests.products_from_city(city_by_name('Лондон'))
        self.assertCountEqual(l, [])
        l = db_requests.products_from_city(city_by_name('Варшава'))
        self.assertCountEqual(l, [])
        l = db_requests.products_from_city(city_by_name('Саратов'))
        self.assertCountEqual(l, [product_by_name('Колонки DarkEJK'), product_by_name('Аккумулятор NY150'),\
            product_by_name('Смартфон CheerfulP94N'), product_by_name('Мышь 9M')])
    
    def test_recent_buyers(self):
        l = db_requests.recent_buyers(datetime.date.fromisoformat('2022-01-17'))
        self.assertCountEqual(l, [user_by_name_surname('Тимур', 'Пономарёв'), user_by_name_surname('Максим', 'Королёв')])
        l = db_requests.recent_buyers(datetime.date.fromisoformat('2022-01-18'))
        self.assertCountEqual(l, [user_by_name_surname('Тимур', 'Пономарёв')])
        l = db_requests.recent_buyers(datetime.date.fromisoformat('2077-11-23'))
        self.assertCountEqual(l, [])
    
    def test_favorite_of_user(self):
        self.assertEqual(db_requests.favorite_of_user(user_by_name_surname('Владимир', 'Фомичёв')), [product_by_name('Процессор JSM')])
        self.assertEqual(db_requests.favorite_of_user(user_by_name_surname('Марк', 'Антонов')), [product_by_name('Ноутбук FCNPZ')])
    
    def test_country_of_provider(self):
        a=228
        for x in Providers.query.all():
            a=x
        pv = provider_by_name('WatermelonApricot')
        t = db_requests.country_of_provider(pv)
        self.assertEqual(t, country_by_name('Россия'))
        self.assertEqual(db_requests.country_of_provider(provider_by_name('PeaCherry')), country_by_name('Канада'))
    
    def test_last_supply_of_product(self):
        self.assertEqual(db_requests.last_supply_of_product(product_by_name('Флагман 1O47')), datetime.date.fromisoformat('2021-04-15'))
        self.assertEqual(db_requests.last_supply_of_product(product_by_name('Мышь ConceitedJF9G')), datetime.date.fromisoformat('2019-10-23'))

class AppTest(unittest.TestCase):
    def setUp(self) -> None:
        copyfile(BASE_DIR+'/app/testing/testing.db', BASE_DIR+'/app/testing/temp.db')
        self.db_fd, app_obj.config["DATABASE"] = tempfile.mkstemp()
        app_obj.config["TESTING"] = True
        self.client = app_obj.test_client()
        alch.create_all()

    def tearDown(self) -> None:
        os.close(self.db_fd)
        os.unlink(app_obj.config["DATABASE"])
    
    def test_page_opening(self):
        for addr in ('/', '/about', '/catalog', '/login', '/registration'):
            resp = self.client.get(addr)
            self.assertEqual(resp.status_code, 200, f'could not open {addr}')
    
    def test_log_in_out(self):
        with self.client:
            resp = self.client.post(
                "/registration",
                follow_redirects=True,
                data={
                    "name": "ivan_9182",
                    "surname": "peatrauveetsch",
                    "password": "ъъъ",
                    "birth_date": "2020-09-01",
                    "email": "ivpet@rambler.com"
                }
            )
            self.assertEqual(flask.request.cookies.get('name'), 'ivan_9182', 'wrong name in cookie')
            self.assertEqual(flask.session['email'], 'ivpet@rambler.com', 'wrong email in session cookie')
            resp = self.client.get('/catalog')
            self.assertNotIn('Успешная регистрация.'.encode('utf-8'), resp.data, 'repeating the message')
            self.assertIn(b'ivan_9182', resp.data, 'no username visible on page')
            resp = self.client.get('/logout', follow_redirects = True)
            self.assertNotEqual(flask.request.cookies.get('name'), 'ivan_9182', 'cookies remain')
            self.assertNotEqual(flask.session.get('email'), 'ivpet@rambler.com', 'session remain')
        with self.client:
            resp = self.client.post('/login', data={'email': 'ivpet@rambler.com', 'password': 'ёёё'}, follow_redirects = True)
            self.assertIn('Неправильный'.encode('utf-8'), resp.data)
            resp = self.client.post('/login', data={'email': 'ivpet@rambler.com', 'password': 'ъъъ'}, follow_redirects = True)
            self.assertIn('Добро пожаловать, ivan_9182!'.encode('utf-8'), resp.data, 'could not log in')
            self.assertEqual(flask.request.cookies.get('name'), 'ivan_9182', 'wrong name in cookie after login')
            self.assertEqual(flask.session['email'], 'ivpet@rambler.com', 'wrong email in session cookie after login')

if __name__=='__main__':
    unittest.main()