# Class String Reverse

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

print(py_solution().reverse_words('This is a reverse word'))
