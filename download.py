import wget


url = "https://golang.org/dl/go1.17.3.windows-amd64.zip"
file = wget.download(url)
print("\n")
print(file)
