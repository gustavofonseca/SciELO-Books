import csv
import json

def csv2json(f):
    '''
    Returns an iterable object, in json format, based on a given csv file.
    '''

    csv_dict = csv.DictReader(open(f))
    #if to_file:
    #    file_handler = open('out.json', 'w')

    for dict_row in csv_dict:        
        yield json.dumps(dict_row)
    
        #if to_file:
        #    json.dump(dict_row, file_handler, indent=2)
        
    #if file_handler: file_handler.close()
    
