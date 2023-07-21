# `term_2048`: 2048 in the terminal

This is a small implementation of Gabriele Cirulli's [2048 game](https://play2048.co/) in the terminal using Python. I wrote it to learn about using the [`curses`](https://docs.python.org/3/howto/curses.html)library in Python. I learned enough about `curses` to prefer the much smoother [`blessed`](https://blessed.readthedocs.io/en/latest/intro.html) library instead, so that's what's used here.

## Installation

```bash
pip install term_2048
```

## Running `term_2048`

Once you've installed the package, you can run the game from the terminal:

```bash
term_2048
```

Use `term_2048 --help` to print help options:

```bash
usage: term_2048 [-h] [-w WIDTH] [--height HEIGHT] [-s {S,M,L,XL}] [--start_value START_VALUE]

2048 game in the terminal. Inspired by https://play2048.co/

options:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        Width of the board (default: 4)
  --height HEIGHT       Height of the board (default: 4)
  -s {S,M,L,XL}, --size {S,M,L,XL}
                        Board size (options: S, M, L, XL; default: M)
  --start_value START_VALUE
                        Highest starting tile value (default: 4)
```

## Compatibility

I've only run this on MacOS so far, and the terminal management is pretty naive.
Let me know if you have issues on a given OS or terminal setup.

### Contact & bug reports

Bug reports and pull requests are welcome!
Feel free to contact me on [Github](https://github.com/etjones/term2048) or by email at [evan_jones@mac.com](mailto:evan_jones@mac.com).)
