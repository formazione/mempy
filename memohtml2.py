import os

memo = {
	
	"Da pagare" : "tim, enel",
	"Wip" : """
			Skate Jack - game,
			matchpair - game,
			Posizionamento - article for aziendaitalia
			"""
}


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