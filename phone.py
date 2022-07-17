from Class import phone, Tablet

iphone = phone("iphone", False, 5.5, "1000$")
samsung = phone("samsung", True, 5, "950$")
Note = Tablet("Samsung", True, 5, "950$", "Black")

print(iphone.model)
print(samsung.model)

print(iphone.is_touch)
print(samsung.price)

print(iphone.is_touchtable())
print(samsung.is_touchtable())

print(Note.model)
print(Note.color)