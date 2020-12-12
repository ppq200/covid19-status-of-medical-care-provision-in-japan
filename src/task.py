import pandas as pd
from .formatter import (
    get_formated_df,
    get_point_of_time,
    get_annotations,
    get_indication,
)

from .crawler import get_latest_xlsx_url
from .spreadsheet import get_sh, update, get_cell_url


def main():
    sh = get_sh()

    latest_xlsx_url = get_latest_xlsx_url()
    print(latest_xlsx_url)

    xlsx_url_on_spreadsheet = get_cell_url(sh)
    print(xlsx_url_on_spreadsheet)

    if latest_xlsx_url == xlsx_url_on_spreadsheet:
        message = f"no update. latest url is ${latest_xlsx_url}."
        print(message)
        return message

    unformatted_df = pd.read_excel(latest_xlsx_url)
    df = get_formated_df(unformatted_df)
    point_of_time_df = get_point_of_time(unformatted_df)
    annotations_df = get_annotations(unformatted_df)
    readme_df = pd.read_csv("./README_worksheet.md", header=None)
    indication_df = get_indication(unformatted_df)

    update(
        sh,
        df,
        point_of_time_df,
        annotations_df,
        readme_df,
        latest_xlsx_url,
        indication_df,
    )

    message = f"spreadsheet is updated. latest url is ${latest_xlsx_url}"
    return message
