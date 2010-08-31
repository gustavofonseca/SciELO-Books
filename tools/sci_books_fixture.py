from csv2json import csv2json

container = []

for i, item in enumerate(csv2json('banco_dados_livros.csv')):
    item_dict = eval(item)
    
    dict_editora = {"pk": i+1, 
        "model": "catalogo.editora", 
        "fields": {"nome": item_dict['editora']}}
                   
    del item_dict['editora']
    
    dict_livro = {"pk": i+1, "model": "catalogo.livro", "fields": item_dict}

         
    container.append(dict_livro)
    container.append(dict_editora)

print container