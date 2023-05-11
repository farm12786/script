import json
from src.repository.ruejai_api_repository import RuejaiAPIRepository
from settings import SC_ASSET_PROJECT_LIST

patterns = {
    "1": "Number(2digit)",
    "2": "Number(3digit)",
    "3": "C+Number",
    "4": "C+INT",
    "5": "C+Number(2digit)",
}

project_pattern_list = {
    "Number(2digit)": [],
    "Number(3digit)": [],
    "C+INT": ["BB-RW"],
    "C+Number(2digit)": [],
}

if __name__ == "__main__":
    reujai_repo = RuejaiAPIRepository()
    project_code_list = SC_ASSET_PROJECT_LIST
    count_1 = 0
    count_2 = 0

    for project_code in project_code_list:
        home_list = reujai_repo.get_homes(project_code=project_code)
        
        # for home in home_list:
        #     with open(f"./home_data/{project_code}.txt", "a") as file:
        #         file.write(f"{home.plot_code}\n")
        
        if len(home_list) != 0:
            middle_home_plot_code = home_list[int(len(home_list) / 2)].plot_code
            count_2 = count_2 + 1
            try:
                int(middle_home_plot_code[0])
                if len(middle_home_plot_code) == 2:
                    project_pattern_list[patterns["1"]].append(project_code)
                elif len(middle_home_plot_code) == 3:
                    project_pattern_list[patterns["2"]].append(project_code)
            except ValueError:
                slice_middle_home_plot_code = middle_home_plot_code[1:]
                if len(slice_middle_home_plot_code) ==2:
                    project_pattern_list[patterns["5"]].append(project_code)
        count_1 = count_1 + 1
    print(json.dumps(project_pattern_list, indent=4))
    print(count_1, count_2)
