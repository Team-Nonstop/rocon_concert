#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_concert/hydro-devel/concert_orchestra/LICENSE
#
##############################################################################
# Imports
##############################################################################

import rospy
import concert_careercenter

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':
    rospy.init_node('careercenter')  # , log_level=rospy.DEBUG)
    center = concert_careercenter.CareerCenter()
    rospy.loginfo("Initialized")
    center.spin()
