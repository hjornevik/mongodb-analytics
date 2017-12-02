from pymongo import MongoClient
import pprint

# Replace XXXX with your connection URI from the Atlas UI
client = MongoClient("mongodb://analytics:analytics-password@mflix-shard-00-00-ycjfo.mongodb.net:27017,mflix-shard-00-01-ycjfo.mongodb.net:27017,mflix-shard-00-02-ycjfo.mongodb.net:27017/mflix?ssl=true&replicaSet=mflix-shard-0&authSource=admin")

print(client.mflix)

db = client.mflix
collection = db.movies_initial
posts = db.posts


print(db.collection_names(include_system_collections=False))

## find one post based on objectID
#pprint.pprint(collection.find_one())
#{u'_id': ObjectID('5a23052fd8539356b3e61bb3'),
# }

pprint.pprint(collection.find_one({"title": "The Big Short", "runtime": "130 min"}))