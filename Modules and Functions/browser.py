import webbrowser


#
# webbrowser.open("https://www.facebook.com/" )
# help(webbrowser)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open('http://docs.python.org/')