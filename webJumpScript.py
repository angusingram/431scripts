import webbrowser

url = 'http://docs.python.org/'
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

urls = open("urls.txt", "r")
for url in urls:
    webbrowser.open(url)
