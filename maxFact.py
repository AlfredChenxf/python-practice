__author__ = 'Alfred'


def showMaxFactor(num):
    count = num/2
    while count > 1:
        if num % count == 0:
            print "Largest factor of %d is %d" % (num, count)
            break
        count -= 1
    else:
        print num, "is a prime"

if __name__ == '__main__':
    for x in range(10, 34):
        showMaxFactor(x)