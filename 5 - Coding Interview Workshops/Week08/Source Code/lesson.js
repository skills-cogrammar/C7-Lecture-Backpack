class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
  }

  insert_at_beginning(data) {
    const new_node = new Node(data);
    new_node.next = this.head;
    this.head = new_node;
  }

  insert_at_end(data) {
    const new_node = new Node(data);
    if (this.head === null) {
      this.head = new_node;
      return;
    }
    let current = this.head;
    while (current.next) {
      current = current.next;
    }
    current.next = new_node;
  }

  insert_after(node, data) {
    const new_node = new Node(data);
    new_node.next = node.next;
    node.next = new_node;
  }

  delete_at_beginning() {
    if (this.head === null) {
      return;
    }
    this.head = this.head.next;
  }

  delete_at_end() {
    if (this.head === null) {
      return;
    }
    if (this.head.next === null) {
      this.head = null;
      return;
    }
    let current = this.head;
    while (current.next.next) {
      current = current.next;
    }
    current.next = null;
  }

  delete_node(node) {
    if (node === null || node.next === null) {
      return;
    }
    node.data = node.next.data;
    node.next = node.next.next;
  }

  search(data) {
    let current = this.head;
    while (current) {
      if (current.data === data) {
        return current;
      }
      current = current.next;
    }
    return null;
  }

  traverse() {
    let current = this.head;
    while (current) {
      console.log(current.data);
      current = current.next;
    }
  }
}

class DoublyLinkedListNode {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  insert_at_beginning(data) {
    const new_node = new DoublyLinkedListNode(data);
    new_node.next = this.head;
    if (this.head) {
      this.head.prev = new_node;
    } else {
      this.tail = new_node;
    }
    this.head = new_node;
  }

  insert_at_end(data) {
    const new_node = new DoublyLinkedListNode(data);
    if (this.tail === null) {
      this.head = new_node;
      this.tail = new_node;
      return;
    }
    new_node.prev = this.tail;
    this.tail.next = new_node;
    this.tail = new_node;
  }

  insert_after(node, data) {
    const new_node = new DoublyLinkedListNode(data);
    new_node.next = node.next;
    new_node.prev = node;
    if (node.next) {
      node.next.prev = new_node;
    } else {
      this.tail = new_node;
    }
    node.next = new_node;
  }

  delete_at_beginning() {
    if (this.head === null) {
      return;
    }
    this.head = this.head.next;
    if (this.head) {
      this.head.prev = null;
    } else {
      this.tail = null;
    }
  }

  delete_at_end() {
    if (this.tail === null) {
      return;
    }
    this.tail = this.tail.prev;
    if (this.tail) {
      this.tail.next = null;
    } else {
      this.head = null;
    }
  }

  delete_node(node) {
    if (node === null) {
      return;
    }
    if (node.prev) {
      node.prev.next = node.next;
    } else {
      this.head = node.next;
    }
    if (node.next) {
      node.next.prev = node.prev;
    } else {
      this.tail = node.prev;
    }
  }

  search(data) {
    let current = this.head;
    while (current) {
      if (current.data === data) {
        return current;
      }
      current = current.next;
    }
    return null;
  }

  traverse() {
    let current = this.head;
    while (current) {
      console.log(current.data);
      current = current.next;
    }
  }
}

function reverseLinkedList(head) {
  let prev = null;
  let current = head;
  while (current !== null) {
    const next_node = current.next;
    current.next = prev;
    prev = current;
    current = next_node;
  }
  return prev;
}

function detectLoop(head) {
  let slow = head;
  let fast = head;
  while (slow && fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      return true;
    }
  }
  return false;
}

function findMiddle(head) {
  let slow = head;
  let fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}

const chardet = require("chardet");
const fs = require("fs");

function detectEncoding(filePath) {
  const buffer = fs.readFileSync(filePath);
  return chardet.detect(buffer);
}

function convertEncoding(text, fromEncoding, toEncoding) {
  const buffer = Buffer.from(text, fromEncoding);
  return buffer.toString(toEncoding);
}

function normalizeUnicode(text, form = "NFC") {
  return text.normalize(form);
}

function caseFold(text) {
  return text.toLowerCase();
}

function replaceUnicodeCharacters(text, property, replacement) {
  const pattern = new RegExp(`\\p{${property}}`, "gu");
  return text.replace(pattern, replacement);
}
