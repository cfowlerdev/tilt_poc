import logging
from typing import AsyncGenerator
from fastapi import FastAPI
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    logger.info("*** Server Starting UP ***")
    yield

    logger.info("*** Server shutting DOWN ***")

app = FastAPI(title="Account Services", lifespan=lifespan)

