import math

def input_triangle():
    input_param = input("Input triagle name and it's 3 sides through the ',':")
    input_param=input_param.split(',')
    return input_param

def real_triangle(a,b,c):
    if a+b > c and a+c > b and b+c >a> 0 and b> 0 and c> 0:
        return True
    else:
        print("Enter correct value\n")
        input_triangle()

def sq_Gerona(side1, side2, side3):
    p = float((side1 +side2 +side3)/2)
    return math.sqrt(p*(p-side1)*(p-side2)*(p-side3))



def main():
    triangles = {}
    while(True):
        triangle = input_triangle()
        print(triangle[3])
        if(real_triangle(float(triangle[1]),float(triangle[2]),float(triangle[3]))):
            area = sq_Gerona(float(triangle[1]),float(triangle[2]),float(triangle[3]))
            triangles[triangle[0]] = area
        cont = input("Do you want to continue:").lower()
        if (cont != 'y'): break
    list_triangles = list(triangles.items())
    list_triangles.sort(key=(lambda i: i[1]),reverse=True)
    for i in list_triangles:
        print(i[0], ':', i[1])

    
if __name__ == '__main__':
    main()

