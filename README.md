# x64 NASM starter code

[По сути форк этого проекта с уже мёртвым сайтом](https://github.com/whiteeagle44/x86-nasm-starter-code) 
1. Лично я дописал makefile чтобы можно было пользоваться сишными процедурами
2. Что-то ещё

1. Для запуска нужен linux (либо wsl)
2. `sudo apt-get install nasm`
3. `sudo apt-get install make`
4. Запустить команду make в проекте

После этих действий скомпилируется программа programm

Для отладки рекомендую использовать vs code с плагином nasm, и плагин lldb. Также потребуется сам lldb ибо gdb ни на одной у меня линукс машине под x64 архитектуру взлетать не хотел

`sudo apt-get install lldb`
