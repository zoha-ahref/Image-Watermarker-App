from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

image_to_edit = "/Users/zohakaukab/Desktop/5.png"
save_image_path = "/Users/zohakaukab/Desktop/pic82.png"
logo_path = "/Users/zohakaukab/Desktop/logo-3.png"
text_for_watermark = "@Copyright Zoha Kaukab"
pos_add_text = (10, 10)
pos_add_logo = (10, 10)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.app_window()

    #creates a window
    def app_window(self):
        self.master.title("Image Watermarker App")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.exit_window)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Watermark with Text",
                         command=lambda: self.add_text(image_to_edit, save_image_path, text_for_watermark, pos_add_text))
        edit.add_command(label="Watermark with Logo",
                         command=lambda: self.add_logo(image_to_edit, save_image_path, logo_path, pos_add_logo))
        menu.add_cascade(label="Edit", menu=edit)

    # function to watermark images by adding text
    def add_text(self, initial_image_path, final_image_path, text, pos):
        photo = Image.open(initial_image_path)
        drawing = ImageDraw.Draw(photo)
        black_text = (3,8,12)
        font = ImageFont.truetype("arial.ttf", 35)
        drawing.text(pos, text, fill=black_text, font=font)
        photo.save(final_image_path)
        img = ImageTk.PhotoImage(photo)
        panel = Label(self, image=img)
        panel.image = img
        panel.place(x=0, y=0)

    # function to watermark images by adding a logo
    def add_logo(self, initial_image_path, final_image_path, logo, pos):
        photo = Image.open(initial_image_path)
        watermark_logo = Image.open(logo)
        width, height = photo.size
        trans_back_img = Image.new('RGBA', (width, height), (0,0,0,0))
        trans_back_img.paste(photo, (0,0))
        trans_back_img.paste(watermark_logo, pos, mask=watermark_logo)
        trans_back_img.save(final_image_path)
        img = ImageTk.PhotoImage(trans_back_img)
        panel = Label(self, image=img)
        panel.image = img
        panel.place(x=0, y=0)
    #function to exit
    def exit_window(self):
        exit()

root = Tk()

root.geometry("400x300")
app = Window(root)
root.mainloop()