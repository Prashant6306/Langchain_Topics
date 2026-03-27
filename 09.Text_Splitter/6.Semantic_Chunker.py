from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

mixed_topic_text = '''
Farmers cultivated crops for the season. The weather was ideal.
The cricket championship attracted millions globally.

Climate change threatens ecosystems. Scientists warn of rising
temperatures. Urgent action needed to prevent catastrophe.
'''

load_dotenv()

# Create semantic chunker (experimental)
semantic_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1  # 1 std dev
)

semantic_chunks = semantic_splitter.create_documents([mixed_topic_text])
print(f"Semantic chunks: {len(semantic_chunks)}")
for i, chunk in enumerate(semantic_chunks):
    print(f"\nChunk {i+1}:\n{chunk.page_content}")