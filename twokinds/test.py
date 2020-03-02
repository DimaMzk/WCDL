import urllib.request
url = "https://harpygee.com/comic/page-1"
response = urllib.request.Request(url)
data = urllib.request.urlopen(response)
data_read = (data.read().decode('UTF-8'))
print(data_read)
#find the string "Comic Page" as it only shows up once
comic_page_index = data_read.find("cc-comic\"")
snippet = data_read[:comic_page_index-1]
# #find https
snippet = snippet[snippet.rfind("http"):]
url = snippet[:snippet.find("\"")]
file_ext = url.split(".")[-1]
print(url)
comic_next_page_index = data_read.find("cc-next\"")
next_page_snippet = data_read[comic_next_page_index+9:]
# #find https
next_page_snippet = next_page_snippet[next_page_snippet.find("http"):]
next_url = next_page_snippet[:next_page_snippet.find("\"")].split("/")
print(next_url[4])

# with urllib.request.urlopen(url) as response, open("twokinds/852." + file_ext, 'wb') as out_file:
#     data = response.read() # a `bytes` object
#     out_file.write(data)