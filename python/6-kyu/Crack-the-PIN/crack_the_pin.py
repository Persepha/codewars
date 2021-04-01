from hashlib import md5

def crack(hash):
    hash_table = {md5(f'{x:0>5}'.encode()).hexdigest() : f'{x:0>5}' for x in range(100000)}
    return hash_table.get(hash)
