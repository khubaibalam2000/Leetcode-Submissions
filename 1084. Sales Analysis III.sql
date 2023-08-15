select product_id, product_name from product where product_id not in (
    select product.product_id from product join sales on product.product_id = sales.product_id where sale_date < '2019-01-01' or sale_date > '2019-03-31'
) and product_id in (select product_id from sales)