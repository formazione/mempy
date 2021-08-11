# mempy

This app will make you save your memos with python and tkinter.

![](https://pythonprogramming.altervista.org/wp-content/uploads/2021/08/image-11.png)

![](https://pythonprogramming.altervista.org/wp-content/uploads/2021/08/image-14.png)


This is the most basic code to convert the data in the dictionary into a html table code

      import os

      a = {

        "First" : ["1","2"],
        "Second" : ["1","2","3"] 
      }


      data = ""
      for k in a:
        data += "&lt;td>" + k + "&lt;/td>"
        for d in a[k]:
          data += "&lt;td>" + d + "&lt;/td>"
        data += "&lt;tr>"

      data = "&lt;table border=1>" + data + "&lt;table>"
      print(data)
      with open("file.html", "w") as file:
        file.write(data)

      os.startfile("file.html")
