import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["resume"]

# myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mycol = mydb["sites"]

collist = mydb. list_collection_names()
# collist = mydb.collection_names()
if "sites" in collist:   # 判断 sites 集合是否存在
    print("集合已存在！")