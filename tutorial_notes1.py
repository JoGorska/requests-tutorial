import requests

r = requests.get('https://xkcd.com/353')
print(dir(r))  # gives me all methods and attributes of this response object
print(help(r))  # gives more information than above
print(r.text)  # gives content of the response in unicode - just html

# keyword file= in print allows save result of the print statement into a file
sourceFile = open('results/website.html', 'w')
print(r.text, file=sourceFile)
sourceFile.close()

# to get image
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content)  # gets image in bytes

# reading and writing files with python:
with open('results/comic.png', 'wb') as f:
    f.write(r.content)


# http status_code

r = requests.get('https://imgs.xkcd.com/comics/python.png')
# 200 s are success
# 300 s are redirects
# 400 s are client errors, like forbidden
# 500 s are server errors, site crashed
print(r.status_code)
# r.ok gives True for anything that is less than 400
print(r.ok)
# todo write website monitori script - that checks just that

# more info about this response
print(r.headers)
