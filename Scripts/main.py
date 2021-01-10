import tkinter as tk,os
from tkinter import ttk ,messagebox
from PIL import Image,ImageTk
from .documentReader import Doc
from tkinter import *
from datetime import datetime,time
from .createNoted import newNoted
from pathlib import Path

class book():

    def __init__(self):
        self.root   = tk.Tk()
        self.root.title('books')
        try :
            # auto maximaze windows
            self.root.attributes('-zoomed', True)
        except :
            # auto maximisze linux because iam use linux 
            self.root.attributes('-fullscreen', True)

        self.root.minsize(1100,600)
        self.width  = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.utility()
        self.position()
        self.update_clock()
        self.root.mainloop()

    def utility(self):
        # main window
        self.windowLeft     = tk.Frame(self.root, height = self.height, width=((self.width/2)/2), bg='gray75')
        self.windowRight    = tk.Frame(self.root, height=(self.height), width=(((self.width/2)/2) + (self.width/2)),bg='gray60')
        # Header Text
        self.Text           = Label(self.windowLeft, text='My Book APP', font=("Arial",30,"bold"), bg='gray75', fg='blue')
        self.Timer          = Label(self.windowLeft, text='', font=("Arial",22), bg='gray75', fg='blue')
        
    #     left
        self.addBooks       = tk.Button(self.windowLeft, height=3, width=40, text='Buku baru', bg='blue', fg='white', command=self.btnAddBooks)
        self.chooseBooks    = tk.Button(self.windowLeft, height=3, width=40, text='Pilih baru', bg='blue', fg='white', command=self.btnChooseBooks)
        self.Exit           = tk.Button(self.windowLeft, height=3, width=40, text='Exit', bg='red', fg='white', command=self.Exit)

    def position(self):
        self.windowLeft.pack(side="left")
        self.windowRight.pack(side='right')
    #     left
        self.Text.place(relx=0.5,rely=0.1, anchor='center')
        self.Timer.place(relx=0.5,rely=0.4, anchor='center')
        self.addBooks.place(x=0, rely=0.7)
        self.chooseBooks.place(x=0, rely=0.8)
        self.Exit.place(x=0, rely=0.9)

    # function untuk menambahkan buku
    def btnAddBooks(self):
        def tambah():
            namaMhs     = inputNamaMhs.get()
            nimMhs      = inputNimMhs.get()
            semester    = inputSemester.get()
            matakuliah  = inputMatakuliah.get()
            namaDosen   = inputNamaDosen.get()
            prodi       = inputPrody.get()
            kelas       = inputKelas.get()

            # statemen ini untuk pengguna baru jika dia belum ada directory buku maka akan dibuatkan
            # jika tidak ada semester yang diinginkan akan dibuatkan 

            if namaMhs != "" and nimMhs != "" and semester != "" and semester != "" and matakuliah != "" and namaDosen != "" and prodi != "" and kelas != "" :
                path = "semester " + semester + '/'   
                # check forder jika tersedia semua track telah menghandel kemungkinan yyang ada
                try :
                    os.chdir('buku/')
                    try :
                        os.chdir(str(path))
                        try :
                            os.chdir(matakuliah)
                            Doc().CreateNoted(namaMhs=namaMhs, nimMhs=nimMhs, semester=semester, matakuliah=matakuliah, prodi=prodi, kelas=kelas)
                            os.chdir('../../../')
                            tk.messagebox.showinfo('info', "Berhasil membuat catatan baru")
                            # save ident
                            try:
                                os.chdir('Info')
                                Doc().SaveIdent(namaMhs=namaMhs, nimMhs=nimMhs, prodi=prodi,kelas=kelas)
                                os.chdir('../')
                            except:
                                os.mkdir('info')
                                os.chdir('info')
                                Doc().SaveIdent(namaMhs=namaMhs, nimMhs=nimMhs, prodi=prodi,kelas=kelas)
                                os.chdir('../')
                        except:
                            os.mkdir(matakuliah)
                            os.chdir(matakuliah)
                            Doc().CreateNoted(namaMhs=namaMhs, nimMhs=nimMhs, semester=semester, matakuliah=matakuliah, prodi=prodi, kelas=kelas)
                            os.chdir('../../../')
                            tk.messagebox.showinfo('info', "Berhasil membuat catatan baru")
                            # save ident
                            try:
                                os.chdir('Info')
                                Doc().SaveIdent(namaMhs=namaMhs, nimMhs=nimMhs, prodi=prodi,kelas=kelas)
                                os.chdir('../')
                            except:
                                os.mkdir('info')
                                os.chdir('info')
                                Doc().SaveIdent(namaMhs=namaMhs, nimMhs=nimMhs, prodi=prodi,kelas=kelas)
                                os.chdir('../')
                    except:
                        os.mkdir(str(path))
                        os.chdir(str(path))
                        os.mkdir(matakuliah)
                        os.chdir(matakuliah)
                        Doc().CreateNoted(namaMhs=namaMhs, nimMhs=nimMhs, semester=semester, matakuliah=matakuliah, prodi=prodi, kelas=kelas)
                        os.chdir('../../../')
                        tk.messagebox.showinfo('info', "Berhasil membuat catatan baru")
                        # save ident
                        try:
                            os.chdir('Info')
                            Doc().SaveIdent(namaMhs=namaMhs, nimMhs=nimMhs, prodi=prodi,kelas=kelas)
                            os.chdir('../')
                        except:
                            os.mkdir('info')
                            os.chdir('info')
                            Doc().SaveIdent(namaMhs=namaMhs, nimMhs=nimMhs, prodi=prodi,kelas=kelas)
                            os.chdir('../')
                except:
                    os.mkdir('buku')
                    os.chdir('buku')
                    os.mkdir(str(path))
                    os.chdir(str(path))
                    os.mkdir(matakuliah)
                    os.chdir(matakuliah)
                    Doc().CreateNoted(namaMhs=namaMhs, nimMhs=nimMhs, semester=semester, matakuliah=matakuliah, prodi=prodi, kelas=kelas)
                    os.chdir('../../../')
                    tk.messagebox.showinfo('info', "Berhasil membuat catatan baru")
                    # save ident
                    try:
                        os.chdir('Info')
                        Doc().SaveIdent(namaMhs=namaMhs, nimMhs=nimMhs, prodi=prodi,kelas=kelas)
                        os.chdir('../')
                    except:
                        os.mkdir('info')
                        os.chdir('info')
                        Doc().SaveIdent(namaMhs=namaMhs, nimMhs=nimMhs, prodi=prodi,kelas=kelas)
                        os.chdir('../')
            else :
                tk.messagebox.showinfo('info', "Harap isi semua form yang ada")
                

        self.ClearAllForm() #clear all form pada windows ketika pindah tombol navigasi
        self.windowRight = tk.Frame(self.root, height=(self.height), width=(((self.width / 2) / 2) + (self.width / 2)),
                                    bg='gray60')
        self.windowRight.pack(side='right')

        Header = tk.Label(self.windowRight, text='Tambah Buku Baru', font=("system",25,"bold"), bg="gray60", fg='white').place(relx=0.5, y=20, anchor='n')
        self.CanvasForm = tk.Frame(self.windowRight, bg='gray80', width=(self.windowRight.winfo_reqwidth()-100), height=(self.windowRight.winfo_reqheight()-300)).place(relx=0.5, y=100, anchor='n')
        
        labelNamaMhs = tk.Label(self.CanvasForm, text='Nama Mahasiswa', fg='black',bg="gray80").place(relx=0.4,rely=0.3, anchor='w')
        inputNamaMhs = tk.Entry(self.CanvasForm, )
        inputNamaMhs.place(relx=0.5, rely=0.3, anchor='w')

        labelNimMhs = tk.Label(self.CanvasForm, text='Nim Mahasiswa', fg='black',bg="gray80").place(relx=0.4,rely=0.4, anchor='w')
        inputNimMhs = tk.Entry(self.CanvasForm, )
        inputNimMhs.place(relx=0.5, rely=0.4, anchor='w')

        labelPrody = tk.Label(self.CanvasForm, text='Prodi', fg='black',bg="gray80").place(relx=0.4,rely=0.5, anchor='w')
        inputPrody = tk.Entry(self.CanvasForm, )
        inputPrody.place(relx=0.5, rely=0.5, anchor='w')

        labelKelas = tk.Label(self.CanvasForm, text='Kelas', fg='black',bg="gray80").place(relx=0.4,rely=0.6, anchor='w')
        inputKelas = tk.Entry(self.CanvasForm, )
        inputKelas.place(relx=0.5, rely=0.6, anchor='w')

        labelSemester = tk.Label(self.CanvasForm, text='Semester', fg='black',bg="gray80").place(relx=0.7,rely=0.3, anchor='w')
        inputSemester = ttk.Combobox(self.CanvasForm, value=('1','2','3','4','5','6','7','8'))
        inputSemester.place(relx=0.8, rely=0.3, anchor='w')

        labelMatakuliah = tk.Label(self.CanvasForm, text='Matakuliah', fg='black',bg="gray80").place(relx=0.7,rely=0.4, anchor='w')
        inputMatakuliah = tk.Entry(self.CanvasForm, )
        inputMatakuliah.place(relx=0.8, rely=0.4, anchor='w')

        labelNamaDosen = tk.Label(self.CanvasForm, text='Nama Dosen', fg='black',bg="gray80").place(relx=0.7,rely=0.5, anchor='w')
        inputNamaDosen = tk.Entry(self.CanvasForm, )
        inputNamaDosen.place(relx=0.8, rely=0.5, anchor='w')

        btnTambahBuku = tk.Button(self.CanvasForm, text='Submit', width=50, bg='blue', fg='white', command=tambah).place(relx=0.6, rely=0.7, anchor='w')

        # check if identify is exist
        Identify = Path("info/Identify.docx")
        if Identify.is_file():
            
            def update():
                os.remove('info/Identify.docx')
                self.addBooks.invoke()

            result = Doc().CheckIdent()
            inputNamaMhs.insert(0, result['Name'])
            inputNimMhs.insert(0, result['Nim'])
            inputKelas.insert(0, result['Kelas'])
            inputPrody.insert(0, result['Prodi'])

            btnDeleteAutoComplete = tk.Button(self.CanvasForm, text='Delete auto complite form', bg='red', fg='white', command=update).place(relx=0.4, rely=0.7, anchor='w')
    
    # function main untuk melihat catatan
    def btnChooseBooks(self):

        def CheckSemester(event=None):
            try:
                os.chdir('buku')
                allSemester = os.listdir()
                os.chdir('../')
                # check untuk menghapus catatan field jika mengubah semesternya
                try:
                    varCatatan.set('')
                except:
                    pass
                return allSemester
            except:
                tk.messagebox.showinfo('info', "Daftar semester tidak ditemukan, silahkan buat catatan baru terlebih dahulu")

        def CheckMatakuliah(event=None):
            Semester = semester.get()
            try:
                # pindah directory ke- semester list 
                path = "buku/{}".format(Semester)
                os.chdir(path)
                # jika tombol semester ditrigger tombol matakuliah akan diupdate
                if event:
                    varCatatan.set('')
                    matakuliah.configure(value=tuple(os.listdir()))    
                    matakuliah.current(0)
                    os.chdir(matakuliah.get())
                    catatan.configure(value=tuple(os.listdir()))
                    os.chdir('../')
                SemuaMatkul = os.listdir() # semua list didalam matakuliah
                os.chdir('../../')
                return SemuaMatkul
            except:
                SemuaMatkul = ()
                return SemuaMatkul
            
        # func for Check the Noted from semester.get and matakuliah.get
        def CheckCatatan(event=None,Catatan=None):
            # get form
            Semester    = semester.get()
            Matakuliah  = matakuliah.get()
            # change directory to path Noted
            path = "buku/{}/{}".format(Semester,Matakuliah)
            os.chdir(path)
            catatan.configure(value=os.listdir())# catatan update
            SemuaCatatan = os.listdir()
            # take all Noted to list and give to isiBuku
            allNoted = Doc().getBooks(semester=Semester, matakuliah=Matakuliah,catatan=None)
            # clear all Noted is Exist dan menulis ulang buku
            isiBuku.delete('1.0', END)
            for Noted in allNoted:
                isiBuku.insert(END,str(Noted + "\n"))
            os.chdir('../../../')
            return SemuaCatatan

        def isi_buku(event=None,Catatan=None):
            # get form
            Semester    = semester.get()
            Matakuliah  = matakuliah.get()
            path        = "buku/{}/{}".format(Semester,Matakuliah)# change directory to path Noted
            os.chdir(path)
            # take all Noted to list and give to isiBuku
            allNoted = Doc().getBooks(semester=Semester, matakuliah=Matakuliah,catatan=Catatan)
            # clear all Noted is Exist dan menulis ulang buku
            isiBuku.delete('1.0', END)
            for Noted in allNoted:
                isiBuku.insert(END,str(Noted + "\n"))
            os.chdir('../../../')

        def btnCreateNoted():
            # get all informations user
            Semester    = semester.get()
            Matakuliah  = matakuliah.get()
            
            User        = Doc().CheckIdent()
            newNoted().Create(namaMhs=User['Name'],nimMhs=User['Nim'],semester=Semester, matakuliah=Matakuliah,prodi=User['Prodi'],kelas=User['Kelas'])
            catatan.configure(value=tuple(CheckCatatan()))
            

        def btnDeleteNoted():
            # get all informations user
            Semester    = semester.get()
            Matakuliah  = matakuliah.get()
            Noted       = catatan.get()
            isDelete    = tk.messagebox.askyesno('Hapus','Apakah anda yakin ?')
            if isDelete :
                path = "buku/{}/{}".format(Semester,Matakuliah)
                os.chdir(path)
                os.remove(Noted)
                os.chdir('../../../')
                catatan.configure(value=tuple(CheckCatatan()))

        def save():
            # get all form
            Semester    = semester.get()
            Matakuliah  = matakuliah.get()
            Noted       = catatan.get()
            Text        = isiBuku.get("1.0", END)
            path        = "buku/{}/{}".format(Semester,Matakuliah)
            os.chdir(path)
            if len(isiBuku.get("1.0", END))!=1 and Noted != '' :
                Save = tk.messagebox.askyesno('Save','Save Noted ?')
                if Save :
                    Doc().Update(Noted,Text)
                    tk.messagebox.showinfo('Save', 'Success')

            os.chdir('../../../')


        self.ClearAllForm()
        self.windowRight = tk.Frame(self.root, height=(self.height), width=(((self.width / 2) / 2) + (self.width / 2)),
                                    bg='gray60')
        self.windowRight.pack(side='right')

        Header = tk.Label(self.windowRight, text='Buku', font=("system",25,"bold"), bg="gray60", fg='white').place(relx=0.5, y=20, anchor='n')
        self.CanvasForm = tk.Frame(self.windowRight, bg='gray90' ,width=(self.windowRight.winfo_reqwidth()-510), height=(self.windowRight.winfo_reqheight()-210)).place(relx=0.6, rely=0.6, anchor='center')

        # buku
        isiBuku = tk.Text(self.windowRight, height = 32, width = 63)
        isiBuku.place(relx=0.6, rely=0.6, anchor='center')

        labelSemester = tk.Label(self.windowRight, text='Semester', bg='gray60', fg='white').place(x=60, y=170,anchor='center')
        # Combobox Semester
        try :
            semester = ttk.Combobox(self.windowRight, width=28, value=tuple(CheckSemester()))
            semester.current(0)
        except:
            tk.messagebox.showinfo('info', "Tidak dapat memuat, pastikan catatan sudah pernah ada", icon='warning')
            self.addBooks.invoke()
        semester.place(x=145, y=210, anchor='center')

        # matakuliah
        labelmatakuliah = tk.Label(self.windowRight, text='matakuliah', bg='gray60', fg='white').place(x=63, y=240,anchor='center')
        # Combobox matakuliah
        matakuliah = ttk.Combobox(self.windowRight, width=28)
        try:
            matakuliah['values'] = tuple(CheckMatakuliah())
            matakuliah.current(0)
        except:
            matakuliah['values'] = tuple()
        matakuliah.place(x=145, y=270, anchor='center')

        labelBuatBaru = tk.Label(self.windowRight, text='Buat catatan baru', bg='gray60', fg='white').place(x=83, y=300,anchor='center')
        buatBaru = tk.Button(self.windowRight, text='Buat baru', bg='blue', fg='white', width=28, command=btnCreateNoted).place(x=145, y=330,anchor='center')

        labelHapusCatatan = tk.Label(self.windowRight, text='Hapus catatan', bg='gray60', fg='white').place(x=73, y=360, anchor='center')
        HapusCatatan = tk.Button(self.windowRight, text='Hapus', bg='red', fg='white', width=28, command=btnDeleteNoted).place(x=145, y=390,anchor='center')
        # info text
        textInfo = tk.Label(self.windowRight, text='My Noted', font=("Arial",30,"bold") ,bg='gray60', fg='white').place(x=150, y=500, anchor='center')
        # catatan
        labelCatatan = tk.Label(self.windowRight, text='Catatan', bg='gray60', fg='white').place(x=63, y=600,anchor='center')
        # Combobox Catatan
        varCatatan = tk.StringVar()
        catatan = ttk.Combobox(self.windowRight,textvariable=varCatatan, width=28)
        # check jika catatan sudah pernah ada
        try:
            catatan['values'] = tuple(CheckCatatan())
        except:
            catatan['values'] = tuple()

        catatan.place(x=145, y=630, anchor='center') # call Noted for update books

        # SaveButton
        save = tk.Button(self.windowRight, text='save', padx=15, bg='blue', fg='white', command=save).place(relx=0.9, y=170,anchor='center')

        # bind
        semester.bind('<<ComboboxSelected>>', CheckMatakuliah)
        matakuliah.bind('<<ComboboxSelected>>', lambda x : CheckCatatan())
        catatan.bind('<<ComboboxSelected>>', lambda x : isi_buku(Catatan=catatan.get()))
        
    #funtions untuk clear semua form
    def ClearAllForm(self):
        try:
            self.windowRight.destroy()
        except:
            pass

    # function untuk menampilkan waktu secata
    def update_clock(self):
        day     = datetime.today().strftime("%A")
        time    = datetime.today().strftime('%d-%m-%Y')
        now_clock = datetime.now().strftime('%H:%M:%S')
        show = '_________________________\n\n' +  day + ' : ' + time + '\n' + now_clock + '\n_________________________'
        self.Timer.configure(text=show)
        self.root.after(1000, self.update_clock)

    def Exit(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
