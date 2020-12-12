import google.auth
import gspread

from .settings import settings

scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]


def get_sh():
    credentials, _ = google.auth.default(scopes=scopes)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key(settings.spreadsheet_id)
    return sh


def update(sh, df, point_of_time, annotations, readme, url, indication):
    worksheet = sh.worksheet("医療提供体制")
    stat = worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print(stat, flush=True)

    worksheet = sh.worksheet("時点")
    stat = worksheet.update(
        [point_of_time.columns.values.tolist()] + point_of_time.values.tolist()
    )
    print(stat, flush=True)

    worksheet = sh.worksheet("注釈")
    stat = worksheet.update(annotations.values.tolist())
    print(stat, flush=True)

    worksheet = sh.worksheet("README")
    stat = worksheet.update(readme.values.tolist())
    print(stat, flush=True)

    worksheet = sh.worksheet("URL")
    stat = worksheet.update([[url]])
    print(stat, flush=True)

    worksheet = sh.worksheet("ステージの指標")
    stat = worksheet.update(
        [indication.columns.values.tolist()] + indication.values.tolist()
    )
    print(stat, flush=True)


def get_cell_url(sh):
    worksheet = sh.worksheet("URL")
    return worksheet.acell("A1").value
