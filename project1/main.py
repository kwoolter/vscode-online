#import project1.package1 as p1
import package1 as p1


def main():
    print("Hello World")

    a = p1.A("Keith")
    a.move()
    print(str(a))

    b = p1.B("Jack")
    print(str(b))

    exit(0)


if __name__ == "__main__":
    main()