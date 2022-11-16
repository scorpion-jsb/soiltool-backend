from fastapi import FastAPI, HTTPException
import json
from models import SearchData
import logging

app = FastAPI()

logger = logging.getLogger(__name__)

@app.get("/", response_model=SearchData)
async def get_json_data(
    category: bool=True,
    description: bool=True,
    next_inspection: bool=True,
    operator: bool=True,
    ordz: bool=True,
    site: bool=True,
    page: int=0,
    limit: int=10
):
    data = None
    try:
        with open("search.json", "r") as json_file:
            data = json.load(json_file)[page * limit: (page + 1) * limit]
    except Exception as error:
        logger.error(f"Error reading json file: {error}")

    if data:
        json_data = []
        for row in data:
            row_data = {}
            if category:
                row_data['category'] = row['category']
            if description:
                row_data['description'] = row['description']
            if next_inspection:
                row_data['next_inspection'] = row['next_inspection']
            if operator:
                row_data['operator'] = row['operator']
            if ordz:
                row_data['ordz'] = row['ordz']
            if site:
                row_data['site'] = row['site']
            json_data.append(row_data)

        return { 'data': json_data }

    raise HTTPException(400, "Bad Request")
