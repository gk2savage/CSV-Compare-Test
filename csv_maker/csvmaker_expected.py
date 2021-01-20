import csv
with open('expected.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["var", "data"])
    writer.writerow(["id",101])
    writer.writerow(["name","gk"])
    writer.writerow(["department","Security"])
    writer.writerow(["address","D-601, White Apartments, Highway Road"])
    writer.writerow(["pincode",123456])
    writer.writerow(["joining","10/1/2010"])
    writer.writerow(["creds",'{"access-level":"A1","server-access":"yes","ftp-user":"gk5012","ssh-user":"a1user","ssh-pass":"s3cur3"}'])

