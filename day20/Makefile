a: a.c
	clang -o a a.c -Wall -Wextra -Wpedantic --std=c11 -O3

b: a.c
	clang -o b a.c -Wall -Wextra -Wpedantic --std=c11 -O3 -DITERATIONS=50

c: a.c
	clang -o c a.c -Wall -Wextra -Wpedantic --std=c11 -O3 -fopenmp -DITERATIONS=1000