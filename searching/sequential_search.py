class SequentialSearchST:

    class Node:

        def __init__(self, key, value, next):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self):
        self.first = None

    def put(self, key, value):
        # check if key already exists in entries
        current = self.first
        while current:
            if current.key == key:
                current.value = value
                return

            current = current.next

        # search miss, add new entry
        new_entry = self.Node(key, value, self.first)
        self.first = new_entry

    def get(self, key):
        current = self.first
        while current:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def delete(self, key):
        current = self.first
        while current:
            if current.key == key:
                current.value = None
                break

    def keys(self):
        keys = []
        current = self.first
        while current:
            keys.append(current.key)
            current = current.next

        return keys


def main():
    symbol_table = SequentialSearchST()
    for value, key in enumerate("searchexample"):
        symbol_table.put(key, value)

    for key in symbol_table.keys():
        print(f"{key} : {symbol_table.get(key)}")


if __name__=="__main__":
    main()
