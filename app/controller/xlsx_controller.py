# app/controller/xlsx_controller.py

from fastapi import APIRouter, Depends
from app.util.res_util import ResUtil
from app.service.file_job_service import FileJobService

router = APIRouter()

@router.get("/testSetData")
async def test_set_data(file_job_service: FileJobService = Depends(FileJobService.instance)):
    result = await file_job_service.test_set_data()
    return ResUtil.success(result)
