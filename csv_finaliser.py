import csv
import os

def csv_finaliser(filename):
    with open(r"./extracted/currently_building.csv", "r", encoding="UTF-8") as input_file, \
         open(r"./extracted/{}.csv".format(filename), "a+", encoding="UTF-8", newline="") as output_file: # opens files for editing
        reader = csv.reader(input_file, delimiter="↊")
        writer = csv.writer(output_file, delimiter=",", dialect="excel")

        mail_counter = 0
        phone_counter = 0
        #loops over every line of the file
        for line in reader:

            title            = line[0]
            url              = line[1]
            description      = line[2]
            site_description = line[3]
            screenshot       = line[4]
            mail             = line[5]
            phone            = line[6]

            #converts mail-string to list
            if len(mail) == 2:
                mail = []
            else:
                mail = mail.replace("[", "")
                mail = mail.replace("]", "")
                mail = mail.replace("'", "")
                mail = mail.replace(" ", "")
                mail = list(mail.split(","))
                mail_counter += len(mail)
            #converts phone-string to list
            if len(phone) == 2:
                phone = []
            else:
                phone = phone.replace("[", "")
                phone = phone.replace("]", "")
                #phone = phone.replace("'", "") #toggle between number and string
                phone = phone.replace(" ", "")
                phone = list(phone.split(","))
                phone_counter += len(phone)

            #writes new lines to a new file
            while len(mail) > 0 and len(phone) > 0:
                writer.writerow([url, mail.pop(), phone.pop()])
            while len(mail) > 0:
                writer.writerow([url, mail.pop(), ""])
            while len(phone) > 0:
                writer.writerow([url, "", phone.pop()])

        #finishes editing the files
        input_file.close()
        output_file.close()

    #removes temporary file
    os.remove(r"./extracted/currently_building.csv")
    return(mail_counter, phone_counter)
