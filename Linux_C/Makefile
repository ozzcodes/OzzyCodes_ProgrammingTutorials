#target (what you wish to produce): what is needed to do so
	#how to produce

program: program.c weather.so
	gcc -std=c11 -Wall -fmax-errors=10 -Wextra program.c weather.so -o program

weather.so: weather.c weather.h
	gcc -std=c11 -Wall -fmax-errors=10 -Wextra -c weather.c -o weather.so

launch: program
	./program

