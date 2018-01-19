# Описание
Репозиторий иллюстрирует пример реализации map-reduce из книжки [Эффективный питон: 59 советов](https://www.amazon.com/Effective-Python-Specific-Software-Development/dp/0134034287) (совет 24)

Чтобы проверить работу map-reduce, выполните:
```shell
./count_words.py
```

В файле [transform_example.py](transform_example.py) добавлена простая реализация map-reduce воркера `Transformer`, который применяет произвольную трансформирующую функцию к последовательности, которую возвращает reader. В качестве примера показано, как выполнить трансформацию из класса CountVectorizer.
Чтобы проверить работу трансформера, запустите из командной строки
```shell
./transform_example.py
```
