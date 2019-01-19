require 'rubygems'
require 'mongo'

include Mongo

client = Mongo::Client.new(['127.0.0.1:27017'], database: 'LXF')
collection = client[:someData]

# List all the indexes of the someData collection,
# belonging to the LXF database
def method_name(index)
  p index
end

collection.indexes.each(&method(:method_name))
