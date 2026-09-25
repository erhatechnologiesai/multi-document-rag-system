import re

CORPUS = [
    {"doc_id": "doc_1", "name": "hr_policy.md", "type": "md", "text": "Annual leave policy allows 24 paid vacation days and 10 public holidays per year."},
    {"doc_id": "doc_2", "name": "system_architecture.txt", "type": "txt", "text": "The distributed cluster uses gRPC for inter-service communication and Kafka for event streaming."},
    {"doc_id": "doc_3", "name": "financial_summary.pdf", "type": "pdf", "text": "Q3 revenue grew by 43% year-over-year driven by multi-agent enterprise contracts."},
    {"doc_id": "doc_4", "name": "security_guidelines.docx", "type": "docx", "text": "Mandatory two-factor authentication is required for all cloud infrastructure access."}
]

def search_corpus(query: str, doc_type: str = "all"):
    words = set(re.findall(r'\w+', query.lower()))
    matches = []
    for doc in CORPUS:
        if doc_type != "all" and doc["type"] != doc_type:
            continue
        doc_words = set(re.findall(r'\w+', doc["text"].lower()))
        overlap = len(words.intersection(doc_words))
        if overlap > 0:
            matches.append((overlap, doc))
    matches.sort(key=lambda x: x[0], reverse=True)
    return [m[1] for m in matches] or [CORPUS[0]]
