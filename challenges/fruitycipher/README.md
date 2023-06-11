# solution
- find out it is a homophonic cipher (hint "there are more than 26 symbols")
- solve manually by guessing words
  - words with the same symbol appearing multiple times
    - 🍉🥝🍅🥝🥦🍉🥝🍓🍍🥐 = homophonic
    - see `src/solve/findword.py`
  - common, short words
    - 🍏🍉🍇 the
    - 🧅🥝🥖 = you
    - 🍎🥝 = to
    - 🥭🍋 = is
  - (guess letters by shape)
    - 🥐 = c
    - 🥝 = o
  - replace known symbols with letters
  - repeat: guess more, partially replaced words

# generate
- `src/generate.py`
