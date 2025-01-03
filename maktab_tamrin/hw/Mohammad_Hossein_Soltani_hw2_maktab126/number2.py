def parse_contacts():
    """reads a file named contacts.txt and returns a dictionary 
    where the keys are the names and the values are the phone numbers"""

    # error handling for reading file in case of any error
    try:
        # opening file
        with open("contacts.txt", "r") as f:
            lines = f.readlines()
            contacts = dict()
            # reading lines of file
            for line in lines:
                # editing line for a good output
                contact = line.strip().split(",")
                for x in range(len(contact)):
                    contact[x] = contact[x].strip()
                # adding to dictionary
                contacts[contact[0]] = contact[1]
            return contacts
    except:
        return "Error in reading contacts file"
# test
print(parse_contacts())