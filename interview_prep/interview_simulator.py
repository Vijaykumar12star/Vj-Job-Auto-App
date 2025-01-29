from transformers import pipeline
import random

qa_pipeline = pipeline('question-answering')

def conduct_mock_interview(job_description):
    questions = [
        "Tell me about yourself",
        "What experience do you have with {tech}?",
        "How would you handle {situation}?"
    ]
    
    # Generate technical questions from job description
    doc = nlp(job_description)
    tech_terms = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT']]
    
    interview = []
    for _ in range(5):
        template = random.choice(questions)
        if '{tech}' in template and tech_terms:
            interview.append(template.format(tech=random.choice(tech_terms)))
        else:
            interview.append(template)
    
    return interview

def evaluate_answer(question, answer):
    result = qa_pipeline(question=question, context=answer)
    return result['score']
