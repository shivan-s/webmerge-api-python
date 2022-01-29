# api.py
# contains the api code

import json
import logging
from pydoc import doc

import requests
from requests.structures import CaseInsensitiveDict

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


class BaseAPI:
    """
    This is the base API class
    """

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret
        self.url = "https://www.webmerge.me"  # url endpoint


class DocumentsAPI(BaseAPI):
    """
    Inherits from BaseAPI

    Document related things
    """

    # create
    # TODO: need to write docstring and handle exceptions
    def create_document(
        self,
        **kwargs,
    ) -> dict:
        """creates a document

        Args:
            document_name (str): name of the document
            document_type (str, optional): document type. Defaults to "html".
            document_output_type (str, optional): . Defaults to "pdf".

            if document_type is "html",
                html (str): html content
                size_width (int)
                size_height (int)

            if document_type is "pdf", "docx", "xlsx" or "pptx",
                file_contents (str)
                files_url (str)
                notification (str)

        Returns:
            dict: [description]
        """

        url = self.url + "/api/documents"
        data = json.dumps(kwargs)

        logging.info(data)

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        response = requests.post(
            url, headers=headers, data=data, auth=(self.key, self.secret)
        )
        return response

    # read
    # TODO: allow ability to search
    def get_documents(self) -> list:
        """gives list of documents in json format

        Raises:
            Exception: if not get 200 response code

        Returns:
            list: list of documents in json format
        """
        url = self.url + "/api/documents"
        response = requests.get(url, auth=(self.key, self.secret))
        if response.status_code == 200:
            documents = list(response.json())
        else:
            raise Exception

        return documents

    def get_document(self, document_id: str) -> dict:
        """get infomation about a document

        Args:
            id (str): document id

        Returns:
            dict: contains all the data for the document including merge fields
        """
        url = self.url + "/api/documents/" + document_id
        response = requests.get(url, auth=(self.key, self.secret))
        if response.status_code == 200:
            document = response.json()
        else:
            raise Exception

        return document

    # update
    # TODO: to make this

    # delete
    # TODO: write this properly
    def delete_document(self, document_id: str) -> bool:
        """Deletes a document

        Args:
            document_id (str): [description]

        Raises:
            Exception: [description]

        Returns:
            bool: True is delete successful
        """
        url = self.url + "/api/document/" + document_id

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        response = requests.delete(
            url, headers=headers, auth=(self.key, self.secret)
        )

        if response.status_code == 200:
            if response.json()["success"] == "1":
                return True
            else:
                return False
        else:
            raise Exception

    # merge
    def merge_document(
        self,
        document_id: str,
        document_key: str,
        merge_data: dict,
        test: bool = False,
        download: bool = True,
    ) -> str:
        """merge documents

        Args:
            document_id (str): this is the document id
            document_key (str): this is the key associated with the document
            merge_data (dict): this is the merge data
            test (bool, optional): if your want to test this. Defaults to False.
            download (bool, optional): downloads the pdf?. Defaults to True.
        """
        url = self.url + "/merge/" + document_id + "/" + document_key

        if any([test, download]):
            url = url + "?"
        if test == True:
            url = url + "test=1"
        if download == True:
            if test == True:
                url = url + "&"
            url = url + "download=1"

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        response = requests.post(url, headers=headers, data=merge_data)

        if response.status_code == 201:
            return response
        else:
            raise Exception

    # copy

    # send via email? delievery


# TODO: to write this class
class DataRoutesAPI(BaseAPI):
    """Uses the data routes"""

    pass
