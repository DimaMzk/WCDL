import urllib.request
import traceback
def update():
    print("Updating Harpy Gee Comic")
    with open('harpygee/status.txt') as f:
        current_page = f.read()
    with open('harpygee/page.txt') as f:
        current_page_number = int(f.read())
    no_error = True
    while(no_error):
        try:
            url = "https://harpygee.com/comic/" + str(current_page)
            print("Downloading Page", current_page_number)
            response = urllib.request.Request(url)
            data = urllib.request.urlopen(response)
            data_read = (data.read().decode('UTF-8'))
            #find the string "Comic Page" as it only shows up once
            comic_page_index = data_read.find("cc-comic\"")
            snippet = data_read[:comic_page_index-1]
            # print(snippet)
            #find https
            snippet = snippet[snippet.rfind("http"):]
            url = snippet[:snippet.find("\"")]
            file_ext = url.split(".")[-1]
            with urllib.request.urlopen(url) as response, open("harpygee/"+ str(current_page_number) + "." + file_ext, 'wb') as out_file:
                data = response.read() # a `bytes` object
                out_file.write(data)
            comic_next_page_index = data_read.find("cc-next\"")
            next_page_snippet = data_read[comic_next_page_index+9:]
            # #find https
            next_page_snippet = next_page_snippet[next_page_snippet.find("http"):]
            next_url = next_page_snippet[:next_page_snippet.find("\"")].split("/")
            with open('harpygee/status.txt', "w+") as f:
                f.write(current_page)
            with open('harpygee/page.txt', "w+") as f:
                f.write(str(current_page_number))
            current_page = next_url[4]
            current_page_number = current_page_number + 1
            
        except UnicodeDecodeError:
            print("Hmm Something Went Wrong, I Might Be Able To Fix It")
            try:
                url = "https://harpygee.com/comic/" + str(current_page)
                print("Downloading Page", current_page_number)
                response = urllib.request.Request(url)
                data = urllib.request.urlopen(response)
                data_read = (data.read().decode('latin-1'))
                #find the string "Comic Page" as it only shows up once
                comic_page_index = data_read.find("cc-comic\"")
                snippet = data_read[:comic_page_index-1]
                # print(snippet)
                #find https
                snippet = snippet[snippet.rfind("http"):]
                url = snippet[:snippet.find("\"")]
                file_ext = url.split(".")[-1]
                with urllib.request.urlopen(url) as response, open("harpygee/"+ str(current_page_number) + "." + file_ext, 'wb') as out_file:
                    data = response.read() # a `bytes` object
                    out_file.write(data)
                comic_next_page_index = data_read.find("cc-next\"")
                next_page_snippet = data_read[comic_next_page_index+9:]
                # #find https
                next_page_snippet = next_page_snippet[next_page_snippet.find("http"):]
                next_url = next_page_snippet[:next_page_snippet.find("\"")].split("/")
                with open('harpygee/status.txt', "w+") as f:
                    f.write(current_page)
                with open('harpygee/page.txt', "w+") as f:
                    f.write(str(current_page_number))
                current_page = next_url[4]
                current_page_number = current_page_number + 1
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                no_error = False
        except Exception as e:
            print(e)
            no_error = False
    with open('harpygee/status.txt', "w+") as f:
        current_page = f.write(str(current_page))
    with open('harpygee/page.txt', "w+") as f:
        f.write(str(current_page_number))
    


