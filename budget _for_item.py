prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0


for index,each in enumerate(prices):
    if each <= budget_per_item:
        affordable_items.append(items[index])
        total_needed+=prices[index]
    else:
        cant_afford+=1    
# Write your code below
# print(prices)


print("prices",prices)
print("items",items)
print("budget per item",budget_per_item)
print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)

#10,25,5,15
#hammer,saw,nails,brush
#12