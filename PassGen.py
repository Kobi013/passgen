import os
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def askforbirthdate():
    birthDay = ""
    while not (validate(birthDay)):
        birthDay = input("Birthday (dd-MM-yyyy): ")
    return birthDay


def setUserPath():
    user_name = os.getlogin()
    save_path = 'C:\\Users\\{}\\Documents\\Rainbow'.format(user_name)
    file_name = 'rainbow.txt'
    completePath = os.path.join(save_path, file_name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    return (completePath)    


try:
    with open(setUserPath(), 'w') as f:
        firstName = input("Firstname: ")
        lastName = input("Lastname: ")
        birthDay = askforbirthdate()
        date_time_obj = datetime.datetime.strptime(birthDay, '%d-%m-%Y')


        firstNameVariations = [firstName, firstName[0], firstName.upper()[0]]
        lastNameVariations = [lastName, lastName[0], lastName.upper()[0]]
        birthDateVariations = [
        str(date_time_obj.day), 
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
        print("Rainbow table created in {}.".format(setUserPath()))

except OSError:
    print("Something went wrong, try again.") 
