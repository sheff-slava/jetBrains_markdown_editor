def bold(text):
    return f'**{text}**'


def italic(text):
    return f'*{text}*'


def inline_code(text):
    return f'`{text}`'


def link(label, url):
    return f'[{label}]({url})'


def header(level, text):
    if 1 <= level <= 6:
        return '#' * level + ' ' + text
    else:
        return -1


def ordered_list(*rows):
    output = str()
    for index, row in enumerate(rows):
        output = output + f'{index + 1}. {row}' + '\n'
    return output


def unordered_list(*rows):
    output = str()
    for index, row in enumerate(rows):
        output = output + f'* {row}' + '\n'
    return output


formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
formatted_text = str()
command = input('- Choose a formatter: ')

while command != '!done':
    if command == '!help':
        print('Available formatters:', *formatters)
        print('Special commands: !help !done')
    elif command in formatters:
        if command == 'plain':
            p = input('- Text: ')
            formatted_text = formatted_text + p
        if command == 'bold':
            b = bold(input('- Text: '))
            formatted_text = formatted_text + b
        if command == 'italic':
            i = italic(input('- Text: '))
            formatted_text = formatted_text + i
        if command == 'inline-code':
            ic = inline_code(input('- Text: '))
            formatted_text = formatted_text + ic
        if command == 'header':
            h = header(int(input('- Level: ')), input('- Text: '))
            while h == -1:
                print('The level should be within the range of 1 to 6')
                h = header(int(input('- Level: ')), input('- Text: '))
            formatted_text = formatted_text + h + '\n'
        if command == 'link':
            l = link(input('- Label: '), input('- URL: '))
            formatted_text = formatted_text + l
        if command == 'new-line':
            formatted_text = formatted_text + '\n'
        if command == 'ordered-list':
            n = int(input('- Number of rows: '))
            while n <= 0:
                print('The number of rows should be greater than zero')
                n = int(input('- Number of rows: '))
            row_list = list()
            for i in range(n):
                row_list.append(input(f'- Row #{i + 1}: '))
            ol = ordered_list(*row_list)
            formatted_text = formatted_text + ol
        if command == 'unordered-list':
            n = int(input('- Number of rows: '))
            while n <= 0:
                print('The number of rows should be greater than zero')
                n = int(input('- Number of rows: '))
            row_list = list()
            for i in range(n):
                row_list.append(input(f'- Row #{i + 1}: '))
            ul = unordered_list(*row_list)
            formatted_text = formatted_text + ul
        print(formatted_text)
    else:
        print('Unknown formatting type or command. Please try again.')
    command = input('- Choose a formatter: ')

with open('output.md', 'w') as file:
    file.write(formatted_text)
