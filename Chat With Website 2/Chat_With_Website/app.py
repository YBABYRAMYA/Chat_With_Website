from flask import Flask, render_template, request, jsonify
from fetcher import fetch_webpage_content, extract_relevant_text, split_into_chunks, create_query_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_query():
    try:
        urls = request.form.get('urls').split(',')
        query = request.form.get('query')
        search_keywords = ["research", "focus", "mission", "innovation", "academics", "knowledge"]
        
        aggregated_chunks = []
        for url in urls:
            page_content = fetch_webpage_content(url.strip())
            if page_content:
                filtered_text = extract_relevant_text(page_content, search_keywords)
                chunks = split_into_chunks(filtered_text)
                aggregated_chunks.extend(chunks)
        
        if aggregated_chunks:
            final_response = create_query_response(query, aggregated_chunks)
            return jsonify({'response': final_response})
        else:
            return jsonify({'response': "Unable to process any content from the given URLs."})
    except Exception as e:
        return jsonify({'response': f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
