import json
from google_sheet_repository import GoogleSheetRepository
import pandas as pd
from settings import SC_ASSET_PROJECT_LIST
from src.entity.get_home_response_entity import RuejaiHomeListEntity

from src.repository.ruejai_api_repository import RuejaiAPIRepository


if __name__ == "__main__":
    project_code_list = SC_ASSET_PROJECT_LIST

    gg_sheet_repo = GoogleSheetRepository(sheet_title="SC_ASSET_HOMES")
    reujai_repo = RuejaiAPIRepository()
    column_list = [key for key in RuejaiHomeListEntity.__fields__]

    for project_code in project_code_list:
        # CREATE SHEET
        old_worksheet = gg_sheet_repo.get_worksheet_by_title(
            worksheet_title=project_code
        )
        if old_worksheet:
            gg_sheet_repo.delete_worksheet(old_worksheet)

        gg_sheet_repo.add_worksheet(worksheet_title=project_code)

        home_list = reujai_repo.get_homes(project_code=project_code)
        data = {}
        for key in column_list:
            data[key] = [home.dict()[key] for home in home_list]
        df = pd.DataFrame(data=data)
        df_column_list = [df.columns.values.tolist()]
        df_data_list = df.values.tolist()

        gg_sheet_repo.update_worksheet(
            worksheet_title=project_code,
            column_list=df_column_list,
            data_list=df_data_list,
        )

        # FORMATTING SHEET
        gg_sheet_repo.worksheet_formatting(
            worksheet_title=project_code,
            cell_range="A1:D1",
            format={
                "backgroundColor": {"red": 0.7, "green": 0.7, "blue": 0.7},
                "horizontalAlignment": "CENTER",
                "textFormat": {
                    "fontSize": 12,
                    "bold": True,
                },
                "borders": {
                    "top": {"style": "SOLID"},
                    "bottom": {"style": "SOLID"},
                    "left": {"style": "SOLID"},
                    "right": {"style": "SOLID"},
                },
            },
        )
