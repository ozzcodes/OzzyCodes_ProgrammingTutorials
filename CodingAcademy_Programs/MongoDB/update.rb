require 'rubygems'
require 'mongo'

include Mongo

$client = Mongo::Client.new(['127.0.0.1:27017'], database: 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
$collection = $client[:someData]

# Updating documents with the 'update_many()' function
result = $collection.find('n' =>
                               { '$gt' => 205_000 }).update_many(
                                 '$inc' => { code: 10 }
                               )
# The next command returns the number of documents,
# that were updated
puts result.n
