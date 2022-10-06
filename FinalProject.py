from PIL import Image
from urllib.parse import quote
from IPython.display import display
from cgitb import text
import csv
import datetime
import requests as r

url = "https://api.covid19api.com/dayone/country/brazil"

resp = r.get(url)

print(resp.status_code)

raw_data = resp.json()

print(raw_data[0])

final_data = []
for obs in raw_data:
    final_data.append([obs["Confirmed"], obs["Deaths"],
                      obs["Recovered"], obs["Active"], obs["Date"]])

final_data.insert(0, ["Confirmed", "Deaths", "Recovered", "Active"])

confirmed = 0
deaths = 1
recovered = 2
active = 3
date = 4

for i in range(1, len(final_data)):
    final_data[i][date] = final_data[i][date][:10]

print(final_data)

#print(datetime.time(12, 6, 21, 7), "Hour:minute:second.millisecond")
#print(datetime.date(2020, 4, 25), "Year-month-day")
#print(datetime.datetime(2020,4,25,12,6,21,7),"Year-month-day Hour:minute:second.millisecond")

with open("brasil-covid.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1, len(final_data)):
    final_data[i][date] = datetime.datetime.strptime(
        final_data[i][date], "%Y-%m-%d")

print(final_data)


def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                "label": labels[i],
                "data": y[i]
            })
        return datasets
    else:
        return [{
            "label": labels[0],
                "data": y
                }]


def set_title(title=""):
    if title != "":
        display = "true"
    else:
        display = "false"
    return {
        "title": title,
        "display": display
    }


def create_chart(x, y, labels, kind="bar", title=""):

    datasets = get_datasets(y, labels)
    options = set_title(title)

    chart = {
        "type": kind,
        "data": {
            "labels": x,
            "datasets": datasets
        },
        "options": options
    }

    return chart


def get_api_chart(chart):
    url_base = "https://quickchart.io/chart"
    resp = r.get(f"{url_base}?c={str(chart)}")
    return resp.content


def save_image(path, content):
    with open(path, "wb") as image:
        image.write(content)


def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


y_data_1 = []
for obs in final_data[1:75]:
    # for obs in final_data[1::10]:
    y_data_1.append(obs[confirmed])

y_data_2 = []
for obs in final_data[1:75]:
    # for obs in final_data[1::10]:
    y_data_2.append(obs[recovered])

labels = ["Confirmed", "Recovered"]

x = []

for obs in final_data[1:75]:
    # for obs in final_data[1::10]:
    x.append(obs[date].strftime("%d/%m/%Y"))

chart = create_chart(x, [y_data_1, y_data_2], labels,
                     title="Confirmed x Recovered")

chart_content = get_api_chart(chart)

save_image("my-first-graph.png", chart_content)

display_image("my-first-graph.png")


def get_api_qrcode(link):
    text = quote(link)  # parsing from link to url
    url_base = "https://quickchart.io/qr"
    resp = r.get(f"{url_base}?text={text}")
    return resp.content


url_base = "https://quickchart.io/chart"
link = f"{url_base}?c={str(chart)}"
save_image("qr-code.png", get_api_qrcode(link))
display_image("qr-code.png")