select user_id as 'buyer_id', join_date, ifnull(count(order_id),0) as 'orders_in_2019'
from users left join orders on users.user_id = orders.buyer_id 
and order_date >= '2019-01-01' group by user_id