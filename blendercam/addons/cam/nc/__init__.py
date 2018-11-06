################################################################################
# __init__.py
#
# This is here to make python see NC folder
#
# Hirutso Enni, 2009-01-13

from collections import OrderedDict
# tuple field layout:
# ( post processor file name, g-code file extension, menu item name, processor description)
postprocessors = OrderedDict()
postprocessors['ISO'] = ('iso', '.tap', 'Iso', 'exports standardized gcode ISO 6983 (RS-274)')
postprocessors['MACH3'] = ('mach3', '.tap', 'Mach3', 'default mach3')
postprocessors['EMC'] = ('emc2b', '.ngc', 'LinuxCNC - EMC2', 'Linux based CNC control software - formally EMC2')
postprocessors['GRBL'] = ('grbl', '.ngc', 'grbl', 'optimized gcode for grbl firmware on Arduino with cnc shield')
postprocessors['HM50'] = ('hm50', '.tap', 'Hafco HM-50', 'Hafco HM-50')
postprocessors['HEIDENHAIN'] = ('heiden', '.H', 'Heidenhain', 'heidenhain')
postprocessors['TNC151'] = ('tnc151', '.tap', 'Heidenhain TNC151', 'Post Processor for the Heidenhain TNC151 machine')
postprocessors['SIEGKX1'] = ('siegkx1', '.tap', 'Sieg KX1', 'Sieg KX1')
postprocessors['CENTROID'] = ('centroid1', '.tap', 'Centroid M40', 'Centroid M40')
postprocessors['ANILAM'] = ('anilam_crusader_m', '.tap', 'Anilam Crusader M', 'Anilam Crusader M')
postprocessors['GRAVOS'] = ('gravos', '.nc', 'Gravos', 'Gravos')
postprocessors['WIN-PC'] = ('winpc', '.din', 'WinPC-NC', 'German CNC by Burkhard Lewetz')
postprocessors['SHOPBOT MTC'] = ('shopbot_mtc', '.sbp', 'ShopBot MTC', 'ShopBot MTC')
postprocessors['LYNX_OTTER_O'] = ('lynx_otter_o', '.nc', 'Lynx Otter o', 'Lynx Otter o')


def getPostProcessorMenuItems():
	items = []
	
	for keyname, postp in postprocessors.items():
		items.append((keyname, postp[2], postp[3]))
		
	return items
