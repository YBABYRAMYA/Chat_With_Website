from bs4 import BeautifulSoup
import requests
from sentence_transformers import SentenceTransformer, util

# Load the SentenceTransformer model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to fetch and clean webpage content
def fetch_webpage_content(target_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract relevant text content
        extracted_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        webpage_text = "\n".join([element.get_text(strip=True) for element in extracted_elements])
        return webpage_text
    except Exception as error:
        print(f"Failed to fetch content from {target_url}: {error}")
        return ""

# Function to filter content based on keywords
def extract_relevant_text(content_text, search_terms):
    text_lines = content_text.split("\n")
    filtered_text = [line for line in text_lines if any(term.lower() in line.lower() for term in search_terms)]
    return "\n".join(filtered_text)

# Function to split content into smaller chunks
def split_into_chunks(cleaned_text, word_limit=100):
    paragraphs = [para.strip() for para in cleaned_text.split("\n") if para.strip()]
    text_chunks = []
    for para in paragraphs:
        words = para.split()
        for start in range(0, len(words), word_limit):
            text_chunks.append(" ".join(words[start:start + word_limit]))
    return text_chunks

# Function to locate the most relevant chunks for the query
def get_relevant_chunks(user_query, chunks, top_results=3):
    chunk_vectors = embedding_model.encode(chunks, convert_to_tensor=True)
    query_vector = embedding_model.encode(user_query, convert_to_tensor=True)
    similarity_scores = util.cos_sim(query_vector, chunk_vectors).squeeze(0)
    best_matches = similarity_scores.argsort(descending=True)[:top_results]
    relevant_texts = [chunks[idx] for idx in best_matches]
    return "\n".join(relevant_texts)

# Function to construct the final response
def create_query_response(user_query, text_chunks):
    matched_text = get_relevant_chunks(user_query, text_chunks)
    if not matched_text.strip():
        return "Sorry, no relevant information was found for your query."
    return f"Question: {user_query}\n\nHere is the most relevant information:\n\n{matched_text}"
