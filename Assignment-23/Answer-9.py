def tringleExsists_tringlePerimeter(tringlePerimeter):
    def tringleExsists(l):
        first_side, second_side, third_side = tuple(l)
        if (first_side + second_side >= third_side) and (third_side + second_side >= first_side) and (third_side + first_side >= second_side):
            print(" Tringle Exsists")
            print("Perimeter of Given Tringle is:",tringlePerimeter(l))
        else:
            print("Tringle Not Exsists")
    return tringleExsists

@tringleExsists_tringlePerimeter
def tringlePerimeter(l):
    frist_side,second_side,third_side=tuple(l)
    return frist_side + second_side + third_side


tringlePerimeter([int(e) for e in input("Enter Sides Of Tringle seprated by Comma: ").split(",")])