require 'rubygems'
require 'mongo'

include Mongo

client = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'LXF')
collection = client[:someData]

collection.indexes.each do |index|
  p index
end