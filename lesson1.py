import torch
import random
from pudb import set_trace
num_entries = 50
db = torch.rand(num_entries) > 0.5  # uniform
print('db:', db)


def db_drop_index(db, i):
    return torch.cat((db[:i], db[i+1:]))

def create_parallel_dbs(num_entries):
    db = torch.rand(num_entries) > 0.5  # uniform
    pdbs = []
    for i in range(len(db)):
        pdb = db_drop_index(db, i)
        pdbs.append(pdb)
    return db, pdbs

def query(db):
    return db.sum()

print('sum', query(db))
# set_trace()
full_db_results = query(db)
print('full db', full_db_results)

db, pdbs = create_parallel_dbs(num_entries)
# print(pdbs)
print('length', len(pdbs))
print('length of one parallel db', len(pdbs[random.randint(0, num_entries - 1)]))

print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))
print(query(pdbs[random.randint(0, num_entries - 1)]))


full_db_result = query(db)
max_distance = 0
for pdb in pdbs:
    pdb_result = query(pdb)
    db_distance = torch.abs(full_db_result - pdb_result)
    print('db_distance', db_distance)
    if db_distance > max_distance:
        max_distance = db_distance

print('max_distance', max_distance)
