import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def askforbirthdate():
    geboortedatum = ""
    while not (validate(geboortedatum)):
        geboortedatum = input("Geef geboortedatum in (dd-MM-yyyy): ")
    return geboortedatum


filepath = input("Vul pad in (bijv. C:\\temp\\rainbow.txt): ")

try:
    with open(filepath, 'w') as f:
        voornaam = input("Geef voornaam in: ")
        achternaam = input("Geef achternaam in: ")
        geboortedatum = askforbirthdate()
        date_time_obj = datetime.datetime.strptime(geboortedatum, '%d-%m-%Y')


        firstNameVariations = [voornaam, voornaam[0], voornaam.upper()[0]]
        lastNameVariations = [achternaam, achternaam[0], achternaam.upper()[0]]
        birthDateVariations = [str(date_time_obj.day), 
        str(date_time_obj.month), 
        str(date_time_obj.year), 
        str(date_time_obj.day) + str(date_time_obj.month), 
        str(date_time_obj.day) + str(date_time_obj.month) + str(date_time_obj.year)]


        for firstnamevar in firstNameVariations:
            for lastnamevar in lastNameVariations:
                for birthdatevar in birthDateVariations:
                    f.write(firstnamevar + lastnamevar + birthdatevar)
                    f.write("\n")
                    f.write(firstnamevar[::-1] + birthdatevar)
                    f.write("\n")
                    f.write(firstnamevar + birthdatevar)
                    f.write("\n")
                f.write(firstnamevar + lastnamevar)
                f.write("\n")
                f.write(lastnamevar + firstnamevar)
                f.write("\n")
            f.write(firstnamevar[::-1])
            f.write("\n")
        print("Woohoo! Rainbow table created")
except OSError:
    print("Could not open/read file:")