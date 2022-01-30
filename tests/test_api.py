import io
import json
import os
import time

import PyPDF2
import pytest

from webmerge.api import DocumentsAPI


class TestDocumentsAPI:
    @pytest.fixture()
    def api(self):
        KEY = os.getenv("KEY")
        SECRET = os.getenv("SECRET")
        api = DocumentsAPI(KEY, SECRET)
        return api

    def test_create_document(self, api):
        """Creates a document and checks if created document exists"""
        test_data = {
            "name": "test_42",
            "type": "html",
            "output": "pdf",
            "html": "<H1>Test</H1> {$test}",
        }
        create_document = api.create_document(**test_data)

        # checking if documents was created
        document_id = create_document["id"]
        document_info = api.get_document(document_id)
        document_name = document_info["name"]
        assert document_name == test_data["name"]

        # deletes newly created document
        api.delete_document(document_id)

    def test_get_documents(self, api):
        """Gets a list of documents"""
        previous_documents = api.get_documents()

        # creates dummy documents
        test_data_1 = {
            "name": "test_01",
            "type": "html",
            "output": "pdf",
            "html": "<H1>Test</H1> {$test}",
        }
        create_document_1 = api.create_document(**test_data_1)
        test_data_2 = {
            "name": "test_01",
            "type": "html",
            "output": "pdf",
            "html": "<H1>Test</H1> {$test}",
        }
        create_document_2 = api.create_document(**test_data_2)

        # checks current list of documents
        current_documents = api.get_documents()
        assert type(current_documents) == list
        assert len(current_documents) - len(previous_documents) == 2

        # delete dummy document
        api.delete_document(create_document_1["id"])
        api.delete_document(create_document_2["id"])

    def test_get_document(self, api):
        """Gets a single document using the the document id"""
        # create dummy document
        test_data = {
            "name": "test_42",
            "type": "html",
            "output": "pdf",
            "html": "<H1>Test</H1> {$test}",
        }
        create_document = api.create_document(**test_data)

        document = api.get_document(create_document["id"])
        assert type(document) == dict
        assert document["name"] == test_data["name"]

        # delete dummy document
        api.delete_document(create_document["id"])

    def test_merge_document(self, api):
        """Merges an newly created document"""
        # create dummy document
        test_data = {
            "name": "test_42",
            "type": "html",
            "output": "pdf",
            "html": "<H1>Test</H1> {$test}",
        }
        create_document = api.create_document(**test_data)

        # merge document data
        merge_data_dict = {"Test": "test"}
        merge_data = json.dumps(merge_data_dict)
        file = api.merge_document(
            create_document["id"],
            create_document["key"],
            merge_data,
        )
        try:
            PyPDF2.PdfFileReader(io.BytesIO(file.content))
        except PyPDF2.utils.PdfReadError:
            assert False
        else:
            assert True

        # delete dummy document
        api.delete_document(create_document["id"])

    def test_delete_document(self, api):
        """Delete a document"""
        previous_documents = api.get_documents()
        # create dummy document
        test_data = {
            "name": "test_42",
            "type": "html",
            "output": "pdf",
            "html": "<H1>Test</H1> {$test}",
        }
        create_document = api.create_document(**test_data)
        assert len(previous_documents) + 1 == len(api.get_documents())

        # delete document and test
        output = api.delete_document(create_document["id"])
        assert output == True
        output = api.delete_document(create_document["id"])
        assert output == False
        assert len(previous_documents) == len(api.get_documents())
