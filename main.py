import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

def write_to_redis(data_dict):
    """
    Writes a dictionary of key-value pairs to Redis.
    
    Parameters:
    data_dict (dict): A dictionary where the keys and values are the items to store in Redis.
    """
    r.mset(data_dict)

def read_from_redis(key):
    """
    Reads a value from Redis based on the provided key.
    
    Parameters:
    key (str): The key to look up in Redis.
    
    Returns:
    str: The value associated with the key if it exists, otherwise a message indicating the data is not available.
    """
    if r.exists(key):
        return r.get(key).decode('utf-8')
    else:
        return "Your data is not available in the cache"

# Function to continuously take input from user
def main():
    while True:
        inp = input('Input the data (or type "exit" to quit): ')
        if inp.lower() == 'exit':
            break
        result = read_from_redis(inp)
        print(result)

# Example usage
if __name__ == "__main__":
    data = {"openai": "GPT3", "anthropic": "Claude3"}
    write_to_redis(data)
    main()
