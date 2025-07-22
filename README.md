# Spidey

**Spidey** is a Python tool for crawling and scraping web pages.

## Requirements

- Python 3 
- `requests`
- `beautifulsoup4`
- `lxml`
- `art`

## Install dependencies:

```bash
git clone https://github.com/Amrloksha151/Spidey
```

```bash 
cd Spidey
```

```bash
pip install -r requirements.txt
```
***Alternatively you can download the binary version from releases, executable located under dist***

## Usage

```bash
python main.py `[-h] -u URL [-p PORT] [-c COOKIE] -t THREADS [-d] [-o OUTPUT]`

```

**Options:**
  - `-h, --help            show this help message and exit`
  - `-u URL, --url URL     Target url`
  - `-p PORT, --port PORT  Custom Target port`
  - `-c COOKIE, --cookie COOKIE Cookies to be used`
  - `-t THREADS, --threads THREADS Number of threads`
  - `-d, --deep            Deep digging`
  - `-o OUTPUT, --output OUTPUT Output file to save results`

## Example

```bash
python main.py https://foobar.com -t 3 -d -o /home/output.txt
```

## Donation
send usdt to this wallet bnb smart chain wallet: **0x9371BbCA1d1C0b40ea13e91b56fFE45c99541212** to help me continue innovating