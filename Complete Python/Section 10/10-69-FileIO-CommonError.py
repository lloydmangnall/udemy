import shelve

# a literal dictionary of books definition
# books = {'recipes': {'blt': ['bacon', 'lettuce', 'tomato', 'bread'],
#                     'bean on toast': ['beans', 'bread'],
#                     'scrambled eggs': ['eggs', 'butter', 'milk'],
#                     'soup': ['tin of soup'],
#                     'pasta': ['pasta', 'cheese']},
#         'maintenance': {'stuck': ['oil'],
#                         'loose': ['gaffer tape']}}

# shelve the dictionary of books items as individual key/value pairs
books = shelve.open('book')
books['recipes'] = {'blt': ['bacon', 'lettuce', 'tomato', 'bread'],
                    'bean on toast': ['beans', 'bread'],
                    'scrambled eggs': ['eggs', 'butter', 'milk'],
                    'soup': ['tin of soup'],
                    'pasta': ['pasta', 'cheese']}
books['maintenance'] = {'stuck': ['oil'],
                        'loose': ['gaffer tape']}

print(books['recipes']['soup'])
# print(books['recipes']['scrambled eggs'])
#
# print(books['maintenance']['loose'])
# shelve.close(books)
