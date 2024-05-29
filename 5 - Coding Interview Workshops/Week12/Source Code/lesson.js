const { Worker, isMainThread, workerData } = require("worker_threads");
const Mutex = require("async-mutex").Mutex;

// Locks and Mutexes
if (isMainThread) {
  const sharedData = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT);
  const lock = new Int32Array(sharedData);

  const worker = new Worker(__filename, { workerData: { sharedData } });
} else {
  const { sharedData } = workerData;
  const lock = new Int32Array(sharedData);

  Atomics.wait(lock, 0, 0);
  // Access shared resources
  Atomics.notify(lock, 0, 1);
}

// Semaphores
if (isMainThread) {
  const sharedData = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT);
  const semaphore = new Int32Array(sharedData);

  const worker1 = new Worker(__filename, { workerData: { sharedData } });
  const worker2 = new Worker(__filename, { workerData: { sharedData } });
} else {
  const { sharedData } = workerData;
  const semaphore = new Int32Array(sharedData);

  Atomics.sub(semaphore, 0, 1);
  // Access shared resources
  Atomics.add(semaphore, 0, 1);
}

// Condition Variables
if (isMainThread) {
  const sharedData = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT);
  const condition = new Int32Array(sharedData);

  const producerWorker = new Worker(__filename, {
    workerData: { sharedData, role: "producer" },
  });
  const consumerWorker = new Worker(__filename, {
    workerData: { sharedData, role: "consumer" },
  });
} else {
  const { sharedData, role } = workerData;
  const condition = new Int32Array(sharedData);

  if (role === "producer") {
    Atomics.store(condition, 0, 1);
    Atomics.notify(condition, 0, 1);
  } else if (role === "consumer") {
    Atomics.wait(condition, 0, 0);
    // Consume data
  }
}

// Scheduling Algorithms
function roundRobin(processes, quantum) {
  const readyQueue = [];
  processes.forEach((process) => readyQueue.push(process));

  while (readyQueue.length > 0) {
    const process = readyQueue.shift();
    // Execute process for the given quantum
    // If process is not finished, put it back in the queue
    if (!process.isFinished()) {
      readyQueue.push(process);
    }
  }
}

function priorityScheduling(processes) {
  const readyQueue = [];
  processes.forEach((process) => readyQueue.push(process));

  readyQueue.sort((a, b) => a.priority - b.priority);

  while (readyQueue.length > 0) {
    const process = readyQueue.shift();
    // Execute process until completion or preemption
  }
}

// Interview-Style Questions
let instance = null;
const lock = new Mutex();

class Singleton {
  constructor() {
    if (!instance) {
      lock.acquire();
      if (!instance) {
        instance = this;
      }
      lock.release();
    }
    return instance;
  }
}

class ConcurrentQueue {
  constructor() {
    this._queue = [];
    this._lock = new Mutex();
    this._condition = new Condition(this._lock);
  }

  put(item) {
    this._lock.acquire();
    this._queue.push(item);
    this._condition.notify();
    this._lock.release();
  }

  get() {
    this._lock.acquire();
    while (this._queue.length === 0) {
      this._condition.wait();
    }
    const item = this._queue.shift();
    this._lock.release();
    return item;
  }
}

class ReaderWriterLock {
  constructor() {
    this._readLock = new Mutex();
    this._writeLock = new Mutex();
    this._readers = 0;
  }

  acquireRead() {
    this._readLock.acquire();
    this._readers++;
    if (this._readers === 1) {
      this._writeLock.acquire();
    }
    this._readLock.release();
  }

  releaseRead() {
    this._readLock.acquire();
    this._readers--;
    if (this._readers === 0) {
      this._writeLock.release();
    }
    this._readLock.release();
  }

  acquireWrite() {
    this._writeLock.acquire();
  }

  releaseWrite() {
    this._writeLock.release();
  }
}
