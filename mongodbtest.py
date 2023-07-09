import pymongo
client = pymongo.MongoClient("mongodb+srv://senthura_pandi:pandimads7@cluster0.jz4zkmg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"senthura",
    "email":"rvani1262@gmail.com",
    "age":"22"
}

d = {
    "name":"senthura",
    "email":"rvani1262@gmail.com",
    "age":"22"
}
d = {
    "name":"senthura",
    "email":"rvani1262@gmail.com",
    "age":"22"
}
d = {
    "name":"senthura",
    "email":"rvani1262@gmail.com",
    "age":"22"
}
d = {
    "name":"senthura",
    "email":"rvani1262@gmail.com",
    "age":"22"
}
d = {
    "name":"senthura",
    "email":"rvani1262@gmail.com",
    "age":"22"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)