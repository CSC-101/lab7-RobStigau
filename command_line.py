import sys

def main()->float:
    tot = 0
    for value in sys.argv:
        try:
            tot += float(value)
        except ValueError:
            continue
    return tot

if __name__ == '__main__':
    print(main)
    print(sys.argv)

