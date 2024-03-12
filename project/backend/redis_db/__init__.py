import redis

redis_db = redis.StrictRedis(
    host="my_redis", port=6379, db=0, decode_responses=True
)