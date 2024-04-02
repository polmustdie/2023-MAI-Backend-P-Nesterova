from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        check = self.cache.get(key, None)
        if check:
            self.cache.move_to_end(key)
            print(check)
            return check
        else:
            return -1

    def set(self, key: str, value: str) -> None:
        check = self.cache.get(key, None)
        if check:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def rem(self, key: str) -> None:
        return self.set(key, "")


cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
cache.get('Jesse')  # вернёт 'James'
cache.rem('Walter')
cache.get('Walter')  # вернёт ''
