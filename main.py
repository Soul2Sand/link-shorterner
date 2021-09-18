import pyshorteners

link = input("input your link: ")

shortener = pyshorteners.Shortener()

new_link = shortener.tinyurl.short(link)

print(new_link)