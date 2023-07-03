from tkinter import*

root = Tk()
root.title('Drag using mouse')
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=20)

# Add Image or shape to Canvas
img = PhotoImage(file="c:/KK.jpg")
my_image = my_canvas.create_image(260,125,image=img)
my_rectangle =  my_canvas.create_rectangle(50, 150, 250, 50, fill="red")
#Move
def move(e):
    #e.x
    #e.y
    global img
    img = PhotoImage(file="c:/KK.jpg")
    my_image = my_canvas.create_image(260, 125, image=img)
    my_label.config(text="coordinates: x " + str(e.x) + " y: " + str(e.y))

my_label = Label(root, text="")
my_label.pack(pady=20)

my_canvas.bind('<B1-Motion>', move)
#root.bind("<Left>", left)
#root.bind("<Right>", right)
#root.bind("<Up>", up)
#root.bind("<Down>", down)

root.mainloop()
