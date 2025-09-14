
def translate(from_letters, to_letters, text):
    """
    The translate function does a letter to letter translation.
    The from_letters and to_letters parameters are expected to
    be strings of uppercase letters and both strings need to be 
    the same length. The from_letters and to_letters strings define
    a mapping such that from_letters[i] found in the text string 
    parameter will be converted to to_letters[i].  All characters in 
    the text parameter not found in from_letters are left as-is.
    Case of letters in the text parameter are preserved in the result.
    For example translate("ABC","CAB","C3PO-aBA") will return the 
    string "B3PO-cAC".  Likewise, translate("CAB","ABC","B3PO-cAC")
    will return the string "C3PO-aBA".   
    """
    # Check that parameters meet assumptions. The only assumption not
    # tested is that each character in from_letters should occur once.
    # Students should not change this code.  It is here to catch mistakes.
    if not(from_letters.isupper() and from_letters.isalpha() and 
           to_letters.isupper() and to_letters.isalpha()):
        raise ValueError("from_letters and to_letters must be all uppercase letters")
    if len(from_letters) != len(to_letters):
        raise ValueError("from_letters and to_letters must be the same length")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Students should add their code below for the translate function

    word = ""
    for i in range(len(text)):
        if text[i] == (text[i].upper()):       
            index = from_letters.find(text[i])
            if (index == -1):
                word = word + text[i] #adds original character if the letter is not in the key
            else:
                word = word + to_letters[index] # adds the corresponding value of the key
        else:
            index = from_letters.find(text[i].upper())
            if (index == -1):
                word = word + text[i]
            else:
                word = word + to_letters[index].lower()
    return word




def get_key(line):
    """ takes a textfile name in and returns the first line of the file"""
    
    infile = open(f"{line}", "r")
    key = infile.readline()
    infile.close()
    return key

def get_input(line):
    """reads the lines of a textfile (input is the name of textfile) and 
        returns contents in a list"""
    input = []
    infile = open(f"{line}", "r")
    text = infile.readline()
    while text!= "":
        input.append(text)
        text = infile.readline()
    infile.close()
    return input


def main():
    """completes the task of either decrypting or encrpyting 
    a file all based on a command file which includes the name of a key file,
    the order to encrypt or decrypt, the file to act on and the 
    file to output the result to"""
    infile = open("/Users/jovandosanjh/python/dsa/Cryptography project/commands.txt", "r")
    line = infile.readline()
    contents = []
    
    while line!= "":
        contents.append(line.strip())
        line = infile.readline()    
    infile.close()
    
    key = get_key(contents[0])

    input = get_input(contents[2])
    
    alpha = ""
    for i in range(26):
        alpha = alpha + (chr(65+i))
        
    newfile = contents[len(contents) - 1]
    output = open(f"{newfile}", "w")
    
    if contents[1] == "encrypt":
        for i in range(len(input)):
            word = translate(alpha,key,input[i])
            output.write(f"{word}")
    elif contents[1] == "decrypt":
        for i in range(len(input)):
            word = translate(key,alpha,input[i])
            output.write(f"{word}")

    output.close

    



if __name__ == "__main__":
    main()