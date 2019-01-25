#!/usr/bin/env bash

# Using cat to display the hw.erl file code
waldorna@waldorna-ThinkPad-E570 ~ $ cat hw.erl
%%%-------------------------------------------------------------------
%%% @author waldrona
%%% @doc
%%%
%%% @end
%%% Created : 24. Jan 2019 10:30 PM
%%%-------------------------------------------------------------------

%% Hello World program
-module(hw).
%% API
-export([helloWorld/0]).

helloWorld() ->
  io:fwrite("Hello, world!").

# Creating the hw.beam file by compiling hw.erl using erlc:
waldorna@waldorna-ThinkPad-E570 ~ $ erlc hw.erl

# Running the hw.beam compiled file in the linux terminal
waldorna@waldorna-ThinkPad-E570 ~ $ erl -V -noshell -s hw helloWorld -s init stop
Hello, world!

# Using thr Erl shell to compile the code in the hw.erl file
waldorna@waldorna-ThinkPad-E570 ~ $ erl

1> c(hw).
{ok,hw}

2> hw:helloWorld().
Hello, world!ok
3> <
