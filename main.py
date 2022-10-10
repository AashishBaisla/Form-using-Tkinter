from tkinter import *
import mysql.connector
from tkcalendar import Calendar, DateEntry

window = Tk()
window.resizable(True,True)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.minsize(750,screen_height-250)
window.maxsize()
window.title("Registration Form - Created by Aashish Baisla")
window.columnconfigure(0, weight=0, minsize=150)
window.columnconfigure(1, weight=1, minsize=100)
window.columnconfigure(2, weight=1, minsize=100)
window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13], weight=1)
window.config(padx=20)
window.wm_iconbitmap('form_icon.ico')
screen_width = window.winfo_screenwidth()
screen_width = window.winfo_screenheight()
#window.attributes('-fullscreen', True)
#window.config(bg = 'green')
#window.wm_attributes('-transparentcolor','yellow')

#Get all values from Registration Form
def store_in_DB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="registrations_2022"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO reg_details (First_Name, Last_Name, Gender, Date_of_Birth, Email, Contact_No, Blood_Group, Country, State, Address, Skills) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (first_name.get(), last_name.get(), gender.get(), sel.get(), email.get(), contact.get(), blood.get(), country.get(), state.get(),
           Entry_Address.get("1.0", END), f"{var_python.get()} {var_C.get()} {var_Java.get()} {var_SQL.get()}")

    mycursor.execute(sql, val)
    mydb.commit()

    Label_Submit = Label(text="Details Submitted!", fg="blue", font="Ariel 15")
    Label_Submit.grid(row=13, column=0, columnspan=4)

def check_entries(event=None):
    if ( first_name.get()=='' or last_name.get()=='' or gender.get()=='' or email.get()=='' or contact.get()=='' or blood.get()==''
            or country.get()=='' or state.get()=='' or Entry_Address.get("1.0", END)=='' or f"{var_python.get()} {var_C.get()} {var_Java.get()} {var_SQL.get()}"=='   '):

        Label_Error = Label(text="Please fill all Details!", fg="red", font="Ariel 12", pady=5)
        Label_Error.grid(row=13, column=0, columnspan=4)
        def delay_in_label(l):
            l.after(2000, l.destroy)
        delay_in_label(Label_Error)

    else:
        store_in_DB()

def clear_all_details():
    first_name.set(''), last_name.set(''), gender.set(''), sel.set('YYYY-MM-DD'), email.set(''), contact.set(''),
    blood.set(''), country.set(''), state.set(''), Entry_Address.delete(1.0, END),
    var_python.set(''), var_C.set(''), var_Java.set(''), var_SQL.set('')

#Title
Title_Label = Label(window, text="Registration Form - Created by Aashish Baisla", fg="white", bg="green",font="Arial 14", padx=6, pady=6)
Title_Label.grid(row=0, column=0, columnspan=4, pady=10)

#Variables for storing inserted data
first_name = StringVar()
last_name = StringVar()
gender = StringVar()
sel= StringVar()
email = StringVar()
contact = StringVar()
blood = StringVar()
country = StringVar()
state = StringVar()
#Variables for storing checkbutton values
var_python = StringVar()
var_C = StringVar()
var_Java = StringVar()
var_SQL = StringVar()

#Label & Entry
Label_Name = Label(window, text="First Name").grid(row=1, column=0, padx=4, pady=4, sticky="w")
Entry_Name = Entry(window,textvariable=first_name, borderwidth=2, border=3, fg="green").grid(row=1, column=1, columnspan=2, padx=4, pady=4, ipady=7, sticky="we")

Label_Lang = Label(window, text="Last Name").grid(row=2, column=0, padx=4, pady=4, sticky="w")
Entry_Lang = Entry(window, textvariable=last_name, borderwidth=2, border=3, fg="green").grid(row=2, column=1, columnspan=2, padx=4, pady=4, ipady=7, sticky="we")

Label_Gender = Label(window, text="Gender").grid(row=3, column=0, padx=4, pady=4, sticky="w")
Entry_Gender1 = Radiobutton(window, text="Male", fg="green", variable=gender, value="Male").grid(row=3, column=1, pady=6, sticky="w")
Entry_Gender2 = Radiobutton(window, text="Female", fg="green", variable=gender, value="Female").grid(row=3, column=1, padx=100, sticky="e")
Entry_Gender3 = Radiobutton(window, text="Other", fg="green", variable=gender, value="Other").grid(row=3, column=2, sticky="w")

Label_Date = Label(window, text="Date of Birth").grid(row=4, column=0, padx=4, pady=4, sticky="w")
Entry_Date = DateEntry(window, textvariable=sel, locale='en_US', date_pattern='YYYY-MM-DD')
Entry_Date.grid(row=4, column=1, columnspan=2, padx=4, pady=4, ipady=7, sticky="we")

Label_Email = Label(window, text="Email").grid(row=5, column=0, padx=4, pady=4, sticky="w")
Entry_Email = Entry(window, textvariable=email, borderwidth=2, border=3, fg="green").grid(row=5, column=1, columnspan=2, padx=4, pady=4, ipady=7, sticky="we")

Label_Contact = Label(window, text="Contact No").grid(row=6, column=0, padx=4, pady=4, sticky="w")
Entry_Contact = Entry(window, textvariable=contact, borderwidth=2, border=3, fg="green").grid(row=6, column=1, columnspan=2, padx=4, pady=4, ipady=7, sticky="we")

Label_Blood_Grp = Label(window, text="Blood Group").grid(row=7, column=0, padx=4, pady=4, sticky="w")
Entry_Blood_Grp = Entry(window, textvariable=blood, borderwidth=2, border=3, fg="green").grid(row=7, column=1, columnspan=2, padx=4, pady=4, ipady=7, sticky="we")

Label_Country = Label(window, text="Country").grid(row=8, column=0, padx=4, pady=4, sticky="w")
#Entry_Country = Entry(window, textvariable=country, borderwidth=2, border=3, fg="green").grid(row=8, column=1, columnspan=2, padx=4, pady=4, ipady=7, sticky="we")

choices = ['India', 'Australia', 'United States', 'United Kingdom', 'Germany', 'Japan', 'France', 'Russia']
Entry_Country = OptionMenu(window, country, *choices)
Entry_Country.grid(row=8, column=1, ipady=4, sticky="we")
Entry_Country.config(bg="white")
Entry_Country.config(fg="green")

Label_State = Label(window, text="State").grid(row=9, column=0, padx=4, pady=4, sticky="w")
Entry_State = Entry(window, textvariable=state , borderwidth=2, border=3, fg="green").grid(row=9, column=1, columnspan=2, padx=4, pady=4, ipady=7, sticky="we")

Label_Address = Label(window, text="Address").grid(row=10, column=0, padx=4, pady=4, sticky="w")
Entry_Address = Text(window, borderwidth=2, border=3, fg="green", height=2, wrap='word')
Entry_Address.grid(row=10, column=1, columnspan=2, padx=4, pady=4, sticky="we")
sb = Scrollbar(window)
sb.grid(row=10, column=3, sticky="w")
Entry_Address.config(yscrollcommand=sb.set)
sb.config(command = Entry_Address.yview)

Label_Skills = Label(window, text="Skills").grid(row=11, column=0, padx=4, pady=4, sticky="w")
Skills_Check1 = Checkbutton(window, text="Python",fg="green", variable=var_python, onvalue="Python", offvalue='').grid(row=11, column=1,sticky="w")
Skills_Check2 = Checkbutton(window, text="C/C++",fg="green", variable=var_C, onvalue="C/C++", offvalue='').grid(row=11, column=1, padx=80, sticky="e")
Skills_Check3 = Checkbutton(window, text="Java",fg="green", variable=var_Java, onvalue="Java", offvalue='').grid(row=11, column=2, padx=80, sticky="w")
Skills_Check4 = Checkbutton(window, text="SQL",fg="green", variable=var_SQL, onvalue="SQL", offvalue='').grid(row=11, column=2, sticky="e")

#Button to Submit the Registration form
Button_Submit = Button(window, text="SUBMIT", bg="red", fg="white", width=10, font="Arial 11 bold",command=check_entries, borderwidth=5)
Button_Submit.grid(row=12, column=1,padx=100, pady=10)

Button_Clear = Button(window, text="Clear", bg="red", fg="white", width=10, font="Arial 11 bold",command=clear_all_details, borderwidth=5)
Button_Clear.grid(row=12, column=2,padx=100, pady=10)

window.mainloop()