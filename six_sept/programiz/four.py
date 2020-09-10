
# merge mails


# when we want to send the same invitation to many people, the body does of the mail does not change.
# only the name needs to be changed

# mail merge is a process of doing this. Instead of writing each mail separately, we have a
# template for body of the mail and a list of names that we merge together to form all the mails.



# names are in the file names.txt
# body of the mail is in the body.txt

# open names.txt for reading
with open("body.txt", 'r', encoding = 'utf-8') as names_file:

    # open body.txt for reading
    with open("body.txt", 'r', encoding = 'utf-8') as body_file:


        # read entire content of the body
        body = body_file.read()

        # iterate over names
        for name in names_file:
            mail = 'Hello '+name+body

            # write the mails to individual files
            with open(name.strip()+".txt", 'w', encoding = 'utf-8') as mail_file:
                mail_file.write(mail)


print(mail)














