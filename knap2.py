def knap(cap,items):
    items.sort(key=lambda x : x[1]/x[0], reverse=True)
    tvalue=0

    for w,v in items:
        if cap>=w:
            tvalue+=v
            cap-=w
        else:
            tvalue+=v*(cap/w)
            break
    return tvalue

cap=int(input("capacity of bag:"))
n=int(input("enter no of items:"))

items = []
for i in range(n):
    w = float(input(f"Enter weight of item {i+1}: "))
    v = float(input(f"Enter value of item {i+1}: "))
    items.append((w, v))

print(items)
maxvalue=knap(cap,items)
print("maxvalue of the bag is:",maxvalue)

    
#O(nlogn)+O(n)
#O(n)





# capacity of bag: 50
# enter no of items: 3
# Enter weight of item 1: 10
# Enter value of item 1: 60
# Enter weight of item 2: 20
# Enter value of item 2: 100
# Enter weight of item 3: 30
# Enter value of item 3: 120
