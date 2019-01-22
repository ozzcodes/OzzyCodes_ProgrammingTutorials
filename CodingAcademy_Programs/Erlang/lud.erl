%%%-------------------------------------------------------------------
%%% @author waldorna
%%% @doc
%%%
%%% @end
%%% Created : 22. Jan 2019 3:50 PM
%%%-------------------------------------------------------------------
-module(lud).

%% API
-export([addList/1, addList/2, patternMatch/1]).

%% Add List Items
addList([]) -> 0;
addList(List) -> addList(List, 0).
addList([], Total) -> Total;
addList([Head | Tail], Total) -> addList(Tail, Total + Head).


%% Pattern Match
patternMatch(Number) ->
  case Number of
    10 -> io:fwrite("10!");
    20 -> io:fwrite("20!");
    _ -> io:fwrite("Unkown!")
  end.