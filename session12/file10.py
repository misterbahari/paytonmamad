import hashlib

res = hashlib.sha1(b'8585')

res2 = hashlib.md5(b'8585')
print(res)
print(res.digest())
print(res.hexdigest())

print(res2)
print(res2.digest())
