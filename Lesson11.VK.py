import vk_requests
import auth, requests
from tkinter import*
api = vk_requests.create_api(app_id= 5944123, login=auth.tel, password=auth.password) # connect to vk


def s1():
    idd = enID.get()
    result = api.users.get(user_ids=idd) # use USERS.GET() if u know ID of user
    n = result[0]['first_name']
    s = result[0]['last_name']
    name.config(text=n+" " +s)

def s2():
    qq = enQ.get()
    c = enC.get()
    if c == "":
        c = 5
    print(api.users.search(q=qq, count=c)) # use USERS.SEARCH() if u don't know ID of user
    
wn = Tk()
wn.title("Search")

fr1 = Frame(wn)
fr1.grid(row=0, column=0)

fr2 = Frame(wn)
fr2.grid(row=0, column=1)


label = Label(fr1, text="ID: ")
label.pack()

enID = Entry(fr1)
enID.pack()

b1 = Button(fr1, text="Search", command=s1)
b1.pack()

name = Label(fr1)
name.pack()


label = Label(fr2, text="Q: ")
label.pack()

enQ = Entry(fr2)
enQ.pack()

label = Label(fr2, text="Count: ")
label.pack()

enC = Entry(fr2)
enC.pack()

b2 = Button(fr2, text="Search", command=s2)
b2.pack()

"""
result = api.users.get(user_ids=1, fields=["bdate", "city", "photo_big", "has_mobile"])
fname = result[0]['first_name']
lname = result[0]['last_name']
url = result[0]['photo_big']


print(fname, lname)
print(url)

data = requests.get(url)
f = open("Durov.jpg", "wb")
f.write(data.content)
f.close()

"""
