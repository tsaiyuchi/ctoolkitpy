


from typing import List


items: List[int] = []
for idx in range(30):
    items.append(int(idx))


print(len(items))
for idx in range(31):
    if(items):
        print(items.pop(0))
print(len(items))


