import google.auth
import gspread

from .settings import settings

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def get_sh():
    credentials, _ = google.auth.default(scopes=scopes)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key(settings.spreadsheet_id)
    return sh


def update(sh, df, point_of_time, annotations, readme, url, indication):
    worksheet = sh.worksheet("医療提供体制")
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    worksheet = sh.worksheet("時点")
    worksheet.update(
        [point_of_time.columns.values.tolist()] + point_of_time.values.tolist()
    )

    worksheet = sh.worksheet("注釈")
    worksheet.update(annotations.values.tolist())

    worksheet = sh.worksheet("README")
    worksheet.update(readme.values.tolist())

    worksheet = sh.worksheet("URL")
    worksheet.update([[url]])

    worksheet = sh.worksheet("ステージの指標")
    rows = [indication.columns.values.tolist()] + indication.values.tolist()
    worksheet.update(rows)


def get_cell_url(sh):
    worksheet = sh.worksheet("URL")
    return worksheet.acell("A1").value
