from datetime import datetime
from elasticsearch import Elasticsearch

# By default we connect to localhost:9200
es = Elasticsearch()

# Datetimes will be serialized...
es.index(index="my-index-000001", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})


# ...but not deserialized
es.get(index="my-index-000001", doc_type="test-type", id=42)['_source']