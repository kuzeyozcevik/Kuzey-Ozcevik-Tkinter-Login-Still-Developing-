from tkinter import *
root = Tk()
frame1 = Frame(root)
frame1.pack()
dict = {}
def tab1():
    def tab2():
        global dict
        welcome1.destroy()
        button1.destroy()
        button2.destroy()
        def back():
            username.destroy()
            password.destroy()
            button.destroy()
            username_enter.destroy()
            password_enter.destroy()
            button.destroy()
            return_button.destroy()
            tab1()
        username = Label(frame1,text="Username :")
        username.grid(row=0,column=0)
        password = Label(frame1,text="Password :")
        password.grid(row=1,column=0)
        username_enter = Entry(frame1)
        username_enter.grid(row=0,column=1)
        password_enter = Entry(frame1)
        password_enter.grid(row=1,column=1)
        def loginf():
            count = 0
            for n in dict:
                if n == username_enter.get():
                    count += 1
            if count == 1:
                if dict[username_enter.get()] == password_enter.get():
                    print("Succesfully logged in")
                else:
                    print("You couldn't logged in, your password is wrong.")
            else:
                print("You couldn't logged in, your username is wrong.")
        button = Button(frame1,text="Log In",command=loginf)
        button.grid(row=2,column=1)
        return_button = Button(frame1,text="Return",command=back)
        return_button.grid(row=2,column=2)
    def tab3():
        global dict
        welcome1.destroy()
        button1.destroy()
        button2.destroy()
        def back():
            username.destroy()
            password.destroy()
            button.destroy()
            username_enter.destroy()
            password_enter.destroy()
            button.destroy()
            return_button.destroy()
            tab1()
        username = Label(frame1,text="Username :")
        username.grid(row=0,column=0)
        password = Label(frame1,text="Password :")
        password.grid(row=1,column=0)
        username_enter = Entry(frame1)
        username_enter.grid(row=0,column=1)
        password_enter = Entry(frame1)
        password_enter.grid(row=1,column=1)
        def signupf():
            dict[username_enter.get()] = password_enter.get()
            print(dict)
            username_enter.delete(0,END)
            password_enter.delete(0,END)
        button = Button(frame1,text="Sign Up",command=signupf)
        button.grid(row=2,column=1)
        return_button = Button(frame1,text="Return",command=back)
        return_button.grid(row=2,column=2)
    welcome1 = Label(frame1,text="Welcome to Dashboard",font="Arial 14 bold")
    welcome1.grid(row=0,column=0,columnspan=3)
    button1 = Button(frame1,text="Log In",command=tab2)
    button1.grid(row=1,column=0,columnspan=1)

    button2 = Button(frame1,text="Sign In",command=tab3)
    button2.grid(row=1,column=2,columnspan=1)
tab1()
root.mainloop()
