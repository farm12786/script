import requests

from settings import RUEJAI_API_BASE_URL, RUEJAI_API_REQUEST_HEADER
from src.entity.get_home_response_entity import RuejaiGetHomeResponseEntity


class RuejaiAPIRepository:
    def __init__(self) -> None:
        self.base_url = RUEJAI_API_BASE_URL
        self.headers = {"authorization": f"Bearer {RUEJAI_API_REQUEST_HEADER}"}

    def get_homes(self, project_code):
        response = requests.get(
            f"{self.base_url}homes/{project_code}", headers=self.headers
        )
        response = RuejaiGetHomeResponseEntity.parse_obj(response.json())
        return response.result
