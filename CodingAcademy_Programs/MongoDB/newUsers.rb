require 'rubygems'
require 'mongo'

include Mongo

$client = Mongo::Client.new(['127.0.0.1:27017'], database: 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
$collection = $client[:someData]

# Adding/ creating users using the Ruby MongoDB Driver
$client.database.users.create(
  'linuxFormat',
  password: 'aPassword',
  roles: [Mongo::Auth::Roles::READ_WRITE]
)
