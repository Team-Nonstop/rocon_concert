#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_concert/hydro-devel/concert_orchestra/LICENSE
#
##############################################################################
# Imports
##############################################################################

import rospy
import concert_msgs.msg as concert_msgs
import concert_msgs.srv as concert_srvs

class CareerCenter(object):

    _subscriber      = {}
    _publisher       = {}
    _service_server  = {}
    _param           = {}
    _solution        = {}

    def __init__(self):
        self.init_subscriber()
        self.init_services()
        self.init_params()

    def init_subscriber(self):
        self._subscriber = {}
        self._subscriber["list_concert_clients"] = rospy.Subscriber("list_concert_clients", concert_msgs.ConcertClients, self.process_list_concert_clients)

    def init_services(self):
        self._service_server['add_service'] = rospy.Service('add_service',concert_srvs.AddService, self.process_add_service)
        self._service_server['remove_service'] = rospy.Service('remove_service',concert_srvs.RemoveService, self.process_remove_service)
        pass

        
    def init_params(self):
        self._param = {}
        self._param['name']         = rospy.get_param("~name","Solution 42")
        self._param['services']         = rospy.get_param("~services",[])

    def process_list_concert_clients(self,msg):
        rospy.loginfo("hello concert")

    def process_add_service(self,req):
        return AddServiceResponse()

    def process_remove_service(self,req):
        return RemoveServiceResponse()


    def spin(self):
        rospy.loginfo("In spin")
        rospy.loginfo(str(self._param['services']))
        rospy.spin()

