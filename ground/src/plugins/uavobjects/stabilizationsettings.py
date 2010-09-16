##
##############################################################################
#
# @file       stabilizationsettings.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the StabilizationSettings object. This file has been 
#             automatically generated by the UAVObjectGenerator.
# 
# @note       Object definition file: stabilizationsettings.xml. 
#             This is an automatically generated file.
#             DO NOT modify manually.
#
# @see        The GNU Public License (GPL) Version 3
#
#############################################################################/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#


import uavobject

import struct
from collections import namedtuple

# This is a list of instances of the data fields contained in this object
_fields = [ \
	uavobject.UAVObjectField(
		'UpdatePeriod',
		'B',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'RollMax',
		'B',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'PitchMax',
		'B',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'YawMax',
		'B',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'YawMode',
		'b',
		1,
		[
			'0',
		],
		{
			'0' : 'rate',
			'1' : 'heading',
		}
	),
	uavobject.UAVObjectField(
		'ThrottleMax',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'ThrottleMin',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'RollIntegralLimit',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'PitchIntegralLimit',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'YawIntegralLimit',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'PitchKp',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'PitchKi',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'PitchKd',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'RollKp',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'RollKi',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'RollKd',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'YawKp',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'YawKi',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
	uavobject.UAVObjectField(
		'YawKd',
		'f',
		1,
		[
			'0',
		],
		{
		}
	),
]


class StabilizationSettings(uavobject.UAVObject):
    ## Object constants
    OBJID        = 117768092
    NAME         = "StabilizationSettings"
    METANAME     = "StabilizationSettingsMeta"
    ISSINGLEINST = 1
    ISSETTINGS   = 1

    def __init__(self):
        uavobject.UAVObject.__init__(self,
                                     self.OBJID, 
                                     self.NAME,
                                     self.METANAME,
                                     0,
                                     self.ISSINGLEINST)

        for f in _fields:
            self.add_field(f)
        
    def __str__(self):
        s  = ("0x%08X (%10u)  %-30s  %3u bytes  format '%s'\n"
                 % (self.OBJID, self.OBJID, self.NAME, self.get_struct().size, self.get_struct().format))
        for f in self.get_tuple()._fields:
            s += ("\t%s\n" % f)
        return (s)

def main():
    # Instantiate the object and dump out some interesting info
    x = StabilizationSettings()
    print (x)

if __name__ == "__main__":
    #import pdb ; pdb.run('main()')
    main()
