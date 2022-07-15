import requests
import json

list = ["District", "Central", "Circle", "Piccadilly", "Bakerloo", "Hammersmith-City", "Jubilee", "Metropolitan", "Victoria", "Northern"]
bad = []
status_bad = []

for line in list:
    reply = requests.get("https://api.tfl.gov.uk/Line/" + line + "/Status")

    data = reply.json()

    Status = (data[0]["lineStatuses"][0]["statusSeverityDescription"])

    if Status != "Good Service":
        bad.append(line)
        status_bad.append(Status)


    print(
        "\n" + "Line: " + line +
        "\n" + "Status: " + Status +
        "\n"
        )