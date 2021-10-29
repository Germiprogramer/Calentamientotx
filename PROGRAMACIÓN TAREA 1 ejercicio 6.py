customer_basket_cost = 34
customer_basket_weight = 44

if customer_basket_cost > 100:
    precio_envio = 0
else:
    precio_envio = 1.2 * customer_basket_weight

coste_total = (customer_basket_cost + customer_basket_weight + precio_envio)
print(coste_total)

customer_basket_cost = 101
customer_basket_weight = 44

if customer_basket_cost > 100:
    precio_envio = 0
else:
    precio_envio = 1.2 * customer_basket_weight

coste_total = (customer_basket_cost + customer_basket_weight + precio_envio)
print(coste_total)