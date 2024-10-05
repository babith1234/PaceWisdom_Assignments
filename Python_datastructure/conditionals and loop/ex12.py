no_of_classes_held = int(input("Enter the number of classes held"))
no_of_classes_attended = int(input("Enter the number of attended classes"))

attendence_percent = (no_of_classes_attended/no_of_classes_held)*100
print(attendence_percent)

if(attendence_percent>75):
    print("Allowed")
else:
    print("Not Allowed")    