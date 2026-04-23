import json
import click
import openpyxl

with open("config.json", "r") as f:
    config = json.load(f)

xlsx_path = config.get("spreadsheet_path")
if xlsx_path is None:
    click.secho(
        "No spreadsheet path defined in config. Please define 'spreadsheet_path'."
    )
    exit()

wb = openpyxl.load_workbook(xlsx_path)
ws = wb["Paper-Presenter"]

for row in ws.iter_rows(min_row=2, max_col=4, max_row=25, values_only=True):
    paper_id, paper_title, _, presenter_name = row
    print(f"{paper_id=} {paper_title=} {presenter_name=}")
