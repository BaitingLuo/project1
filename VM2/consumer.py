#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os   # need this for popen
import time # for sleep
from kafka import KafkaConsumer  # consumer of events
import json
import couchdb
# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I ehave on my local VMs
couch = couchdb.Server('http://admin:1251314qwe@127.0.0.1:5984/')
database = couch['weather']
# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
print("consumer start")
consumer = KafkaConsumer (bootstrap_servers="129.114.27.120:9092",value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# subscribe to topic
consumer.subscribe (topics=["utilizations"])
#file = open("consumer_output.txt", 'w')
# we keep reading and printing
for msg in consumer:
    # what we get is a record. From this record, we are interested in printing
    # the contents of the value field. We are sure that we get only the
    # utilizations topic because that is the only topic we subscribed to.
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    #
    # convert the value field into string (ASCII)
    #
    # Note that I am not showing code to obtain the incoming data as JSON
    # nor am I showing any code to connect to a backend database sink to
    # dump the incoming data. You will have to do that for the assignment.
    database.save(msg.value)
    #file = open("consumer_output.txt", 'a')
    #str = ""
    #for i in msg.value.items():
    #    str += i[0]
    #    str += ","
    #    str += i[1]
    #    str += ","
    #str += "\n"
    #file.write(str)
    #file.close()           
    #print (msg.value)
    time.sleep(1)

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close ()
    






