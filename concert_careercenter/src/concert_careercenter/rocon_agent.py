#!/usr/bin/env python
#
# License: BSD
#

import rospy
from rocon_app_manager import RappManager

import std_msgs.msg as std_msgs 
import concert_msgs.msg as concert_msgs
import concert_msgs.srv as concert_srvs


class RoconAgent(RappManager):

    pub  = {}
    sub  = {}
    srv  = {}
    
    def __init__(self):
        self.app_manger = RappManager()

        self.init_publishers()
        self.init_subscribers()
        self.init_services()

    def init_subscribers(self):
        self.sub['update_on_jobs'] = rospy.Subscriber('update_on_jobs',std_msgs.Empty,self.process_update_notification)

    def init_publishers(self):
        self.pub['apply_for_job'] = rospy.Publisher('apply_for_job',concert_msgs.JobApplication)

    def init_services(self):
        self.srv['query_jobs'] = rospy.ServiceProxy('query_jobs',concert_srvs.QueryJobs)

    def process_update_notification(self,msg):
        self.log("Hola!")


    def log(self,msg):
        rospy.loginfo("Agent : " + str(msg))

    def spin(self):
        self.log("Whoola")
        self.app_manger.spin()
