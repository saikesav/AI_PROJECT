from logpy import Relation, facts, run, var, conde, fact
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox


class color:
    Purple = '\033[95m'
    Cyan = '\033[96m'
    Darkcyan = '\033[36m'
    Blue = '\033[94m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Red = '\033[91m'
    Bold = '\033[1m'
    Underline = '\033[4m'
    End = '\033[0m'




def create_frames(self):
   self.left_frame = tk.Frame(width=500, height=1040, background='green')
   self.left_frame.grid(row=0, column=0)

   self.right_frame = tk.Frame(width=500, height=1040, background='red')
   self.right_frame.grid(row=0, column=1)



class start(tk.Frame):
   def __init__(self, master):
       self.master = master
       tk.Frame.__init__(self, self.master)
       self.configure_gui()
       self.create_widgets()

   def CHOOSE(self):
       MainApplication(root)
       root.mainloop()


   def configure_gui(self):
       self.master.title(' FAMILY RELATIONSHIP')
       self.master.geometry('1000x500')
       self.master.resizable(0, 0)

   def create_widgets(self):
       self.create_frames()
       self.create_buttons()

   def create_frames(self):
       self.left_frame = tk.Frame(width=500, height=1040, background='green')
       self.left_frame.grid_propagate(0)
       self.left_frame.grid(row=0, column=0)

       self.right_frame = tk.Frame(width=500, height=1040, background='green')
       self.right_frame.grid_propagate(0)
       self.right_frame.grid(row=0, column=1)

   def create_buttons(self):
       self.create_left_frame_buttons()
       self.create_right_frame_buttons()


   def create_left_frame_buttons(self):
       self.button1 = tk.Button(self.left_frame, text='START',height=10,width=30,command=self.CHOOSE)
       self.button1.grid(row=0, column=0, padx=100, pady=20)





   def create_right_frame_buttons(self):
       self.button1 = tk.Button(self.right_frame, text='EXIT',height=10,width=30,command=quit)
       self.button1.grid(row=0, column=0, padx=20, pady=20)







class MainApplication(tk.Frame):
   def __init__(self, master):
       self.master = master
       tk.Frame.__init__(self, self.master)
       self.configure_gui()
       self.create_widgets()

   def configure_gui(self):
       self.master.title(' FAMILY RELATIONSHIP')
       self.master.geometry('1000x800')
       self.master.resizable(0, 0)

   def create_widgets(self):
       self.create_frames()
       self.create_buttons()

   def create_frames(self):
       self.left_frame = tk.Frame(width=500, height=1040, background='red')
       self.left_frame.grid_propagate(0)
       self.left_frame.grid(row=0, column=0)

       self.right_frame = tk.Frame(width=500, height=1040, background='gold2')
       self.right_frame.grid_propagate(0)
       self.right_frame.grid(row=0, column=1)

   def create_buttons(self):
       self.create_left_frame_buttons()
       self.create_right_frame_buttons()

   def create_left_frame_buttons(self):
       self.button1 = tk.Button(self.left_frame, text='JOHN',height=3,width=10,command=choice1)
       self.button1.grid(row=0, column=0, padx=100, pady=20)

       self.button2 = tk.Button(self.left_frame, text='WILLIAM',height=3,width=10,command=choice2)
       self.button2.grid(row=1, column=0, padx=30, pady=20)

       self.button1 = tk.Button(self.left_frame, text='DAVID',height=3,width=10,command=choice3)
       self.button1.grid(row=2, column=0, padx=30, pady=20)

       self.button2 = tk.Button(self.left_frame, text='ADAM',height=3,width=10,command=choice4)
       self.button2.grid(row=3, column=0, padx=30, pady=20)

       self.button1 = tk.Button(self.left_frame, text='CHRIS',height=3,width=10,command=choice5)
       self.button1.grid(row=4, column=0, padx=30, pady=20)

       self.button2 = tk.Button(self.left_frame, text='WYANE',height=3,width=10,command=choice6)
       self.button2.grid(row=5, column=0, padx=30, pady=20)

       self.button1 = tk.Button(self.left_frame, text='NEIL',height=3,width=10,command=choice7)
       self.button1.grid(row=6, column=0, padx=30, pady=20)

       self.button2 = tk.Button(self.left_frame, text='PETER',height=3,width=10,command=choice8)
       self.button2.grid(row=7, column=0, padx=30, pady=20)




   def create_right_frame_buttons(self):
       self.button1 = tk.Button(self.right_frame, text='MEGAN',height=3,width=10,command=choice9)
       self.button1.grid(row=0, column=0, padx=20, pady=20)

       self.button2 = tk.Button(self.right_frame, text='EMMA',height=3,width=10,command=choice10)
       self.button2.grid(row=1, column=0, padx=70,pady=20)

       self.button1 = tk.Button(self.right_frame, text='OLIVIA',height=3,width=10,command=choice11)
       self.button1.grid(row=2, column=0, padx=20, pady=20)

       self.button2 = tk.Button(self.right_frame, text='SOPHIA',height=3,width=10,command=choice12)
       self.button2.grid(row=3, column=0, padx=70,pady=20)

       self.button1 = tk.Button(self.right_frame, text='JULIE',height=3,width=10,command=choice13)
       self.button1.grid(row=4, column=0, padx=20, pady=20)

       self.button2 = tk.Button(self.right_frame, text='STEPHANE',height=3,width=10,command=choice14)
       self.button2.grid(row=5, column=0, padx=70,pady=20)

       self.button1 = tk.Button(self.right_frame, text='LILY',height=3,width=10,command=choice15)
       self.button1.grid(row=6, column=0, padx=20, pady=20)

       self.button2 = tk.Button(self.right_frame, text='TIFFANY',height=3,width=10,command=choice16)
       self.button2.grid(row=7, column=0, padx=20,pady=20)


class relation(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.master.title(' FAMILY RELATIONSHIP')
        self.master.geometry('1000x600')
        self.master.resizable(0, 0)

    def create_widgets(self):
        self.create_frames()
        self.create_buttons()

    def create_frames(self):
        self.left_frame = tk.Frame(width=500, height=1040, background='red')
        self.left_frame.grid_propagate(0)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = tk.Frame(width=500, height=1040, background='gold2')
        self.right_frame.grid_propagate(0)
        self.right_frame.grid(row=0, column=1)

    def create_buttons(self):
        self.create_left_frame_buttons()
        self.create_right_frame_buttons()

    def create_left_frame_buttons(self):
        self.button1 = tk.Button(self.left_frame, text='PARENT', height=3, width=13)
        self.button1.grid(row=0, column=0, padx=100, pady=20)

        self.button2 = tk.Button(self.left_frame, text='GRANDPARENT', height=3, width=13)
        self.button2.grid(row=1, column=0, padx=30, pady=20)

        self.button1 = tk.Button(self.left_frame, text='UNCLE', height=3, width=13)
        self.button1.grid(row=2, column=0, padx=30, pady=20)

        self.button2 = tk.Button(self.left_frame, text='SIBLING', height=3, width=13)
        self.button2.grid(row=3, column=0, padx=30, pady=20)

    def create_right_frame_buttons(self):
        self.button1 = tk.Button(self.right_frame, text='AUNTY', height=3, width=13, )
        self.button1.grid(row=0, column=0, padx=20, pady=20)

        self.button2 = tk.Button(self.right_frame, text='CHILDREN', height=3, width=13, )
        self.button2.grid(row=1, column=0, padx=70, pady=20)

        self.button1 = tk.Button(self.right_frame, text='COUPLE', height=3, width=13, )
        self.button1.grid(row=2, column=0, padx=20, pady=20)


choice=None
def choice1():
    global choice
    choice='john'
    relation(root)
    root.mainloop()
def choice2():
    global choice
    choice=' william'
    choice = None
    relation(root)
    root.mainloop()
def choice3():
    global choice
    choice = ' david'
    relation(root)
    root.mainloop()
def choice4():
    global choice
    choice = 'adam '
def choice5():
    global choice
    choice='chris'
def choice6():
    global choice
    choice = 'wyane'
    relation(root)
    root.mainloop()

def choice7():
    global choice
    choice=' neil'
    relation(root)
    root.mainloop()

def choice8():
    global choice
    choice = ' peter'
    relation(root)
    root.mainloop()

def choice9():
    global choice
    choice = 'megan'
    relation(root)
    root.mainloop()

def choice10():
    global choice
    choice = 'emma'
    choice = None
    relation(root)
    root.mainloop()

def choice11():
    global choice
    choice = 'olivia'
    relation(root)
    root.mainloop()

def choice12():
    global choice
    choice = 'sophia '
    relation(root)
    root.mainloop()

def choice13():
    global choice
    choice = 'julie'
    relation(root)
    root.mainloop()

def choice14():
    global choice
    choice = 'stephane'
    relation(root)
    root.mainloop()

def choice15():
    global choice
    choice = 'lily'
    choice = None
    relation(root)
    root.mainloop()

def choice16():
    global choice
    choice = 'tiffany'
    relation(root)
    root.mainloop()

def start_main():
    def parents(x, y):
        return conde([Father(x, y)], [Mother(x, y)])

    def grandparents(x, y):
        z = var()
        return conde((parents(x, z), parents(z, y)))

    def grandfather(x, y):
        z = var()
        return conde((grandparents(x, y), Male(x)))

    def grandmother(x, y):
        z = var()
        return conde((grandparents(x, y), Female(x)))

    def uncle(m, y):
        z = var()
        x = var()
        return conde((Father(x, z), Father(x, m), Father(z, y), Male(m)))

    def sibling(x, y):
        z = var()
        return conde((parents(z, x), parents(z, y)))

    def brother(x, y):
        z = var()
        return conde((parents(z, x), parents(z, y), Male(x)))

    def sister(x, y):
        z = var()
        return conde((parents(z, x), parents(z, y), Female(x)))

    def aunty(x, y):
        z = var()
        return conde((uncle(z, y), Couple(z, x), Female(x)))

    def children(x, y):
        return ((parents(x, y)))

    def son(x, y):
        return ((parents(x, y), Male(y)))

    def daughter(x, y):
        return ((parents(x, y), Female(y)))

    global choice

    Father = Relation()

    Mother = Relation()

    Male = Relation()

    Female = Relation()

    Couple = Relation()

    facts(Couple, ('john', 'megan'),
          ('william', 'emma'),
          ('david', 'olivia'),
          ('adam', 'lily'))
    facts(Father, ('john', 'william'),
          ('john', 'david'),
          ('john', 'adam'),
          ('william', 'chris'),
          ('william', 'stephaine'),
          ('david', 'wayne'),
          ('david', 'tiffany'),
          ('david', 'julie'),
          ('david', 'neil'),
          ('david', 'peter'),
          ('adam', 'sophia'))

    facts(Mother, ('megan', 'william'),
          ('megan', 'david'),
          ('megan', 'adam'),
          ('emma', 'chris'),
          ('emma', 'stephaine'),
          ('olivia', 'wayne'),
          ('olivia', 'tiffany'),
          ('olivia', 'julie'),
          ('olivia', 'neil'),
          ('olivia', 'peter'),
          ('lily', 'sophia'))

    fact(Male, 'john')
    fact(Male, 'william')
    fact(Male, 'david')
    fact(Male, 'adam')
    fact(Male, 'chris')
    fact(Male, 'wayne')
    fact(Male, 'neil')
    fact(Male, 'peter')

    fact(Female, 'megan')
    fact(Female, 'emma')
    fact(Female, 'tiffany')
    fact(Female, 'julie')
    fact(Female, 'olivia')
    fact(Female, 'sophia')
    fact(Female, 'lily')
    fact(Female, 'stephaine')

    x = var()
    y = var()
    z = var()
    #
    # print(
    #     color.Bold + "---------------------------------Welcome to Relation Predicting Program------------------------------" + color.End + "\n\n")
    # print(
    #     color.Bold + "-----------------------------------------------------------------------------Created by:" + color.End,
    #     color.Darkcyan + color.Bold + "RUPESH YADAV" + color.End, "\n\n")
    # print("-----------------------------------------------------------------------------------------------------")
    # print(color.Bold + color.Blue + "Enter The Name Below From Above To Know There Realtives" + color.End)
    # print("-----------------------------------------------------------------------------------------------------")
    # print(color.Red + "1)JOHN\n2)WILLIAM\n3)DAVID\n4)ADAM\n5)CHRIS\n6)WAYNE\n7)NEIL\n8)PETER\n" + color.End)
    # print(
    #     color.Green + "9)MEGAN\n10)EMMA\n11)TIFFANY\n12)JULIE\n13)OLIVIA\n14)SOPHIA\n15)LILY\n16)STEPHAINE" + color.End)

    NameList = ['john', 'megan',
                'william', 'emma',
                'david', 'olivia',
                'adam', 'lily',
                'peter', 'neil',
                'sophia', 'julie',
                'tiffany', 'stephaine',
                'wayne', 'chris']

    name = input()
    FakeName = name.upper()
    name = name.lower()
    if name in NameList:
        print(color.Red + "Which Realtion Of" + color.End,
              color.Cyan + color.Bold + color.Underline + FakeName + color.End,
              color.Red + "You want to know?" + color.End)

        print(
            color.Blue + "1)PARENT\n2)SIBLING\n3)GRANDPARENT\n)4)UNCLE\n5)AUNTY\n6)CHILDREN\n7)COUPLE\n\n" + color.End)

        Relat = input()
        Relat = Relat.lower()
        if Relat == 'parent':
            print(
                color.Yellow + "Press 1 To Know The Name of Both Parent\nPress 2 To Know The Name Of Mother\nPress 3 To Know The Name Of Father" + color.End)
            option = int(input())
            if option == 1:
                out = (run(0, x, parents(x, name)))
            elif option == 2:
                out = (run(0, x, Mother(x, name)))
            else:
                out = (run(1, x, Father(x, name)))
            if len(out) == 0:
                print(color.Cyan + color.Bold + color.Underline + FakeName + color.End,
                      color.Green + "Parent Details Not In DataBase---SORRY" + color.End)
            else:
                print(out)
        elif Relat == 'sibling':
            print(
                color.Yellow + "Press 1 To Know The Name of Both Gender Sibling\nPress 2 To Know The Name Of Sisters\nPress 3 To Know The Name Of Brother" + color.End)
            option = int(input())
            if option == 1:
                out = (run(0, x, sibling(x, name)))
            elif option == 2:
                out = (run(1, x, sister(x, name)))
            else:
                out = (run(1, x, brother(x, name)))
            list1 = list(out)

            if name in list1:
                list1.remove(name)

            if len(list1) == 0:
                print(color.Cyan + color.Bold + color.Underline + FakeName + color.End,
                      color.Green + "Does not have Entered type sibling ---SORRY" + color.End)
            else:
                print(list1)
        elif Relat == 'grandparent':
            print(
                color.Yellow + "Press 1 To Know The Name of Both Grandmaa and Grandpaa\nPress 2 To Know The Name Of GrandFather\nPress 3 To Know The Name Of GrandMother" + color.End)
            option = int(input())
            if option == 1:
                out = (run(0, x, grandparents(x, name)))
            elif option == 2:
                out = (run(1, x, grandfather(x, name)))
            else:
                out = (run(1, x, grandmother(x, name)))
            list1 = list(out)

            if name in list1:
                list1.remove(name)

            if len(list1) == 0:
                print(color.Cyan + color.Bold + color.Underline + FakeName + color.End,
                      color.Green + "Does not have GrandParent data ---SORRY" + color.End)
            else:
                print(list1)
        elif Relat == 'uncle':
            out1 = run(1, x, Father(x, name))
            out = run(0, x, uncle(x, name))
            a = out1[0]
            list1 = list(out)
            if a in list1:
                list1.remove(a)
            print(list1)
        elif Relat == 'aunty':
            out = (run(0, x, aunty(x, name)))
            out1 = run(0, x, Mother(x, name))
            list1 = list(out)
            a = out1[0]
            if a in list1:
                list1.remove(a)
            print(list1)
        elif Relat == 'children':
            print(run(0, x, children(name, x)))
        elif Relat == 'couple':
            print(run(1, x, Couple(x, name)))
        else:
            print(color.Red + "The Relation You Is Wrong Or May Not Be In Database" + color.End)

    else:
        print(color.Blue + "The Name" + color.End, color.Red + color.Underline + FakeName + color.End,
              color.Blue + "You Have Entered Is Not In The DataBase" + color.End)

def create_buttons(self):
   self.create_left_frame_buttons()
   self.create_right_frame_buttons()

def create_left_frame_buttons(self):
   self.button1 = tk.Button(self.left_frame, text='Button1')
   self.button1.grid(row=0, column=0, padx=30, pady=20)

   self.button2 = tk.Button(self.left_frame, text='Button2')
   self.button2.grid(row=1, column=0, padx=30, pady=20)

def create_right_frame_buttons(self):
   self.button1 = tk.Button(self.right_frame, text='Button3')
   self.button1.grid(row=0, column=0, padx=20, pady=50)

   self.button2 = tk.Button(self.right_frame, text='Button4')

   self.button2.grid(row=0, column=0, padx=70, pady=50)





root = tk.Tk()
main_app =  start(root)
root.mainloop()