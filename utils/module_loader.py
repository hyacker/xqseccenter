#!/usr/bin/env python
#coding:utf-8
import os
import imp

def get_module(ModFolder):
    modules = []
    possiblejobs = os.listdir(ModFolder)
    for i in possiblejobs:
        if i != "__init__.py" and i.endswith(".py"):
            model_name = i.replace(".py","")
            info = imp.find_module(model_name, [ModFolder])
            modules.append({"name": model_name, "info": info})

    return modules

def load_module(model_name,job):
    return imp.load_module(model_name,*job["info"])
