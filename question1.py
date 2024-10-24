number_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20",
}

path_="zen.txt"
# Open the input file for reading
with open(path_,"r") as f:
    text_ = f.read()

# Replace words with corresponding numbers
for word, number in number_mapping.items():
    text_ = text_.replace(word, number)

# Open the output file for writing
with open(path_, mode="w") as f:
    f.write(text_)
