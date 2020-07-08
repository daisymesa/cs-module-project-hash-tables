class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        str_bytes = key.encode()

        hash_total = 5381

        for b in str_bytes:
            hash_total = ((hash_total << 5) + hash_total) + b
            hash_total &= 0xffffffff

        return hash_total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # index = self.hash_index(key)
        # self.size += 1
        # self.storage[index] = HashTableEntry(key, value)
        # return None

        # Find the hash index
        # Search the list for the key
        # If it's there, replace the value
        # If it's not, append a new item to the list

        index = self.hash_index(key)
        current = self.storage[index]

        if current is not None:
            # loop to search the list for the key
            while current is not None:
                if current.key == key:
                    # If it's there, replace the value
                    current.value = value
                    break

                current = current.next
            # If it's not there, append a new record to the list
            else:
                new_node = HashTableEntry(key, value)
                new_node.next = self.storage[index]
                self.storage[index] = new_node

        else:
            self.storage[index] = HashTableEntry(key, value)

        # when load factor goes above 0.7, automatically rehash to double its size
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)

        return None

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # self.size -= 1
        # self.put(key, None)
        # return None

        # Find the hash index
        # Search the list for the key
        # If found, delete form the list
        # Else, return None

        # Find the hash index
        index = self.hash_index(key)

        # Search the list for the key
        current = self.storage[index]
        # while current is not None
        while current is not None:
            # if found, delete node from list
            if current.key == key:
                current.value = None
                break
            current = current.next

        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index = self.hash_index(key)

        # if self.storage[index] is not None:
        #     return self.storage[index].value

        # return self.capacity[index]

        # Find the hash index
        index = self.hash_index(key)

        # Search the list for the key
        current = self.storage[index]
        # while current is not None
        while current is not None:
            # if found, return node from list
            if current.key == key:
                return current.value
            current = current.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # 1. make new, bigger table / array
        # 2. go through all old elements, hash into new list

        # make new, bigger table / array
        old_storage = self.storage
        self.storage = [None] * new_capacity

        # go through all old elements + hash into new list
        for current in old_storage:
            if current is not None and current.next is None:
                self.put(current.key, current.value)
            if current is not None and current.next is not None:
                while current.next is not None:
                    self.put(current.key, current.value)
                    current = current.next
                self.put(current.key, current.value)

        return None


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
