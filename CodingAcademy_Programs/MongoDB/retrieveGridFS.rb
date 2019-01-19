require 'rubygems'
require 'mongo'

include Mongo

$client = Mongo::Client.new(['127.0.0.1:27017'], database: 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
$files = $client[:files]

# Upload a text file
fs = $client.database.fs
$file = File.open('connect.rb')
$file_id = fs.upload_from_stream('connect.rb', $file)
$file.close

# Download a file
$file_to_write = File.open('perfectCopy', 'w')
fs.download_to_stream($file_id, $file_to_write)
