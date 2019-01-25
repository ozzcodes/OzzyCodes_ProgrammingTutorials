%%%-------------------------------------------------------------------
%%% @author waldorna
%%% @doc
%%%
%%% @end
%%% Created : 24. Jan 2019 11:28 PM
%%%-------------------------------------------------------------------

%% Using more_fun:check_temp/1
-module(more_fun).
%% API
-export([check_temp/1]).

check_temp(Temp) ->
  case Temp of
    {celcius, N} when N >= 20, N =< 45 ->
      'Hot';
    {celcius, N} when N >= 46 ->
      'Way too hot!';
    {celcius, N} when N =< 19 ->
      'It iss getting cold...';
    {kelvin, N} ->
      'Cannot tell about Kelvin';
    {farenheit, N} ->
      'Do no know about Farenheit';
    _ ->
      'what!?'
  end.
