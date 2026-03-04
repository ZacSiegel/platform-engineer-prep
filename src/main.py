from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import uuid

app = FastAPI()

services = {}


class Service(BaseModel):
    name: str
    owner: str
    version: str
    status: Optional[str] = 'active'


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/services')
async def list_all_services():
    result = []
    for key, value in services.items():
        service = {
            "id": key,
            "name": value["name"],
            "owner": value["owner"],
            "version": value["version"],
            "status": value["status"]
        }
        result.append(service)
    return result


# Add a service
@app.post('/services/add_service')
async def add_new_service(service: Service):
    service_id = str(uuid.uuid4())
    services[service_id] = service.model_dump()
    return [{"id": key, **value} for key, value in services.items()]
    # return services[service_id]


# update a service
@app.put('/services/update_service/{service_id}')
async def update_service(service_id: str, service: Service):
    if service_id not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    services[service_id] = service.model_dump()
    return [{"id": key, **value} for key, value in services.items()]


# delete a service
@app.delete('/services/delete_service/{service_id}')
async def delete_service(service_id: str):
    if service_id not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    del services[service_id]
    return {"message": "Service deleted successfully"}
