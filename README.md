# Server Code For The Cosignerpool Plugin

The Electrum cosignerpool plugin facilitates the use of multi-signatures wallets.
It sends and receives partially signed transactions from/to your cosigner wallet.

This is the server that stores the encrypted transactions.

## How to run

### Docker
A Docker file is included in the repository. To run it using docker-compose:

````yaml
version: '2'
services:
  cosignerpool:
    image: bauerj/cosignerpool:0.1
    ports:
      - "80:80"
    volumes:
      - /var/volumes/cosignerpool:/data
````

### Manually
To run it without Docker, use e.g.

    apt install libleveldb-dev
    pip install -r requirements.txt
    DB_PATH=/db python3 ./cosignerpool.py