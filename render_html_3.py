import tkinter as tk
from tk_html_widgets import HTMLLabel

root = tk.Tk()

def tag(_type="h1", text="hello", color="black",text_align="center"):
	"Parses some html tags"
	html_label = HTMLLabel(root, html=f'<{_type} style="color: {color}; text-align: {text_align}"> {text} >/{_type}>')
	html_label.pack(fill="both", expand=True)
	html_label.fit_height()
	return html_label

def html(code):
	html_code = HTMLLabel(root,
		html=code)
	html_code.pack(fill="both", expand=True)
	html_code.fit_height()
	return html_code


html("""
<h1>Title</h1>
<p style='color:blue'>Hello this is the whole <u>page</u></p>
<ul>
<li>1
<li>2
</ul>
""")

root.mainloop()
