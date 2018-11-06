import unittest

from blendercam.addons.cam_utils.Format import Format

class BCTesFormat(unittest.TestCase):
    
    def bctest_none(self):
        format = Format()
        self.assertEqual("None", format.string(None))

    def bctest_simple1(self):
        format = Format()
        self.assertEqual("24.400", format.string(24.4))

    def bctest_simple2(self):
        format = Format()
        self.assertEqual("-77.777", format.string(-77.777))

        
