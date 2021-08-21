import tkinter as tk
from tkinterhtml import HtmlFrame



root = tk.Tk()
frame = HtmlFrame(root, horizontal_scrollbar="auto")
 
frame.set_content("""
	<html>

	<body>

<p> Hello</p>

</body

	</html>""")
frame.pack()

root.mainloop()