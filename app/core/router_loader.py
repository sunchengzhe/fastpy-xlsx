# app/core/router_loader.py

import os
import importlib
from fastapi import FastAPI

def router_loader(app: FastAPI):
    base_path = "app.controller"
    controller_dir = os.path.join(os.path.dirname(__file__), "..", "controller")

    for filename in os.listdir(controller_dir):
        if filename.endswith("_controller.py"):
            module_name = f"{base_path}.{filename[:-3]}"  # 去掉 .py
            module = importlib.import_module(module_name)

            # 检查模块中是否有 router 对象
            if hasattr(module, "router"):
                router = getattr(module, "router")
                app.include_router(router)
