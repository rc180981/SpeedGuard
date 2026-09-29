import re

with open('d:/FAJAR Apps/speed-violation-app/initial_data_126.js', 'r', encoding='utf-8') as f:
    js_initial = f.read()

with open('d:/FAJAR Apps/speed-violation-app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace STORAGE_KEY to force fresh reload of 126 records
html = html.replace("const STORAGE_KEY = 'puninar_v2';", "const STORAGE_KEY = 'puninar_v3_126';")
html = html.replace("let nextId = 18;", "let nextId = 127;")
html = html.replace("nextId=p.nextId||18;", "nextId=p.nextId||127;")
html = html.replace("nextId = 18;", "nextId = 127;")

# Replace INITIAL array
pattern = r'const INITIAL = \[[\s\S]*?\];'
html = re.sub(pattern, js_initial, html, count=1)

with open('d:/FAJAR Apps/speed-violation-app/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('SUCCESS: Updated index.html with 126 records!')
