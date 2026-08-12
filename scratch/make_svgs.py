import os

in_file = r'c:\DEV\Template Savaro\assets\lines.svg'
out_white = r'c:\DEV\Template Savaro\assets\lines-white.svg'
out_red = r'c:\DEV\Template Savaro\assets\lines-red.svg'

with open(in_file, 'r', encoding='utf-8') as f:
    content = f.read()

with open(out_white, 'w', encoding='utf-8') as f:
    f.write(content)

content_red = content.replace('fill="white"', 'fill="#FE120F"').replace('stroke="white"', 'stroke="#FE120F"')

with open(out_red, 'w', encoding='utf-8') as f:
    f.write(content_red)

print('SVG files created successfully!')
