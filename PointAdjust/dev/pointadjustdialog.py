# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PointAdjustDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_pointadjust import Ui_PointAdjust
# create the dialog for zoom to point


class PointAdjustDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_PointAdjust()
        self.ui.setupUi(self)
