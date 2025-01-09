from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, SessionLocal
from schemas import (
    AluguelCreate, AluguelResponse, AluguelUpdate,
    ApartamentoCreate, ApartamentoResponse, ApartamentoUpdate,
    DespesaCreate, DespesaResponse, DespesaUpdate,
    EdificioCreate, EdificioResponse, EdificioUpdate,
    GaragemCreate, GaragemResponse, GaragemUpdate,
    GastoCreate, GastoResponse, GastoUpdate,
    ProprietarioCreate, ProprietarioResponse, ProprietarioUpdate
)