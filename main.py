#!/usr/bin/env python
# main.py - The main script lives here
# documentation for webmerge api: https://www.webmerge.me/developers

import os
from rich import print
from webmerge.api import DocumentsAPI


KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")


def main():
    api = DocumentsAPI(key=KEY, secret=SECRET)

    documents = api.get_documents()
    print(documents)

    document = api.get_document("872936")
    print(document)


if __name__ == "__main__":
    main()
