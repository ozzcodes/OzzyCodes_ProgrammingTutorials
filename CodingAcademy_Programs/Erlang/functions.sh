#!/usr/bin/env bash

# Using functions in Erlang
waldorna@waldorna-ThinkPad-E570 ~ $ Erl
1> F=fun(X) -> 2*X end.
#Fun<erl_eval.6.99386804>
2> <

# The previous function has one anonymous functions with the variable F (atom):
2> F(4).
8
3> F(4.5).
9.0
4> <

waldorna@waldorna-ThinkPad-E570 ~ $ Erl

# Passing a  function as argument to another function:
1> F=fun(X) -> 2*X end.
#Fun<erl_eval.6.99386804>

2> Five = fun(N, Function) -> 5 * Function(N) end.
#Fun<erl_eval.12.99386804>
3> Five(10, F).
100

4> F(10).
20
5> <


# More Functions for Erlang
waldorna@waldorna-ThinkPad-E570 ~ $ erl

# Using the tuples.erl code, executing it within the erl shell:
1> c(tuples).
{ok,tuples}
2> tuples:main().
Size: 6 First element: [1,2]
Size: 4 First element: a
ok
3> <

# More function example for erl
waldorna@waldorna-ThinkPad-E570 ~/OzzyCodes_ProgrammingTutorials/CodingAcademy_Programs/Erlang $ erl

# Using the tuple.erl code
1> c(tuples).
{ok,tuples}
2> tuples:main().
Size: 6 First element: [1,2]
Size: 4 First element: a
ok

# Using the more_fun.erl code
3> c(more_fun).
more_fun.erl:22: Warning: variable 'N' is unused
more_fun.erl:24: Warning: variable 'N' is unused
{ok,more_fun}
4> more_fun:check_temp({farenheit, 50)}.
* 1: syntax error before: ')'
4> more_fun:check_temp({farenheit, 50}).
'Do no know about Farenheit'
5> more_fun:check_temp([kelvin, 50]).
'what!?'
6> more_fun:check_temp({celcius, 50}).
'Way too hot!'
7> more_fun:check_temp({celcius, 10}).
'It iss getting cold...'
8>


