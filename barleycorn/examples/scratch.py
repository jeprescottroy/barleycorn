__author__ = 'jjpr'

import barleycorn
import barleycorn.examples.designs as designs

def xRS01(tk):
  stand = designs.RockerStand01()
  return [stand]

def xRAll01(tk):
  stand = designs.RockerStand01()
  middle = designs.RockerMiddle01(stand.clearance_radius_inner, stand.rim_radius_major, stand.wall_thickness)
  center = designs.RockerCenter01(middle.clearance_radius_inner, middle.rim_radius_major, middle.wall_thickness)
  return [stand, middle, center]
