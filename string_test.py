import redis

def connect_to_redis():
    return redis.Redis(host='localhost', port=6379, db=0)

def keys_pattern(r, pattern):
    return r.keys(pattern)

def set_key(r, key, value):
    r.set(key, value)

def get_key(r, key):
    return r.get(key)

def delete_key(r, key):
    r.delete(key)

def flush_all(r):
    r.flushall()

def setex_key(r, key, time, value):
    r.setex(key, time, value)

def ttl_key(r, key):
    return r.ttl(key)

def psetex_key(r, key, time_ms, value):
    r.psetex(key, time_ms, value)

def setnx_key(r, key, value):
    return r.setnx(key, value)

def strlen_key(r, key):
    return r.strlen(key)

def mset_keys(r, kv_dict):
    r.mset(kv_dict)

def incr_key(r, key):
    return r.incr(key)

def decr_key(r, key):
    return r.decr(key)

def incrby_key(r, key, amount):
    return r.incrby(key, amount)

def decrby_key(r, key, amount):
    return r.decrby(key, amount)

def append_key(r, key, value):
    return r.append(key, value)

def main():
    r = connect_to_redis()

    while True:
        print("\nChoose a command to execute:")
        print("1. keys *")
        print("2. get, set, del, flushall")
        print("3. setex, ttl, psetex")
        print("4. setnx")
        print("5. strlen")
        print("6. mset")
        print("7. decr, incr, incrby, decrby")
        print("8. append")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            pattern = input("Enter the pattern (e.g., 'user:*', 'session:?'): ")
            print(keys_pattern(r, pattern))
        elif choice == '2':
            action = input("Choose action (get/set/del/flushall): ")
            if action == 'set':
                key = input("Enter key: ")
                value = input("Enter value: ")
                set_key(r, key, value)
            elif action == 'get':
                key = input("Enter key: ")
                print(get_key(r, key))
            elif action == 'del':
                key = input("Enter key: ")
                delete_key(r, key)
            elif action == 'flushall':
                flush_all(r)
                print("All keys deleted.")
        elif choice == '3':
            action = input("Choose action (setex/ttl/psetex): ")
            if action == 'setex':
                key = input("Enter key: ")
                time = int(input("Enter expiration time (seconds): "))
                value = input("Enter value: ")
                setex_key(r, key, time, value)
            elif action == 'ttl':
                key = input("Enter key: ")
                print(ttl_key(r, key))
            elif action == 'psetex':
                key = input("Enter key: ")
                time_ms = int(input("Enter expiration time (milliseconds): "))
                value = input("Enter value: ")
                psetex_key(r, key, time_ms, value)
        elif choice == '4':
            key = input("Enter key: ")
            value = input("Enter value: ")
            print(setnx_key(r, key, value))
        elif choice == '5':
            key = input("Enter key: ")
            print(strlen_key(r, key))
        elif choice == '6':
            kv_dict = {}
            n = int(input("Enter the number of key-value pairs: "))
            for _ in range(n):
                key = input("Enter key: ")
                value = input("Enter value: ")
                kv_dict[key] = value
            mset_keys(r, kv_dict)
        elif choice == '7':
            action = input("Choose action (decr/incr/incrby/decrby): ")
            key = input("Enter key: ")
            if action == 'incr':
                print(incr_key(r, key))
            elif action == 'decr':
                print(decr_key(r, key))
            elif action == 'incrby':
                amount = int(input("Enter amount to increment by: "))
                print(incrby_key(r, key, amount))
            elif action == 'decrby':
                amount = int(input("Enter amount to decrement by: "))
                print(decrby_key(r, key, amount))
        elif choice == '8':
            key = input("Enter key: ")
            value = input("Enter value to append: ")
            append_key(r, key, value)
            print(get_key(r, key))
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
