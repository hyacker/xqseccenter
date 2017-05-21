#coding=UTF-8
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import os

import config
sys.path.append(os.path.split(os.path.realpath(__file__))[0]+"/../../")
from utils import module_loader


sche_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jobs_dir = os.path.join(sche_dir,"xqseccenter/scheduler/jobs")

jobs = module_loader.get_module(jobs_dir)
scheduler = BlockingScheduler()

def block_scheduler():
    for i in jobs:
        job = module_loader.load_module(i["name"],i)
        if "task_run" in dir(job):
            scheduler.add_job(job.task_run,'interval',seconds=30)

def start():
    block_scheduler()
    scheduler.start()


if __name__ == '__main__':
        block_scheduler()
        try:
            scheduler.start()
        except (SystemExit):
            pass
