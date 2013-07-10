#!/usr/bin/env python
#
# License: BSD
#
#

import rospy
import concert_careercenter

if __name__ == '__main__':
    rospy.init_node('rocon_agent')
    client = concert_careercenter.RoconAgent()
    rospy.loginfo("Initialized")
    client.spin()
