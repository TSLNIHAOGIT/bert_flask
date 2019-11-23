from collections import namedtuple
Account = namedtuple("Account", ["name","pwd"])
# account = Account(*("bingyang", "123456"))
account = Account(name="bingyang",pwd= "123456")
print(account.name)
# 'bingyang'
print(account.pwd)
# '123456'