usablechar = 'urldjkxzcg'   #'urldjkxzcgs' 


TASfile_loc = input("Full location of the tas file > ") #../TAS_into_sally/ExampleTAS.tas

uppercase = input('Do you want the commands to be in uppercase? [y/n] ').upper() == 'Y' #only yes means yes


try:
    TASfile = open(TASfile_loc)
except:
    raise ValueError("I mean, is not that difficut, just copy the path of the file")
lines_list = TASfile.readlines()

toremove = []


for i in range(len(lines_list)):

    lines_list[i] = lines_list[i].replace(' ', '').replace('\n', '').replace(',', '')

    if not uppercase:
        lines_list[i] = lines_list[i].lower()

    try:
        if not lines_list[i][0].isdigit():
            toremove.append(lines_list[i])
    except:
        toremove.append(lines_list[i])
        

for x in toremove:
    lines_list.remove(x)

command = ' '.join(lines_list)

for x in command:
    if (x not in usablechar) and (not x.isdigit()) and (x != ' '):
        print(f'Warning: \'{x}\' is not an usable char')

print("You can copypaste this in chat (probably, i didnt debug much lol):\n" + command)
