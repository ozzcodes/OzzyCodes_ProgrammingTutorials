#!/usr/bin/env bash

# Using Tuples and Guards types
waldorna@waldorna-ThinkPad-E570 ~$ erl
1> T1 = {linux, 2}.
{linux,2}
2> <

# Using the element() functions allows for access of given item in tuple
2> element(2, T1).
2
3> element(1, T1).
linux
4> <

# The setelement function allows you to change the value of an existing tuple item
5> T2 = setelement(1, T1, unix).
{unix,2}
6> <
