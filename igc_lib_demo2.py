#!/usr/bin/env python

import itertools
import os
import sys

import igc_lib
import lib.dumpers


def print_flight_details(flight):
    print "Flight:", flight
    print "Takeoff:", flight.takeoff_fix
    print"landingtime", flight.landing_fix
    print"thermals", flight.thermals

    print dir(flight)

"""
    zipped = itertools.izip_longest(flight.thermals, flight.glides)
    for x, (thermal, glide) in enumerate(zipped):
        if glide:
            print "  glide[%d]:" % x, glide
        if thermal:
            print "  thermal[%d]:" % x, thermal



    print "Landing:", flight.landing_fix
"""

def main():


    input_file = "C:/Users/bethge-adm/Documents/fredmaster/Tracks/2018-08-11_12.56_Disentis.igc"

    flight = igc_lib.Flight.create_from_file(input_file)

    print_flight_details(flight)



if __name__ == "__main__":
    main()
