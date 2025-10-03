x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
chess1 = (x1+y1)%2
chess2 = (x2+y2)%2
if chess1 == chess2:
    print("YES")
    if chess1 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")