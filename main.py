from datetime import datetime
from pydantic import BaseModel
from typing import Optional

import pytz
from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

# Create a mapping of simplified date format strings to strftime format strings
format_mapping = {
    "dd/mm/yyyy": "%d/%m/%Y",
    "mm/dd/yyyy": "%m/%d/%Y",
    "yyyy-mm-dd": "%Y-%m-%d",
    "yyyy/mm/dd": "%Y/%m/%d",
    "dd.mm.yyyy": "%d.%m.%Y",
    "mm.dd.yyyy": "%m.%d.%Y",
    "dd-month-yyyy": "%d-%B-%Y",
    "mm-month-yyyy": "%m-%B-%Y",
    "yyyy.month.dd": "%Y.%B.%d",
    # Add more format mappings as needed
}

epoch_param = Path(..., description="Epoch timestamp")
date_format_param = Path(..., description="Desired date and time format")


@app.get("/")
def hello_world():
    return {"message": "It is working"}


@app.get("/date_formats/")
def get_date_formats():
    return format_mapping


class DateTimeRequest(BaseModel):
    epoch: int
    date_format: str
    time_zone: Optional[str] = None


@app.post("/convert_epoch_to_datetime/")
def convert_epoch_to_datetime(data: DateTimeRequest):
    if data.time_zone is None:
        timezone = pytz.timezone("Asia/Kolkata")
    else:
        if data.time_zone not in pytz.all_timezones:
            raise HTTPException(status_code=400, detail="Invalid Timezone")

        timezone = pytz.timezone(data.time_zone)
    epoch = data.epoch
    date_format = data.date_format

    time_format = "%H:%M:%S"
    # Map the simplified date format to strftime format
    strftime_format = format_mapping.get(date_format)

    if strftime_format is None:
        raise HTTPException(status_code=400, detail="Invalid date format")

    formatted_datetime = datetime.fromtimestamp(epoch, tz=timezone).strftime(
        strftime_format
    )
    formatted_time = datetime.fromtimestamp(epoch, tz=timezone).strftime(
        time_format
    )
    return {"formatted_date": formatted_datetime, "time": formatted_time}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
