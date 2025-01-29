import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

def optimize_resume(job_description, resume_text):
    # Extract keywords using NLP
    doc = nlp(job_description)
    keywords = [token.text.lower() for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    
    # Calculate TF-IDF scores
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([job_description, resume_text])
    feature_names = vectorizer.get_feature_names_out()
    
    # Get important terms
    dense = tfidf_matrix.todense()
    important_terms = sorted(
        [(feature_names[i], dense[0,i]) for i in range(len(feature_names))],
        key=lambda x: x[1], 
        reverse=True
    )[:10]
    
    return {
        'missing_keywords': [kw for kw in keywords if kw not in resume_text.lower()],
        'important_terms': important_terms
    }
