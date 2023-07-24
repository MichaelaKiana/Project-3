from flask import Flask, request, jsonify
import numpy as np
import sqlalchemy
import json
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 

#################################################
# Database Setup
#################################################


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

