#! python3
# A simple script to rename pdf report cards based on student info

import os, PyPDF2, re, sys
 
regex_text = r'(\w+, \w+\n |\w+, \w+ \w+\n |\w+, \w+\n \n|\w+, \w+ \w+\n \n)\(\d+\)'
search_regex = re.compile(regex_text)
# search for student info using regexes

count = 0
# used to count the number of files changed

if(len(sys.argv) < 2):
  print(r'''usage: python3 renamepdf.py  '[path to folder] ' - renames all files in folder''')
  exit()
elif(os.path.exists(sys.argv[1]) == False):
  print('Invalid path please get the right path and try again')
  exit()
# Verifies that user typed a patn and if the path exists
    
print(sys.argv[1])
for root, subfolders, filenames in os.walk(str(sys.argv[1])):
  for file in filenames:
    file_path = root + '/' + file
    get_pdf = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(get_pdf)
    get_page = pdf_reader.getPage(0)
    get_text = get_page.extractText()
    search_name = search_regex.search(get_text)
    if(search_name != None ):
      get_name = search_name.group()
      new_name = root + '/' + get_name + '.pdf'
      os.rename(file_path, new_name)
      get_pdf.close()
      count += 1
print('Done!!! total changed: ' + str(count))