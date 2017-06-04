import unittest
import doctest

class DeviceTest( unittest.TestCase ):
	# This is a simple test that just tries to load the module
	def runTest( self ):
		try:
			import myimplementation
		except ImportError, e:
			self.Fail( str( e ) )