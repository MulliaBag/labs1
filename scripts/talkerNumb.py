#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

rospy.init_node('talkerNumb')
pub = rospy.Publisher('my_MYSELF_topic', Int16, queue_size=10)
newpub=rospy.Publisher('my_my_my_topic', Int16, queue_size=10)
rate = rospy.Rate(10)
hello_num=0

def start_talkerNumb():
    msg = Int16()
    global hello_num
    while not rospy.is_shutdown():
        hello_num = hello_num + 2 
        rospy.loginfo(hello_num)

        msg.data = hello_num
        pub.publish(msg)

        if hello_num>=100:
           hello_num=0
           msg.data=hello_num
           newpub.publish(msg)

        rate.sleep()


try:
    start_talkerNumb()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
