names = []

with open("names.txt") as txt_file:
    # print(txt_file)
    # this means it's in read mode when you take it off the hashtag!
    for line in txt_file:
        line = line.strip()
        names.append(line)

print(names)

for name in names:
    print(name)

    # /n is read on terminal - we don't want. means new line 
    # To get rid of that we put in the - line.strip gets rid of /n

    with open("names_output.txt", "w") as txt_file:
        for name in names:
            txt_file.write(name + "/n")
    #un-indenting closes the file

    