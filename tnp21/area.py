def area(l,w,bw):
    inn_len=l-2*bw
    inn_wid=w-2*bw
    ar=inn_len*inn_wid
    t_ar=l*w
    br_ar=t_ar-ar
    print("The inner area is",ar)
    print("The Border area is",br_ar)
l=int(input("Enter the Length"))
w=int(input("Enter the width"))
bw=int(input("enter the brick width"))
area(l,w,bw)