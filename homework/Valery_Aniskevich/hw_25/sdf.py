c = {"car": "Citroen", "computer": "HP", "phone": "Iphone", "watch": "Rolex"}
a = [f"{key} {value}" for key, value in c.items()]
print(type(a[0]))
print(a[0])
