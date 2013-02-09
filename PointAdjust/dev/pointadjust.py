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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from pointadjustdialog import PointAdjustDialog
# Import the ui stuff
from ui_pointadjust import Ui_PointAdjust
# Import math module
import math

class PointAdjust:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/pointadjust"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/pointadjust_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog and keep reference
        self.dlg = PointAdjustDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/PointAdjust/pointadjust.png"), "Point adjustment", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Point Adjustment", self.action)
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Point Adjustment", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # Clear and repopulate combobox
        self.dlg.ui.comboLayer.clear()
        for lyr in self.vectorLayers():
            self.dlg.ui.comboLayer.addItem(lyr)  
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
     
        # See if OK was pressed
        if result == 1:
            # Get selected layer
            self.layer = self.getSelectedLayer(self.dlg.ui.comboLayer.currentText())
            # Check if all fields are filled
            if self.dlg.ui.x1.text().isEmpty() or self.dlg.ui.y1.text().isEmpty() or self.dlg.ui.x2.text().isEmpty() or self.dlg.ui.y2.text().isEmpty() or self.dlg.ui.fid1.text().isEmpty() or self.dlg.ui.fid2.text().isEmpty():
                QMessageBox.information( self.iface.mainWindow(),"Error", "Fill in the adjustment parameters first" )
            else:
                if (not self.layer.isEditable()):
                    QMessageBox.information( self.iface.mainWindow(),"Error", "Layer not in edit mode" )
                else:
                    # Define points A and B. The former is used for initial translation.
                    pointA = int(self.dlg.ui.fid1.text())
                    pointB = int(self.dlg.ui.fid2.text())
                    # Get the desired (new) x, y values for points A and B
                    x1 = float(self.dlg.ui.x1.text())
                    y1 = float(self.dlg.ui.y1.text())
                    x2 = float(self.dlg.ui.x2.text())
                    y2 = float(self.dlg.ui.y2.text())  
                    # call moveAllPnt method to do the adjustments
                    self.moveAllPnt(x1,y1, x2, y2, pointA, pointB)                

    def moveAllPnt(self, AnewX, AnewY, BnewX, BnewY, pointAfid, pointBfid):
        layer = self.getSelectedLayer(self.dlg.ui.comboLayer.currentText())
        layer.beginEditCommand("editing")

        # Use point A coordinates (AoldX, AoldY) and A' coordinates (AnewX, AnewY) to get dAx and dAy
        feat = QgsFeature()
        layer.featureAtId(pointAfid, feat)
        geom = feat.geometry().asPoint()
        AoldX = float(geom.x())
        AoldY = float(geom.y())
        # Get the difference between old and new coordinates
        dAx = AnewX - AoldX
        dAy = AnewY - AoldY

        # Get the new temporary point C coordinates
        Cx = BnewX - dAx
        Cy = BnewY - dAy

        # To get the angle we need the old Point B coordinates
        layer.featureAtId(pointBfid, feat)
        geom = feat.geometry().asPoint()
        BoldX = float(geom.x())
        BoldY = float(geom.y())         
        # Get the angle
        angle = self.getAngle(AoldX, AoldY, BoldX, BoldY, Cx, Cy)
        
        # Error measurement
        distAB = self.distance(AoldX, AoldY, BoldX, BoldY)
        distAC = self.distance(AoldX, AoldY, Cx, Cy)
        diffABAC = distAB - distAC
        QMessageBox.information( self.iface.mainWindow(),"Error measurement", "Difference measurement in map units: " + str(diffABAC) + "\n (Positive number: new points too much apart; Negative number: new points too close)" )
        
        # Move points
        provider = layer.dataProvider()
        count = layer.dataProvider().featureCount()
        for i in range(count):
            self.transPnt(dAx,dAy,i)
            self.rotPnt(AnewX, AnewY, angle, i)
    
        layer.endEditCommand()
        self.iface.mapCanvas().refresh()

    def getAngle(self, Ax, Ay, Bx, By, Cx, Cy):
        layer = self.getSelectedLayer(self.dlg.ui.comboLayer.currentText())
        
        # Get distances between points AB (ideally AB should equal AC) and BC.
        #ab = self.distance(pointAx, pointAy, pointBx, pointBy)
        #ac = self.distance(pointAx, pointAy, pointCx, pointCy)
        #bc = self.distance(pointBx, pointBy, pointCx, pointCy)
                
      
        # Getting the angle BAC using vector dot product
        vABx = Bx - Ax
        vABy = By - Ay
        #vABlen = (vABx**2 + vABy**2)**0.5
        vACx = Cx - Ax
        vACy = Cy - Ay
        #vAClen = (vACx**2 + vACy**2)**0.5      
        #vABAC = vABx*vACx + vABy*vACy
        #angle = vABAC / (vABlen*vAClen)
        angle = math.atan2(vACy,vACx) - math.atan2(vABy,vABx)
        
        # In case angle is negative
        if angle < 0:
            angle = 2*math.pi + angle

        # Calculate the angle CAB (alpha) using cos theorem
        #angle = math.acos((ac**2 + ab**2 - bc**2)/(2 * ac * ab))
        
        return angle
        
    def transPnt(self, x, y, fid):
        layer = self.getSelectedLayer(self.dlg.ui.comboLayer.currentText())
        feat = QgsFeature()
        layer.featureAtId(fid, feat)
        geom = feat.geometry().asPoint()
        newx = float(geom.x()) + x
        newy = float(geom.y()) + y
        layer.moveVertex(newx, newy, fid, 0) # x, y, feature id, vertex id (should be 0 for points)

    def rotPnt(self, xCenter, yCenter, angle, fid):
        layer = self.getSelectedLayer(self.dlg.ui.comboLayer.currentText())
        feat = QgsFeature()
        layer.featureAtId(fid, feat)
        geom = feat.geometry().asPoint()
        x = float(geom.x())
        y = float(geom.y())
        
        # Get the new rotated coordinates
        xRot = xCenter + math.cos(angle) * (x - xCenter) - math.sin(angle) * (y - yCenter)
        yRot = yCenter + math.sin(angle) * (x - xCenter) + math.cos(angle) * (y - yCenter)
        
        # move point
        layer.moveVertex(xRot, yRot, fid, 0)


    def distance(self, x1, y1, x2, y2):
        # Returns distance between two points
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
    def vectorLayers(self):
        layerMap=QgsMapLayerRegistry.instance().mapLayers()
        layerList = []
        for (name,layer) in layerMap.iteritems():
            if (layer.type() == 0): # 0 is vector layer
                layerList.append(layer.name())
        return layerList
    
    def getSelectedLayer(self, layerName):
        layersmap=QgsMapLayerRegistry.instance().mapLayers()
        for (name,layer) in layersmap.iteritems():
            if layerName==layer.name():
                return layer        