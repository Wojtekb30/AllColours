from PIL import Image  
r = 0
g = 0
b = 0
x = 0
y = 0
img  = Image.new( mode = "RGB", size = (4096,4096) )
while y<4096 and x<4096:
    img.putpixel((x,y), (r,g,b))
    x=x+1
    if x==4096:
        x=0
        y=y+1
    
    b=b+1
    if b>255:
        b=0
        g=g+1
    if g>255:
        g=0
        r=r+1

    print("XY: "+str(x)+ " "+str(y) + " Color: "+str(r)+" "+str(g)+" "+str(b))






img.save("AllColors.png")
print("Done")
