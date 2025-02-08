from langchain_community.document_loaders import WebBaseLoader

# Step 1: Load data from the given URL
url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
documents = loader.load()

# Print a preview of the extracted data
print(f"Extracted {len(documents)} documents")
print(documents[:2])  # Show the first two documents

