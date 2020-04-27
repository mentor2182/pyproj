def sumation(*kwargs):
    addition = 0;
    for i in kwargs:
        addition += i
    return addition

def sumation1(*kwargs):
    addition = 0;
    for i in kwargs:
        addition += i
    return addition

def main():
    print (sumation(1, 2))
    print (sumation1(1, 2, 5))

if __name__ == '__main__':
    main()