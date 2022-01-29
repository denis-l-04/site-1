#Поставщик для товара с именем product
def provider_of_product(cursor, product: str) -> str:
    cursor.execute(f'SELECT name FROM providers WHERE id = (SELECT provider_id FROM products WHERE name = \'{product}\');')
    return cursor.fetchall()[0][0]

#Товары, произведённые в городе city
def product_from_city(cursor, city: str) -> list:
    cursor.execute(f'SELECT name FROM products WHERE producer_id IN (SELECT id FROM producers WHERE city_id = (SELECT id from cities WHERE name = \'{city}\'));')
    return cursor.fetchall()

#Пользователи, купившие последний товар не раньше даты date
def recent_buyers(cursor, date: str) -> list:
    cursor.execute(f'SELECT name, surname FROM users WHERE id IN (SELECT DISTINCT user_id FROM purchases WHERE purchases.date >= \'{date}\');')
    return cursor.fetchall()

#Товар, купленный пользователем name surname наибольшее число раз
def favorite_of_user(cursor, name: str, surname: str) -> str:
    cursor.execute(f'''
SELECT name
FROM products
WHERE id = (
	SELECT product_id from (
		SELECT product_id, max(goods) FROM (
			SELECT product_id, sum(amount) AS goods
			FROM purchases
			WHERE user_id = (SELECT id FROM users WHERE name = '{name}' AND surname = '{surname}')
			GROUP BY product_id
		)
	)
)
;
''')
    return cursor.fetchall()[0][0]


#Страна поставщика provider
def country_of_provider(cursor, provider: str) -> str:
    cursor.execute(f'SELECT name FROM countries WHERE id = (SELECT country_id FROM cities WHERE id = (SELECT city_id FROM providers WHERE name = \'{provider}\'));')
    return cursor.fetchall()[0][0]

#Дата последней поставки товара product
def last_supply_of_product(cursor, product: str) -> str:
    cursor.execute(f'SELECT max(supplies.date) FROM supplies WHERE product_id = (SELECT id FROM products WHERE name = \'{product}\');')
    return cursor.fetchall()[0][0]