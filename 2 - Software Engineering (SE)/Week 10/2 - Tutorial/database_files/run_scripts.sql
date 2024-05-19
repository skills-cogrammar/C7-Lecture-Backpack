select orders.order_id, orders.product_id, orders.quantity, customers.customer_name,
customers.customer_address, products.product_name, orders.order_date
from orders
inner join customers on orders.customer_id = customers.customer_id
inner join products on orders.product_id = products.product_id
where customers.customer_id = 100;