import math

class Triangle(object):
    def __init__(self,name:str, side_a:float,side_b:float,side_c:float):
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area_Gerona(self):
        p = float((self.side_a + self.side_b + self.side_c) / 2)
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def real_triangle(self):
        if self.side_a + self.side_b > self.side_c and self.side_a + self.side_c > self.side_b and\
            self.side_b + self.side_c > self.side_a > 0 and self.side_b > 0 and self.side_c > 0:
            return True
        else: return False


def input_values():
    while(True):
        triangle_name = input("Enter name of triangle:")
        side_a = float(input("Enter value of side a:"))
        side_b = float(input("Enter value of side b:"))
        side_c = float(input("Enter value of side c:"))
        return triangle_name,side_a,side_b,side_c

def main():
    all_triangles = {}
    while(True):
        input_triangle = input_values()
        triangle = Triangle(*input_triangle)
        if(triangle.real_triangle()):
            all_triangles[input_triangle[0]]= triangle.area_Gerona()
        continue_work = input("Do you want to continue?").lower()
        if continue_work != "y":
            break
    list_triangles = list(all_triangles.items())
    list_triangles.sort(key=(lambda i: i[1]), reverse=True)
    for i in list_triangles:
        print(i[0], ':', i[1])

if __name__ == '__main__':
    main()
