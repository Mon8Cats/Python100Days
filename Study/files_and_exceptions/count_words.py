def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"\nSorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"\nThe file {filename} has about {num_words} words.")


filename = "alice.txt"
count_words(filename)
