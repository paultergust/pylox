import sys


class Scanner:

    def __init__(self, source=None):
        self.src = source

    def run_prompt(self):
        a = ''
        while a is not None:
            try:
                a = input('>')
            except EOFError:
                exit(0)
            # just print tokens for now
            print(a.split())

    def run_file(self, filename):
        file = self.open_file(filename)
        tokens = file.readlines()
        # print tokens for now
        for token in tokens:
            print(token)

    def run(self):
        # run from src file
        if self.src is not None:
            self.run_file(self.src)
        # if no src file is provided, run as prompt/interpreter
        else:
            self.run_prompt()

    def open_file(self, filename):
        return open(filename, 'r')


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else None
    scanner = Scanner(src)
    scanner.run()
