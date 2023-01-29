from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import fungsi
import model

#Base App dimension
root = Tk()
root.title('ARIA - App for Bathimetry ')
root.iconbitmap('aria_icon.ico')
root.geometry("1100x700")
CONS_DATA = dict()
df = None
model_data = None


# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('winnative')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame, orient=VERTICAL, )
tree_scroll_down = Scrollbar(tree_frame,orient=HORIZONTAL)
tree_scroll.pack( side=RIGHT, fill= Y)
tree_scroll_down.pack( side=BOTTOM, fill=X )

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_down.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)
tree_scroll_down.config(command=my_tree.xview)

# Define Our Columns
my_tree['columns'] = ("Nomor Order", "Measuring Point", "Revision Number", "Posting Date Input", "USV Name", "Start", "End", "Panjang STA", "Water Level/OGL", "Lebar atas/DA", "Lebar bawah/DB")
# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Nomor Order", anchor=CENTER, width=140)
my_tree.column("Measuring Point", anchor=CENTER, width=140)
my_tree.column("Revision Number", anchor=CENTER, width=140)
my_tree.column("Posting Date Input", anchor=CENTER, width=140)
my_tree.column("USV Name", anchor=CENTER, width=140)
my_tree.column("Start", anchor = CENTER, width=140)
my_tree.column("End", anchor = CENTER, width=140)
my_tree.column("Panjang STA", anchor=CENTER, width=140)
my_tree.column("Water Level/OGL", anchor=CENTER, width=140)
my_tree.column("Lebar atas/DA", anchor=CENTER, width=140)
my_tree.column("Lebar bawah/DB", anchor=CENTER, width=140)


my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Nomor Order", text="Nomor Order", anchor=CENTER)
my_tree.heading("Measuring Point", text="Measuring Point", anchor=CENTER)
my_tree.heading("Revision Number", text="Revision Number", anchor=CENTER)
my_tree.heading("Posting Date Input", text="Posting Date Input", anchor=CENTER)
my_tree.heading("USV Name", text="USV Name", anchor=CENTER)
my_tree.heading("Start", text="Start", anchor=CENTER)
my_tree.heading("End", text="End", anchor=CENTER)
my_tree.heading("Panjang STA", text="Panjang STA", anchor=CENTER)
my_tree.heading("Water Level/OGL", text="Water Level/OGL", anchor=CENTER)
my_tree.heading("Lebar atas/DA", text="Lebar atas", anchor=CENTER)
my_tree.heading("Lebar bawah/DB", text="Lebar bawah", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Jika mau basisdata sementara di python
# datas = ['']
# for record in datas:
# 	if count % 2 == 0:
# 		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]), tags=('evenrow',))
# 	else:
# 		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]), tags=('oddrow',))
# 	# increment counter
# 	count += 1


# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Tempat mengisi", labelanchor= 'n', cursor="xterm" )
data_frame.pack(fill="both", expand="yes", pady=10, padx = 1)

order_label = Label(data_frame, text="Nomor Order").grid(row=0, column=0, padx=5, pady=7)
order_entry = Entry(data_frame)
order_entry.grid(row=0, column=1, padx=5, pady=7)

measure_label = Label(data_frame, text="Measuring Point").grid(row=0, column=3, padx=5, pady=7)
measure_entry = Entry(data_frame)
measure_entry.grid(row=0, column=4, padx=5, pady=7)

revision_label = Label(data_frame, text="Revision number").grid(row=1, column=0, padx=5, pady=7)
revision_entry = Entry(data_frame)
revision_entry.grid(row=1, column=1, padx=5, pady=7)

post_label = Label(data_frame, text="Posting Date Input").grid(row=1, column=3, padx=5, pady=7)
post_entry = Entry(data_frame)
post_entry.grid(row=1, column=4, padx=5, pady=7)

usv_label = Label(data_frame, text="USV Name").grid(row=2, column=0, padx=5, pady=7)
usv_entry = Entry(data_frame)
usv_entry.grid(row=2, column=1, padx=5, pady=7)

post_pengukuran_label = Label(data_frame, text="Posting Date Pengukuran").grid(row=2, column=3, padx=5, pady=7)
post_pengukuran_entry = Entry(data_frame)
post_pengukuran_entry.grid(row=2, column=4, padx=5, pady=7)

start_label = Label(data_frame, text="Start").grid(row=3, column=0, padx=5, pady=7)
start_entry = Entry(data_frame)
start_entry.grid(row=3, column=1, padx=5, pady=7)

end_label = Label(data_frame, text="End").grid(row=3, column=3, padx=5, pady=7)
end_entry = Entry(data_frame)
end_entry.grid(row=3, column=4, padx=5, pady=7)

panjang_label = Label(data_frame, text="Panjang STA").grid(row=4, column=0, padx=5, pady=7)
panjang_entry = Entry(data_frame)
panjang_entry.grid(row=4, column=1, padx=5, pady=7)

water_label = Label(data_frame, text="Water Level/OGL").grid(row=4, column=3, padx=5, pady=7)
water_entry = Entry(data_frame)
water_entry.grid(row=4, column=4, padx=5, pady=7)

DA_label = Label(data_frame, text="Lebar Atas").grid(row=5, column=0, padx=5, pady=7)
DA_entry = Entry(data_frame)
DA_entry.grid(row=5, column=1, padx=5, pady=7)

DB_label = Label(data_frame, text="Lebar Bawah").grid(row=5, column=3, padx=5, pady=7)
DB_entry = Entry(data_frame)
DB_entry.grid(row=5, column=4, padx=5, pady=7)

#input function for form
def Check():
        
    if len(order_entry.get())== 12 :
        order_check = Label(data_frame, text="done", fg='blue').grid(row=0, column=2, padx = 2)
        CONS_DATA['order'] = order_entry.get()
    else:
        # order_check = Label(data_frame, text="check again").grid(row=2, column=2, padx = 10)
        order_check = Label(data_frame, text="12 C!", fg="red").grid(row=0, column=2, padx=2)
    
    # if opn_box.get().isdigit() == True and len(opn_box.get())==4:
    #     opn_check = Label(data_frame, text="done").grid(row=3, column=2, padx = 10)
    #     CONS_DATA['opsno'] = opn_box.get()
    # else:
    #     opn_check = Label(data_frame, text="check again").grid(row=3, column=2, padx = 10)
        
    if len(measure_entry.get())==12:
        measure_check = Label(data_frame, text="done", fg='blue').grid(row=0, column=5, padx = 2)
        CONS_DATA['measure_point'] = measure_entry.get()
    else:
        measure_check =Label(data_frame, text="12 C!", fg="red").grid(row=0, column=5, padx=2)


    if len(revision_entry.get())==3 and revision_entry.get().isdigit():
        revision_check = Label(data_frame, text="done", fg='blue').grid(row=1, column=2, padx = 2)
        CONS_DATA['revision'] = revision_entry.get()
    else:
        revision_check = Label(data_frame, text="3 D!", fg='red').grid(row=1, column=2, padx = 2)
    
    
    if len(post_entry.get())==8 and post_entry.get().isdigit():
        post_check = Label(data_frame, text="done", fg='blue').grid(row=1, column=5, padx = 2)
        CONS_DATA['posting_date'] = post_entry.get()
    else:
        post_check = Label(data_frame, text="8 D!", fg='red').grid(row=1, column=5, padx = 2)
    
    
    if len(usv_entry.get())==4:
        usv_check = Label(data_frame, text="done", fg='blue').grid(row=2, column=2, padx = 2)
        CONS_DATA['usv_name'] = usv_entry.get()
    else:
        usv_check = Label(data_frame, text="4 C!", fg='red').grid(row=2, column=2, padx = 2)    

    # if len(start_entry.get())==5:
    #     start_check = Label(data_frame, text="done", fg='blue').grid(row=4, column=5, padx = 2)
    #     CONS_DATA['start'] = start_entry.get()
    # else:
    #     start_check = Label(data_frame, text="5 C!", fg='red').grid(row=4 column=5, padx = 2)     

    # if len(end_entry.get())==5:
    #     end_check = Label(data_frame, text="done", fg='blue').grid(row=4, column=5, padx = 2)
    #     CONS_DATA['end'] = end_entry.get()
    # else:
    #     end_check = Label(data_frame, text="5 C!", fg='red').grid(row=4 column=5, padx = 2)       
    
    if len(panjang_entry.get())==2 and panjang_entry.get().isdigit():
        panjang_check = Label(data_frame, text="done", fg='blue').grid(row=4, column=2, padx = 2)
        CONS_DATA['sta'] = panjang_entry.get()
    else:
        measread_check = Label(data_frame, text="2 D!", fg='red').grid(row=4, column=2, padx = 2)      
          
    
    if len(water_entry.get())==5:
        water_check = Label(data_frame, text="done", fg='blue').grid(row=4, column=5, padx = 2)
        CONS_DATA['ogl'] = water_entry.get()
    else:
        water_check = Label(data_frame, text="5 C!", fg='red').grid(row=4, column=5, padx = 2)     
    
    
    if len(DA_entry.get())==4:
        DA_check = Label(data_frame, text="done", fg='blue').grid(row=5, column=2, padx = 2)
        CONS_DATA['da'] = DA_entry.get()
    else:
        DA_check = Label(data_frame, text="4 C!", fg='red').grid(row=5, column=2, padx = 2)         
    
    
    if len(DB_entry.get())==4:
        DB_check = Label(data_frame, text="done", fg='blue').grid(row=5, column=5, padx = 2)
        CONS_DATA['db'] = DB_entry.get()
    else:
        DB_check = Label(data_frame, text="4 C!", fg='red').grid(row=5, column=5, padx = 2)       

    model_data = model.ModelData(CONS_DATA)


global count
count = 0

def export_qc():
    pass


def update_record():
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(order_entry.get(), measure_entry.get(), revision_entry.get(),post_entry.get(), usv_entry.get(), start_entry.get(), end_entry.get(), panjang_entry.get(), water_entry.get(), DA_entry.get(), DB_entry.get(),))

    order_entry.delete(0,END)
    measure_entry.delete(0,END)
    revision_entry.delete(0,END)
    post_entry.delete(0,END)
    post_pengukuran_entry.delete(0,END)
    usv_entry.delete(0,END)
    panjang_entry.delete(0,END)
    start_entry.delete(0,END)
    end_entry.delete(0,END)
    water_entry.delete(0,END)
    DA_entry.delete(0,END)
    DB_entry.delete(0,END)

def select_record(e):
	# Clear entry boxes
    order_entry.delete(0,END)
    measure_entry.delete(0,END)
    revision_entry.delete(0,END)
    post_entry.delete(0,END)
    usv_entry.delete(0,END)
    post_pengukuran_entry.delete(0,END)
    start_entry.delete(0,END)
    end_entry.delete(0,END)
    panjang_entry.delete(0,END)
    water_entry.delete(0,END)
    DA_entry.delete(0,END)
    DB_entry.delete(0,END)

	# Grab record Number
    selected=my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

	# outpus to entry boxes
    order_entry.insert(0, values[0])
    measure_entry.insert(0, values[1])
    revision_entry.insert(0, values[2])
    post_entry.insert(0, values[3])
    usv_entry.insert(0, values[4])
    panjang_entry.insert(0, values[7])
    start_entry.insert(0, values[5])
    end_entry.insert(0,values[6])
    water_entry.insert(0, values[8])
    DA_entry.insert(0, values[9])
    DB_entry.insert(0, values[10])

def ExportQC():
    # pass
    # my_tree.g
    df[variable]    = "0"
    df['AUFNR']     = order_box.get()
    df['OPN']       = opn_box.get()
    df['MPOINT']    = mpoint_box.get()    
    df['REV']       = rev_box.get()
    df['BUDAT']     = budat_box.get()
    df['TERMINAL']  = terminal_box.get().ljust(15)
    df['N']         = "X"
    df['MEAREAD']   = measread_box.get()
    df['spasi14']   = "              "
    df['WL']        = float(wl_box.get())
    df['WL']        = df['WL'].apply(lambda x: "{:.3f}".format(x))    
    df['WD']        = df['Depth(m)'].astype(float)
    df['WD']        = df['WD'].apply(lambda x: "{:.3f}".format(x))   
    df['DA']        = int(DA_box.get())
    df['DA']        = df['DA'].apply(lambda x: "{:.2f}".format(x) if len(str(x)) > 1 else "{:.3f}".format(x))
    df['DB']        = int(DB_box.get())
    df['DB']        = df['DB'].apply(lambda x: "{:.2f}".format(x) if len(str(x)) > 1 else "{:.3f}".format(x))
    df['spasi2']    = "   "
    df['OC']        = "AX"
    #ini yang gw belom kelar
    list_sta = []
    temp_df = pd.DataFrame()
    for n in range (0, len(df.index)):
        temp_df = temp_df.append(df.iloc[n])
        if n == 0:
            temp_df.at[n,'MEAREAD']='00'
        list_sta.append("S" + str(n*20).zfill(4))
    print('panjang',len(temp_df.index))
    temp_df['data_STA'] = list_sta
    temp_df["MDTEXT"] = temp_df['data_STA'] + "-" + temp_df["WL"] + "-" + temp_df['WD'] + "-" +temp_df['DA'] + temp_df['DB'] + "/" + temp_df['MEASDATE']
    
    df_QC = temp_df['AUFNR'] + temp_df['OPN'] + temp_df['MPOINT'] + temp_df['REV'] + temp_df['BUDAT'] + temp_df['TERMINAL'] + temp_df['N'] + temp_df['MEASDATE'] + temp_df['MEAREAD'] + temp_df['spasi14'] + temp_df["MDTEXT"] + temp_df['spasi2'] + temp_df['OC']
    # print(df_QC)
    df_QC.to_csv('result-qc.txt', index=False, header=False, quoting=csv.QUOTE_NONE)
    # print(len(df.index))




def add_record():
	global count
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(order_entry.get(), measure_entry.get(), revision_entry.get(),post_entry.get(), usv_entry.get(),  start_entry.get(), end_entry.get(), panjang_entry.get(),water_entry.get(), DA_entry.get(), DB_entry.get()), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(order_entry.get(), measure_entry.get(), revision_entry.get(),post_entry.get(), usv_entry.get(), start_entry.get(), end_entry.get(), panjang_entry.get(), water_entry.get(), DA_entry.get(), DB_entry.get()), tags=('oddrow',))
	# increment counter
	count += 1

	order_entry.delete(0, END)
	measure_entry.delete(0, END)
	revision_entry.delete(0, END)
	post_entry.delete(0, END)
	usv_entry.delete(0, END)
	post_pengukuran_entry.delete(0,END)
	start_entry.delete(0,END)
	end_entry.delete(0,END)
	panjang_entry.delete(0, END)
	water_entry.delete(0, END)
	DA_entry.delete(0, END)
	DB_entry.delete(0, END)

#import Function
def OpenFile():
    csv_path = filedialog.askopenfilename(initialdir="data", title="select csv file", filetypes=(("all files", "*.*"), ("csv files", "*.csv")))
    df = fungsi.load_csv(str(csv_path))
    sta = len(df.index)*int(model_data['sta'])/500 #20 dirubah variable
    df = df[::int(sta)]
    df['MEASDATE'] = df['Time(Local)'].str[:10]
    df['MEASDATE'] = df['MEASDATE'].str.replace('/',"")
# csv_data = pd.read_csv(r'E:\ARIA\WKS\data-raw\all_data.CSV')

# Remove one record
def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)


#Separator line
separator=ttk.Separator(data_frame, orient=VERTICAL, style='TSeparator', class_=ttk.Separator, takefocus=1, cursor='man')
separator.grid(row=0, column=6, rowspan=7, ipady=175, padx=35)


check_button = Button(data_frame, text="Check data", command=Check)
check_button.grid(row=0, column=7, padx= 20, pady = 5)

add_button = Button(data_frame, text="Add data", command=add_record)
add_button.grid(row=0, column=8, padx=20)

#create open csv button
open_csv_button = Button(data_frame, text="Load CSV", command=OpenFile)
open_csv_button.grid(row=0, column=9, padx=20)

update_button = Button(data_frame, text="Update data", command=update_record)
update_button.grid(row=1, column=7, padx=20, pady=10)

remove_one_button = Button(data_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=1, column=8, padx=20, pady=10)

#create export button qc kanal
exportqc_button = Button(data_frame, text="export QC kanal", command=ExportQC)
exportqc_button.grid(row=1, column=9, padx = 20, pady = 10)

# #create export button pra inspeksi
# exportpi_button = Button(data_frame, text="export Pra Inspeksi", command=ExportPI)
# exportpi_button.grid(row=12, column=3, padx = 10, pady = 10)


# def up():
# 	rows = my_tree.selection()
# 	for row in rows:
# 		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# # Move Rown Down
# def down():
# 	rows = my_tree.selection()
# 	for row in reversed(rows):
# 		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# # Remove one record
# def remove_one():
# 	x = my_tree.selection()[0]
# 	my_tree.delete(x)

# # Remove Many records
# def remove_many():
# 	x = my_tree.selection()
# 	for record in x:
# 		my_tree.delete(record)

# # Remove all records
# def remove_all():
# 	for record in my_tree.get_children():
# 		my_tree.delete(record)

# # Clear entry boxes
# def clear_entries():
# 	# Clear entry boxes
# 	notif_entry.delete(0, END)
# 	order_entry.delete(0, END)
# 	ops_entry.delete(0, END)
# 	measure_entry.delete(0, END)
# 	revision_entry.delete(0, END)
# 	post_entry.delete(0, END)
# 	usv_entry.delete(0, END)
# 	panjang_entry.delete(0, END)
# 	water_entry.delete(0, END)
# 	lebarA_entry.delete(0, END)
# 	lebarB_entry.delete(0, END)


# # Select Record
# def select_record(e):
# 	# Clear entry boxes
# 	notif_entry.delete(0, END)
# 	order_entry.delete(0, END)
# 	ops_entry.delete(0, END)
# 	measure_entry.delete(0, END)
# 	revision_entry.delete(0, END)
# 	post_entry.delete(0, END)
# 	usv_entry.delete(0, END)
# 	panjang_entry.delete(0, END)
# 	water_entry.delete(0, END)
# 	lebarA_entry.delete(0, END)
# 	lebarB_entry.delete(0, END)
# 	# Grab record Number
# 	selected = my_tree.focus()
# 	# Grab record values
# 	values = my_tree.item(selected, 'values')

# 	# outpus to entry boxes
# 	notif_entry.insert(0, values[0])
# 	order_entry.insert(0, values[1])
# 	ops_entry.insert(0, values[2])
# 	measure_entry.insert(0, values[3])
# 	revision_entry.insert(0, values[4])
# 	post_entry.insert(0, values[5])
# 	usv_entry.insert(0, values[6])
# 	panjang_entry.insert(0, values[7])
# 	water_entry.insert(0, values[8])
# 	lebarA_entry.insert(0, values[9])
# 	lebarB_entry.insert(0, values[10])

# # Update record
# def update_record():
# 	# Grab the record number
# 	selected = my_tree.focus()
# 	# Update record
# 	my_tree.item(selected, text="", values=(notif_entry.get(), order_entry.get(), ops_entry.get(), measure_entry.get(), revision_entry.get(), post_entry.get(), usv_entry.get(), panjang_entry.get(), water_entry.get(), lebarA_entry.get(), lebarB_entry.get(),))

# 	# Clear entry boxes
# 	notif_entry.delete(0, END)
# 	order_entry.delete(0, END)
# 	ops_entry.delete(0, END)
# 	measure_entry.delete(0, END)
# 	revision_entry.delete(0, END)
# 	post_entry.delete(0, END)
# 	usv_entry.delete(0, END)
# 	panjang_entry.delete(0, END)
# 	water_entry.delete(0, END)
# 	lebarA_entry.delete(0, END)
# 	lebarB_entry.delete(0, END)


my_tree.bind("<ButtonRelease-1>", select_record)

root.mainloop()