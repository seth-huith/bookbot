def count_words(text):
    return len(text.split())

def count_characters_occurrences(text):
    occurrences = {}
    for char in text:
        key = char.lower()
        if key not in occurrences:
            occurrences[key] = 0
        occurrences[key] += 1
    return occurrences

def sort_occurrences(occurrences):
    sorted = []
    for char in occurrences:
        sorted.append({
            "char": char,
            "count": occurrences[char],
        })
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(dict):
    return dict["count"]