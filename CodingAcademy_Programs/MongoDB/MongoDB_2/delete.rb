require 'rubygems'
require 'mongo'

include Mongo

$client = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
puts 'connected!'

$users = $client[:someData]

result = $users.find(:name => 'Björk').delete_one
puts result.n


result = $users.find(:name => 'Björk').delete_many
puts result.n
