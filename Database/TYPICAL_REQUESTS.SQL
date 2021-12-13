--Поставщик для товара с именем ***
--SELECT name FROM providers WHERE id = (SELECT provider_id FROM products WHERE name = 'Redmi Note 10');

--Товары, произведённые в городе ***
--SELECT name FROM products WHERE producer_id IN (SELECT id FROM producers WHERE city_id = (SELECT id from cities WHERE name = 'Среднеколымск'));

--Пользователи, купившие последний товар не раньше даты ***
--SELECT name, surname FROM users WHERE id IN (SELECT DISTINCT user_id FROM purchases WHERE purchases.date >= '2021-08-01');

--Товар, купленный пользователем *** наибольшее число раз
/*
SELECT name
FROM products
WHERE id = (
	SELECT product_id from (
		SELECT product_id, max(goods) FROM (
			SELECT product_id, sum(amount) AS goods
			FROM purchases
			WHERE user_id = (SELECT id FROM users WHERE name = 'Екатерина' AND surname = 'Доронина')
			GROUP BY product_id
		)
	)
)
;
*/

--Страна поставщика ***
--SELECT name AS 'Страна' FROM countries WHERE id = (SELECT country_id FROM cities WHERE id = (SELECT city_id FROM providers WHERE name = 'TradeRockRetail'));

--Последняя поставка товара ***
--SELECT max(supplies.date) FROM supplies WHERE product_id = (SELECT id FROM products WHERE name = 'Флагман AF423');