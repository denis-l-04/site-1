import unittest
import os
import sys
import inspect
db_dir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
print('path is', db_dir)
sys.path.insert(0, db_dir)
import db_init
import TYPICAL_REQUESTS


db_con, db_cur = db_init.init(db_dir+'\\testing\\testing.db')

class WrappedRequestsTest(unittest.TestCase):    
    def tearDown(self) -> None:
        db_con.rollback()
    
    @classmethod
    def tearDownClass(self) -> None:
        db_con.close()
    
    def test_provider_of_product(self):
        self.assertEqual(TYPICAL_REQUESTS.provider_of_product(db_cur, 'Ноутбук FCNPZ'), 'Handsome Company')
        self.assertEqual(TYPICAL_REQUESTS.provider_of_product(db_cur, 'Флагман P1'), 'TurnipDisagreeable Technologies')
        self.assertEqual(TYPICAL_REQUESTS.provider_of_product(db_cur, 'Салфетки для техники IGUU'), 'EnergeticPumpkin')
    
    def test_product_from_city(self):
        l = TYPICAL_REQUESTS.product_from_city(db_cur, 'Вашингтон')
        self.assertCountEqual(l, [('Флагман P1',)])
        l = TYPICAL_REQUESTS.product_from_city(db_cur, 'Лондон')
        self.assertCountEqual(l, [])
        l = TYPICAL_REQUESTS.product_from_city(db_cur, 'Варшава')
        self.assertCountEqual(l, [])
        l = TYPICAL_REQUESTS.product_from_city(db_cur, 'Саратов')
        self.assertCountEqual(l, [('Колонки DarkEJK',), ('Аккумулятор NY150', ), ('Смартфон CheerfulP94N',), ('Мышь 9M',)])
    
    def test_recent_buyers(self):
        l = TYPICAL_REQUESTS.recent_buyers(db_cur, '2022-01-17')
        self.assertCountEqual(l, [('Тимур', 'Пономарёв'), ('Максим', 'Королёв')])
        l = TYPICAL_REQUESTS.recent_buyers(db_cur, '2022-01-18')
        self.assertCountEqual(l, [('Тимур', 'Пономарёв')])
        l = TYPICAL_REQUESTS.recent_buyers(db_cur, '2077-11-23')
        self.assertCountEqual(l, [])
    
    def test_favorite_of_user(self):
        self.assertEqual(TYPICAL_REQUESTS.favorite_of_user(db_cur, 'Владимир', 'Фомичёв'), 'Процессор JSM')
        self.assertEqual(TYPICAL_REQUESTS.favorite_of_user(db_cur, 'Марк', 'Антонов'), 'Ноутбук FCNPZ')
    
    def test_country_of_provider(self):
        self.assertEqual(TYPICAL_REQUESTS.country_of_provider(db_cur, 'WatermelonApricot'), 'Россия')
        self.assertEqual(TYPICAL_REQUESTS.country_of_provider(db_cur, 'PeaCherry'), 'Канада')
    
    def test_last_supply_of_product(self):
        self.assertEqual(TYPICAL_REQUESTS.last_supply_of_product(db_cur, 'Флагман 1O47'), '2021-04-15')
        self.assertEqual(TYPICAL_REQUESTS.last_supply_of_product(db_cur, 'Мышь ConceitedJF9G'), '2019-10-23')

if __name__=='__main__':
    unittest.main()