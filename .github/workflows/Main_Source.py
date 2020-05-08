import sys
import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('XML File Path')
root = tree.getroot()  

docs = []
doc_ = []
doc_content = {}
coloumn = ['DocID', 'DocNo', 'Orginal File', 'Issue', 'Date_Western', 'Date_Persian', 'Cat_Fa', 'Cat_En', 'Title', 'Text']

for doc in root:
    for node in doc:
        docs.append(node.text)

for i in range (int(len(docs) / 101)):
    for j in range (int(len(docs) / 10)):
        doc_.append(docs[i + (j * 10)])
    doc_content[coloumn[i]] = doc_
    doc_ = []

df = pd.DataFrame(doc_content)
