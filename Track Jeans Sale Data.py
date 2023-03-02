stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("Hit jeans sales target:")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock:")
print(in_stock)

#Used knowledge of number equality. Application compares jeans_sold with target and check if thar are jeans still in stock.
