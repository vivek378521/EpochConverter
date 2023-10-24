from fastapi.testclient import TestClient
from main import app
import pytz
from datetime import datetime


client = TestClient(app)


def test_get_date_formats():
    response = client.get("/date_formats/")
    assert response.status_code == 200
    assert response.json() == {
        "dd/mm/yyyy": "%d/%m/%Y",
        "mm/dd/yyyy": "%m/%d/%Y",
        "yyyy-mm-dd": "%Y-%m-%d",
        "yyyy/mm/dd": "%Y/%m/%d",
        "dd.mm.yyyy": "%d.%m.%Y",
        "mm.dd.yyyy": "%m.%d.%Y",
        "dd-month-yyyy": "%d-%B-%Y",
        "mm-month-yyyy": "%m-%B-%Y",
        "yyyy.month.dd": "%Y.%B.%d",
    }


def test_convert_epoch_to_datetime():
    # Define the request data
    request_data = {"epoch": 1636136665, "date_format": "dd/mm/yyyy"}

    response = client.post("/convert_epoch_to_datetime/", json=request_data)
    assert response.status_code == 200  # Assuming a successful response

    data = response.json()
    assert "formatted_date" in data
    assert "time" in data

    # Additional assertions to validate the content of the response data
    formatted_date = data["formatted_date"]
    formatted_time = data["time"]

    # Convert the expected epoch to IST time zone
    expected_datetime = datetime.fromtimestamp(
        1636136665, tz=pytz.timezone("Asia/Kolkata")
    )

    # Format the expected datetime using the date format
    expected_formatted_date = expected_datetime.strftime("%d/%m/%Y")
    expected_formatted_time = expected_datetime.strftime("%H:%M:%S")

    assert formatted_date == expected_formatted_date
    assert formatted_time == expected_formatted_time
