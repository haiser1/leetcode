class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        

    def pop(self) -> int:
        self._move_if_needed()  # Pindahkan elemen jika stack_out kosong
        return self.stack_out.pop() if self.stack_out else None
        

    def peek(self) -> int:
        self._move_if_needed()  # Pastikan stack_out memiliki elemen
        return self.stack_out[-1] if self.stack_out else None
        

    def empty(self) -> bool:
         return not self.stack_in and not self.stack_out  # Queue kosong jika kedua stack kosong
    
    def _move_if_needed(self):
        """Memindahkan elemen dari stack_in ke stack_out jika stack_out kosong"""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())  # Pindahkan elemen dari stack_in ke stack_out
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()