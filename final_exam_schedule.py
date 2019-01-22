from tkinter import *

class App(Tk):
    
    def __init__(self):

        super().__init__()
        
        self.title('Final Exam Schedule')
        self.geometry('500x700')
        
        self.times_days_label = Label(self, text='Times - Days')        
        self.entry_day_one = Entry(self)
        self.entry_day_two = Entry(self)
        self.entry_day_three = Entry(self)
        self.entry_day_four = Entry(self)
        self.entry_day_five = Entry(self)
        self.entry_day_six = Entry(self)        

        self.l_m.grid(row=0, column=0)
        self.e_m.grid(row=0, column=1)
        self.l_k.grid(row=2, column=0)
        self.e_k.grid(row=2, column=1)
        
    def miles_entered(self, evnt):
        mls = float(self.e_m.get())
        km = 1.6 * mls
        self.miles.set('')
        self.km.set(str(km))
        
    def km_entered(self, evnt):
        km = float(self.e_k.get())
        mls = 0.63 * km
        self.miles.set(str(mls))
        self.km.set('')

root = App()
root.mainloop()