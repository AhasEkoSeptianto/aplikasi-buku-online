import tkinter as tk
from datetime import datetime
from .documentReader import Doc
import os

# class untuk menambahkan Catatan Baru / Membuat windows baru untuk membuat Noted baru
class newNoted():

    def Create(self,namaMhs,nimMhs,semester,matakuliah,prodi,kelas):
        # function untuk save buuton
        def Save():
            Doc().CreateNoted(namaMhs=namaMhs, nimMhs=nimMhs, semester=semester, matakuliah=matakuliah, prodi=prodi, kelas=kelas,opsiName=OpsiNotedName)
            os.chdir("../../../")
            self.Opsi.destroy()

        path        = "buku/{}/{}".format(semester,matakuliah)
        os.chdir(path)
        self.Opsi   = tk.Tk()
        self.Opsi.title("Create Noted")
        self.Opsi.protocol('WM_DELETE_WINDOW', lambda : tk.messagebox.showerror('err','please just click submit first') )
        Header      = tk.Label(self.Opsi, text='Buat catatan baru').grid(column=0, row=0, columnspan=2, pady=10)
        OpsiNotedName = "Noted " + datetime.today().strftime('%d-%m-%Y') + ".docx"
        
        # check Name Note if he exist he will change 
        for i in range(1,20):
            if OpsiNotedName in os.listdir():
                OpsiNotedName = "Noted " + datetime.today().strftime('%d-%m-%Y') + str(i) + ".docx"
        
        labelNoted      = tk.Label(self.Opsi, text='Save as : ').grid(column=0,row=1, pady=10)
        inputNameNoted  = tk.Entry(self.Opsi,)
        inputNameNoted.insert(0,OpsiNotedName)
        inputNameNoted.grid(column=1, row=1)

        btnSubmit = tk.Button(self.Opsi, text='Submit', fg='white', bg='blue', command=Save).grid(column=0, row=2, columnspan=2, pady=10)


        self.Opsi.mainloop()