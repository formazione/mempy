import os
import pickle
import tkinter as tk
import tkinter.ttk as ttk

def save_template():
	global memo
	memo = {
		
		"Da pagare" : "tim, enel",
		"Wip" : """
				Skate Jack - game,
				matchpair - game,
				Posizionamento - article for aziendaitalia
				"""
	}
	with open("memo.pkl", "wb") as file:
		pickle.dump(memo, file)



def load_template():
	with open("memo.pkl", "rb") as file:
		memo = pickle.load(file)
	return memo

def save_once():
	save_template()

def to_html():
	data = ""
	for k in memo:
		data += "<td>" + k + "</td>"
		for d in memo[k].split(","):
			data += "<td>" + d + "</td>"
		data += "<tr>"

	data = "<table border=1>" + data + "<table>"
	print(data)
	with open("file.html", "w") as file:
		file.write(data)

	os.startfile("file.html")

# get data from pickle
memo = load_template()

# window

def show(event):
	''' call this to show the note in the tbx '''
	
	mm = lst.get(lst.curselection())
	tbx.delete("0.0", tk.END)
	tbx.insert(tk.END, mm)

def help():
	''' call this to show some help '''

	print('''
memo is the dictionary
	key = name of the event
	value = multiline with things to remember separated by comma
lbx is the listbox with the keys


		''')

root = tk.Tk()
# ==================== Change theme =============== 
style = ttk.Style(root)
root.tk.call('source', 'azure dark\\azure dark.tcl')
style.theme_use('azure')

frm1 = tk.Frame(root)
frm1.pack(side="left", fill="both", expand=True)
lst = tk.Listbox(frm1)
lst.pack(side="left", fill="both", expand=True)
for k in memo:
	lst.insert(tk.END, k)
frm2 = tk.Frame(root)
frm2.pack(side="left")
tbx = tk.Text(frm2)
tbx.pack(side="left")
lst.bind("<<ListboxSelect>>", show)
root.mainloop()