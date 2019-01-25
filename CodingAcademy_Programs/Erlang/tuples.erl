%%%-------------------------------------------------------------------
%%% @author waldorna
%%% @doc
%%%
%%% @end
%%% Created : 24. Jan 2019 11:20 PM
%%%-------------------------------------------------------------------
-module(tuples).
%% API
-export([main/0]).

process_tuple(TUPLE) when is_tuple(TUPLE) ->
  N = tuple_size(TUPLE),
  W = element(1, TUPLE),
  io:format("Size: ~w First element: ~w ~n", [N, W]);

process_tuple(_) ->
  io:format('This is nor a tuple!~n').

main() ->
  T1 = {[1,2], 2, 3, 4, 5, 6},
  T2 = {a, b, c, d},
  process_tuple(T1),
  process_tuple(T2).
