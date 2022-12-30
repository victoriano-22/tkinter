from tkinter import *
from tkinter import ttk


root = Tk()
root.title('ARIA - App for Bathimetry ')
root.iconbitmap('aria_icon.ico')
root.geometry("1080x600")

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
my_tree['columns'] = ("Notification No.", "Nomor Order", "Ops Number", "Measuring Point", "Revision Number", "Posting Date Input", "USV Name", "Panjang STA", "Water Level/OGL", "Lebar atas", "Lebar bawah")
# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Notification No.", anchor=CENTER, width=140)
my_tree.column("Nomor Order", anchor=CENTER, width=140)
my_tree.column("Ops Number", anchor=CENTER, width=100)
my_tree.column("Measuring Point", anchor=CENTER, width=140)
my_tree.column("Revision Number", anchor=CENTER, width=140)
my_tree.column("Posting Date Input", anchor=CENTER, width=140)
my_tree.column("USV Name", anchor=CENTER, width=140)
my_tree.column("Panjang STA", anchor=CENTER, width=140)
my_tree.column("Water Level/OGL", anchor=CENTER, width=140)
my_tree.column("Lebar atas", anchor=CENTER, width=140)
my_tree.column("Lebar bawah", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Notification No.", text="Notification No.", anchor=CENTER)
my_tree.heading("Nomor Order", text="Nomor Order", anchor=CENTER)
my_tree.heading("Ops Number", text="Ops Number", anchor=CENTER)
my_tree.heading("Measuring Point", text="Measuring Point", anchor=CENTER)
my_tree.heading("Revision Number", text="Revision Number", anchor=CENTER)
my_tree.heading("Posting Date Input", text="Posting Date Input", anchor=CENTER)
my_tree.heading("USV Name", text="USV Name", anchor=CENTER)
my_tree.heading("Panjang STA", text="Panjang STA", anchor=CENTER)
my_tree.heading("Water Level/OGL", text="Water Level/OGL", anchor=CENTER)
my_tree.heading("Lebar atas", text="Lebar atas", anchor=CENTER)
my_tree.heading("Lebar bawah", text="Lebar bawah", anchor=CENTER)


# Add Fake Data
data = [
	["000515", "123456", "0010" , "654987", "65", "4561", "324", "A20", "45", "677", "123"],
	["012515", "126156", "1010" , "231487", "25", "4521", "124", "B20", "46", "657", "113"],
	["000515", "123456", "0010" , "654987", "65", "4561", "324", "A20", "45", "677", "123"],
	["012515", "126156", "1010" , "231487", "25", "4521", "124", "B20", "46", "657", "113"],
	["000515", "123456", "0010" , "654987", "65", "4561", "324", "A20", "45", "677", "123"],
	["012515", "126156", "1010" , "231487", "25", "4521", "124", "B20", "46", "657", "113"],
	["000515", "123456", "0010" , "654987", "65", "4561", "324", "A20", "45", "677", "123"],
	["012515", "126156", "1010" , "231487", "25", "4521", "124", "B20", "46", "657", "113"],
	["000515", "123456", "0010" , "654987", "65", "4561", "324", "A20", "45", "677", "123"],
	["012515", "126156", "1010" , "231487", "25", "4521", "124", "B20", "46", "657", "113"],
	["000515", "123456", "0010" , "654987", "65", "4561", "324", "A20", "45", "677", "123"],
	["012515", "126156", "1010" , "231487", "25", "4521", "124", "B20", "46", "657", "113"],
	["000515", "123456", "0010" , "654987", "65", "4561", "324", "A20", "45", "677", "123"],
	["012515", "126156", "1010" , "231487", "25", "4521", "124", "B20", "46", "657", "113"],	
]

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add our data to the screen
global count
count = 0

for record in data:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]), tags=('oddrow',))
	# increment counter
	count += 1


# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Tambahan baru")
data_frame.pack(fill="x", expand="yes", padx=20)

notif_label = Label(data_frame, text="Notification No.")
notif_label.grid(row=0, column=0, padx=10, pady=10)
notif_entry = Entry(data_frame)
notif_entry.grid(row=0, column=1, padx=10, pady=10)

order_label = Label(data_frame, text="Nomor Order")
order_label.grid(row=0, column=2, padx=10, pady=10)
order_entry = Entry(data_frame)
order_entry.grid(row=0, column=3, padx=10, pady=10)

ops_label = Label(data_frame, text="Ops Number")
ops_label.grid(row=0, column=4, padx=10, pady=10)
ops_entry = Entry(data_frame)
ops_entry.grid(row=0, column=5, padx=10, pady=10)

measure_label = Label(data_frame, text="Measuring Point")
measure_label.grid(row=0, column=6, padx=10, pady=10)
measure_entry = Entry(data_frame)
measure_entry.grid(row=0, column=7, padx=10, pady=10)

revision_label = Label(data_frame, text="revision number")
revision_label.grid(row=1, column=0, padx=10, pady=10)
revision_entry = Entry(data_frame)
revision_entry.grid(row=1, column=1, padx=10, pady=10)

post_label = Label(data_frame, text="Posting Date Input")
post_label.grid(row=1, column=2, padx=10, pady=10)
post_entry = Entry(data_frame)
post_entry.grid(row=1, column=3, padx=10, pady=10)

usv_label = Label(data_frame, text="USV Name")
usv_label.grid(row=1, column=4, padx=10, pady=10)
usv_entry = Entry(data_frame)
usv_entry.grid(row=1, column=5, padx=10, pady=10)

panjang_label = Label(data_frame, text="Panjang STA")
panjang_label.grid(row=1, column=6, padx=10, pady=10)
panjang_entry = Entry(data_frame)
panjang_entry.grid(row=1, column=7, padx=10, pady=10)

water_label = Label(data_frame, text="Water Level/OGL")
water_label.grid(row=2, column=0, padx=10, pady=10)
water_entry = Entry(data_frame)
water_entry.grid(row=2, column=1, padx=10, pady=10)

lebarA_label = Label(data_frame, text="Lebar Atas")
lebarA_label.grid(row=2, column=2, padx=10, pady=10)
lebarA_entry = Entry(data_frame)
lebarA_entry.grid(row=2, column=3, padx=10, pady=10)

lebarB_label = Label(data_frame, text="Lebar Bawah")
lebarB_label.grid(row=2, column=4, padx=10, pady=10)
lebarB_entry = Entry(data_frame)
lebarB_entry.grid(row=2, column=5, padx=10, pady=10)

# list_entry = [notif_entry, order_entry, ops_entry, measure_entry, revision_entry, post_entry, usv_entry]

# Move Row Up
def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Rown Down
def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Remove one record
def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)

# Remove Many records
def remove_many():
	x = my_tree.selection()
	for record in x:
		my_tree.delete(record)

# Remove all records
def remove_all():
	for record in my_tree.get_children():
		my_tree.delete(record)

# Clear entry boxes
def clear_entries():
	# Clear entry boxes
	notif_entry.delete(0, END)
	order_entry.delete(0, END)
	ops_entry.delete(0, END)
	measure_entry.delete(0, END)
	revision_entry.delete(0, END)
	post_entry.delete(0, END)
	usv_entry.delete(0, END)
	panjang_entry.delete(0, END)
	water_entry.delete(0, END)
	lebarA_entry.delete(0, END)
	lebarB_entry.delete(0, END)


# Select Record
def select_record(e):
	# Clear entry boxes
	notif_entry.delete(0, END)
	order_entry.delete(0, END)
	ops_entry.delete(0, END)
	measure_entry.delete(0, END)
	revision_entry.delete(0, END)
	post_entry.delete(0, END)
	usv_entry.delete(0, END)
	panjang_entry.delete(0, END)
	water_entry.delete(0, END)
	lebarA_entry.delete(0, END)
	lebarB_entry.delete(0, END)
	# Grab record Number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	# outpus to entry boxes
	notif_entry.insert(0, values[0])
	order_entry.insert(0, values[1])
	ops_entry.insert(0, values[2])
	measure_entry.insert(0, values[3])
	revision_entry.insert(0, values[4])
	post_entry.insert(0, values[5])
	usv_entry.insert(0, values[6])
	panjang_entry.insert(0, values[7])
	water_entry.insert(0, values[8])
	lebarA_entry.insert(0, values[9])
	lebarB_entry.insert(0, values[10])

# Update record
def update_record():
	# Grab the record number
	selected = my_tree.focus()
	# Update record
	my_tree.item(selected, text="", values=(notif_entry.get(), order_entry.get(), ops_entry.get(), measure_entry.get(), revision_entry.get(), post_entry.get(), usv_entry.get(), panjang_entry.get(), water_entry.get(), lebarA_entry.get(), lebarB_entry.get(),))

	# Clear entry boxes
	notif_entry.delete(0, END)
	order_entry.delete(0, END)
	ops_entry.delete(0, END)
	measure_entry.delete(0, END)
	revision_entry.delete(0, END)
	post_entry.delete(0, END)
	usv_entry.delete(0, END)
	panjang_entry.delete(0, END)
	water_entry.delete(0, END)
	lebarA_entry.delete(0, END)
	lebarB_entry.delete(0, END)




button_frame = LabelFrame(root, text="Tombol")
button_frame.pack(fill="x", expand="yes", padx=20)

check_button = Button(button_frame, text = "Check Data")
check_button.grid(row=1, column = 0, padx=30, pady=10)

load_button = Button(button_frame, text = "Load CSV")
load_button.grid(row=1, column = 1, padx=30, pady=10)

export_QC_button = Button(button_frame, text = "Export QC kanal")
export_QC_button.grid(row=1, column = 2, padx=30, pady=10)

export_Inspek_button = Button(button_frame, text = "export Pra Inspeksi")
export_Inspek_button.grid(row=1, column = 3, padx=30, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=1, column=4, padx=30, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=1, column=5, padx=30, pady=10)


update_button = Button(button_frame, text="Update data", command=update_record)
update_button.grid(row=0, column=0, padx=30, pady=10)

add_button = Button(button_frame, text="Add data")
add_button.grid(row=0, column=1, padx=30, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=2, padx=30, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=3, padx=30, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=4, padx=30, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=5, padx=30, pady=10)


# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

root.mainloop()