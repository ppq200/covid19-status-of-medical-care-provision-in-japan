import requests
import re

page_url = "https://www.mhlw.go.jp/stf/seisakunitsuite/newpage_00035.html"
base_url = baseurl = "https://www.mhlw.go.jp"


def get_latest_xlsx_url():
    response = requests.get(page_url)
    pattern = r"/content/10900000/[0-9]+\.xlsx"
    latest_xlsx_path = re.findall(pattern, response.text)[0]
    xlsx_url = baseurl + latest_xlsx_path
    return xlsx_url
