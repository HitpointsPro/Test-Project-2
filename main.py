import os

def main():
    pass

if __name__ == "__main__":
    main()

# Создаем директорию .dist, если она не существует
os.makedirs('.dist', exist_ok=True)

# Генерируем index.html
with open('.dist/index.html', 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html>\n<html>\n<head>\n    <title>Простой сайт</title>\n    <link rel="stylesheet" href="style.css">\n</head>\n<body>\n    <h1>Добро пожаловать на мой сайт!</h1>\n    <script src="script.js"></script>\n</body>\n</html>')

# Генерируем style.css
with open('.dist/style.css', 'w', encoding='utf-8') as f:
    f.write('body {\n    font-family: Arial, sans-serif;\n    background-color: #f0f0f0;\n    color: #333;\n    padding: 20px;\n} \
h1 {\n    color: #007BFF;\n} \
')

# Генерируем script.js
with open('.dist/script.js', 'w', encoding='utf-8') as f:
    f.write('alert("Добро пожаловать на простой сайт!");')

print('Веб-сайт успешно создан в папке .dist')
