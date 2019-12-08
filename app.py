# 0-ADDING DEPENDENCIES
#adding basic dependencies
import pandas as pd 
import datetime as dt
import numpy as np 

#adding sqlalchemy related dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#adding flask dependencies
from flask import Flask, jsonify

#----------------------
#1- SET UP THE DATABASE
#set up our db engine for Flask app
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the db into our classes
Base = automap_base()

#reflect our tables
Base.prepare(engine, reflect=True)

#create variables for each of the classes
measurement = Base.classes.measurement
station = Base.classes.station

#create a session link from python to our db
session = Session(engine)

#----------------------
#3- SET UP FLASK
#create and define a Flask app called "app"
app = Flask(__name__)

#define welcome route
@app.route("/")

#add the routing information for each of the other routes
def welcome():
    return(
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
	)

#add precipitation route
@app.route("/api/v1.0/precipitation")

#create precipitation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(measurement.date, measurement.prcp).filter(measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#add stations route
@app.route("/api/v1.0/stations")

#create stations function
def stations():
    results = session.query(station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations)

#add temperature route
@app.route("/api/v1.0/tobs")

#create temperature function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

#add statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#create statistics function
def stats(start, end):
    
    sel = [func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs)]
    
    if not end:
        results = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    
    results = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)