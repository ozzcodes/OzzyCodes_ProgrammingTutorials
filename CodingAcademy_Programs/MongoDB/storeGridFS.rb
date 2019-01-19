require 'rubygems'
require 'mongo'

include Mongo

$client = Mongo::Client.new(['127.0.0.1:27017'], database: 'LXF')

fs = $client.database.fs
$file = File.open('image.png')
$file_id = fs.upload_from_stream('image.png', $file)
$file.close

# To create a file with raw data and insert it
file = Mongo::Grid::File.new('I am a NEW file stored in GridFS',
                             filename: 'aFile.txt')
$client.database.fs.insert_one(file)
