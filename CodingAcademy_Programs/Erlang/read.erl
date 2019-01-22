%%%-------------------------------------------------------------------
%%% @author waldorna
%%% @doc
%%%
%%% @end
%%% Created : 22. Jan 2019 4:15 PM
%%%-------------------------------------------------------------------
-module(read).

%% API
-export([readLines/1, process_line/1]).

readLines(FileName) ->
  {ok, Device} = file:open(FileName, [read]),
  try process_line(Device)
  after file:close(Device)
  end.


process_line(Device) ->
  io:fwrite(".").