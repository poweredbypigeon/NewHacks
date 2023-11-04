import PyPDF2
file1 = r'C:/Users/compl/Documents/Engineering Science/Y1S1/ESC194H1/James Stewart, Daniel K. Clegg, Saleem Watson - Calculus-Cengage Learning (2020).pdf'
file2 = r'C:/Users/compl/Documents/summations.pdf'
reader = PyPDF2.PdfReader(file1)
# print(reader.extractText())
page = reader.getPage(406)
# print(page)
# print('Page type: {}'.format(str(type(page))))
text = page.extractText()
print(text)
print(len(text))