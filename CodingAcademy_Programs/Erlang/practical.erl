-module(practical).
-export([fib/1, fibtailrec/1]).

fib(0) -> 0;
fib(1) -> 1;
fib(N) -> fib(N - 2) + fib(N - 1).

fibtailrec(N) -> fibtailrecwork(N, 2, 1, 2).

fibtailrecwork(0, _, _, _) -> 1;
fibtailrecwork(1, _, _, _) -> 1;
fibtailrecwork(N, N, _, Accum) -> Accum;
fibtailrecwork(N, Cur, Prev, Accum) -> fibtailrecwork(N, Cur + 1, Accum, Prev + Accum).
