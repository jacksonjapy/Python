"""
Write By Jackson
"""


if __name__ == '__main__':
    path1 = r"test1.txt"
    path2 = r"test2.txt"

    with open(path1, 'r') as f1, open(path2, 'w') as f2:
        f2.write(f1.read())
