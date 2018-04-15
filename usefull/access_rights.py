access rights ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# 

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

1  2   3   4
- rwx rw- r--
# 1 тип файла
# 2 привилегии для владельца
# 3 привилегии для группы
# 4 привилегии для всех остальных



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Типы файлов

-
# Обычный файл

d
# Каталог

l
# Символическая ссылка. Обратите внимание, что для символических ссылок все 
# остальные атрибуты имеют значение rwxrwxrwx и не отражают действительные 
# права доступа. Фактические права доступа к файлу определяются атрибутами 
# самого файла, на который указывает символическая ссылка

c
# Специальный файл символьного устройства. Файлы этого типа соответствуют 
# устройствам, таким как терминал или модем, которые обрабатывают данные как 
# потоки байтов

b
# Специальный файл блочного устройства. Файлы этого типа соответствуют 
# устройствам, таким как привод жесткого диска или CD-ROM, которые обрабатывают 
# данные блоками



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Атрибуты прав доступа

r
# Файлы
# Разрешается открывать и читать содержимое файла 

# Каталоги
# Разрешается читать содержимое каталога, если вместе с этим атрибутом 
# установлен атрибут права на выполнение


w
# Файлы
# Разрешается записывать в файл или усекать его; однако этот атрибут не дает 
# права переименовывать и удалять файлы. Возможность переименования и удаления 
# файлов определяется атрибутами вмещающего каталога

# Каталоги
# Разрешается создавать, удалять и переименовывать файлы внутри каталога, если 
# вместе с этим атрибутом установлен атрибут права на выполнение


x
# Файлы
# Разрешается интерпретировать файл как программу и выполнять ее. Файлы, 
# содержащие программы на языках сценариев, дополнительно должны быть доступны 
# для чтения, иначе они не будут выполняться

# Каталоги
# Разрешается входить в каталог, то есть выполнять команду cd для перехода в 
# него



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Режимы доступа к файлу в двоичном и восьмеричном представлениях

0     000     ---
1     001     --x
2     010     -w-
3     011     -wx
4     100     r--
5     101     r-x
6     110     rw-
7     111     rwx



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Символическая форма записи аргументов команды chmod

u
# Сокращенно от user (пользователь), означает владельца файла или каталога

g
# Группа

o
# Сокращенно от other (другие, остальные), означает весь остальной мир

a
# Сокращенно от all (все); комбинация из всех трех символов: u, g и o
