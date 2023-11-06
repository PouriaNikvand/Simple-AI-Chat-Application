import redis


class BaseRedisClient:
    """
    Using redis as a user caching method for loading Users data and expire the cache after a proper time
    """

    def __init__(self, host, port, db):
        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
        )

    def set(self, key, value):
        self.client.set(key, value)

    def multiple_set(self, key_value_dict):
        self.client.mset(key_value_dict)

    def get(self, key):
        return self.client.get(key)

    def multiple_get(self, keys_list):
        return self.client.mget(keys_list)


class InteractionsRedisClient(BaseRedisClient):
    def get_user(self, user_id: str):
        return self.get(user_id)

    def get_messages(self, interaction_ids: list):
        return self.multiple_get(interaction_ids)
