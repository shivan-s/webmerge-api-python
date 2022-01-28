import os

import pytest

from webmerge.api import DocumentsAPI


@pytest.fixture()
def api():
    KEY = os.getenv("KEY")
    SECRET = os.getenv("SECRET")
    api = DocumentsAPI(KEY, SECRET)
    return api


def test_get_documents(api):
    """
    Gets a list of documents
    """
    documents = api.get_documents()
    assert type(documents) == list
    assert len(documents) == 2


def test_get_document(api):
    """
    Gets a single document
    """
    documents = api.get_documents()
    document_id = documents[0]["id"]
    document = api.get_document(document_id)
    assert type(document) == dict
    assert document["name"] == "Optometry Handout"
