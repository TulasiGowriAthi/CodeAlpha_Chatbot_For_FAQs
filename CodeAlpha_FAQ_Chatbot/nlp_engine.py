import json
import string
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    """Tokenizes text, converts to lowercase, and strips punctuation."""
    # Convert to lowercase
    text = text.lower()
    # Tokenize words safely
    words = word_tokenize(text)
    # Remove punctuation marks
    cleaned_words = [w for w in words if w not in string.punctuation]
    # Recombine back into a clean sentence string
    return " ".join(cleaned_words)

def load_faqs(file_path="faqs.json"):
    """Loads questions and answers from the JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_best_faq_match(user_query, faq_data):
    """
    Uses TF-IDF Vectorization and Cosine Similarity to find 
    the best matching answer for the user's question.
    """
    # 1. Extract and preprocess all existing FAQ questions
    faq_questions = [faq["question"] for faq in faq_data]
    preprocessed_faqs = [preprocess_text(q) for q in faq_questions]
    
    # 2. Preprocess the user's current question
    clean_user_query = preprocess_text(user_query)
    
    # 3. Combine everything into one list for the vectorizer
    all_texts = preprocessed_faqs + [clean_user_query]
    
    # 4. Turn text sentences into mathematical TF-IDF numerical vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # 5. Split vectors back into FAQ vectors vs User Query vector
    faq_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]
    
    # 6. Compute mathematical Cosine Similarity matrix
    similarity_scores = cosine_similarity(user_vector, faq_vectors)[0]
    
    # 7. Find the index of the highest score
    best_match_idx = similarity_scores.argmax()
    highest_score = similarity_scores[best_match_idx]
    
    # 8. Set a confidence threshold (e.g., 0.2). If similarity is too low, don't guess blindly!
    if highest_score > 0.2:
        return faq_data[best_match_idx]["answer"]
    else:
        return "I'm sorry, I couldn't find a confident match for that question in my database. Could you try rephrasing or asking something else about AI tools and automation?"