#.append() metodo para anadir un item al final de la lista
#.insert() metodo para anadir un item en un lugar especifico
#.remove() metodo para eliminar un item de la lista basado en un valor
#.pop() metodo para remover el item en la posicion indicada
#.clear() Metodo para remover todo lo de la lista
#.copy() Devuelve la lista
#.count() Devuelve el numero de veces que aparece un valor en la lista
#.index() Devuelve el indice del valor dentro de la lista
#.reverse() Invierte los lugares de la lista
#.sort() Ordena la lista

#ejemplo

# dna = ['AUG','AUC','UCG']
# print(dna)
# dna.append('UAA')
# print(dna)
# dna.insert(2, 'GAU')
# print(dna)
# dna.remove('AUC')
# print(dna)
# dna.pop(0)
# print(dna)

#ejercicio
# Let's start a book club by making a list of popular books! 📚

# Create a reading_list.py program that stores the following items in a books list:

#     'Harry Potter'
#     '1984'
#     'The Fault in Our Stars'
#     'The Mom Test'
#     'Life in Code'

# Suppose we want to add 'Pachinko' to the list. Can you use a list method to do so?

# Let's say we finished reading 'The Fault in Our Stars' and '1984'. Can you use the .remove() method to remove one and the .pop() method to remove the other?

# Print the updated list out to make sure everything's good to go!

books = [
    'Harry Potter',
    '1984',
    'The Fault in Our Stars',
    'The Mom Test',
    'Life in Code'
]

books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)
print(books)