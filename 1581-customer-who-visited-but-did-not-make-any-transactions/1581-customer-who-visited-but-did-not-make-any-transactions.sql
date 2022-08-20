SELECT Visits.customer_id, 
count(*) AS count_no_trans 
FROM Visits 
LEFT JOIN 
Transactions ON Visits.visit_id = Transactions.visit_id 
WHERE Transactions.visit_id IS null
GROUP BY customer_id;