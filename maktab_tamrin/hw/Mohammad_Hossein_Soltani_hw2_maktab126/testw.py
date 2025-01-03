
# open the file and read the content
with open("ddd.txt", 'r') as file:
    content = file.read()
    # replace the pattern_string with the replacement_string
    content_new = content.replace("Asus", "replacement_string")
# write the new content to a new file
with open("ddd.txt", 'w') as file:
    file.write(content_new)
# if an error occurs, return the following message