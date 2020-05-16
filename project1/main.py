#import project1.package1 as p1
import package1 as p1
import random
import pandas as pd
import matplotlib as plt
plt.use('Agg')

def main():
    print("Hello World")

    df = pd.DataFrame([], columns=list("XYZ"))

    a = p1.A("Keith")
    
    for i in range(0,10):
        #a.move(p1.A.VECTOR_NORTH, 2)
        a.move(random.choice(p1.A.VALID_VECTORS), random.randint(1,3))
        df2 = pd.DataFrame([list(a.pos)], columns=list("XYZ"))
        df = df.append(df2, ignore_index=True)

    print(df)
    df.plot()

    print(str(a))

    b = p1.B("Jack")
    print(str(b))

    exit(0)


if __name__ == "__main__":
    main()