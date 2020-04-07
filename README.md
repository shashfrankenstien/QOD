# Quote Of The Day
Quotes from www.quotery.com (with CLI)

![Python](https://img.shields.io/badge/python-blue.svg)

## Installation

- Latest
```sh
pip install -U git+https://github.com/shashfrankenstien/QOD.git
```

- v1.0.0
```sh
pip install -U git+https://github.com/shashfrankenstien/QOD.git@v1.0.0
```



## Usage example

> CLI
```sh
qod
qod latest
qod --help
```

> Python Package
```py
import qod
print(qod.quote())
```

> cowsay
```
qod --plain | cowsay

 ______________________________________
/ We don’t have to be smarter than the \
| rest. We have to be more disciplined |
\ than the rest. - Warren Buffett      /
 --------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```