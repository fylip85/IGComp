#!/usr/bin/env python

import itertools
import os
import sys

import igc_lib
import lib.dumpers



def print_flight_details(flight):
    print "Flight:", flight
    print "Takeoff:", flight.takeoff_fix
    zipped = itertools.izip_longest(flight.thermals, flight.glides)
    for x, (thermal, glide) in enumerate(zipped):
        if glide:
            print "  glide[%d]:" % x, glide
        if thermal:
            print "  thermal[%d]:" % x, thermal
    print "Landing:", flight.landing_fix



def get_details(input_file, task_file):
    print(input_file)
    flight = igc_lib.Flight.create_from_file(input_file)
    if not flight.valid:
        print "Provided flight is invalid:"
        print flight.notes
        return

    print_flight_details(flight)
    task = igc_lib.Task.create_from_lkt_file(task_file)
    reached_turnpoints = task.check_flight(flight)
    for t, fix in enumerate(reached_turnpoints):
        print "Turnpoint[%d] achieved at:" % t, fix.rawtime



        



def main(): #wird halt ausgefhrt weil main eingangspunkt

    dir_path = os.path.dirname(os.path.realpath(__file__))      #use os to get this file directory  #string
    task_file = dir_path + "\\DISENTIS.Lkt"                        #taskfile absolut path           #string
    path = dir_path + "\\Tracks\\"                                  #igc file directory             #string
    tracks = os.listdir( path )                                     #list of files in igc directos    #liste oder enumeration

    for name in tracks:                                     #
        if name.endswith(".igc"):
            fullpath = path + name
            get_details(fullpath, task_file)

if __name__ == '__main__':
    main()
