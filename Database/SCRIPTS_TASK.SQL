update users set birth_date = substr(birth_date, 7, 4) || '-' || substr(birth_date, 4, 2) || '-' || substr(birth_date, 1, 2);
update users set sign_up_date = substr(sign_up_date, 7, 4) || '-' || substr(sign_up_date, 4, 2) || '-' || substr(sign_up_date, 1, 2);
update supplies set date = substr(date, 7, 4) || '-' || substr(date, 4, 2) || '-' || substr(date, 1, 2);
update purchases set date = substr(date, 7, 4) || '-' || substr(date, 4, 2) || '-' || substr(date, 1, 2);

select email from users where sign_up_date = (select max(sign_up_date) from users);

select DISTINCT substr(birth_date, 1, 4) as by1 from users order by by1;

select sum(amount) as total_items from products;

select
	avg(
		CAST(substr(date('now'), 1, 4) AS INT)-CAST(substr(birth_date, 1, 4) AS INT)+
		CASE
			WHEN substr(date('now'), 6, 2) < substr(birth_date, 6, 2) THEN -1
			WHEN substr(date('now'), 6, 2) = substr(birth_date, 6, 2) THEN
				CASE
					WHEN substr(date('now'), 9, 2) < substr(birth_date, 9, 2) THEN -1
					ELSE 0
				END
			ELSE 0
		END
	) AS 'Average age'
from users where sign_up_date >= '2021-08-24';