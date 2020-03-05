import sys

from spider.og import find_title

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("python " + sys.argv[0] + " url")
        exit(1)

    link = sys.argv[1]

    result = find_title(link)
