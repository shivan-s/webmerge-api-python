#!/usr/bin/env python
# main.py - The main script lives here
# documentation for webmerge api: https://www.webmerge.me/developers

import json
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

    document_id = document["id"]
    document_key = document["key"]

    print(f"{document_id=}")
    print(f"{document_key=}")

    merge_data_dict = {
        "Name": "Shivan Sivakumaran",
        "Email": "shivan.sivakumaran@gmail.com",
        "Address": "Address",
        "mildcataract": "yes",
        "severecataract": "no",
        "macdegen": "yes",
        "wetarmd": "no",
    }

    merge_data = json.dumps(merge_data_dict)

    pdf = api.merge_document(
        document_id,
        document_key,
        merge_data,
    )

    print(pdf.content)

    with open("/tmp/data.pdf", "wb") as f:
        f.write(pdf.content)

    # data = {
    #     "name": "test",
    #     "type": "html",
    #     "output": "pdf",
    #     "html": "<H1>Test</H1>",
    # }

    # create_res = api.create_document(**data)


# print(create_res.json())


if __name__ == "__main__":
    main()
