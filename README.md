## Currently deployed at vercel on the free tier: 

```https://epoch-converter-vivek378521.vercel.app/docs```


### Live APIs
POST - ```https://epoch-converter-vivek378521.vercel.app/convert_epoch_to_datetime/```

GET - ```https://epoch-converter-vivek378521.vercel.app/date_formats/```

# FastAPI Epoch Conversion API

This repository contains a FastAPI application that provides two endpoints for date and time conversions: "Get Supported Date Formats" and "Convert Epoch to Datetime."

## Get Supported Date Formats

The "Get Supported Date Formats" endpoint allows you to retrieve a list of supported date formats that you can use for conversions.

- **Endpoint:** `GET /date_formats/`
- **Description:** Get a list of supported date formats.

### Response Example
```
{
  "dd/mm/yyyy": "%d/%m/%Y",
  "mm/dd/yyyy": "%m/%d/%Y",
  "yyyy-mm-dd": "%Y-%m-%d",
  "yyyy/mm/dd": "%Y/%m/%d",
  "dd.mm.yyyy": "%d.%m.%Y",
  "mm.dd.yyyy": "%m.%d.%Y",
  "dd-month-yyyy": "%d-%B-%Y",
  "mm-month-yyyy": "%m-%B-%Y",
  "yyyy.month.dd": "%Y.%B.%d"
}
```

### Usage

- Send a GET request to the `/date_formats/` endpoint to retrieve the list of supported date formats.

## Convert Epoch to Datetime

The "Convert Epoch to Datetime" endpoint allows you to convert an epoch timestamp to a human-readable date and time format based on your desired format.

- **Endpoint:** `POST /convert_epoch_to_datetime/`
- **Description:** Convert an epoch timestamp to a human-readable date and time format.

### Request Example

```http
POST /convert_epoch_to_datetime/

{
  "epoch": 1636136665,
  "date_format": "dd/mm/yyyy"
  "time_zone": "America/New_York" # Optional, defaults to Asia/Kolkata
}
```

### Response Example
```
{
  "formatted_date": "05/11/2021",
  "time": "23:54:25"
}
```

### Usage

- Send a POST request to the `/convert_epoch_to_datetime/` endpoint with the epoch timestamp and desired date format in the request body.
- The response includes the formatted date and time.
- If you want specific time_zone then add the time_zone field otherwise it defaults to Asia/Kolkata
[Time zones](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)
Feel free to explore and use these APIs for your timestamp conversion and date formatting needs. If you have any questions or encounter issues, please refer to the API documentation (<host>/docs) for further details.
