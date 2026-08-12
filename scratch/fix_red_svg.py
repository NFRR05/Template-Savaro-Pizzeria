with open(r'c:\DEV\Template Savaro\assets\lines.svg', 'r', encoding='utf-8') as f:
    text = f.read()

red_text = text.replace('stroke="white"', 'stroke="#FE120F"')

with open(r'c:\DEV\Template Savaro\assets\lines-red.svg', 'w', encoding='utf-8') as f:
    f.write(red_text)

print('Updated lines-red.svg successfully!')
