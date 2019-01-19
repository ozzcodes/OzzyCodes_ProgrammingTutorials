require 'rubygems'
require 'mongo'

include Mongo

$client = Mongo::Client.new(['127.0.0.1:27017'], database: 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
$collection = $client[:someData]

500.times do |n| # loop 500 times, using n as the iterator
  doc = {
      username: 'LinuxFormat',
      code: rand(4), # random value max is 4 (0 - 3) inclusive

      time: Time.now.utc,
      n: n * n

  }
  $collection.insert_one(doc)
end
