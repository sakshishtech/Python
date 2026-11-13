
import time


class TTLCache:

    def __init__(self):
        self.cache = {}

    def put(self, key, value, ttl):
        expiry_time = time.time() + ttl
        self.cache[key] = (value, expiry_time)

    def get(self, key):
        if key not in self.cache:
            return None

        value, expiry_time = self.cache[key]

        if time.time() >= expiry_time:
            del self.cache[key]
            return None

        return value

    def evict(self):
        current_time = time.time()

        for key in list(self.cache):
            if current_time >= self.cache[key][1]:
                del self.cache[key]
