# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from datetime import timedelta
from environs import Env

env = Env()
env.read_env()


ENV = env.str("FLASK_ENV", default="development")
DEBUG = ENV == "development"
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False

