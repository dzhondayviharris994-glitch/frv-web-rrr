import os

# Содержимое файла
content = '''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>INFO</title>
<link rel="stylesheet" href="www.css">
</head>
<body>

<div class="anime-info">
  <h1>FORVERUNU'S CORP.</h1>

  <div class="field">
    <div class="label"><b>Название сериала:</b></div>
    <div class="value"></div>
  </div>

  <div class="field">
    <div class="label"><b>Краткая рецензия:</b></div>
    <div class="value"></div>
  </div>

  <div class="field">
    <div class="label"><b>Оценка (от 1 до 10):</b></div>
    <div class="rating"></div>
  </div>

  <button class="back-button" onclick="history.back()">Вернуться</button>
</div>

<div class="container">
  <div class="image-panel">
    <img class="qe" src="" alt="Картинка">
  </div>
   <div class="image-panel">
    <img class="qw" src="" alt="Картинка">
  </div>
</div>
</body>
</html>'''

folder_path = r"C:\Пользователи\Общие\django-website"

os.makedirs(folder_path, exist_ok=True)

for i in range(3, 201):
    filename = f"serial{i}.html"
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Создан файл: {file_path}")

print("Все файлы успешно созданы!")