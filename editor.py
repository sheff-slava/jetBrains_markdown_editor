formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']

command = input('- Choose a formatter: ')

while command != '!done':
    if command == '!help':
        print('Available formatters:', *formatters)
        print('Special commands: !help !done')
    elif command not in formatters:
        print('Unknown formatting type or command. Please try again.')
    command = input('- Choose a formatter: ')
