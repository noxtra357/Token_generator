# Token Generator

A small command-line tool written in Python that generates random tokens: API-style keys, session IDs, codes, or strong passwords. It uses Python's built-in `secrets` module, which is designed for security-sensitive randomness.

> The program's menu and messages are in Russian.

## Features

- **Four token types**: letters and digits, hex, URL-safe, and strong (letters, digits, and symbols).
- **Custom length**: 8 to 256 characters (default 32).
- **Batch generation**: 1 to 100 tokens at once (default 1).
- **Strong mode guarantee**: every "strong" token contains at least one lowercase letter, one uppercase letter, one digit, and one symbol.
- **Optional saving**: append the generated tokens to a text file.
- **Input checking**: invalid numbers are rejected and you are asked again.

## Requirements

- Python 3.9 or newer
- No third-party packages, only the standard library

## Quick start

### In PyCharm

1. Add `token_generator.py` to your project.
2. Right-click the file and choose **Run 'token_generator'**.
3. Click inside the Run window at the bottom and type your answers there, pressing Enter after each one.

### In a terminal

```bash
python token_generator.py
```

## How to use

The program shows a menu:

```
1 - Letters and digits
2 - Hex (digits 0-9 and letters a-f)
3 - URL-safe (letters, digits, - and _)
4 - Strong (letters, digits and symbols)
0 - Exit
```

After you choose a type, it asks for two numbers. Press Enter to accept the default:

| Question | Range | Default |
| --- | --- | --- |
| Token length | 8 to 256 | 32 |
| How many tokens | 1 to 100 | 1 |

The tokens are printed in the Run window. Finally the program asks whether to save them to `tokens.txt` (`д` = yes, `н` = no). After that the menu appears again, so you can generate more. Enter `0` to quit.

### Example session

```
Your choice: 4
Token length (8 to 256, Enter = 32): 20
How many tokens (1 to 100, Enter = 1): 3

6-cE(6PU#WUOcodzT&K9
!g=FyE-dvG6_@@HIuqh8
k6793-yBVz?imydPbG(G
```

The tokens above are only examples. Never use a token that was copied from documentation.

## Token types

| Type | Characters used | Good for |
| --- | --- | --- |
| Letters and digits | `A-Z a-z 0-9` | general-purpose IDs and keys |
| Hex | `0-9 a-f` | API-style keys and hashes |
| URL-safe | `A-Z a-z 0-9 - _` | links, session IDs, anything placed in a URL |
| Strong | letters, digits, and `!@#$%^&*()-_=+?` | passwords |

For scale: a 32-character hex token carries 128 bits of randomness, which is far beyond what can be guessed by brute force.

## Saving tokens

If you answer `д` to the save question, the tokens are **appended** (one per line) to a file named `tokens.txt` in the current working directory. In PyCharm that is the project folder. The program prints the full path of the file after saving.

Keep in mind:

- `tokens.txt` is plain text, so anyone who can open the file can read the tokens.
- Do not store real passwords or production keys in it without protecting the file.
- If your project is in Git, add `tokens.txt` to `.gitignore` so it is never uploaded by accident.

## How it works

- `secrets.choice()` picks each character from the chosen alphabet using the operating system's secure random source. Unlike the regular `random` module, the result is not predictable.
- In strong mode, a token is generated again if it happens to miss one of the four character kinds, so the final token always passes the check.

## Project structure

```
.
├── token_generator.py          # the whole program
└── README_token_generator.md
```

## Ideas for next steps

- Copy the token to the clipboard automatically
- Choose which symbols are allowed in strong mode
- Add a passphrase mode made of random words
- Build a window with buttons using `tkinter`
