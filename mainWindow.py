from tkinter import *
import main_controller
import xlwt

def abrir():
    f = open("youtube-data.txt", "r")
    #content = f.read().splitlines()
    row_format = "{:50} {:20} {:15} {:15} {:15} {:8}"

    for l in list(f.read):
        #listBox.insert(END, row_format.format(*l.read(), sp=" " * 2))
        print(l)
    f.close()

def save():
    file = open("youtube-data.txt", "w")

    for i in range(listBox.size()):
        file.write(str(listBox.get(i)))
        file.write('\n')
    print("Se Has guardado los datos")
    file.close()

    """book = xlwt.Workbook(encoding="utf-8")

    sheet1 = book.add_sheet("Youtube-data")

    sheet1.write(0, 0, "Title")
    sheet1.write(0, 1, "Channel")
    sheet1.write(0, 2, "Likes")
    sheet1.write(0, 3, "Dislikes")
    sheet1.write(0, 4, "Views")
    sheet1.write(0, 5, "Published date")

    print("=======================================")

    rango = listBox.size()
    lista = listBox

    for r in range(rango):
        for c in lista.get(r):
            print(str(c))


    print ("Se Has guardado los datos xls")
    book.save("youtube-data.xls")"""



def search():
    try:
        url = txt_searcher.get()
        soup = main_controller.Main_controller.soup(url)
    except UnboundLocalError:
        lbn_avise.config(text= "URL incorrecto!")


    title = main_controller.Main_controller.title(soup)
    channel = main_controller.Main_controller.channel(soup)
    like = main_controller.Main_controller.like(soup)
    dislike = main_controller.Main_controller.dislike(soup)
    view = main_controller.Main_controller.view(soup)
    date = main_controller.Main_controller.date(soup)

    #Result
    txt_resultTitle.config(text=title)
    txt_channel.config(text=channel)
    txt_like.config(text=like)
    txt_dislike.config(text=dislike)
    txt_views.config(text=view)
    txt_date.config(text=date)

    list = [title, channel, like, dislike, view, date]
    return list

def clear():
    txt_resultTitle.config(text="")
    txt_channel.config(text="")
    txt_like.config(text="")
    txt_dislike.config(text="")
    txt_views.config(text="")
    txt_date.config(text="")


def add_listBox():
    lista = search()
    row_format = "{:50} {:20} {:15} {:15} {:15} {:8}"
    listBox.insert(END, row_format.format(*lista, sp=" "*2))


def delete_listBox():
    selection = listBox.curselection()
    listBox.delete(selection[0])


root = Tk()
root.title("Youtube-Data")
root.geometry("800x500")

#Creating side of Frames

titleFrame = Frame(root)
titleFrame.pack()

searchFrame = Frame(root)
searchFrame.pack()

FrameSearch = Frame(root)
FrameSearch.pack()

resultFrame = Frame(FrameSearch)
resultFrame.pack(side=LEFT)

resultFrameButton = Frame(FrameSearch)
resultFrameButton.pack(side=LEFT)

tableFrame = Frame(root)
tableFrame.pack() 


	#Creating inside Frames elements

	#Search

lbn_title = Label(titleFrame, text="YouTube-Data", fg="red", font=("Helvetica", 24))
lbn_title.pack()

lbn_url = Label(searchFrame, text="URL")
lbn_url.pack(side=LEFT)
url = ""
txt_searcher = Entry(searchFrame, textvariable = url)
txt_searcher.pack(side=LEFT)
btn_search = Button(searchFrame, text="Search", command=search)
btn_search.pack(side=LEFT)
lbn_avise = Label(searchFrame, text="")

#result

lbn_resultTitle = Label(resultFrame, text="Title")
txt_resultTitle = Label(resultFrame)


lbn_channel = Label(resultFrame, text="Channel")
txt_channel = Label(resultFrame)

lbn_like = Label(resultFrame, text="Like")
txt_like = Label(resultFrame)

lbn_dislike = Label(resultFrame, text="Dislike")
txt_dislike = Label(resultFrame)

lbn_views = Label(resultFrame, text="Views")
txt_views = Label(resultFrame)

lbn_date = Label(resultFrame, text="Published date")
txt_date = Label(resultFrame)

btn_add = Button(resultFrameButton, text="Add", width="10", command=add_listBox)
btn_clear = Button(resultFrameButton, text="Clear", width="10", command=clear)

#Grid result

lbn_resultTitle.grid(row=0, sticky=E)
txt_resultTitle.grid(row=0, column=1)

lbn_channel.grid(row=1, sticky=E)
txt_channel.grid(row=1, column=1)

lbn_like.grid(row=2, sticky=E)
txt_like.grid(row=2, column=1)

lbn_dislike.grid(row=3, sticky=E)
txt_dislike.grid(row=3, column=1)

lbn_views.grid(row=4, sticky=E)
txt_views.grid(row=4, column=1)

lbn_date.grid(row=5, sticky=E)
txt_date.grid(row=5, column=1)

btn_add.grid(row=6, sticky=E)
btn_clear.grid(row=7, column=0, sticky=W)


#Table
btn_open = Button(tableFrame, text="Open", command=abrir)
btn_edit = Button(tableFrame, text="Edit")
btn_delete = Button(tableFrame, text="Delete", command=delete_listBox)
btn_save = Button(tableFrame, text="Save", command=save)
#Grid button table

btn_open.grid(row=0, column=0)
btn_edit.grid(row=0, column=1)
btn_delete.grid(row=0, column=2)
btn_save.grid(row=0, column=3)

listBox = Listbox(root, width=750)
listBox.pack()

#headers = [" Título ", " Canal", "Like", "Dislike", " Visitas", "Fecha de publicación"]

#row_format = "{:70} {:10} {:15} {:15} {:15} {:8}"

#listBox.insert(0, row_format.format(*headers, sp=" "*2))

root.mainloop()


