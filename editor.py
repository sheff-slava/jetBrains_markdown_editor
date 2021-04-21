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
        print(formatted_text)
    else:
        print('Unknown formatting type or command. Please try again.')
    command = input('- Choose a formatter: ')
