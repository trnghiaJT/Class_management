from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style, Treeview
from tkinter.ttk import Frame, Style
import tkinter as tk
from tkinter import ttk
import sqlite3
con = sqlite3.connect("D:\code\SQLprojectt\QuanLiSinhVien1.db")

cur = con.cursor()

window= Tk()
#title
window.title("QLSV")
#createtheme
window.geometry("1000x640")

s = Style()
s.configure('My.TFrame', background='navy')
frame = Frame(window, relief=GROOVE,style='My.TFrame', borderwidth=1)
frame.pack(fill=BOTH, expand=True)
#NameStystem
namesystem= Label(frame,text="DANH SÁCH SINH VIÊN  ",width=70, height=1 ,font=("Bernard MT Condensed", 15), fg="navy",bg="orange")
namesystem.pack()

filename=PhotoImage(file="D:\code\python\Screenshot 2021-10-01 024334.png")
bg_l=Label(frame, image=filename)
bg_l.place(x=0,y=50)
window.configure(bg='navy')
# save value when input the entry
findVar = tk.StringVar()
idst = tk.StringVar()
name = tk.StringVar()
address = tk.StringVar()
classId = tk.StringVar()
def show(rows):
    tree.delete(*tree.get_children())
    for i in rows:
        tree.insert('', 'end', values=i)
def show(rows1):
    tree.delete(*tree.get_children())
    for i in rows1:
        tree.insert('', 'end', values=i)


def up():
    try:
        StudentID = idst.get()
        StudentName = name.get()
        StudentAddress = address.get()
        ClassID = inputclass.get()
        if not StudentID or not StudentName or not StudentAddress or not ClassID :
            messagebox.showerror('Lỗi người dùng', 'Vui lòng điền đủ thông tin!')
            return
        if messagebox.askyesno('Xác nhận', 'Bạn có chắc chắn về những thay đổi?'):
            sql = "UPDATE Student SET StudentName= ?, StudentAddress= ?, ClassID= ? WHERE StudentID= ?"
            val = (StudentName, StudentAddress,ClassID,StudentID)
            cur.execute(sql, val)
            con.commit()
            hienthi()
            resetForm()
    except sqlite3.Error as e:
        messagebox.showerror('Error', e)
def find():
    n = findVar.get()
    if not n:
        messagebox.showerror('Lỗi người dùng', 'Nhập ID để tìm kiếm!')
        return
    cur.execute("SELECT * FROM Student WHERE StudentID=?", [n])
    rows = cur.fetchall()
    show(rows)
    inputFind.delete(0, END)
"""def find2():
    n1 = findVar1.get()
    if not n1:
        messagebox.showerror('Lỗi người dùng', 'Nhập tên để tìm kiếm!')
        return
    cur.execute("SELECT * FROM Student WHERE ClassID=?", [n1])
    rows = cur.fetchall()
    show(rows)
    inputFind1.delete(0, END)"""
def findwindow():
    window3 = tk.Toplevel(window)
    window3.title("FIND")
    window3.configure(bg='darkorange')
    window3.geometry("400x70")
    s1 = Style()
    s1.configure('My.TFrame', background='navy')
    f = Frame(window3, relief=GROOVE,style='My.TFrame', borderwidth=1)
    f.pack(fill=BOTH, expand=True)
    global inputFind
    findst = Label(f,text="NHẬP ID SV CẦN TÌM ",font=("Times new roman", 14),fg="white",bg="dodgerblue")
    findst.pack(side=LEFT,padx=5)
    inputFind = Entry(f,textvariable=findVar,relief=GROOVE,width=45,font=("Times new roman", 15))
    inputFind.pack(side=LEFT,padx=5)
    #findbutton:
    findb= Button(window3,text=" Find ",font=("Bernard MT Condensed",14),fg="navy",bg="orange",command=find)
    findb.pack(side=RIGHT)    

def reset():
    query = ''
    cur.execute(query)
    rows = cur.fetchall()
    show(rows)

def ins():
    try:
        StudentID = idst.get()
        StudentName = name.get()
        StudentAddress = address.get()
        ClassID = inputclass.get()
        """StudentPhone=phone.get()"""
        if not StudentID or not StudentName or not StudentAddress or not ClassID :
            messagebox.showerror('Lỗi người dùng', 'Vui lòng điền đủ thông tin!')
            return
        if messagebox.askyesno('Xác nhận', 'Bạn có chắc muốn thêm thông tin này không?'):
            sql = """INSERT INTO Student (StudentID, StudentName, StudentAddress,ClassID)
                        VALUES (?, ?, ?, ?)"""
            val = (StudentID, StudentName, StudentAddress,ClassID)
            cur.execute(sql, val)
            con.commit()
            hienthi()
            resetForm()
            """resetCombobox()"""
    except sqlite3.Error as e:
        messagebox.showerror('Error', e)


def dele():
    try:
        StudentID = idst.get()
        if not StudentID:
            messagebox.showerror('Lỗi người dùng', 'Vui lòng nhập ID cần xóa!')
            return
        if messagebox.askyesno('Xác nhận', 'Bạn có chắc muốn xóa thông tin này không?'):
            query = "DELETE FROM Student WHERE StudentID=?"
            cur.execute(query, [StudentID])
            con.commit()
            hienthi()
            resetForm()
    except sqlite3.Error as e:
        messagebox.showerror('Error', e)

def hienthi():
        n2=combo.get()
        if not n2:
            messagebox.showerror('Lỗi người dùng', 'Vui lòng chọn mã lớp cần lọc!')
        if n2=="Hiển thị tất cả":
           query = 'SELECT * FROM Student'
           rows=cur.execute(query)
           show(rows)
        if n2=="L01":
           cur.execute('SELECT * FROM Student WHERE ClassID=?',[n2])
           rows = cur.fetchall()
           show(rows)
        elif n2=="L02":
           cur.execute('SELECT * FROM Student WHERE ClassID=?',[n2])
           rows = cur.fetchall()
           show(rows) 
        elif n2=="L03":
           cur.execute('SELECT * FROM Student WHERE ClassID=?',[n2])
           rows = cur.fetchall()
           show(rows)
        elif n2=="L04":
           cur.execute('SELECT * FROM Student WHERE ClassID=?',[n2])
           rows = cur.fetchall()
           show(rows)
        elif n2=="L05":
           cur.execute('SELECT * FROM Student WHERE ClassID=?',[n2])
           rows = cur.fetchall()
           show(rows)

 
def resetForm():
    inputadd.delete(0, END)
    inputnamest.delete(0, END)
    inputclass.delete(0, END)
    inputidst.delete(0,END)
"""def combo_values_input():

    query1 = cur.execute('SELECT ClassID FROM Student')

    data = []
    for rows1 in cur.fetchall():
        data.append(rows1[0])
    return datA
def resetForm1():
    data.delete(0, END)
def resetCombobox():
    s=set(combo_values_input())
    l=list(s)
    combo['values'] = l """   
"""# save value when input the entry
findVar = tk.StringVar()
idst = tk.StringVar()
name = tk.StringVar()
address = tk.StringVar()
classId = tk.StringVar()"""
#Reset
but6= Button(window,text="  RESET  ",font=("Bernard MT Condensed", 15),relief=GROOVE, fg="navy",bg="orange",command=reset)
but6.pack(side=RIGHT)
"""#FINDNAME
but5= Button(window,text="  FIND  ",font=("Bernard MT Condensed", 15),relief=GROOVE, fg="navy",bg="orange",command=find2)
but5.place(x=907,y=495)
findst1 = Label(window,text="NHẬP TÊN LỚP CẦN TÌM",font=("Times new roman", 12),relief=FLAT, fg="white",bg="navy")
findst1.place(x=700,y=442)
inputFind1 = Entry(window,textvariable=findVar1,width=45)
inputFind1.place(x=700,y=471)"""
#FINDWITHID
but= Button(window,text="  FIND  ",font=("Bernard MT Condensed", 15),relief=GROOVE, fg="navy",bg="orange",command=findwindow)
but.pack(side=RIGHT)

"""#Dienthoai
phonenum = Label(window,text="DTSV   ",font=("Times new roman", 12), fg="white",bg="navy")
phonenum.place(x=85,y=600)
inputnum = Entry(window,textvariable=phone,font=("Times new roman", 12),width=57)
inputnum.place(x=150,y=600)"""

"""#UP
but1= Button(window,text=" UPDATE ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=windowinsert)
but1.place(x=100,y=300)
#DEL
but2= Button(window,text=" DELETE ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=windowinsert)
but2.place(x=300,y=300)"""


#comboboxCLASSID
combo = ttk.Combobox(frame, width=50, height=20)
combo.set("")
class1=("Hiển thị tất cả","L01","L02","L03","L04","L05")
combo.pack(side=TOP)
combo['values'] = class1
#SearchInformation
but7= Button(window,text="SHOW",font=("Bernard MT Condensed", 8),relief=GROOVE, fg="navy",bg="orange",command=hienthi)
but7.place(x=665,y=30)
#stylestreeview

styletree=ttk.Style()

styletree.configure("Treeview",
                background="#dcdcdc",
                foreground="black",
                fieldbackground="sliver")
#styleSelect
styletree.map('Treeview',
          background=[('selected','navy')])

# create table data
tree = Treeview(frame,columns=(1, 2, 3, 4), show="headings", height=13)
tree.pack()


# add heading
tree.heading(1, text="MSSV")
tree.heading(2, text="TEN SV")
tree.heading(3, text="DCSV")
tree.heading(4, text="MA LOP")

classinoption=("L01","L02","L03","L04","L05")
def windowinsert():
    window2 = tk.Toplevel(window)
    window2.title("INSERT")
    window2.geometry("450x270")
    s = Style()
    s.configure('My.TFrame', background='navy')
    frame = Frame(window2, relief=GROOVE,style='My.TFrame', borderwidth=1)
    frame.pack(fill=BOTH, expand=True)
    window2.configure(bg='darkorange')
    global inputnamest
    global inputidst
    global inputclass
    global inputadd

    #INSERT
    but3= Button(window2,text=" INSERT ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command= ins)
    but3.pack(side=RIGHT)
    #NAMEST
    namest = Label(frame,text="TENSV ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    namest.place(x=0,y=15)
    inputnamest = Entry(frame,textvariable=name,font=("Times new roman", 12),bd=2,width=40)
    inputnamest.pack(pady=15)
    #ID
    Idst = Label(frame,text="MSSV   ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    Idst.place(x=0,y=68+4)
    inputidst = Entry(frame,textvariable=idst,font=("Times new roman", 12),bd=2,width=40)
    inputidst.pack(pady=15)
    #class
    classid = Label(frame,text="MALOP",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    classid.place(x=0,y=68+53+5)
    inputclass = ttk.Combobox(frame,font=("Times new roman", 12),width=38)
    inputclass['value']=classinoption
    inputclass.insert(0,combo.get())
    inputclass.config(state=DISABLED)
    inputclass.pack(pady=15)
    #Diachi
    Address = Label(frame,text="DCSV   ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    Address.place(x=0,y=68+53*2+7)
    inputadd = Entry(frame,textvariable=address,font=("Times new roman", 12),width=40,bd=2)
    inputadd.pack(pady=15)
    #quit
    but1= Button(window2,text=" QUIT ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=window2.destroy)
    but1.pack(side=LEFT)
def windowinsert1():
    window3 = tk.Toplevel(window)
    window3.title("UPDATE")
    window3.geometry("450x270")
    s1 = Style()
    s1.configure('My.TFrame', background='navy')
    frame2 = Frame(window3, relief=GROOVE,style='My.TFrame', borderwidth=1)
    frame2.pack(fill=BOTH, expand=True)
    window3.configure(bg='darkorange')
    global inputnamest
    global inputidst
    global inputclass
    global inputadd
    #UP
    but1= Button(window3,text=" UPDATE ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=up)
    but1.pack(side=RIGHT)
    #NAMEST
    namest = Label(frame2,text="TENSV ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    namest.place(x=0,y=15)
    inputnamest = Entry(frame2,textvariable=name,font=("Times new roman", 12),bd=2,width=40)
    inputnamest.pack(pady=15)
    #ID
    Idst = Label(frame2,text="MSSV   ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    Idst.place(x=0,y=68+4)
    inputidst = Entry(frame2,textvariable=idst,font=("Times new roman", 12),bd=2,width=40)
    inputidst.pack(pady=15)
    #class
    classid = Label(frame2,text="MALOP",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    classid.place(x=0,y=68+53+5)
    inputclass = ttk.Combobox(frame2,font=("Times new roman", 12),width=38)
    inputclass['value']=classinoption
    inputclass.insert(0,combo.get())
    inputclass.pack(pady=15)
    #Diachi
    Address = Label(frame2,text="DCSV   ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    Address.place(x=0,y=68+53*2+7)
    inputadd = Entry(frame2,textvariable=address,font=("Times new roman", 12),width=40,bd=2)
    inputadd.pack(pady=15)
    #quit
    but1= Button(window3,text=" QUIT ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=window3.destroy)
    but1.pack(side=LEFT)
def windowinsert2():
    window4 = tk.Toplevel(window)
    window4.title("DELETE")
    s2 = Style()
    s2.configure('My.TFrame', background='navy')
    frame3 = Frame(window4, relief=GROOVE,style='My.TFrame', borderwidth=1)
    frame3.pack(fill=BOTH, expand=True)
    window4.configure(bg='darkorange')
    global inputidst
    #DEL
    but2= Button(window4,text=" DELETE ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=dele)
    but2.pack(side=RIGHT)
    #ID
    Idst = Label(frame3,text="MSSV   ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
    Idst.pack(side=LEFT)
    inputidst = Entry(frame3,textvariable=idst,font=("Times new roman", 12),bd=2,width=40)
    inputidst.pack(pady=15)
    #quit
    but1= Button(window4,text=" QUIT ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=window4.destroy)
    but1.pack(side=LEFT)
#INSERTMAINWINDOW
but3= Button(window,text=" INSERT ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command= windowinsert)
but3.pack(side=RIGHT)
#UPDATEMAINWINDOW
but4= Button(window,text=" UPDATE ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command= windowinsert1)
but4.pack(side=RIGHT)
#DELETEMAINWINDOW
but5= Button(window,text=" DELETE",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command= windowinsert2)
but5.pack(side=RIGHT)
#QUITMAINWINDOW
but12 = Button(window, text=" QUIT ", font=("Bernard MT Condensed", 15), fg="navy", relief=GROOVE, bg="orange",command=window.destroy)
but12.pack(side=LEFT)
# initial table data
query = 'SELECT * FROM Student'
cur.execute(query)
rows = cur.fetchall()
show(rows)
def getDataRow(event):
    rowid = tree.identify_row(event.y)
    item = tree.item(tree.focus())
    idst.set(item['values'][0])
    name.set(item['values'][1])
    address.set(item['values'][2])
    combo.set(item['values'][3])
tree.bind('<Double 1>', getDataRow)

#initial table data
query1 = ''
cur.execute(query1)
rows1 = cur.fetchall()
show(rows1)
window.mainloop()

"""submit_button = tkinter.Button(root, text='Submit' , command=print_answers)
submit_button.pack()"""

"""#UP
but1= Button(window2,text=" UPDATE ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=up)
but1.pack(side=RIGHT)
#DEL
but2= Button(window2,text=" DELETE ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=dele)
but2.pack(side=RIGHT)
#INSERT
but3= Button(window2,text=" INSERT ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command= ins)
but3.pack(side=RIGHT)
#NAMEST
namest = Label(frame,text="TENSV ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
namest.place(x=0,y=15)
inputnamest = Entry(frame,textvariable=name,font=("Times new roman", 12),width=57)
inputnamest.pack(pady=15)
#ID
Idst = Label(frame,text="MSSV   ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
Idst.place(x=0,y=68)
inputidst = Entry(frame,textvariable=idst,font=("Times new roman", 12),width=57)
inputidst.pack(pady=15)
#class
classid = Label(frame,text="MALOP",font=("Times new roman", 11), fg="white",bg="dodgerblue")
classid.place(x=0,y=68+53)
inputclass = Entry(frame,textvariable=classId,font=("Times new roman", 12),width=57)
inputclass.pack(pady=15)
#Diachi
Address = Label(frame,text="DCSV   ",font=("Times new roman", 11), fg="white",bg="dodgerblue")
Address.place(x=0,y=68+53*2)
inputadd = Entry(frame,textvariable=address,font=("Times new roman", 12),width=57)
inputadd.pack(pady=15)
#quit
but1= Button(window2,text=" QUIT ",font=("Bernard MT Condensed", 15), fg="navy",relief=GROOVE,bg="orange",command=window2.destroy)
but1.pack(side=LEFT)"""
"""submit_button = tkinter.Button(root, text='Submit' , command=print_answers)
submit_button.pack()"""
