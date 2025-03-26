# Calculator Bot

This is a super-simple Python script which is executed as part of the Bacalhau Bluesky Bot network. 

When invoked, it will take the processed text of a Bluesky post that has mentioned the bot, and perform a calculation contained therein (if there is one).

## Building

```bash
python3 -m venv ./VENV
source ./VENV/bin/activate
pip3 install -r requirements.txt
```

## Running

```bash
source ./VENV/bin/activate
PROCESSED_POST=2^2 python3 main.py
// 4.00000000000000

PROCESSED_POST=2^BANANA python3 main.py
// 🔥🧮🔥
```

## Extra Info

This script is available [as a container](https://hub.docker.com/r/seanmtracey/bbb-calculator) on Docker Hub.

You can pull it with:

```bash
docker pull seanmtracey/bbb-calculator
```

... and run it with 

```bash
docker run --rm -e PROCESSED_POST="3*3" seanmtracey/bbb-calculator:latest  
```