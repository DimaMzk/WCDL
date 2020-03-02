import urllib.request
print("Web Comic Downloader Build 20200217001")
print("Setting Configuration")
#reading options and setting configuration
with open('options.txt') as f:
    read_data = f.read()
print(read_data)
config = read_data.split(",\n")
final_config = []
print(config)
for array in config:
    array = array.split(":")
    final_config.append(array)
print(final_config)
print("Done")
print("Importing Classes...")
#import TwoKinds
twokindsSet = False
harpygeeSet = False
if (str(final_config[0][1]).lower() == 'true'):
    print("Importing TwoKinds")
    import twokinds.twokinds
    twokindsSet = True
if (str(final_config[1][1]).lower() == 'true'):
    print("Importing Harpy Gee")
    import harpygee.harpygee
    harpygeeSet = True
print("Imports Complete!")

valid_input = False
while (valid_input == False):
    print("a - Update All")
    if(twokindsSet):
        print("t - Update Twokinds")
    if(harpygeeSet):
        print("h - Update Herpy Gee")
    print("r - Reset Configuration")
    print("q - quit")
    user_input = input(">> ")
    user_input = user_input[0].lower()
    if(user_input == 'a'):
        twokinds.twokinds.update()
        harpygee.harpygee.update()
        valid_input = True
    if(user_input == 't'):
        twokinds.twokinds.update()
        valid_input = True
    if(user_input == 'h'):
        harpygee.harpygee.update()
        valid_input = True
    if(user_input == 'r'):
        print("TODO: Add Config Reset")
        valid_input = True
    if(user_input == 'q'):
        print("Goodbye")
        valid_input = True


# url = "http://twokinds.keenspot.com/comic/1/"
# response = urllib.request.Request(url)
# data = urllib.request.urlopen(response)
# data_read = (data.read().decode('UTF-8'))
# print(data_read)