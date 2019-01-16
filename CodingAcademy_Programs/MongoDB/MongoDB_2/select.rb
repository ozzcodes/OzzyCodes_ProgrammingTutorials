require 'rubygems'
require 'mongo'

include Mongo

$client = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
$collection = $client[:someData]

$collection.find({"n" => {"$gt" => 205000} ,"code" => {"$lt" => 1}}).each do |doc|
  puts doc
end