new_dictionary = {
    'string': 'Hello python',
    'int': 23253464,
    'boolean': True,
    'list': ['Lists', True, False],
    'float': 3324.454,
    'nested-dict': {
        'nest-list': [
            {
                'hello' : 'how are you',
                'list-two': ['Hi', 'Hello'],
                'hello': 'duplicate keys'
            }
        ]
    }
}

for key in new_dictionary:
    print('Keys', key)
    print('values', new_dictionary[key])