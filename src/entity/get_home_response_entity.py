

from typing import List, Optional
from pydantic import BaseModel


class RuejaiHomeProjectTranslationEntity(BaseModel):
    locale: str
    name: str


class RuejaiHomeProjectEntity(BaseModel):
    project_type: str
    project_name: str
    project_translation: List[RuejaiHomeProjectTranslationEntity]
    project_cover: str


class RuejaiHomeListEntity(BaseModel):
    home_id: Optional[str]
    project_code: str
    # project: RuejaiHomeProjectEntity
    plot_code: str
    address_no: Optional[str]
    # address_road: Optional[str]
    # pre_tumbon: Optional[str]
    # tumbon_name: Optional[str]
    # pre_amphur: Optional[str]
    # amphur_name: Optional[str]
    # province_name: Optional[str]
    # zip_code: Optional[str]
    # created_at: str
    # updated_at: str
    # deleted_at: Optional[str]


class RuejaiGetHomeResponseEntity(BaseModel):
    result: List[RuejaiHomeListEntity]
