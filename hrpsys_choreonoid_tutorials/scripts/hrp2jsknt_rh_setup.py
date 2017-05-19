#!/usr/bin/env python

from hrpsys_choreonoid_tutorials.choreonoid_hrp2_hrpsys_config import *

class HRP2JSKNT_HrpsysConfigurator(ChoreonoidJSKHRP2HrpsysConfigurator):
    def getRTCList (self):
        ##return self.getRTCListUnstable()
        return [
            ['seq', "SequencePlayer"],
            ['sh', "StateHolder"],
            ['fk', "ForwardKinematics"],
            ['tf', "TorqueFilter"],
            ['kf', "KalmanFilter"],
            ['vs', "VirtualForceSensor"],
            ['rmfo', "RemoveForceSensorLinkOffset"],
            ['es', "EmergencyStopper"],
            ['ic', "ImpedanceController"],
            ['abc', "AutoBalancer"],
            ['st', "Stabilizer"],
            ['co', "CollisionDetector"],
            # ['tc', "TorqueController"],                                                                                                                           # ['te', "ThermoEstimator"],                                                                                                                           # ['tl', "ThermoLimiter"],
            ['rfu', "ReferenceForceUpdater"],
            ['hes', "EmergencyStopper"],
            ['el', "SoftErrorLimiter"],
            ['log', "DataLogger"]
        ]

    def defJointGroups (self):
        rleg_6dof_group = ['rleg', ['RLEG_JOINT0', 'RLEG_JOINT1', 'RLEG_JOINT2', 'RLEG_JOINT3', 'RLEG_JOINT4', 'RLEG_JOINT5']]
        lleg_6dof_group = ['lleg', ['LLEG_JOINT0', 'LLEG_JOINT1', 'LLEG_JOINT2', 'LLEG_JOINT3', 'LLEG_JOINT4', 'LLEG_JOINT5']]
        rleg_7dof_group = ['rleg', ['RLEG_JOINT0', 'RLEG_JOINT1', 'RLEG_JOINT2', 'RLEG_JOINT3', 'RLEG_JOINT4', 'RLEG_JOINT5', 'RLEG_JOINT6']]
        lleg_7dof_group = ['lleg', ['LLEG_JOINT0', 'LLEG_JOINT1', 'LLEG_JOINT2', 'LLEG_JOINT3', 'LLEG_JOINT4', 'LLEG_JOINT5', 'LLEG_JOINT6']]
        torso_group = ['torso', ['CHEST_JOINT0', 'CHEST_JOINT1']]
        head_group = ['head', ['HEAD_JOINT0', 'HEAD_JOINT1']]
        rarm_group = ['rarm', ['RARM_JOINT0', 'RARM_JOINT1', 'RARM_JOINT2', 'RARM_JOINT3', 'RARM_JOINT4', 'RARM_JOINT5', 'RARM_JOINT6', 'RARM_JOINT7']]
        larm_group = ['larm', ['LARM_JOINT0', 'LARM_JOINT1', 'LARM_JOINT2', 'LARM_JOINT3', 'LARM_JOINT4', 'LARM_JOINT5', 'LARM_JOINT6', 'LARM_JOINT7']]
        if self.ROBOT_NAME == "HRP2JSKNT" or self.ROBOT_NAME == "HRP2JSKNTS":
            self.Groups = [rleg_7dof_group, lleg_7dof_group, torso_group, head_group, rarm_group, larm_group]
        elif self.ROBOT_NAME == "HRP2JSK":
            self.Groups = [rleg_6dof_group, lleg_6dof_group, torso_group, head_group, rarm_group, larm_group]
        else: # HRP2W, HRP2G
            self.Groups = [torso_group, head_group, rarm_group, larm_group]

    def startABSTIMP (self):
        self.startAutoBalancer()
        #self.ic_svc.startImpedanceController("larm")
        #self.ic_svc.startImpedanceController("rarm")
        #time.sleep(5)
        #self.startStabilizer()

if __name__ == '__main__':
    hcf = HRP2JSKNT_HrpsysConfigurator("HRP2JSKNT")
    [sys.argv, connect_constraint_force_logger_ports] = hcf.parse_arg_for_connect_ports(sys.argv)
    if len(sys.argv) > 2 :
        hcf.init(sys.argv[1], sys.argv[2], connect_constraint_force_logger_ports=connect_constraint_force_logger_ports)
        hcf.startABSTIMP()
    elif len(sys.argv) > 1 :
        hcf.init(sys.argv[1], connect_constraint_force_logger_ports=connect_constraint_force_logger_ports)
        hcf.startABSTIMP()
    else :
        hcf.init(connect_constraint_force_logger_ports=connect_constraint_force_logger_ports)
