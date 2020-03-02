import urllib.request

def update():
    print("Updating Twokinds Comic")
    with open('twokinds/status.txt') as f:
        current_page = int(f.read())
    if(current_page == ""):
        current_page = 1
    no_error = True
    while(no_error):
        try:
            url = "http://twokinds.keenspot.com/comic/" + str(current_page) + "/"
            print("Downloading Page", current_page)
            response = urllib.request.Request(url)
            data = urllib.request.urlopen(response)
            data_read = (data.read().decode('UTF-8'))
            #find the string "Comic Page" as it only shows up once
            comic_page_index = data_read.find("Comic Page")
            snippet = data_read[comic_page_index-250:comic_page_index-1]
            # print(snippet)
            #find https
            snippet = snippet[snippet.rfind("http"):]
            url = snippet[:snippet.find("\"")]
            file_ext = url.split(".")[-1]
            with urllib.request.urlopen(url) as response, open("twokinds/"+ str(current_page) + "." + file_ext, 'wb') as out_file:
                data = response.read() # a `bytes` object
                out_file.write(data)
            with open('twokinds/status.txt', "w+") as f:
                f.write(str(current_page - 1))
            current_page = current_page + 1
        except Exception as e:
            print(e)
            no_error = False
    with open('twokinds/status.txt', "w+") as f:
        current_page = f.write(str(current_page - 1))
    