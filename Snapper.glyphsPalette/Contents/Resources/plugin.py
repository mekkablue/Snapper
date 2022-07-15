# encoding: utf-8

###########################################################################################################
#
#
#	Palette Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Palette
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class Snapper (PalettePlugin):
	
	dialog = objc.IBOutlet()
	snapSwitch = objc.IBOutlet()
	
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'Snapper',
			})
		
		# Load .nib dialog (without .extension)
		self.loadNib('IBdialog', __file__)

	@objc.python_method
	def start(self):
		# Adding a callback for the 'GSUpdateInterface' event
		Glyphs.addCallback(self.update, UPDATEINTERFACE)

	@objc.python_method	
	def __del__(self):
		Glyphs.removeCallback(self.update)

	@objc.python_method
	def update(self, sender):
		# Extract font from sender
		currentTab = sender.object()
		if currentTab:
			font = currentTab.parent
			if font and isinstance(font, GSFont):
				self.snapSwitch.setState_(font.snapToObjects) 
	
	# Action triggered by Switch
	@objc.IBAction
	def setSnapping_( self, sender ):
		font = Glyphs.font
		if font:
			# Store value coming in from dialog
			font.snapToObjects = bool(sender.intValue())

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
