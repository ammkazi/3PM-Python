# Adding methods in list

list = ["BMW", "Porsche", "Volvo", "Toyota"]

print(list)

list.append("Audi") # add object to the end of the list
print(list)

list.insert(2, "Pagani")    # Insert object at a specified index
print(list)

list.extend("Spiderman") # Append multiple objects together
print(list)

list = list + ["Wonderman"]
print(list)


items = []
items.append([1, 2])
print(items)
