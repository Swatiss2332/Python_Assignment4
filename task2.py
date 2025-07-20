## Task 2: Write and Append Data to a File

## STEP 1: WRITE 
file=open("output.txt","w")
text_to_write=input("Enter text to write to the file: ")
file.write(text_to_write+"\n")
file.close()
print("Data successfully written to output.txt.")

## STEP 2: APPEND
file=open("output.txt","a")
text_to_append=input("Enter additional text to append: ")
file.write(text_to_append+"\n")
file.close()
print("Data successfully appended.")

## STEP 3: DISPLAY FINAL CONTENT
file=open("output.txt","r")
print("Final content of output.txt: ")
output=file.read()
print(output)
file.close()
