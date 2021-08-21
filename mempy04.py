import os
import pickle
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog
from tk_html_widgets import HTMLLabel, HTMLScrolledText


class Data:
	def save_template():
		global memo
		memo = {
			
			"Help keys" : """
ctrl +
	n   new memo
	d   delete memo selected
	h   show html file with memos
	s   saves the new data

			""",
			"Credits" : """
pythonprogramming.altervista.org
@pythonprogrammi
pythonprogrammi on youtube
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
		
		html("")
		html(Data.html())


	def load_template():
		with open("memo.pkl", "rb") as file:
			memo = pickle.load(file)
		return memo

	def save_once():
		''' cann this once to start from scratch '''
		Data.save_template()

	def to_html(event, show=1):
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
		if show:
			os.startfile("file.html")
		return data

	def html():
		''' this is to be displayed on the right '''
		data = ""
		print(memo)
		for k in memo:
			print(k)
			data += "<b style='color:red'>" + k + "</b>"
			for d in memo[k].split(","):
				data += "<p>" + d + "</p>"
				data += "<br>"
		print(data)
		return data

	def add_memo(event):
		new_memo = simpledialog.askstring("New Memo", "Insert the title of the memo")
		memo[new_memo] = ""
		read_memo()
		show("some")

	def delete_memo(event):
		key2delete = lst.get(lst.curselection())
		del memo[key2delete]
		Data.save_memo()
		read_memo()
		show("some")


# Uncomment the following to have a new start
# Data.save_template()
memo = Data.load_template()

# window

def show(event):
	''' call this to show the note in the tbx '''
	global mem_key
	# print(f"{mem_key=}")
	try:
		mm = lst.get(lst.curselection())
	except:
		mm = mem_key
	tbx.delete("0.0", tk.END)
	tbx.insert(tk.END, memo[mm])



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
def read_memo():
	lst.delete(0, tk.END)
	for k in memo:
		if k != None:
			lst.insert(tk.END, k)
	lst.selection_set(0)

read_memo()
lst.pack(side="left", fill="both", expand=True)
lst.selection_set(0)
mem_key = lst.get(0)
lst.event_generate("<<ListboxSelect>>")
lst.activate(0)


frm2 = tk.Frame(root)
frm2.pack(side="left", fill="both", expand=True)
tbx = tk.Text(frm2)
tbx.pack(side="left")
lst.bind("<<ListboxSelect>>", show)
# Keys to save file or convert to html
root.bind("<Control-s>", Data.save)
root.bind("<Control-h>", Data.to_html)
root.bind("<Control-n>", Data.add_memo)
root.bind("<Control-+>", Data.add_memo)
root.bind("<Control-d>", Data.delete_memo)
frm3 = tk.Frame(root)
frm3.pack(side="left", fill="both", expand=True)
# ================== mempy03

html_code = HTMLScrolledText(frm3,
	html="")
html_code.pack(fill="both", expand=True)
html_code.fit_height()
def html(code):
	html_code.set_html(code)
	return html_code


html(Data.html())
lst.selection_set(0)
show("hello")
root.mainloop()