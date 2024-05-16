from starbase import Connection

print("Creating connection object....")
conn = Connection("127.0.0.1","8001")
print("Created connection object....")

table_name = 'ratings'
ratings = conn.table(table_name)

if (ratings.exists()):
    print(f"Dropping existing {table_name}")
    ratings.drop()

ratings.create('rating')

print(f"Parsing the ml-100k {table_name} data...")
local_file_path = "C:\\Users\krant\Downloads\ml-100k\\u.data"
ratingFile = open(local_file_path,'r')

batch = ratings.batch()

for line in ratingFile:
    (user_id, movie_id, rating, time_stamp) = line.split()
    batch.update(user_id, {'rating':{movie_id:rating}})

ratingFile.close()

print("committing ratings data to HBase via REST...")
batch.commit(finalize=True)

print("Getting Back ratings for some users....")
print("Rating for user id 1: ")
print(ratings.fetch("1"))
print("Rating for user id 2: ")
print(ratings.fetch("34"))