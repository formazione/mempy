import os
import pickle
import tkinter as tk
import tkinter.ttk as ttk

class Data:
	def save_template():
		global memo
		memo = {
			
			"Da pagare" : "tim, enel",
			"Wip" : """
Skate Jack - game,
matchpair - game,
Posizionamento - article for aziendaitalia,
					"""
		}
		with open("memo.pkl", "wb") as file:
			pickle.dump(memo, file)

	def save(event):
		global mem_key
		try:
			key = lst.get(lst.curselection())
			mem_key = key
		except:
			key = mem_key
		memo[key] = tbx.get("0.0", tk.END)
		print("Changes saved")
		with open("memo.pkl", "wb") as file:
			pickle.dump(memo, file)	

	def load_template():
		with open("memo.pkl", "rb") as file:
			memo = pickle.load(file)
		return memo

	def save_once():
		Data.save_template()

	def to_html(event):
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
memo = Data.load_template()

# window

def show(event):
	''' call this to show the note in the tbx '''
	global mem_key
	print(f"{mem_key=}")
	try:
		mm = lst.get(lst.curselection())
	except:
		mm = mem_key
	tbx.delete("0.0", tk.END)
	tbx.insert(tk.END, memo[mm])

def add_memo(event):
	print("Here add a key, asking the name of the key with simpledialog")
	pass

def help():
	''' call this to show some help '''

	print('''
memo is the dictionary
	key = name of the event
	value = multiline with things to remember separated by comma
lst is the listbox with the keys
tbx is the textbox
if you Select a key you see the values in the tbx
		''')

root = tk.Tk()
root.title("Memo - use , to separate the items for each memo")
# ==================== Change theme =============== 
style = ttk.Style(root)
root.tk.call('source', 'azure dark\\azure dark.tcl')
style.theme_use('azure')

frm1 = tk.Frame(root)
frm1.pack(side="left", fill="both", expand=True)
lst = tk.Listbox(frm1)
for k in memo:
	lst.insert(tk.END, k)
lst.pack(side="left", fill="both", expand=True)
lst.selection_set(0)
mem_key = lst.get(0)
lst.event_generate("<<ListboxSelect>>")
lst.activate(0)


frm2 = tk.Frame(root)
frm2.pack(side="left")
tbx = tk.Text(frm2)
tbx.pack(side="left")
lst.bind("<<ListboxSelect>>", show)
# Keys to save file or convert to html
root.bind("<Control-s>", Data.save)
root.bind("<Control-h>", Data.to_html)
root.bind("<Control-+>", add_memo)
root.mainloop()