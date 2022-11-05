import re
import time
starttime=time.time()
for i in range (100):
    def multiple_replace(target_str, replace_values):
        for i, j in replace_values.items():
            target_str = target_str.replace(i, j)
        return target_str
    def fileToString(xmlFile):
        myfile = open(xmlFile, "r", encoding="utf-8")
        xmlString = ''
        for i in myfile:
            xmlString += i
        return xmlString
    data=fileToString("scratch.xml")
    data=data.replace('<?xml version="1.0" encoding="UTF-8" ?>', "")
    data=data.replace('<root>', '{')
    data=data.replace('</root>', '}')

    pattern0=r"<\/lesson8>"
    data=re.sub(pattern0, '}', data)
    pattern1=r"<\/.*?>"
    pattern2=r"</lesson\d>"
    pattern3=r"<lesson(\d)>"
    pattern4=r"<(.*)? \/>"
    pattern5=r"<weekNumber>([2,3])</weekNumber>"
    pattern6=r"<weekNumber>5<\/weekNumber>"
    pattern7=r"<weekNumber>(\d*)<\/weekNumber>"
    pattern8=r"<weekNumber>(16)<\/weekNumber>"
    pattern9=r"<weekNumber>(17)<\/weekNumber>"
    pattern10=r'("finishTime": (.*)?),'
    data=re.sub(pattern3, r'"lesson\1":{', data)
    data=re.sub(pattern5, r'"weekNumber": [\n\t\t\1,', data)
    data=re.sub(pattern6, r'"weekNumber":[\n\t\t5\n\t\t],', data)
    data=re.sub(pattern8, r'\1\n\t\t],', data)
    data=re.sub(pattern9, r'\1\n\t\t],', data)
    data=re.sub(pattern7, r'\1,', data)
    data=re.sub(pattern2, '},', data)
    data=re.sub(pattern1, '",', data)
    data=re.sub(pattern4, r'"\1": null,', data)
    data=data.replace('<', '"')
    data=data.replace('>', '": "')
    data=re.sub(pattern10, r'\1', data)
    #print(data)
    my_file = open("scratch.json", "w+")
    my_file.write(data)
    my_file.close()
print(time.time()-starttime)