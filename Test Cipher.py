from cipher import main
import os

def test_cipher_encryption():
    """
    Tests encryption ability of the cipher program.
    """
    newfile = open("file_to_encrypt.txt", "w")
    newfile.write("  AB\n")
    newfile.write("  ab")
    newfile.close()
    command = open("commands.txt", "w")
    command.write("key.txt \n")
    command.write("encrypt \n")
    command.write("file_to_encrypt.txt \n")
    command.write("encrypted_test_file.txt \n")
    command.close()
    
    key = open("key.txt", "w")
    key.write("JIOCANTRQWUKVEGXPDFZBMHLSY")
    key.close()
    main()
    
    
    result = open("encrypted_test_file.txt", "r")
    line = result.readline()
    results = ""
    while (line!=""):
       results= results + line
       line = result.readline()
    result.close()

    print(results)

    os.remove("key.txt")
    os.remove("commands.txt")
    os.remove("file_to_encrypt.txt")
    os.remove("encrypted_test_file.txt")
    
    assert ( results == "  JI\n  ji")

def test_cipher_decryption():
    """
    Tests decryption ability of the cipher program.
    """
    newfile = open("file_to_decrypt.txt", "w")
    newfile.write("Zafzqet")
    newfile.write("\tZafz 123")
    newfile.close()
    command = open("commands.txt", "w")
    command.write("key.txt \n")
    command.write("decrypt \n")
    command.write("file_to_decrypt.txt \n")
    command.write("decrypted_test_file.txt \n")
    key = open("key.txt", "w")
    key.write("JIOCANTRQWUKVEGXPDFZBMHLSY")
    key.close()
    command.close()
    main()
    
       
    result = open("decrypted_test_file.txt", "r")
    line = result.readline()
    results = ""
    while (line!=""):
       results = results + line
       line = result.readline()
    result.close()

    os.remove("key.txt")
    os.remove("commands.txt")
    os.remove("file_to_decrypt.txt")
    os.remove("decrypted_test_file.txt")
    
    assert ( results == "Testing\tTest 123")

def test_roundtrip():
    """
    Tests the ability of the cipher program by
    encrypting a file and then decryting the file
    in order to verify that the program can return
    the original contents.
    """
    newfile = open("file_to_encrypt.txt", "w")
    newfile.write("Back to normal")
    newfile.close()
    command = open("commands.txt", "w")
    command.write("key.txt \n")
    command.write("encrypt \n")
    command.write("file_to_encrypt.txt \n")
    command.write("encrypted_test_file.txt \n")
    command.close()
    key = open("key.txt", "w")
    key.write("JIOCANTRQWUKVEGXPDFZBMHLSY")
    key.close()
    main()

    
    command = open("commands.txt", "w")
    command.write("key.txt \n")
    command.write("decrypt \n")
    command.write("encrypted_test_file.txt \n")
    command.write("decrypted_test_file.txt \n")
    command.close()
    key = open("key.txt", "w")
    key.write("JIOCANTRQWUKVEGXPDFZBMHLSY")
    key.close()
    main()
    
    
    result = open("decrypted_test_file.txt", "r")
    line = result.readline()
    results = ""
    while (line!=""):
       results = results + line
       line = result.readline()
    result.close()

    os.remove("key.txt")
    os.remove("commands.txt")
    os.remove("file_to_encrypt.txt")
    os.remove("encrypted_test_file.txt")
    os.remove("decrypted_test_file.txt")
    
    assert ( results == "Back to normal")


