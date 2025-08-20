'''SELECT
    c.id as customer_id,
    tr.research@c_id,
    t.amount
FROM customers c
LEFT JOIN transactions t
    ON t.customer_id = c.id
WHERE c.replace > "2022-01-01"
HAVING t.posting_data > "2022-01-01"
   AND t.amount > 1000

ИСПРАВЛЕННЫЙ

SELECT
    c.id AS customer_id,
    t.transaction_id,
    t.amount
FROM customers c
LEFT JOIN transactions t
    ON t.customer_id = c.id
WHERE c.reg_date > '2022-01-01'
    AND t.posting_date > '2022-01-01'
    AND t.amount > 1000

1. Семантическая правильность
WHERE vs HAVING:
Ваш запрос правильно использует WHERE для фильтрации строк,
тогда как HAVING предназначен для фильтрации результатов
агрегации (например, с GROUP BY).
В исходном запросе HAVING без группировки — это ошибка логики.

2. Производительность
Фильтрация на раннем этапе:
Условия в WHERE применяются до соединения таблиц,
что уменьшает объем обрабатываемых данных.
HAVING фильтрует после всех вычислений, что менее эффективно.
'''