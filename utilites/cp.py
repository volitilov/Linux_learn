cp ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# копирует файлы и котологи

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-a, --archive
# Скопировать файлы и каталоги со всеми атрибутами, включая идентификаторы 
# владельцев и права доступа. Без этого параметра копии обычно получают 
# значения атрибутов по умолчанию, определенных для пользователя, 
# выполняющего копирование

-i, --interactive
# Запрашивать у пользователя подтверждение перед пере­записью существующего 
# файла. Если этот параметр отсутствует, команда 'cp' просто перезапишет 
# существующие файлы

-r, --recursive
# Рекурсивно копировать каталоги и их содержимое. Это обязательный параметр 
# (или параметр -a) при копировании каталогов

-u, --update
# При копировании файлов из одного каталога в другой копировать только 
# файлы, отсутствующие в каталоге назначения или более новые

-v, --verbose
# Выводить информационные сообщения в процессе копирования





# example ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

cp file1 file2 
# Скопирует file1 в file2. Если file2 существует, он будет затерт новым 
# файлом file1. Если file2 отсутствует, он будет создан

cp -i file1 file2 
# То же, что и выше, но если файл file2 существует, у пользователя будет 
# запрошено подтверждение перед перезаписью файла

cp file1 file2 dir1 
# Скопирует file1 и file2 в каталог dir1. Каталог dir1 должен существовать

cp dir1/* dir2 
# С использованием группового символа. Скопирует все файлы из каталога 
# dir1 в каталог dir2. Каталог dir2 должен существовать

cp -r dir1 dir2 
# Скопирует каталог dir1 (и все его содержимое) в каталог dir2. Если 
# каталог dir2 не существует, он будет создан и заполнен содержимым 
# каталога dir1

