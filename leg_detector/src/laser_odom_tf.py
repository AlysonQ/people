#!/usr/bin/env python  
# -*- coding: utf-8 -*-
import rospy
import tf
 
if __name__ == '__main__':
    rospy.init_node('odom_laser_tf_broadcaster')
    
    laser_frame_name=rospy.get_param("~laser_frame_id","laser")  # /scan 话题的消息的frame名字
    odom_frame_name=rospy.get_param("~odom_frame_id","/odom_combined")  # leg_detector要能找到/scan话题的frame与/odom_combined的tf变换，这里直接发布这个变换
 
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        br.sendTransform((0.3, 0.0, 0.1),
                            (0.0, 0.0, 0.0, 1.0),
                            rospy.Time.now(),
                            laser_frame_name,
                            odom_frame_name)  # 站在odom看laser
