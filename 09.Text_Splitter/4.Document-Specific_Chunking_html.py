from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.text_splitter import Language

markdown_doc = '''
# Data Analysis Project
A comprehensive analytics platform

## Features
- Real-time dashboards
- Predictive modeling
- Export capabilities

## Tech Stack
- Python 3.10+
- PostgreSQL database
'''

text_splitter=RecursiveCharacterTextSplitter.from_language(language=Language.MARKDOWN,
    chunk_size=120,
    chunk_overlap=4
)

docs=text_splitter.split_text(markdown_doc)

print(len(docs))

print(docs[0])
print("---------------------------------------------------------")
print(docs[1])
print("---------------------------------------------------------")
print(docs[2])