list_ = ["banana", "mouse", "nothing"]
print(f"normal list: {list_}")
# adding new elements:
list_.append("name")
print(f"append:{list_}")

list_.insert(1, "hello")
print(f"insert:{list_}")

list_.extend(["1","a","2","b"])
print(f"extend:{list_}")
# deleting elements:
list_.remove("banana")
print(f'remove:{list_}')

removed = list_.pop(1)
print(f'pop {list_} + returns: {removed}')
