# Project 5 - Leaflet Map

This is a code repository for UO CIS 322's fifth coding project. It 
uses reverse geocoding to locate wherever the user clicks on the map.
The map starts off centered in Eugene, OR, but may be moved to anywhere
on the planet. It employs Leaflet and MapQuest as its primary APIs, though
it also uses bootstrap, Flask, and Gunicorn in less obvious capacities.

## Points of Interest

The six points of interest placed on the map represent some of the most
highly rated sushi locations in Eugene. Unfortunately, it seems that 
MapQuest's database handles the coordinates for these particular locations
poorly (see FIXME).

## Deployment

Installing this should take no more than four commands:

* git clone
* cd (directory name containing the repository)
* bash ./configure
* make run

It should be noted that 'make run' runs the code on a debugging server.
Extended deployment should be done via gunicorn with 'make service'. The
debugging server runs on the flask default (port 5000) and may be changed
in the configuration files.

## FIXME

As of now, MapQuest's reverse geocoding leaves something to be desired;
five of the six POIs do not appear to have any results, causing their
popups to display nothing. Only Mame appears to have a set of coordinates
recognizable in their database. Recommend switching to a better API.

## Contact

You may contact me over email if you have questions regarding the code at
adibb@cis.uoregon.edu. 