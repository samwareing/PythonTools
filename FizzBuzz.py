class FizzBuzz:
    '''An extendable FizzBuzz.'''

    def run(self, n=101, tokens=((3, 'fizz'), (5, 'buzz'))) -> str:
        result = ''
        for i in range(1, n):
            current = ''
            for div, tok in tokens:
                current += (tok if (i % div == 0) else '')
            result += (f"{current if current else i}\n")
        return result


def main():
    tokens = ((3, 'fizz'), (5, 'buzz'), (10, 'plod'))
    n = 101
    print(FizzBuzz().run(n=n, tokens=tokens))


if __name__ == '__main__':
    main()
