import asyncio

from job import Job
from config import Config
   

async def main():
    job = Job(Config())
    try:
        await job.run()
    except Exception as e:
        print(e)
    

asyncio.run(main())