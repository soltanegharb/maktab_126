def replace_content(pattern_string,replacement_string,file_input='file_input.txt',file_output='file_output.txt'):
    """reads a file and replaces a "string" with a "pattern_string"
    and writes the new content to a new file"""
    
    try:
        # open the file and read the content
        with open(file_input, 'r') as file:
            content = file.read()
            # replace the pattern_string with the replacement_string
            content_new = content.replace(pattern_string, replacement_string)
        # write the new content to a new file
        with open(file_output, 'w') as file:
            file.write(content_new)
    # if an error occurs, return the following message
    except:
        return 'Nope,\nSomething Went Wrong\nTry Again'
# test the function
replace_content('Mohammad','Ali','file_input.txt','file_output.txt')
