# -*- encoding=utf8 -*-
__author__ = "15040"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/RPG0219604000769",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
touch(touch(Template(r"tpl1600191895958.png", record_pos=(-0.01, 0.485), resolution=(1080, 2340)))
)
touch(Template(r"tpl1600191921404.png", record_pos=(0.293, 0.224), resolution=(1080, 2340)))
touch(Template(r"tpl1600191950507.png", record_pos=(-0.17, -0.307), resolution=(1080, 2340))）
