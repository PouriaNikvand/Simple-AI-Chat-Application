import redis


class BaseRedisClient:
    """
    Using redis as a user caching method for loading Users data and expire the cache after a proper time
    """

    def __init__(self, configs):
        self.redis_client = redis.Redis(
            host=configs["redis"]["host"],
            port=configs["redis"]["port"],
            db=configs["redis"]["db"],
        )

    def set(self, key, value):
        self.redis_client.set(key, value)

    def multiple_set(self, key_value_dict):
        self.redis_client.mset(key_value_dict)

    def get(self, key):
        return self.redis_client.get(key)

    def multiple_get(self, keys_list):
        return self.redis_client.mget(keys_list)
