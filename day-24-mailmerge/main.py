
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
FORMLETTER_FILE = "./Input/Letters/starting_letter.txt"
NAMESLIST = "./Input/Names/invited_names.txt"
OUTPUTFOLDER = "./Output/ReadyToSend/"

with open(FORMLETTER_FILE, "r") as form:
    form_letter = form.read()

with open(NAMESLIST, "r") as names:
    file_has_lines = True
    while file_has_lines:
        # chose to use readline instead of readlines to avoid holding the namelist
        # in memory
        name = names.readline().strip() # strip drops whitespace including newline from the read
        if name != "":
            personal_letter = form_letter.replace("[name]", name)
            outputfile = f"{OUTPUTFOLDER}letter_for_{name}"
            with open(outputfile,"w") as letter:
                letter.write(personal_letter)
        else:
            # readline produces empty string on EoF; exit the while loop
            file_has_lines = False
