import random
from threading import Thread, Lock

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lock = Lock()

    def add(self, data):
        with self.lock:
            new_node = Node(data)
            if self.head is None:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

    def remove(self):
        with self.lock:
            if self.head is None:
                return None
            data = self.head.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return data


class Producer(Thread):
    def __init__(self, linked_list, max_size):
        super().__init__()
        self.linked_list = linked_list
        self.max_size = max_size

    def run(self):
        while True:
            new_data = random.randint(1, 100)
            if self.linked_list.lock.acquire(blocking=False):
                if len(self.linked_list) < self.max_size:
                    self.linked_list.add(new_data)
                    print(f"Producer added {new_data}")
                else:
                    print(f"Producer waiting, list full")
                self.linked_list.lock.release()
            else:
                print(f"Producer waiting for lock")


class Consumer(Thread):
    def __init__(self, linked_list):
        super().__init__()
        self.linked_list = linked_list

    def run(self):
        while True:
            if self.linked_list.lock.acquire(blocking=False):
                data = self.linked_list.remove()
                if data is not None:
                    print(f"Consumer removed {data}")
                else:
                    print(f"Consumer waiting, list empty")
                self.linked_list.lock.release()
            else:
                print(f"Consumer waiting for lock")


if __name__ == "__main__":
    linked_list = LinkedList()
    max_size = 5

    producer = Producer(linked_list, max_size)
    consumer = Consumer(linked_list)

    producer.start()
    consumer.start()
