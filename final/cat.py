import requests
import random

class CatFact_API:
    """
    CatFact_API
    """
    def __init__(self):
        """
        Initializes base url for the api
        """
        self.base_url = "https://cat-fact.herokuapp.com"
    
    def get_fact(self):
        """
        selects a random cat fact from the api
        """
        url = f"{self.base_url}/facts"
        response = requests.get(url).json()
        length_of_facts = len(response)
        self.fact = response[random.randrange(length_of_facts)]["text"]
        
        
    
    def __str__(self):
        """
        str method that returns the fact to the user

        Returns:
            str: random cat fact got from calling get_fact method
        """
        return self.fact
    