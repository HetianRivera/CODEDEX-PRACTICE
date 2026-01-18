dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_found = False

while item_found != True:
    item_to_find = input('Ingresa 3 Letras: ')
    for item in dna_sequence:
        if item_to_find == item:
            item_found = True
    if item_found == True:
        print("Item Found!")
    else:
        print("Item not found.")