#-Array: Es una estructura de datos que permite almacenar una colección 
#de elementos del mismo tipo u diferente tipo.
#-Son la forma más flexible de "array" en Python, ya que no requieren 
#que todos los elementos sean del mismo tipo. 
#- Son dinámicas: puedes agregar(append()), eliminar(pop()) 
# elementos fácilmente después de su creación. 

#El append()método agrega un elemento al final de la lista.

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)

#El index() método devuelve la posición en la primera aparición 
# del valor especificado.

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

#El remove() método elimina la primera aparición 
#del elemento con el valor especificado.


fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)


#El extend()método agrega los elementos de lista especificados (o cualquier iterable) al final de la lista actual.

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

#El reverse()método invierte el orden de clasificación de los elementos.

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)