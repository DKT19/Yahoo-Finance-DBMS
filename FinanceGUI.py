# Import libraries
import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Stock Data Management System')
window.geometry('1366x768')

def quit_program():
    quit_program = messagebox.askokcancel('Stock Data Management System', 'The application will be closed')
    if quit_program == True:
        window.destroy()
    return

def display_stock_data(event):
    if len(stocksymtarget_entry.get()) == 0:
        messagebox.showerror('Error', 'Please enter stock symbol')
    if len(datetarget_entry.get()) == 0:
        messagebox.showerror('Error', 'Please enter valid date')
    stock_sym_target = stocksymtarget_entry.get()
    date_target = "'" + datetarget_entry.get() + "'"
    conn = sqlite3.connect('Stocks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ' + stock_sym_target + ' WHERE Date LIKE ' + date_target)
    all_stock_data = c.fetchone()
    conn.close()
    if all_stock_data == None:
        messagebox.showerror('Error', 'Invalid Symbol or Date (d/m/Y)')
    else:
        prevc_entry.delete(0, END)
        prevc_entry.insert(END, all_stock_data[0])
        openprice_entry.delete(0, END)
        openprice_entry.insert(END, all_stock_data[1])
        bidprice_entry.delete(0, END)
        bidprice_entry.insert(END, all_stock_data[2])
        askprice_entry.delete(0, END)
        askprice_entry.insert(END, all_stock_data[3])
        dayrange_entry.delete(0, END)
        dayrange_entry.insert(END, all_stock_data[4])
        yearrange_entry.delete(0, END)
        yearrange_entry.insert(END, all_stock_data[5])
        volume_entry.delete(0, END)
        volume_entry.insert(END, all_stock_data[6])
        avgvolume_entry.delete(0, END)
        avgvolume_entry.insert(END, all_stock_data[7])
        marketcap_entry.delete(0, END)
        marketcap_entry.insert(END, all_stock_data[8])
        beta_entry.delete(0, END)
        beta_entry.insert(END, all_stock_data[9])
        peratio_entry.delete(0, END)
        peratio_entry.insert(END, all_stock_data[10])
        eps_entry.delete(0, END)
        eps_entry.insert(END, all_stock_data[11])
        earningsdate_entry.delete(0, END)
        earningsdate_entry.insert(END, all_stock_data[12])
        forwarddividend_entry.delete(0, END)
        forwarddividend_entry.insert(END, all_stock_data[13])
        exdividenddate_entry.delete(0, END)
        exdividenddate_entry.insert(END, all_stock_data[14])
        yeartarget_entry.delete(0, END)
        yeartarget_entry.insert(END, all_stock_data[15])
        dateacq_entry.delete(0, END)
        dateacq_entry.insert(END, all_stock_data[16])

def update_table():
    no_errors = True
    zero_error = ['Entry required', 'Input N/A if not available']
    if len(stocksymtarget_entry.get()) == 0:
        messagebox.showerror('Error', 'Please enter stock symbol')
    stock_sym_target = stocksymtarget_entry.get()
    pc = prevc_entry.get()
    if len(prevc_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    op = openprice_entry.get()
    if len(openprice_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    bp = bidprice_entry.get()
    if len(bidprice_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    ap = askprice_entry.get()
    if len(askprice_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    dr = dayrange_entry.get()
    if len(dayrange_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    yr = yearrange_entry.get()
    if len(yearrange_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    v = volume_entry.get()
    if len(volume_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    av = avgvolume_entry.get()
    if len(avgvolume_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    mc = marketcap_entry.get()
    if len(marketcap_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    b = beta_entry.get()
    if len(beta_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    per = peratio_entry.get()
    if len(peratio_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    eps = eps_entry.get()
    if len(eps_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    ed = earningsdate_entry.get()
    if len(earningsdate_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    fd = forwarddividend_entry.get()
    if len(forwarddividend_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    edd = exdividenddate_entry.get()
    if len(exdividenddate_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    yt = yeartarget_entry.get()
    if len(yeartarget_entry.get()) == 0:
        messagebox.showerror('Error', '\n'.join(zero_error))
        no_errors = False
    if dateacq_entry.get() != datetarget_entry.get():
        messagebox.showerror('Error', 'Can NOT change date!')
    if no_errors == True:
        conn = sqlite3.connect('Stocks.db')
        c = conn.cursor()
        c.execute(
            'UPDATE ' + stock_sym_target + ' SET [Previous Close]=?, [Open]=?, [Bid]=?, [Ask]=?, [Days Range]=?, [52 Week Range]=?, [Volume]=?, [Avg. Volume]=?, [Market Cap]=?, [Beta (3Y Monthly)]=?, [PE Ratio (TTM)]=?, [EPS (TTM)]=?, [Earnings Date]=?, [Forward Dividend & Yield]=?, [Ex-Dividend Date]=?, [1y Target Est]=?',
            (pc, op, bp, ap, dr, yr, v, av, mc, b, per, eps, ed, fd, edd, yt))
        conn.commit()
        conn.close()

def clear_entries():
    prevc_entry.delete(0, END)
    openprice_entry.delete(0, END)
    bidprice_entry.delete(0, END)
    askprice_entry.delete(0, END)
    dayrange_entry.delete(0, END)
    yearrange_entry.delete(0, END)
    volume_entry.delete(0, END)
    avgvolume_entry.delete(0, END)
    marketcap_entry.delete(0, END)
    beta_entry.delete(0, END)
    peratio_entry.delete(0, END)
    eps_entry.delete(0, END)
    earningsdate_entry.delete(0, END)
    forwarddividend_entry.delete(0, END)
    exdividenddate_entry.delete(0, END)
    yeartarget_entry.delete(0, END)
    dateacq_entry.delete(0, END)

master = Canvas(window)
master.grid()

title = Frame(master=master)
title.pack(side=TOP)

show_title = Label(title, font=('Helvetica', 30, 'bold'), text='Stock Data Management System')
show_title.grid()

data = Frame(master=master, height=600, width=1366, padx=20)
data.pack(side=BOTTOM)

stock_data = LabelFrame(data, font=('Helvetica', 15, 'bold'), text='Stock Data\n')
stock_data.pack(side=LEFT)

previousclose = StringVar()
prevc = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Previous Close:')
prevc.grid(row=0, column=0, sticky='W', padx=2)
prevc_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=previousclose, width=75)
prevc_entry.grid(row=0, column=1, sticky='W', padx=2)

openprice = StringVar()
openprice = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Open Price:')
openprice.grid(row=1, column=0, sticky='W', padx=2)
openprice_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=openprice, width=75)
openprice_entry.grid(row=1, column=1, sticky='W', padx=2)

bidprice = StringVar()
bidprice = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Bid Price:')
bidprice.grid(row=2, column=0, sticky='W', padx=2)
bidprice_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=bidprice, width=75)
bidprice_entry.grid(row=2, column=1, sticky='W', padx=2)

askprice = StringVar()
askprice = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Ask Price:')
askprice.grid(row=3, column=0, sticky='W', padx=2)
askprice_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=askprice, width=75)
askprice_entry.grid(row=3, column=1, sticky='W', padx=2)

dayrange = StringVar()
dayrange = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Day Range:')
dayrange.grid(row=4, column=0, sticky='W', padx=2)
dayrange_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=dayrange, width=75)
dayrange_entry.grid(row=4, column=1, sticky='W', padx=2)

yearrange = StringVar()
yearrange = Label(stock_data, font=('Helvetica', 15, 'bold'), text='1-Year Range:')
yearrange.grid(row=5, column=0, sticky='W', padx=2)
yearrange_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=yearrange, width=75)
yearrange_entry.grid(row=5, column=1, sticky='W', padx=2)

volume = StringVar()
volume = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Volume:')
volume.grid(row=6, column=0, sticky='W', padx=2)
volume_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=volume, width=75)
volume_entry.grid(row=6, column=1, sticky='W', padx=2)

avgvolume = StringVar()
avgvolume = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Avg. Volume:')
avgvolume.grid(row=7, column=0, sticky='W', padx=2)
avgvolume_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=avgvolume, width=75)
avgvolume_entry.grid(row=7, column=1, sticky='W', padx=2)

marketcap = StringVar()
marketcap = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Market Cap:')
marketcap.grid(row=8, column=0, sticky='W', padx=2)
marketcap_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=marketcap, width=75)
marketcap_entry.grid(row=8, column=1, sticky='W', padx=2)

beta = StringVar()
beta = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Beta:')
beta.grid(row=9, column=0, sticky='W', padx=2)
beta_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=beta, width=75)
beta_entry.grid(row=9, column=1, sticky='W', padx=2)

peratio = StringVar()
peratio = Label(stock_data, font=('Helvetica', 15, 'bold'), text='PE Ratio:')
peratio.grid(row=10, column=0, sticky='W', padx=2)
peratio_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=peratio, width=75)
peratio_entry.grid(row=10, column=1, sticky='W', padx=2)

eps = StringVar()
eps = Label(stock_data, font=('Helvetica', 15, 'bold'), text='EPS:')
eps.grid(row=11, column=0, sticky='W', padx=2)
eps_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=eps, width=75)
eps_entry.grid(row=11, column=1, sticky='W', padx=2)

earningsdate = StringVar()
earningsdate = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Earnings Date:')
earningsdate.grid(row=12, column=0, sticky='W', padx=2)
earningsdate_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=earningsdate, width=75)
earningsdate_entry.grid(row=12, column=1, sticky='W', padx=2)

forwarddividend = StringVar()
forwarddividend = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Forward Dividend:')
forwarddividend.grid(row=13, column=0, sticky='W', padx=2)
forwarddividend_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=forwarddividend, width=75)
forwarddividend_entry.grid(row=13, column=1, sticky='W', padx=2)

exdividenddate = StringVar()
exdividenddate = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Ex-Dividend Date:')
exdividenddate.grid(row=14, column=0, sticky='W', padx=2)
exdividenddate_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=exdividenddate, width=75)
exdividenddate_entry.grid(row=14, column=1, sticky='W', padx=2)

yeartarget = StringVar()
yeartarget = Label(stock_data, font=('Helvetica', 15, 'bold'), text='1-Year Target:')
yeartarget.grid(row=15, column=0, sticky='W', padx=2)
yeartarget_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=yeartarget, width=75)
yeartarget_entry.grid(row=15, column=1, sticky='W', padx=2)

dateacq = StringVar()
dateacq = Label(stock_data, font=('Helvetica', 15, 'bold'), text='Date:')
dateacq.grid(row=16, column=0, sticky='W', padx=2)
dateacq_entry = Entry(stock_data, font=('Helvetica', 15, 'bold'), textvariable=dateacq, width=75)
dateacq_entry.grid(row=16, column=1, sticky='W', padx=2)

stock_sym = LabelFrame(data, font=('Helvetica', 15, 'bold'), text='Search Data\n', padx=10)
stock_sym.pack(side=RIGHT)

stock_sym_target = StringVar()
stocksymtarget = Label(stock_sym, font=('Helvetica', 15, 'bold'), text='Stock Symbol:')
stocksymtarget.grid(row=0, column=0, sticky='W', padx=2)
stocksymtarget_entry = Entry(stock_sym, font=('Helvetica', 15, 'bold'), textvariable=stock_sym_target)
stocksymtarget_entry.grid(row=1, column=0, sticky='W', padx=2)

date_target = StringVar()
datetarget = Label(stock_sym, font=('Helvetica', 15, 'bold'), text='Date:')
datetarget.grid(row=2, column=0, sticky='W', padx=2)
datetarget_entry = Entry(stock_sym, font=('Helvetica', 15, 'bold'), textvariable=date_target)
datetarget_entry.grid(row=3, column=0, sticky='W', padx=2)

search_button = Button(stock_sym, height=1, width=10, font=('Helvetica', 15, 'bold'), text='Search')
search_button.bind('<Button-1>', display_stock_data)
search_button.grid(row=4, column=0)

buttons = Frame(master=master, height=50, width=1366)
buttons.pack(side=BOTTOM)

delete_button = Button(buttons, height=1, width=20, font=('Helvetica', 15, 'bold'), text='Clear Entries',
                       command=clear_entries)
delete_button.grid(row=0, column=1)
update_button = Button(buttons, height=1, width=20, font=('Helvetica', 15, 'bold'), text='Update Entry',
                       command=update_table)
update_button.grid(row=0, column=2)
quit_button = Button(buttons, height=1, width=20, font=('Helvetica', 15, 'bold'), text='Quit', command=quit_program)
quit_button.grid(row=0, column=3)

window.mainloop()