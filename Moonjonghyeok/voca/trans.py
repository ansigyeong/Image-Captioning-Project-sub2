import openpyxl
import codecs

filename = "voca_test.xlsx"
book = openpyxl.load_workbook(filename)

sheet = book.worksheets[0]

def replaceToJson(text):
    if text == None:
        return ""
    else:
        text = text.replace("\n", "\\n")
        text = text.replace('"', '\\"')
        return text

jsonFile = codecs.open('voca_test.json', 'w', 'utf-8')
jsonFile.write('[' + '\n')

i = 1
max_row = sheet.max_row

for row in sheet.rows:
    word = replaceToJson(row[0].value)
    mean = replaceToJson(row[1].value)
    Toeic = row[2].value
    Opic = row[3].value
    korean_SAT = row[4].value

    baseword = '{"model": "english.vocabulary",'
    baseword += '"pk": ' + str((i - 1)) + ','
    baseword += '"fields": {'

    if i != max_row:
        jsonword = '\t"word": "%s", "mean": "%s", "Toeic": "%s", "Opic": "%s", "korean_SAT": "%s"} },' % (word, mean, Toeic, Opic, korean_SAT)
    else:
        jsonword = '\t"word": "%s", "mean": "%s", "Toeic": "%s", "Opic": "%s", "korean_SAT": "%s"} }' % (word, mean, Toeic, Opic, korean_SAT)

    jsonFile.write(baseword + jsonword + '\n')
    i = i + 1

jsonFile.write(']')
jsonFile.close()