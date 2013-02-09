# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PointAdjust
                                 A QGIS plugin
 Adjusts 2d vector point data according to set coordinates
                             -------------------
        begin                : 2013-01-20
        copyright            : (C) 2013 by Allar Haav
        email                : allar.haav@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Point Adjustment"


def description():
    return "Adjusts 2d vector point data according to set coordinates"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Allar Haav"

def email():
    return "allar.haav@gmail.com"

def classFactory(iface):
    # load PointAdjust class from file PointAdjust
    from pointadjust import PointAdjust
    return PointAdjust(iface)
