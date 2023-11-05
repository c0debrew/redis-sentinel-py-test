# redis-sentinel-py-test
Minimal example to verify how Redis sentinel works. When the current master goes down, Redis Sentinel is expected to route the existing connection to the new master automatically without needing to re-initiate the Redis client.

## How to run
In the example, the Python script will output the IP and the port of the current connected Redis instances.

Redis server instances:
- redis-master
- redis-slave1
- redis-slave2

```bash
# Initialize Redis instances
docker-compose up

# Redis instance can be killed using
docker-compose stop redis-master

# Redis instance can be started using
docker-compose start
```
