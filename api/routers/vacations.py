from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.vacations import (
    Error,
    VacationIn,
    VacationOut,
    VacationRepository
    )

router = APIRouter()


@router.post("/vacations", response_model=Union[VacationOut,Error]) # endpoint defined
def create_vacation(
    vacation: VacationIn,
    response:Response,
    repo:VacationRepository=Depends()
):
    # print('vacation', vacation)
    # print('from date', vacation.from_date.month)
    # print(repo)
    # response.status_code = 200
    # return repo.create(vacation)
    # return vacation
    vacation = repo.create(vacation)
    if vacation is None:
        response.status_code = 400
    return vacation


@router.get("/vacations", response_model=Union[Error,List[VacationOut]]) # endpoint defined
def get_all(
    repo:VacationRepository=Depends()
):
    return repo.get_all()



@router.put("/vacations/{vacation_id}", response_model=Union[VacationOut,Error]) # endpoint defined
def update_vacation(
    vacation_id:int,
    vacation:VacationIn,
    repo:VacationRepository=Depends(),
) -> Union[VacationOut, Error]:
        return repo.update(vacation_id, vacation)


@router.delete("/vacations/{vacation_id}", response_model=bool) # endpoint defined
def delete_vacation(
    vacation_id:int,
    repo:VacationRepository=Depends(),
) -> bool:
        return repo.delete(vacation_id)


@router.get("/vacations/{vacation_id}", response_model=Optional[VacationOut]) # endpoint defined
def get_one_vacation(
    vacation_id:int,
    response:Response,
    repo:VacationRepository=Depends(),
) -> VacationOut:
        vacation = repo.get_one(vacation_id)
        if vacation is None:
            response.status_code = 404
        return vacation
