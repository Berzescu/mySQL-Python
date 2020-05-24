import mysql.connector
from mysql.connector import errorcode
from tkinter import *
from PIL import ImageTk, Image

try:

    connection = mysql.connector.connect(host="lefti.cm.upt.ro",
                                         user="berzescuilie",
                                         password="Cactus98",
                                         database="starwars")
    cursor = connection.cursor()


    def join():
        select_join = '''select people_name nume, group_concat(starship_name) numeNave , group_concat(starship_class) 
        Tip_nave, count(starshipID)  Numar_nave  from starship join starshipclass using (starshipclassID) 
        join people_starships using (starshipID) join people using (peopleID)
                    where substring(people_name, 1,1) between 'a' and 'k'
                    group by people_name
                    limit 10;'''

        cursor.execute(select_join)
        rezultat = cursor.fetchall()
        data = []
        for i in rezultat:
            ok = 0
            for j in i:
                if ok == 0:
                    data.append('Persoana: ' + str(j))
                elif ok == 1:
                    data.append('Dtine nava/navele:' + str(j))
                elif ok == 2:
                    data.append('Care sunt de tipul: ' + str(j))
                else:
                    data.append('Numarul de nave este:' + str(j) + '\n')
                ok += 1

        return '\n'.join(data)


    interogare = Tk()
    root = interogare
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    root.title('Star')
    img = PhotoImage(file='star.png')
    root.iconphoto(True, img)
    root.configure(background='#008282')
    frame = LabelFrame(root, padx=50, pady=50)
    frame.pack(padx=10, pady=10)
    frame.configure(background='#4e0047')

    interogare.title('Aplicatie Starwars *x*')
    interogare.configure(background='#5e0061')

    img_1 = ImageTk.PhotoImage(Image.open('ufo.png'))
    img_2 = ImageTk.PhotoImage(Image.open('car.png'))
    img_3 = ImageTk.PhotoImage(Image.open('alien.png'))
    img_4 = ImageTk.PhotoImage(Image.open('movie.png'))
    img_5 = ImageTk.PhotoImage(Image.open('cloud.png'))
    img_6 = ImageTk.PhotoImage(Image.open('prod.png'))
    img_7 = ImageTk.PhotoImage(Image.open('planet.png'))

    label_1 = Label(frame, image=img_1).grid(row=1, column=0)
    label_2 = Label(frame, image=img_2).grid(row=1, column=1)
    label_3 = Label(frame, image=img_3).grid(row=3, column=0)
    label_4 = Label(frame, image=img_4).grid(row=3, column=1)
    label_5 = Label(frame, image=img_5).grid(row=5, column=0)
    label_6 = Label(frame, image=img_6).grid(row=5, column=1)
    label_7 = Label(frame, image=img_7).grid(row=7, column=0)


    def select_out(x):
        def data():
            Label(framme, text=x, padx=100).grid(row=0, column=0, columnspan=10)

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=500, height=500)

        myframe = Frame(frame, relief=GROOVE, width=450, height=20, bd=1)
        myframe.place(x=470, y=130)
        canvas = Canvas(myframe)

        framme = Frame(canvas)
        framme.configure(background='#1D8112')

        myscrollbar = Scrollbar(myframe, orient="horizontal", command=canvas.xview)
        myscrollbary = Scrollbar(myframe, orient="vertical", command=canvas.yview)

        canvas.configure(xscrollcommand=myscrollbar.set)
        canvas.configure(yscrollcommand=myscrollbary.set)

        myscrollbar.pack(side="bottom", fill="x")
        myscrollbary.pack(side="left", fill="y")

        canvas.pack(side="left")
        canvas.create_window((0, 0), window=framme, anchor='nw')

        framme.bind("<Configure>", myfunction)

        data()

    def select():
        select_out(join())

    def tabele(args):
        cursor.callproc('lefti_berzescuilie.Butoane', args)
        v = []
        for result in cursor.stored_results():
            v.append(result.fetchall())

        b = []
        j = 0
        for i in v:
            for t in i:
                b.append(str(i[j][0]))
                j += 1
        del v[-1]
        return '\n'.join(b)


    def film():

        select_out(tabele(['Film']))

    def vehicul():

        select_out(tabele(['Vehicul']))

    def nave():

        select_out(tabele(['Ship']))

    def vreme():

        select_out(tabele(['Clima']))

    def specie():

        select_out(tabele(['Specie']))

    def producator():

        select_out(tabele(['Producatori']))

    def planeta():
        select_out(tabele(['Planeta']))


    def procedura(args):

        a = None
        b = None

        r = cursor.callproc('lefti_berzescuilie.interogare2X_cursor', [args, a, b])
        a = []
        b = []
        data = []
        a.append(r[1])
        b.append(r[2])

        for i in a:
            data.append('\t' + i + '\n')
        r = ''
        for i in b:
            for j in i:
                r = r + j
                if j == ',' or j == ':':
                    data.append('\t' + r)
                    data.append(' ')
                    r = ''

        data.append('\t' + r + '.')
        return '\n'.join(data)


    eb = Entry(frame, width=50, bg='black', fg='white', borderwidth=10)
    eb.grid(row=0, column=2)
    eb.insert(0, 'Alege un film pentru procedura')


    def proc():
        try:
            a = str(eb.get())
            select_out(procedura(a))
            eb.delete(0, END)

        except TypeError:
            select_out('Numele filmului nu exista')

    buton_1 = Button(frame, text='Filme', padx=80, pady=10, bg='#ff9e00', fg='white', borderwidth=5,
                     command=film).grid(row=4, column=1)
    buton_2 = Button(frame, text='Vehicule', padx=80, pady=10, bg='#599c24', fg='white', borderwidth=5,
                     command=vehicul).grid(row=2, column=1)
    buton_3 = Button(frame, text='Nave', padx=80, pady=10, bg='#ff9e00', fg='white', borderwidth=5,
                     command=nave).grid(row=2, column=0)
    buton_4 = Button(frame, text='Clima', padx=80, pady=10, bg='#ff9e00', fg='white', borderwidth=5,
                     command=vreme).grid(row=6, column=0)
    buton_5 = Button(frame, text='Specie', padx=80, pady=10, bg='#599c24', fg='white', borderwidth=5,
                     command=specie).grid(row=4, column=0)
    buton_6 = Button(frame, text='Producatori', padx=80, pady=10, bg='#599c24', fg='white', borderwidth=5,
                     command=producator).grid(row=6, column=1)
    buton_7 = Button(frame, text='Planete', padx=80, pady=10, bg='#599c24', fg='white', borderwidth=5,
                     command=planeta).grid(row=8, column=0)
    procedura_button = Button(frame, text='Procedura', padx=80, pady=10, bg='#599c24', fg='white', borderwidth=5,
                              command=proc).grid(row=1, column=6)
    mybutton = Button(frame, text="Select", command=select,  padx=80, pady=10, bg='#ff9e00', fg='black', borderwidth=5)\
        .grid(row=1, column=2, columnspan=2)

    text = '''              \tProiect SGD- Starwars \n
                    Student: Berzescu Ilie-Silviu \n
                    Facultate: ETcTI-TST, an III
            '''

    select_out(text)

    interogare.mainloop()


except mysql.connector.Error as error:
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")

    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")

    else:
        print(error)
    print("Failed to execute stored procedure: {}".format(error))

except ConnectionError:
    print('dsa')


finally:
    if connection is not None and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
    '''
    if connection.is_connected():
        connection.close()
    print("MySQL connection is closed")
'''
