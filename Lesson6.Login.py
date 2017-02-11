from tkinter import * # import module tkinter

def click():
     name = le.get()
     passw = pe.get()
     if name == 'samat' and passw =='qwerty':
          wn.destroy() # destroy wn and
          wn1 = Tk() # create new window
          wn1.geometry('400x400') # change wn1 size
          wn1.title("Welcome " + name+"!") 
          welc_lab = Label(wn1, text="Привет! Хотите начать игру?")
          welc_lab.grid(row=0,column = 0)
     else:
          l = Label(wn, text = "Неправильный логин или пароль", fg = "red")
          l.grid(row=1,column = 2)

wn = Tk()
wn.geometry('500x400')

login = Label(wn, text="Login:", fg = "#14c5df", bg= "#ffff11")
login.grid(row = 0, column=0, sticky=W + E) # w- west, e-east

password = Label(wn, text="Password",fg = "#14c5df", bg= "#ffff11")
password.grid(row = 1, column = 0, sticky = W + E)

le = Entry(wn, width = 15)
le.grid(row = 0 , column = 1)

pe = Entry(wn, width = 15, show= "*") # show each symbol as *
pe.grid(row = 1 , column = 1)

check = Checkbutton(wn, text = "Запомнить?") # doesn't work, just for design
check.grid(row = 2, column = 0)

b = Button(wn, text= 'Login', command = click) # do click() function if button is clicked
b.grid(row = 2, column = 1, sticky = E)

wn.mainloop() 
