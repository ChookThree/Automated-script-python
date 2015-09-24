#!/usr/bin/env python     
import time
import os
import datetime
import click

@click.command()
@click.option()

commandOne = "./commandr@"
initTime = datetime.date(2015,7,20)
while True:  
    initTime = initTime + datetime.timedelta(days=1)
    strInitTime = initTime.strftime('%Y-%m-%d')
    command = commandOne + strInitTime + " --product"
    print(command)
    os.system(command)
    if strInitTime == '2015-08-24':
        break
    time.sleep(1800)
    

