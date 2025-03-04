import sys


class Scanner:

    def __init__(self, source=None):
        if source is not None:
            self.run_file(source)
        else:
            self.run_prompt()

    def run_prompt(self):
        a = ''
        while a is not None:
            a = input('>')
            self.run(a)

    def run_file(self, filename):
        file = self.open_file(filename)
        self.run(file)

    def run(self, src):
        for token in self.read_tokens(src):
            print(token)

    def read_tokens(self, line):
        tokens = line.split()
        return tokens

    def open_file(self, filename):
        return open(filename, 'r')


if __name__ == '__main__':
    src = sys.argv[1]
    scanner = Scanner(src)
    scanner.run()
