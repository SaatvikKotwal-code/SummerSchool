def clean_whitespace(text):
    # Remove leading and trailing spaces
    text = text.strip()
    # Replace multiple spaces/newlines with a single space
    text = ' '.join(text.split())
    return text

# Example usage
raw_text = "   This   is   an    example   text with   extra   spaces. \n\n"
cleaned_text = clean_whitespace(raw_text)

print("Original text:", repr(raw_text))
print("Cleaned text:", repr(cleaned_text))

 
