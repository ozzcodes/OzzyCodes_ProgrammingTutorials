require 'rubygems'
require 'mongo'

include Mongo

$client = Mongo::Client.new(['127.0.0.1:27017'], database: 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
$collection = $client[:someData]

# Using the 'find' function to query someData collections of the LXF,
# database and select documents that match certain criteria
$collection.find('n' => { '$gt' => 205_000 }, 'code' =>
    { '$lt' => 1 }).each(&method(:puts))
