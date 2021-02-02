
def createWriteFile():
    writeFile = open("amber-alerts.csv", "x")
    headers = "site,machine,tag,value,type,date"
    writeFile.writelines(headers+'\n')
    writeFile.close()


createWriteFile()


readFile = open('AmberAlertEmails_20201123.txt', 'r')
writeFile = open("amber-alerts.csv", "a")
infoFmt = "{0},{1},{2},{3},{4},{5}"
nextLine = ""
site = ""
machine = ""
tagname = ""
tagvalue = ""
timestamp = ""
alerttype = ""
for line in readFile:

    if "Alert Type" in line:
        alerttype = line.split(":")[1].strip()

    if "Site" in line:
        site = line.split(":")[1].strip()

    if "Machine" in line:
        machine = line.split(":")[1].strip()

    if "Tag Name" in line:
        tagname = line.split(":")[1].strip()

    if "Tag Value" in line:
        tagvalue = line.split(":")[1].strip()

    if "Time" in line:
        timestamp = line.split(":", 1)[1].strip()

    if "From" in line:
        print(infoFmt.format(
            site, machine, tagname, tagvalue, alerttype, timestamp))
        newLine = infoFmt.format(
            site, machine, tagname, tagvalue, alerttype, timestamp)
        writeFile.write(newLine + '\n')
        nextLine = ""
        site = ""
        machine = ""
        tagname = ""
        tagvalue = ""
        timestamp = ""
        alerttype = ""


readFile.close()
writeFile.close()
