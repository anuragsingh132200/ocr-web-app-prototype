# search.py
def search_keywords(extracted_text, keyword):
    results = []
    lines = extracted_text.split('\n')
    for line in lines:
        if keyword.lower() in line.lower():
            results.append(line)
    return results