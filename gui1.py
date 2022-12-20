from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from techniques import *
import cv2


def Grayscale(path):
    img = cv2.imread(path)
    new_img = gray_scale(img)
    cv2.imwrite(".tmp/tmpImg.png", new_img)
    image_path = ".tmp/tmpImg.png"
    new_img = Image.open(image_path)
    new_img = new_img.resize((450, 500), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(new_img)
    lbl1.configure(image=new_img)
    lbl1.image = new_img

def Blur(path, value):
    if not value:
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    else:
        img = cv2.imread(path)
        try:
            value = int(value)
            new_img = median_blur(img, value)
        except:
            messagebox.showinfo("Error", "please enter a positive odd number.")
            return
        cv2.imwrite(".tmp/tmpImg.png", new_img)
        image_path = ".tmp/tmpImg.png"
        new_img = Image.open(image_path)
        new_img = new_img.resize((450, 500), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(new_img)
        lbl1.configure(image=new_img)
        lbl1.image = new_img

def Thresholding(path, value):
    if not value:
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    else:
        img = cv2.imread(path)
        try:
            value = int(value)
            new_img = thresholding(img, value)
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        cv2.imwrite(".tmp/tmpImg.png", new_img)
        image_path = ".tmp/tmpImg.png"
        new_img = Image.open(image_path)
        new_img = new_img.resize((450, 500), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(new_img)
        lbl1.configure(image=new_img)
        lbl1.image = new_img

def EdgeDetection(path, value):
    if not value:
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    else:
        img = cv2.imread(path)
        try:
            value = int(value)
            new_img = sobel_edge_detection(img, value)
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        cv2.imwrite(".tmp/tmpImg.png", new_img)
        image_path = ".tmp/tmpImg.png"
        new_img = Image.open(image_path)
        new_img = new_img.resize((450, 500), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(new_img)
        lbl1.configure(image=new_img)
        lbl1.image = new_img

def BrightnessEnhancement(path, value):
    if not value:
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    else:
        img = cv2.imread(path)
        try:
            value = int(value)
            new_img = brightness_enhancement(img, value)
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        cv2.imwrite(".tmp/tmpImg.png", new_img)
        image_path = ".tmp/tmpImg.png"
        new_img = Image.open(image_path)
        new_img = new_img.resize((450, 500), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(new_img)
        lbl1.configure(image=new_img)
        lbl1.image = new_img

def Cropping(path, value):
    value = value.split(",")
    if len(value) != 4:
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    else:
        img = cv2.imread(path)
        try:
            x = int(value[0])
            y = int(value[0])
            w = int(value[0])
            h = int(value[0])
            new_img = image_cropping(img, x=x,y=y,width=w,height=h)
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        cv2.imwrite(".tmp/tmpImg.png", new_img)
        image_path = ".tmp/tmpImg.png"
        new_img = Image.open(image_path)
        new_img = new_img.resize((450, 500), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(new_img)
        lbl1.configure(image=new_img)
        lbl1.image = new_img

def Sketch(path, value):
    if not value:
      messagebox.showinfo("Error", "Please enter a valid number.")
      return
    else:
      img = cv2.imread(path)
      try:
        value = int(value)
        new_img = image_to_sketch(img, value)
      except:
        messagebox.showinfo("Error", "please enter a positive odd number.")
        return
      cv2.imwrite(".tmp/tmpImg.png", new_img)
      image_path = ".tmp/tmpImg.png"
      new_img = Image.open(image_path)
      new_img = new_img.resize((450, 500), Image.ANTIALIAS)
      new_img = ImageTk.PhotoImage(new_img)
      lbl1.configure(image=new_img)
      lbl1.image = new_img

def Rotation(path, value):
    if not value:
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    else:
        img = cv2.imread(path)
        try:
            value = int(value)
            new_img = image_rotation(img, value)
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        cv2.imwrite(".tmp/tmpImg.png", new_img)
        image_path = ".tmp/tmpImg.png"
        new_img = Image.open(image_path)
        new_img = new_img.resize((450, 500), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(new_img)
        lbl1.configure(image=new_img)
        lbl1.image = new_img

def Scale(path, value):
    value = value.split(",")
    if len(value) != 2:
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    else:
        try:
            value = [float(i) for i in value]
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        img = cv2.imread(path)
        try:
            new_img = image_scaling(img, *value)
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        cv2.imwrite(".tmp/tmpImg.png", new_img)
        image_path = ".tmp/tmpImg.png"
        new_img = Image.open(image_path)
        new_img = ImageTk.PhotoImage(new_img)
        lbl1.configure(image=new_img)
        lbl1.image = new_img

def Translation(path, value):
    value = value.split(",")
    if len(value) != 2:
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    else:
        try:
            value = [int(i) for i in value]
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        img = cv2.imread(path)
        try:
            new_img = translation(img, *value)
        except:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return
        cv2.imwrite(".tmp/tmpImg.png", new_img)
        image_path = ".tmp/tmpImg.png"
        new_img = Image.open(image_path)
        new_img = new_img.resize((450, 500), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(new_img)
        lbl1.configure(image=new_img)
        lbl1.image = new_img

def Reset(path):
    img = Image.open(path)
    img = img.resize((450, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl1.configure(image=img)
    lbl1.image = img

def Save():
    path = filedialog.asksaveasfile(title="Save image", defaultextension=".png")
    if path:
            try:
                cv2.imwrite(path.name, cv2.imread(".tmp/tmpImg.png"))
            except Exception as e:
                print(e)
                messagebox.showinfo("Error", "Image not saved.")
                return
            messagebox.showinfo("success", "Image saved successfully.")
            return
    else:
        messagebox.showinfo("Error", "Image not saved.")
        return


# image segmentation
def ImageSegmentation(img, value):
    img = cv2.imread(path)
    new_img = image_segmentation(img,int(value))
    cv2.imwrite(".tmp/tmpImg.png", new_img)
    image_path = ".tmp/tmpImg.png"
    new_img = Image.open(image_path)
    new_img = new_img.resize((450, 500), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(new_img)
    lbl1.configure(image=new_img)
    lbl1.image = new_img
    # return

def Dilation(img, value):
    img = cv2.imread(path)
    new_img = dilation(img,int(value))
    cv2.imwrite(".tmp/tmpImg.png", new_img)
    image_path = ".tmp/tmpImg.png"
    new_img = Image.open(image_path)
    new_img = new_img.resize((450, 500), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(new_img)
    lbl1.configure(image=new_img)
    lbl1.image = new_img
    # return
def Erosion(img, value):
    img = cv2.imread(path)
    new_img = erosion(img,int(value))
    cv2.imwrite(".tmp/tmpImg.png", new_img)
    image_path = ".tmp/tmpImg.png"
    new_img = Image.open(image_path)
    new_img = new_img.resize((450, 500), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(new_img)
    lbl1.configure(image=new_img)
    lbl1.image = new_img
    # return

path = filedialog.askopenfilename(title="Select Image File",
                                  filetypes=(('PNG file', "*.png"),
                                             ('JPJ file', "*.jpg")))

cv2.imwrite(".tmp/tmpImg.png", cv2.imread(path))

frm1 = Tk()
frm1.title("Select An Image")
frm1.minsize(400, 400)
frm1.config(background="#3D547B")

lbl1 = Label(frm1, border=15, background="#3D547B")
lbl1.pack(side='right')

lbl2 = Label(frm1,
             text='Value for the the selected technique :',
             border=15,
             background="#3D547B",
             fg="white",
             font=20)
lbl2.pack()

T = Entry()
T.pack()

img = Image.open(path)
img = img.resize((450, 500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
lbl1.configure(image=img)
lbl1.image = img

btn1 = Button(frm1,
              text="Blur",
              width=21,
              height=2,
              font=("sans-serif", 9),
              border= 6,
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Blur(path, T.get()))
btn1.place(x=190,y=100)

btn2 = Button(frm1,
              text="Gray Scale",
              width=21,
              height=2,
              border= 6,
              font=("sans-serif", 9),
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Grayscale(path))
btn2.place(x=10,y=100)


btn4 = Button(frm1,
              text="Thresholding",
              width=21,
              height=2,
              border= 6,
              font=("sans-serif", 9),
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Thresholding(path, T.get()))
btn4.place(x=10,y=160)


btn5 = Button(frm1,
              text="Edge Detection",
              width=21,
              height=2,
              border= 6,
              font=("sans-serif", 9),
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: EdgeDetection(path,T.get()))
btn5.place(x=190,y=160)

btn12 = Button(frm1,
              text="Scale",
              width=21,
              height=2,
              border= 6,
              background='#276BC8',
              font=("sans-serif", 9),
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Scale(path, T.get()))
btn12.place(x=10,y=220)

btn3 = Button(frm1,
              text="Brightness Enhancement",
              width=21,
              height=2,
              border= 6,
              background='#276BC8',
              font=("sans-serif", 9),
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: BrightnessEnhancement(path, T.get()))
btn3.place(x=190,y=220)

btn6 = Button(frm1,
              text="Cropping",
              width=21,
              height=2,
              border= 6,
              font=("sans-serif", 9),
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Cropping(path, T.get()))
btn6.place(x=10,y=280)

btn7 = Button(frm1,
              text="Sketch",
              width=21,
              height=2,
              font=("sans-serif", 9),
              border= 6,
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Sketch(path, T.get()))
btn7.place(x=190,y=280)

btn8 = Button(frm1,
              text="Rotation",
              width=21,
              height=2,
              border= 6,
              font=("sans-serif", 9),
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Rotation(path, T.get()))
btn8.place(x=10,y=340)

btn9 = Button(frm1,
              text="Translation",
              width=21,
              height=2,
              border= 6,
              font=("sans-serif", 9),
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Translation(path, T.get()))
btn9.place(x=190,y=340)

btn10 = Button(frm1,
              text="Reset",
              width=21,
              height=2,
              border= 6,
              font=("sans-serif", 9),
              background='#276BC8',
              activebackground='#001230',
              fg='white',
              activeforeground='white',
              command=lambda: Reset(path))
btn10.place(x=10,y=400)

btn11 = Button(frm1,
              text="Save",
              width=21,
              height=2,
              border= 6,
              font=("sans-serif", 9),
              background='#000000',
              activebackground='#005EFF',
              fg='white',
              activeforeground='white',
              command=lambda: Save())
btn11.place(x=190,y=400)

# new button for image segmentation by k-means clustering ==> Ahmed Haytham
btn13 = Button(frm1,
                text="Image Segmentation",
                width=21,
                height=2,
                border= 6,
                font=("sans-serif", 9),
                background='#276BC8',
                activebackground='#001230',
                fg='white',
                activeforeground='white',
                command=lambda: ImageSegmentation(path, T.get()))

btn13.place(x=10,y=460)
#new button for dilation ==> Ahmed Haytham

btn14 = Button(frm1,
                text="Dilation",
                width=21,
                height=2,
                border= 6,
                font=("sans-serif", 9),
                background='#276BC8',
                activebackground='#001230',
                fg='white',
                activeforeground='white',
                command=lambda: Dilation(path, T.get()))

btn14.place(x=190,y=460)
#new button for erosion with KS ==> Ahmed Haytham

btn15 = Button(frm1,
                text="Erosion",
                width=21,
                height=2,
                border= 6,
                font=("sans-serif", 9),
                background='#276BC8',
                activebackground='#001230',
                fg='white',
                activeforeground='white',
                command=lambda: Erosion(path, T.get()))

btn15.place(x=10,y=520)

frm1.mainloop()
