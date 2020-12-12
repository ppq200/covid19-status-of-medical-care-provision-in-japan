import pandas as pd
from src.formatter import (
    get_formated_df,
    get_point_of_time,
    get_annotations,
    get_indication,
)

from src.crawler import get_latest_xlsx_url
from src.spreadsheet import get_sh, update, get_cell_url


def main():
    sh = get_sh()

    latest_xlsx_url = get_latest_xlsx_url()
    print(latest_xlsx_url)

    xlsx_url_on_spreadsheet = get_cell_url(sh)
    print(xlsx_url_on_spreadsheet)

    if latest_xlsx_url == xlsx_url_on_spreadsheet:
        print("end")
        return

    unformatted_df = pd.read_excel(latest_xlsx_url)
    print(unformatted_df.head(3))

    df = get_formated_df(unformatted_df)
    print(df.head(3))
    point_of_time_df = get_point_of_time(unformatted_df)
    print(point_of_time_df.head(3))

    annotations_df = get_annotations(unformatted_df)
    print(annotations_df.head(3))

    readme_df = pd.read_csv("./README_worksheet.md", header=None)
    print(readme_df.head(3))

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


if __name__ == "__main__":
    main()
