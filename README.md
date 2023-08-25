# Вывод на карту ближайших кафе
Программа спрашивает местоположение(город) и в качестве результата выдает сайт с картой, на которой указаны 5 ближайших кафе из файла ```coffee.json```.
## Зависимости
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Переменные окружения
Для работы с ```main.py``` необходимо создать файл ```.env```, записав в него необходимые переменные.
```bash
YANDEX_APIKEY = "Уникальный токен от яндекс карт"
```

## Запуск
Запуск на Linux(Python 3) или Windows:
```bash
$ python main.py 
```