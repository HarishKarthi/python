import PyPDF2
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader=PyPDF2.PdfReader(f)
page_1=pdf_reader.pages[0]
page_one_text=page_1.extract_text()
print(page_one_text)
print("After adding")
pdf_writer=PyPDF2.PdfWriter()
pdf_writer.add_page(page_1)
pdf_output=open("new_doc.pdf","wb+")
pdf_writer.write(pdf_output)
pdf_reader=PyPDF2.PdfReader(pdf_output)
page_1_new=pdf_reader.pages[0]
page_one_text=page_1_new.extract_text()
print(page_one_text)
f.close()