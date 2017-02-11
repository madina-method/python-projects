file1 = open("Lesson5.txt", "r", encoding="UTF-8") #open file for reading

content = file1.read() # read all the file and saves in content variable as ONE BIG string
lines = content.split("\n") # divides content by \n and makes an array of lines ["", "", ""]

before = input("Which symbol/word/number do u want to change?\n") #asks user for input
after = input("To what symbol/word/number do u want to change "+before+"?\n") #nu ponyatno

filename = input("In which file do u want to save modified file?\n") #asks new file name

file2 = open(filename+".txt", "w") #open file for writing
# if something2.txt doesn't exist, program will create it
# else, it will rewrite existing one
# so it's not important does file exist or not

changes = 0  # make an upgrade by adding counter, how many chages were made and notify user
line_number = 1 # to notify user in which line change was made

for line in lines: # for each line in file1
    changes = line.count(before) # counts how mane befores in one line and adds+
    if changes > 0: # there is going to be a change
        print(changes, "changes were made in line ", line_number) # shows it to user in which line
        
    new_line = line.replace(before, after) # replaces before with after in each line
    file2.write(new_line+"\n") # then writes it in new one with enter, a to zhabysyp kalad 1 line-ga
    line_number+=1 # +1 line
    changes = 0 # obnulyaem karoch
    
file2.close() # very important method close(), otherwise we will not see the difference with previous file
#close() it's like save()



