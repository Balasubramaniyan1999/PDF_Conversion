# Import Module
from tkinter import *
from tkinter.filedialog import askopenfilename
import tabula

root = Tk()
root.geometry('400x200')

def select_file():
    global file_name
    file_name = askopenfilename(initialdir = "/",title = "Select File")

# PDF TO EXCEL
def pdf_to_excel():
    if file_name.endswith('.pdf'):
        df = tabula.read_pdf(file_name, pages = "all")[0]
        df.to_excel('Excel.xlsx')

# PDF TO CSV
def pdf_to_csv():
    if file_name.endswith('.pdf'):

        df = tabula.read_pdf(file_name, pages = 1)[0]
        df.to_csv('CSV.csv')


# Add Labels and Buttons
Label(root, text="PDF CONVERSION", font="italic 15 bold").pack(pady=10)

Button(root,text="Select PDF File",command=select_file,font=14).pack(pady=10)

frame = Frame()
frame.pack(pady=20)

excel_btn = Button(frame,text="PDF to Excel",command=pdf_to_excel,relief="solid",
                   bg="white",font=15)
excel_btn.pack(side=LEFT,padx=10)

csv_btn = Button(frame,text="PDF to CSV",command=pdf_to_csv,relief="solid",
                 bg="white",font=15)
csv_btn.pack()


root.mainloop()
