import os

a = {
	
	"Da pagare" : "tim enel".split(" "),
	"Post" : [
			"1",
			"2",
			"3"] 
}


data = ""
for k in a:
	data += "<td>" + k + "</td>"
	for d in a[k]:
		data += "<td>" + d + "</td>"
	data += "<tr>"

data = "<table border=1>" + data + "<table>"
print(data)
with open("file.html", "w") as file:
	file.write(data)

os.startfile("file.html")