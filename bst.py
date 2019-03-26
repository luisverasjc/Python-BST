path = "found:" #Global variable for path string. This is needed due to use of recursion
def main():
    #initialize bst
    root = Node(None)
    #start taking input
    while True:
        try:
            s = input()
        except EOFError:
            return
        spl = s.split(" ")
        mode = spl[0]
        num = int(spl[1])
        if(mode == "i"):
           root.insert(num)
        elif(mode == "q"):
            root.query(num)
        else:
            print("Invalid input.")
            exit(1)

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None 
        self.right = None
    
    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if value == self.value: # Duplicate
                print("error: duplicate value")
                return
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

    def query(self, value, parent = None,):
        global path
        if value == self.value:
            if path == "found:":
                print("found: root")
                return
            else:
                print(path)
                path = "found:" # reset path string
                return
        elif value < self.value:
            if self.left is None:
                path = "not found"
                print(path)
                path = "found:" # reset path string
                return 
            path = path + " l"
            return self.left.query(value, self)
        elif value > self. value:
            if self.right is None:
                path = "not found"
                print(path)
                path = "found:" # reset path string
                return
            path = path + " r"
            return self.right.query(value, self)

if __name__ == '__main__':
    main()

