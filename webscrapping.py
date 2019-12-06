from bs4 import BeautifulSoup

html_doc = """ <html>
<head>
<title>Umer</title>
</head>

<body>
<div class="my"id="first">
FIRST DIV
</div>
<div class="my" id="second">
SECOND DIV
</div>
</body>


</html> """

# print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct
print(soup.body)  # <body>...</body>
print(soup.head.title)  # <title>Umer</title>

# find()    Give only first appreance
firstDiv = soup.find('div')
print(firstDiv)

# findAll()   Give all divs in form of list(Array)
allDivs = soup.findAll('div')
print(allDivs)
print(allDivs[0])
print(allDivs[1])


elementWithID = soup.findAll(id='first')
print(elementWithID)

elementsWithClass = soup.findAll(class_='my') # cannot use class, as class is reserved keyword
print(elementsWithClass) 

#getText() to get text between the tags (actual data)
textOfFirstDiv = soup.find('div').getText()
print(textOfFirstDiv)

######## We can also use select() instead of find() but select always return data in form of list
print('-----------------------------------------------------')
for divText in soup.findAll('div'):
    print(divText.getText())

print('++++++++++++++++++++++++++++++')

# NAVIGATION

body = soup.body
print(body)

bodyContent = soup.body.content
print(bodyContent)

bodyContents = soup.body.contents # in form of array
print(bodyContents)



# run python webscrapping.py


####  Add this in settings.json in case of error

#{
#    "python.pythonPath": "/path/to/your/venv/bin/python",
#}