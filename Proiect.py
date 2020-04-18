import mysql.connector
from mysql.connector import Error
from tkinter import *
from PIL import ImageTk, Image

try:
    connection = mysql.connector.connect(host ="lefti.cm.upt.ro",
                                         user = "berzescuilie",
                                         password = "Cactus98",
                                         database = "starwars")
    cursor = connection.cursor()
    root = Tk()
    root.title('Star')
    img = PhotoImage(file='star.png')
    root.iconphoto(True, img)
    root.configure(background='#008282')
    frame = LabelFrame(root, padx=50, pady=50)
    frame.pack(padx=10, pady=10)
    frame.configure(background='#4e0047')

    e = Entry(frame, width=50, bg='black', fg='white', borderwidth=10)
    e.grid(row=0, column=2, columnspan=2, rowspan=1)
    e.insert(0, 'Cauta')

    img_1 = ImageTk.PhotoImage(Image.open('ufo.png'))
    img_2 = ImageTk.PhotoImage(Image.open('car.png'))
    img_3 = ImageTk.PhotoImage(Image.open('alien.png'))
    img_4 = ImageTk.PhotoImage(Image.open('movie.png'))
    img_5 = ImageTk.PhotoImage(Image.open('cloud.png'))
    img_6 = ImageTk.PhotoImage(Image.open('prod.png'))
    img_7 = ImageTk.PhotoImage(Image.open('planet.png'))

    label_1 = Label(frame, image=img_1, padx=40, pady=40).grid(row=4, column=2, columnspan=2, rowspan=1)
    label_2 = Label(frame, image=img_2).grid(row=4, column=1)
    label_3 = Label(frame, image=img_3).grid(row=6, column=0)
    label_4 = Label(frame, image=img_4).grid(row=4, column=0)
    label_5 = Label(frame, image=img_5).grid(row=4, column=4)
    label_6 = Label(frame, image=img_6).grid(row=6, column=6)
    label_7 = Label(frame, image=img_7).grid(row=4, column=6)

    def tabele(args):
        cursor.callproc('lefti_berzescuilie.cauta',args)
        v = []
        for result in cursor.stored_results():
            v.append(result.fetchall())

        b = []
        j = 0
        for i in v:
            for t in i:
                b.append(str(i[j][0], encoding='utf-8'))
                b.append(' ')
                j += 1
        del v[-1]
        return '\n'.join(b)
    def film():

        l = Label(frame, text=tabele(['film']), width=60, height=20, bg='grey')
        l.grid(row=7, column=2, columnspan=2, rowspan=2)


    def vehicul():

        l = Label(frame, text=tabele(['vehicles']), width=60, height=20, bg='grey')
        l.grid(row=7, column=2, columnspan=2, rowspan=2)


    def nave():

        l = Label(frame, text=tabele(['ship']), width=60, height=20, bg='grey')
        l.grid(row=7, column=2, columnspan=2, rowspan=2)


    def vreme():

        l = Label(frame, text=tabele(['climate']), width=60, height=20, bg='grey')
        l.grid(row=7, column=2, columnspan=2, rowspan=2)


    def specie():

        l = Label(frame, text=tabele(['species']), width=60, height=20, bg='grey')
        l.grid(row=7, column=2, columnspan=2, rowspan=2)


    def producator():

        l = Label(frame, text=tabele(['producer']), width=60, height=20, bg='grey')
        l.grid(row=7, column=2, columnspan=2, rowspan=2)


    def planeta():

        l = Label(frame, text=tabele(['planet|terrain']), width=60, height=20, bg='grey')
        l.grid(row=7, column=2, columnspan=2, rowspan=2)


    buton_1 = Button(frame, text='Filme', padx=80, pady=10, bg='#55552b', fg='white', borderwidth=5, command=film).grid(
        row=5, column=0)
    buton_2 = Button(frame, text='Vehicule', padx=80, pady=10, bg='#55552b', fg='white', borderwidth=5,
                     command=vehicul).grid(row=5, column=1)
    buton_3 = Button(frame, text='Nave', padx=80, pady=10, bg='#55552b', fg='white', borderwidth=5, command=nave).grid(
        row=5, column=2, columnspan=2)
    buton_4 = Button(frame, text='Vremea', padx=80, pady=10, bg='#55552b', fg='white', borderwidth=5,
                     command=vreme).grid(row=5, column=4)
    buton_5 = Button(frame, text='Specie', padx=80, pady=10, bg='#55552b', fg='white', borderwidth=5,
                     command=specie).grid(row=7, column=0)
    buton_6 = Button(frame, text='Producatori', padx=80, pady=10, bg='#55552b', fg='white', borderwidth=5,
                     command=producator).grid(row=7, column=6)
    buton_7 = Button(frame, text='Planete', padx=80, pady=10, bg='#55552b', fg='white', borderwidth=5,
                     command=planeta).grid(row=5, column=6)


    def open():
        interogare = Toplevel()
        interogare.title(e.get())
        interogare.configure(background='#484848')
        frame_o = LabelFrame(interogare, padx=100, pady=100)
        frame_o.pack(padx=10, pady=10)
        frame_o.configure(background='#5e0061')

        apasa = Button(frame_o, text='oare', padx=80, pady=10).grid(row=0, column=0)

        apasa2 = Button(frame_o, text='oare2', padx=80, pady=10).grid(row=1, column=1)


    def click():
        open()
        e.delete(0, END)


    label_out = Label(frame, text='mySQL_output', width=60, height=20, bg='grey').grid(row=7, column=2, columnspan=2,
                                                                                       rowspan=2)

    mybutton = Button(frame, text="Cauta", command=click, bg='#0f575d', fg='#A9A9A9').grid(row=1, column=2,
                                                                                           columnspan=2)

    root.mainloop()

except mysql.connector.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")