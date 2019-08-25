# Quote Of The Day
Quotes from www.quotery.com (with CLI)

![Python](https://img.shields.io/badge/python-blue.svg)

## Installation

```sh
pip install -U git+https://github.com/shashfrankenstien/QOD.git
```


## Usage example

> CLI
```sh
$ qod
$ qod latest
$ qod -s
```

> Cherrypy Server + TaskScheduler
```py
import qod

print(qod.quote())
```