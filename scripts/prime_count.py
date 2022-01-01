#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('prime_counts')
pub = rospy.Publisher('prime_count', Int32, queue_size=1)
rate = rospy.Rate(10)

n = 0

while not rospy.is_shutdown():
    n += 1
    flag=0

    if n==1:
        flag=1
    elif n==2:
        flag=0
    elif n%2 == 0:
        flag=1
    else:
        for x in range(3,n,2):
            if n%x == 0:
                flag=1
                break
    
    if flag==0:
        pub.publish(n)

    rate.sleep()
