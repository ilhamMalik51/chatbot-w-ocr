import requests

class VectorClient():
    def __init__(self, endpoint: str):
        """Instantiate vector client"""
        self.endpoint = endpoint

    def search(self, vector: list, k: int):
        """This method is used for searching"""
        url = f"{self.endpoint}/api/search"
        request_body = {
            "vector": vector,
            "k": k
        }
        response = requests.post(url=url, json=request_body)
        response.raise_for_status()

        result = response.json()

        return result["data"]
    
    def insert_document(self, vector: list, content: str):
        """This method is used for inserting document"""
        url = f"{self.endpoint}/api/document"
        request_body = {
            "vector": vector,
            "content": content
        }
        response = requests.post(url=url, json=request_body)
        response.raise_for_status()
    
    def get_document_size(self,):
        """This method is used for inserting document"""
        url = f"{self.endpoint}/api/documents"
        response = requests.get(url=url)
        response.raise_for_status()

        result = response.json()

        return result["data"]