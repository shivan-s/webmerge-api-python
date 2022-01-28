# api.py
# contains the api code

import requests


class BaseAPI:
    """
    This is the base API class
    """

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret
        self.url = "https://www.webmerge.me/api"  # url endpoint


class DocumentsAPI(BaseAPI):
    """
    Inherits from BaseAPI

    Document related things
    """

    # create
    # TODO: to make this
    def create_document(self) -> str:
        """creats a document

        Raises:
            Exception: [description]
            Exception: [description]

        Returns:
            str: [description]
        """
        pass

    # read
    # TODO: allow ability to search
    def get_documents(self) -> list:
        """gives list of documents in json format

        Raises:
            Exception: if not get 200 response code

        Returns:
            list: list of documents in json format
        """
        url = self.url + "/documents"
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
        url = self.url + "/documents/" + document_id
        response = requests.get(url, auth=(self.key, self.secret))
        if response.status_code == 200:
            document = response.json()
        else:
            raise Exception

        return document

    # update
    # TODO: to make this

    # delete
    # TODO: to make this



class DataRoutesAPI(BaseAPI):
    
