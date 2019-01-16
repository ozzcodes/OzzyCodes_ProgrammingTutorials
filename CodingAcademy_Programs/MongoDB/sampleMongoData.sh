#!/usr/bin/env bash

# Begin using mongo by entering 'mongo' in terminal
ozzycodes@ozzycodes-ML-LIQUID:~$ mongo
#MongoDB shell version v4.0.5
#connecting to: mongodb:
#Implicit session: session { "id" :}
#MongoDB server version: 4.0.5
#Server has startup warnings:
#2019-01-16T17:34:39.427-0500 I STORAGE  [initandlisten]
#2019-01-16T17:34:39.427-0500 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
#2019-01-16T17:34:39.427-0500 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
#2019-01-16T17:34:41.055-0500 I CONTROL  [initandlisten]
#2019-01-16T17:34:41.055-0500 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
#2019-01-16T17:34:41.055-0500 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
#2019-01-16T17:34:41.055-0500 I CONTROL  [initandlisten]
#---
#Enable MongoDBs free cloud-based monitoring service, which will then receive and display
#metrics about your deployment(disk utilization, CPU, operation statistics, etc).
#
#The monitoring data will be available on a MongoDB website with a unique URL accessible to you
#and anyone you share the URL with. MongoDB may use this information to make product
#improvements and to suggest MongoDB products and deployment options to you.
#
#To enable free monitoring, run the following command: db.enableFreeMonitoring()
#To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
#---

# Tell mongo which database to use:
> use LXF
switched to db LXF

# JavaScript code from the MongoDB shell:
> for(var i=0; i<1000; i++) { db.sampleData.insert({x:i, y:i/2}); }
WriteResult({ "nInserted" : 1 })

> db.sampleData.count();
1000

# To delete an entire data collection use 'drop'
> db.sampleData.drop();
true

> db.sampleData.count();
0

# Exit out of MongoDB shell by using Ctrl + D
>
bye
