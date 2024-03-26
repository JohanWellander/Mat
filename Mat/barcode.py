import pytesseract
from PIL import Image
import os
import csv
import re

def extract_first_column_as_string(file_path):
    first_column_string = ""
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            food = remove_non_letters(row['Livsmedelsnamn'].lower())
            if 'é' in food:
                # Replace "é" with "e"
                food = food.replace('é', 'e')
            data.append(food)   # Add a space between each value for separation
    return data

def remove_non_letters(input_string):
    # Use regular expression to remove all non-letter characters except spaces
    cleaned_string = re.sub(r'[^a-öA-Ö\s]', '', input_string)
    return cleaned_string
def remove_short_words(input_string):
    # Split the input string into rows
    rows = input_string.split('\n')
    rows = [row for row in rows if row.strip()]
    

    #print(rows)
    # Filter out rows with words shorter than 3 characters
    
    cleaned_rows = [row for row in rows if all(len(word) >= 3 for word in row.split())]
    # Join the filtered rows back into a string
    cleaned_string = '\n'.join(cleaned_rows)
    return cleaned_string

def remove_accented_e(words):
    # Iterate over each word in the list
    for i in range(len(words)):
        # Check if the word contains "é"
        if 'é' in words[i]:
            # Replace "é" with "e"
            words[i] = words[i].replace('é', 'e')
    return words

def remove_colors(string):
    colors = ["röd", "gul", "svart", "grön", "blå"]
    for word in string:
        if word in colors:
            string.remove(word)
    return string

dir = os.getcwd()
food = extract_first_column_as_string(dir + "/Livsmedel.csv")
#print(food)

# Perform OCR using PyTesseract


image = Image.open(dir + "/kvitto.png")

text = pytesseract.image_to_string(image, lang="swe").lower()
text = remove_non_letters(text)

text = remove_short_words(text)
print(text)
#print(text)
#text = remove_accented_e(text)
#text = remove_colors(text)

new_stuff = []
for word in text:
    if word in food:
        new_stuff.append(word)
    else:
        pass#print("nothing is: " + str(word))
#print(new_stuff)