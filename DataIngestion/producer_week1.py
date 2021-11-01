from kafka import KafkaProducer
import time
import requests
import json
import random
import http.client, urllib.parse


def rapidapiNews():
    """ headers={
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': "46d0252e20mshbe78ec870a908ffp17fd9fjsn5a9d73d5f4e8"
    }
    key_words = []
    querystring = {"q": "sports", "lang": "en"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    global dataset
    new = response.json() """

    conn=http.client.HTTPConnection('api.mediastack.com')

    params=urllib.parse.urlencode({
        'access_key': 'd0f0e1dbdf31d3ef5f48132f1ab3d936',
        'categories': 'technology',  # allowed categories(general,sports,health,science,technology,business,entertainment)
        'sort': 'published_desc',
        'limit': 100,
    })

    conn.request('GET', '/v1/news?{}'.format(params))
    global dataset
    res = conn.getresponse()
    new = res.read()
    a = json.loads(new)
    dataset = a["data"]


def producer_def(dataset, hostname='localhost', port='9092',
                 topic_name='news',
                 nr_messages=2,
                 max_waiting_time_in_sec=60):
    # Function for Kafka Producer with certain settings related to the Kafka's Server
    producer = KafkaProducer(
        bootstrap_servers=hostname + ":" + port, api_version=(0, 10),
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
    )
    j = 0
    j = len(dataset)
    for i in dataset:
        print("Sending data to DB: {}".format(i))
        # print(i)
        producer.send(topic_name, i)
        # Sleeping time
        time.sleep(1)
        # Force flushing of all messages
        if (j % 100) == 0:
            producer.flush()
        j = j + 1

    producer.close()


rapidapiNews()
producer_def(dataset)
