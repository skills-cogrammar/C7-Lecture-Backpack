import threading
import queue

# Locks and Mutexes
lock = threading.Lock()

def critical_section():
    lock.acquire()
    try:
        # Access shared resources
        pass
    finally:
        lock.release()

# Semaphores
semaphore = threading.Semaphore(2)

def resource_access():
    semaphore.acquire()
    try:
        # Access shared resources
        pass
    finally:
        semaphore.release()

# Condition Variables
condition = threading.Condition()
data_available = False

def producer():
    global data_available
    with condition:
        data_available = True
        condition.notify()

def consumer():
    with condition:
        while not data_available:
            condition.wait()
        # Consume data

# Scheduling Algorithms
def round_robin(processes, quantum):
    ready_queue = queue.Queue()
    for process in processes:
        ready_queue.put(process)

    while not ready_queue.empty():
        process = ready_queue.get()
        # Execute process for the given quantum
        # If process is not finished, put it back in the queue
        if not process.is_finished():
            ready_queue.put(process)

def priority_scheduling(processes):
    ready_queue = queue.PriorityQueue()
    for process in processes:
        ready_queue.put((process.priority, process))

    while not ready_queue.empty():
        _, process = ready_queue.get()
        # Execute process until completion or preemption

# Interview-Style Questions
class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

class ConcurrentQueue:
    def __init__(self):
        self._queue = []
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)

    def put(self, item):
        with self._lock:
            self._queue.append(item)
            self._condition.notify()

    def get(self):
        with self._lock:
            while not self._queue:
                self._condition.wait()
            return self._queue.pop(0)

class ReaderWriterLock:
    def __init__(self):
        self._read_lock = threading.Lock()
        self._write_lock = threading.Lock()
        self._readers = 0

    def acquire_read(self):
        with self._read_lock:
            self._readers += 1
            if self._readers == 1:
                self._write_lock.acquire()

    def release_read(self):
        with self._read_lock:
            self._readers -= 1
            if self._readers == 0:
                self._write_lock.release()

    def acquire_write(self):
        self._write_lock.acquire()

    def release_write(self):
        self._write_lock.release()