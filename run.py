#!/usr/bin/env python
# -*- coding:utf-8 -*-


from api import create_app


app = create_app()
if __name__ == "__main__":
    app.run("0.0.0.0", 10010, debug=True)
