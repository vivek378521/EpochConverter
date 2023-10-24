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


def test_convert_epoch_to_datetime_with_optional_time_zone():
    # Define the request data with optional time_zone
    request_data = {
        "epoch": 1636136665,
        "date_format": "dd/mm/yyyy",
        "time_zone": "Asia/Kolkata",  # Provide a time zone (optional)
    }

    response = client.post("/convert_epoch_to_datetime/", json=request_data)
    assert response.status_code == 200  # Assuming a successful response

    data = response.json()
    assert "formatted_date" in data
    assert "time" in data

    # Add more specific assertions to validate the content of the response data as needed


def test_convert_epoch_to_datetime_without_time_zone():
    # Define the request data without the time_zone (optional)
    request_data = {"epoch": 1636136665, "date_format": "dd/mm/yyyy"}

    response = client.post("/convert_epoch_to_datetime/", json=request_data)
    assert response.status_code == 200  # Assuming a successful response

    data = response.json()
    assert "formatted_date" in data
    assert "time" in data


def test_convert_epoch_to_datetime_with_custom_time_zone():
    # Define the request data with a custom time_zone
    request_data = {
        "epoch": 1636136665,
        "date_format": "dd/mm/yyyy",
        "time_zone": "America/New_York",  # Provide a different time zone
    }

    response = client.post("/convert_epoch_to_datetime/", json=request_data)
    assert response.status_code == 200  # Assuming a successful response

    data = response.json()
    print(data)
    assert "formatted_date" in data
    assert "time" in data

    # Add specific assertions to validate the content of the response data
    assert "formatted_date" in data
    assert "time" in data
    assert (
        data["formatted_date"] == "05/11/2021"
    )  # Replace with the expected formatted date for "America/New_York"
    assert (
        data["time"] == "14:24:25"
    )  # Replace with the expected time for "America/New_York"
