# Using Redis with Python

## Introduction

Redis is an in-memory data structure store used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, sorted sets, and more. This guide will help you get started with using Redis in Python.

## Installation Steps

1. **Install the Redis Python Client**
   
   To interact with Redis from Python, you'll need the `redis` package. Install it using pip:
   ```sh
   pip install redis

2. **Run the Redis Server**

   Ensure you have Redis installed on your system. If it's not already installed, you can download and install it from the [official Redis website](https://redis.io/download). Once installed, start the Redis server with the following command:
   ```sh
   redis-server
   
3. **Check Redis Server Status**

   Open another terminal window and use the Redis command line interface (CLI) to check if the server is running:
   ```sh
   redis-cli ping

If the server is running, it should respond with: PONG

## Redis Functions

Here are some commonly used Redis functions:

- **SET key value**: Set the value of a key.
- **GET key**: Get the value of a key.
- **DEL key**: Delete a key.
- **EXISTS key**: Check if a key exists.
- **INCR key**: Increment the integer value of a key by one.
- **LPUSH key value**: Insert a value at the head of the list stored at key.
- **LRANGE key start stop**: Get a range of elements from a list.
- **HSET key field value**: Set the string value of a hash field.
- **HGET key field**: Get the value of a hash field.
- **HDEL key field**: Delete one or more hash fields.

These functions can be executed using the Redis command line interface (CLI) or through a Redis client library such as `redis-py` in Python.

Here is a simple example of how to use Redis with Python:

```python
import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('06892', 'Hussain')

# Get the value of a key
value = r.get('06892')
print(value)  # Output should be b'Hussain'


