class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Link_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        self.head = Node(data, self.head)

    def print(self):
        sos = self.head
        while sos:
            print(sos.data)
            sos = sos.next

    def reverse(self):
        prev = None
        sos = self.head
        while (sos is not None):
            next = sos.next
            sos.next = prev
            prev = sos
            sos = next
        self.head = prev

if __name__ == "__main__":
    lis = Link_list()
    lis.append(4)
    lis.append(5)
    lis.append(9)

    lis.print()
    print("Reverse link list")
    lis.reverse()
    lis.print()
