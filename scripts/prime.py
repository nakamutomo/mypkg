#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Int32

def cb(message):
    rospy.loginfo(message.data)

rospy.init_node('prime')
sub = rospy.Subscriber('prime_count', Int32, cb)
rospy.spin()
