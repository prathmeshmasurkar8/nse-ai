import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def get_sheet():
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    sheet = client.open("NSE AI").worksheet("Recommendation")

    return sheet


def write_test():
    sheet = get_sheet()

    sheet.clear()

    data = [
        ["Rank", "Stock", "Score"],
        [1, "RELIANCE", 95],
        [2, "TCS", 92],
        [3, "BEL", 90]
    ]

    sheet.update("A1", data)

    print("Google Sheet Updated Successfully")
