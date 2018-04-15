Globbing or Wildcards ::::::::::::::::::::::::::::::::::::::::::::::::::::: 

# Так как имена файлов используются в командной оболочке повсеместно, она 
# поддерживает специальные символы, помогающие быстро определять группы 
# имен файлов. Эти специальные символы называют групповыми символами 
# (wildcards). Групповые символы (также известны как символы подстановки 
# (globbing)) позволяют выбирать имена файлов по шаблону.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

*
# Любая последовательность любых символов

?
# Любой один символ

[символы]
# Любой один символ из указанного множества символов

[!символы] 
# Любой один символ, не принадлежащий указанному множеству символов

[[:класс:]]
# Любой один символ, принадлежащий указанному классу

[:alnum:] 
# Любой алфавитно-цифровой символ

[:alpha:] 
# Любой алфавитный символ

[:digit:] 
# Любой цифровой символ

[:lower:] 
# Любая буква в нижнем регистре

[:upper:] 
# Любая буква в верхнем регистре




# example ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

*
# Все имена файлов

g*
# Все имена файлов, начинающиеся с символа «g»

b*.txt
# Все имена файлов, начинающиеся с символа «b», за которым следует любое 
# число других символов, и заканчивающиеся на «.txt»

Data???
# Все имена файлов, начинающиеся с символов «Data», за которыми следуют 
# ровно три любых символа

[abc]*
# Все имена файлов, начинающиеся с символа «a», «b» или «c»

BACKUP.[0-9][0-9][0-9] 
# Все имена файлов, начинающиеся с символов «BACKUP.», за которыми следуют 
# ровно три цифровых символа

[[:upper:]]* 
# Все имена файлов, начинающиеся с буквы в верхнем регистре

[![:digit:]]* 
# Все имена файлов, не начинающиеся с цифры

*[[:lower:]123] 
# Все имена файлов, заканчивающиеся буквой в нижнем регистре или цифрой 
# «1», «2» или «3»
