#!/usr/bin/env bash
waldorna@waldorna-ThinkPad-E570 ~ $ erl
# Erlang/OTP 20 [erts-9.2] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:10] [kernel-poll:false]

# Eshell V9.2  (abort with ^G)

# Erlang Shell example of varianle assignment
1> OneVar = 123.
123
2> OneVar = 1234.
** exception error: no match of right hand side value 1234

# Per above, erlang only uses single assignment methods which can help with avoiding bugs
3> OneVar.
123
4> <


waldorna@waldorna-ThinkPad-E570 ~ $ erl
# Erlang/OTP 20 [erts-9.2] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:10] [kernel-poll:false]

# Eshell V9.2  (abort with ^G)

# Erlang uses algebraic processing for its expressions
1> aVar = 12.
** exception error: no match of right hand side value 12
2> _aVar = 12.
12
3> MyVar = 12.4.
12.4
4> MyVar = MyVar + 1.  # Error because 12.4 = 12.4 + 1 (Mathmatically this is false)
** exception error: no match of right hand side value 13.4
5> 12.4 = MyVar. # This is true
12.4
6> <


# Iterating in Erlang
6> L1 = [-5,-4,-3,-2,-1,0,1,2,3,4,5].
[-5,-4,-3,-2,-1,0,1,2,3,4,5]
7> c(lud).
{error,non_existing} # need to create a lud.erl file in directory
8> c(lud).
{ok,lud}
9> lud:addList(L1).
0
10> lud:addList([2,10,12,22]).
46
11> <

# Using the patternMatch code in lud.erl
waldorna@waldorna-ThinkPad-E570 ~ $ erl

1> c(lud).
{ok,lud}
2> lud:patternMatch(10).
10!ok
3> lud:patternMatch(20).
20!ok
4> lud:patternMatch(30).
Unkown!ok
5> lud:patternMatch(50).
Unkown!ok
6> q().


waldorna@waldorna-ThinkPad-E570 ~ $ erl
#Erlang/OTP 20 [erts-9.2] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:10] [kernel-poll:false]
#
#Eshell V9.2  (abort with ^G)

# Basic Function Examples - using 'b()' to print all active variables
# and f(). to clean all variable assignments or specified variables.

1> MyFloat = .987
1> MyFloat = .987.
* 1: syntax error before: '.'
1> MyFloat = 0.987.
0.987
2> 10 - 5.
5
3> 4.9 - 0.5.
4.4
4> W = 1.
1
5> B = 2.
2
6> b().
B = 2
MyFloat = 0.987
W = 1
ok
7> W - B.
-1
8> 2 = B.
2
9> f(MyFloat).
ok
10> f(MyFloat).
ok
11> b().
B = 2
W = 1
ok
12> f(doesNotExist).
** exception error: no function clause matching call to f/1
13> f(DoesNotExist).
ok
14> f().
ok
15> b().
ok
16> W - B.
* 1: variable 'W' is unbound
17>  <
