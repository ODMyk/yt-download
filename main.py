from sys import exit
from os import rename
import pafy

print("Хотите скачать видео или аудио с YouTube? Просто введите URL ниже...")
url = input("Введите URL: ")

print("Что-бы скачать видео введите: 1 | Что-бы скачать аудио введите: 2 ")
choice = input("Введите цифру: ")

print("Теперь укажите полный путь к директории, в которую нужно скачать файл. Пример: E:\\Downloads")
directory = input("Введите путь: ")

try:
	v = pafy.new(url)

	if choice == "1":
	    streams = v.streams
	elif choice == "2":
	    streams = v.audiostreams
	else:
	    print("Некорректный ввод.")
	    exit()

	print("Выберите желаемое качество видеоролика передав цифру. Пример: 1 ") if choice == "1" else print("Выберите желаемое качество аудио передав цифру. Пример: 2 ")

	available_streams = {}
	count = 1

	for stream in streams:
	    available_streams[count] = stream
	    print(f"{count}: {stream}")
	    count += 1

	stream_count = int(input("Введите номер: "))
	d = streams[stream_count - 1].download(filepath = directory)

	print("Скачивание успешно завершено!")
except:
   print("Упс... Проверьте данные")
