# BookBot

A command-line Python tool that analyzes text from classic books and reports character frequency statistics.

## What it does

- Reads a text file (e.g. a classic book from Project Gutenberg)
- Counts how many times each alphabetic character appears
- Sorts the characters by frequency (most common first)
- Prints a clean report to the terminal

## Technologies Used

- Python 3
- Linux terminal & bash
- File I/O
- Dictionaries and sorting algorithms

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/bookbot.git
   cd bookbot
   ```

2. Add a book to the `books/` directory:
   ```bash
   curl https://www.gutenberg.org/files/84/84-0.txt -o books/frankenstein.txt
   ```

3. Run the program:
   ```bash
   python3 main.py
   ```

## Example Output

```
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24213
s: 21916
...
```

## What I Learned

- Python file I/O using `open()` and `read()`
- Using dictionaries to count character frequency
- Sorting dictionaries by value using `sorted()` and `lambda`
- Filtering characters using `isalpha()`
- Linux terminal commands: `mkdir`, `mv`, `cp`, `chmod`, `grep`, `cat`, `wc`
- File permissions and ownership (`chmod`, `chown`)
- Environment variables (`export`, `$PATH`)
- Redirecting stdout and stderr (`>`, `2>`)
- Git and GitHub for version control

## Project Structure

```
bookbot/
├── books/
│   └── frankenstein.txt
├── main.py
└── README.md
```
