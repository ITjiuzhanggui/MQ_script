#!/usr/bin/env python
"""
ST_PERF_Google_Maps_Zooming_with_2x_H.265_1080p_videos
"""

import time
import os
import sys
import subprocess
import shlex
# from pnplib.testbase import TestBase
# from pnplib.logformatter import LogFormatter
from optparse import make_option, OptionParser
# from pnplib import common as cm
import traceback
import pexpect
import re
import numpy as np
from pexpect import pxssh
import unittest
import logging
# from pnplib import raise_exception_mail
from python_Code.template import paramiko
CUR_DIR = os.path.dirname(__file__)
CUR_DIR = __all__ = ['ExceptionPxssh', 'pxssh']
class Test(unittest.TestCase):
    """class Test"""

    def __init__(self, test_name, seria_no, sub_test, rnd_no, rsd, conf):
        """
        init func of Camera_launch_to_preview_Cold
        """
        self.testname = test_name
        self.tag = self.__class__.__name__
        self.logger = LogFormatter.getInstance('debug', self.tag).logger
        self.result = []
        self.rsd = rsd
        self.rnd_no = rnd_no
        self.comment = ""
        self.ip_address = ""
        self.param_file_dir = ""
        self.sos_dir = ""
        self.sos_passwd = ""
        self.app_id = ""
        self.ssh_client = None
        self.param_dic = {
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_dials_120': 'dials.120',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_dials_160': 'dials.160',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_dials_80': 'dials.80',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_long_10': 'long.10',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_long_160': 'long.160',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_long_30': 'long.30',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_long_80': 'long.80',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_160_geometry': 'multi.160.geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_160_shader': 'multi.160.shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_30_geometry': 'multi.30.geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_30_shader': 'multi.30.shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_80_geometry': 'multi.80.geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_80_shader': 'multi.80.shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_160_geometry': 'single.160.geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_160_shader': 'single.160.shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_30': 'single.30',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_30_geometry': 'single.30.geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_30_shader': 'single.30.shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_80_geometry': 'single.80.geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_80_shader': 'single.80.shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_tex_160': 'tex.160',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_tex_30': 'tex.30',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_tex_80': 'tex.80',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_tex_grey': 'tex.grey'
            }
        self.test_list = [
            'ST_PERF_GPU_Preemption_QoS_Stress_Test',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_dials_120',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_dials_160',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_dials_80',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_long_10',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_long_160',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_long_30',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_long_80',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_160_geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_160_shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_30_geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_30_shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_80_geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_multi_80_shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_160_geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_160_shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_30',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_30_geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_30_shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_80_geometry',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_single_80_shader',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_tex_160',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_tex_30',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_tex_80',
            'ST_PERF_GPU_Preemption_QoS_Stress_Test_tex_grey'
            ]
        self.result_dic = {}
        self.unit = {}
        self.log_dic = {}
        self.comment_dic = {}

    def setup(self):
        super(Test, self).setup()
        self.logger.info('setup %s' % self.testname)
        for key in self.test_list:
            self.log_dic[key] = key
            self.result_dic[key] = []
            self.comment_dic[key] = ""
            self.unit[key] = 'fps'
            self.log_saver.find_logs(self.testname, self.test_list)
        self.ip_address = self.pl.reboot_acrn_and_get_ip(True)
        self.logger.info('DUT IP is %s' % self.ip_address)
        self.pl.airplane_on()
        self.pl.wifi_off()
        self.pl.bt_off()
        self.pl.dislocation()
        self.push_file_and_install()

    def run(self):
        """
        run
        """
        self.logger.info('run %s' % self.testname)
        self.run_test()

    def cleanup(self):
        """
        clean up
        """
        self.logger.info('cleanup %s' % self.testname)
        self.send_line('rm -rf /root/*')
        self.ssh_client.logout()
        self.ssh_client.close()
        self.pl.upload_tcr_multi(self.unit, self.test_list, self.result_dic, self.log_dic)
        for key in self.test_list:
            if not self.result_dic[key]:
                self.result_dic[key].append(int(0))
                self.comment_dic[key] = "exception during case setup"
        self.log_saver.save_logs(self.testname, self.test_list, self.result_dic, self.pl.get_uuid(), self.comment_dic)
        self.pl.plug_usb()
        self.pl.uninstall_app(self.app_id)
        self.pl.reboot_device()
        self.pl.airplane_on()
        super(Test, self).cleanup()

    def push_file_and_install(self):
        self.app_id = self.cfg.get('app_id')
        sos_file_dir = self.cfg.get('sos_file_dir')
        self.sos_dir = cm.get_resource_dir_path(sos_file_dir)
        self.param_file_dir = self.cfg.get('param_dir')
        param_dir = cm.get_resource_dir_path(self.param_file_dir)
        apk_file_name = self.cfg.get('apk')
        apk_file_path = cm.get_resource_abs_path(apk_file_name)
        scp_cmd = 'scp -r %s root@%s:/root/' % (self.sos_dir, self.ip_address)
        self.sos_passwd = self.cfg.get('sos_passwd')
        self.scp_file(scp_cmd, self.sos_passwd)
        self.pl.install_app(apk_file_path, testpack=True)
        time.sleep(3)
        self.launch_ssh(self.ip_address, 'root', self.sos_passwd)
        cmd1 = 'export XDG_RUNTIME_DIR=/run/ias'
        cmd2 = 'systemctl enable ias-earlyapp'
        cmd3 = 'systemctl start ias-earlyapp'
        self.send_line(cmd1)
        self.send_line(cmd2)
        self.send_line(cmd3)
    def scp_file(self, scp_cmd, scp_passwd):
        self.logger.info('copy file to sos: %s' % scp_cmd)
        self.logger.info('Password: %s' % scp_passwd)
        ssh = pexpect.spawn(scp_cmd)
        try:
            i = ssh.expect(['Password: ', 'continue connecting (yes/no)?'])
            if i == 0:
                ssh.sendline(scp_passwd)
            elif i == 1:
                ssh.sendline('yes')
                ssh.expect('Password:')
                ssh.sendline(scp_passwd)
            else:
                self.logger.info('wrong password')
        except pexpect.EOF:
            ssh.close()
        else:
            r = ssh.read()
            ssh.expect(pexpect.EOF)
            ssh.close()
            print(r)

    def launch_ssh(self, ip_addr, username, passwd):
        self.logger.info('launch ssh client')
        try:
            ssh_client = pxssh.pxssh()
            ssh_client.login(ip_addr, username, passwd)

        except Exception as e:
            print(e.message)
            self.logger.info('launch ssh client failed')
            self.ssh_client = None

        else:
            self.logger.info('launch ssh client success')
            self.ssh_client = ssh_client

    def send_line(self, cmd):
        try:
            self.ssh_client.sendline(cmd)
            self.ssh_client.prompt()
            self.logger.info('ssh cmd: %s' % self.ssh_client.before)
        except Exception as e:
            print(e.message)
            self.logger.info('send cmd failed')
            return None

    def reconnect_and_resend(self):
        self.ssh_client.close()
        self.launch_ssh(self.ip_address, 'root', self.sos_passwd)
        cmd1 = 'export XDG_RUNTIME_DIR=/run/ias'
        cmd2 = 'systemctl enable ias-earlyapp'
        cmd3 = 'systemctl start ias-earlyapp'
        echo_cmd = 'echo -1023 > /sys/module/i915/parameters/gvt_workload_priority'
        cd_cmd = 'cd /root/daimler_ic/'
        chmod_cmd = 'chmod +x daimler_ic-wayland'
        self.send_line(cmd1)
        self.send_line(cmd2)
        self.send_line(cmd3)
        self.send_line(echo_cmd)
        self.send_line(cd_cmd)
        self.send_line(chmod_cmd)

    def send_line_and_wait_result(self, cmd, need_retry=True):
        res = None
        try:
            self.ssh_client.sendline(cmd)
            i = 0
            while i < 30:
                i += 1
                self.logger.info('%d', i)
                self.ssh_client.prompt(10)
                res = self.ssh_client.before
                print(res)
                if res.find('10/0') > -1 or i == 30:
                    self.ssh_client.sendcontrol('c')
                    self.ssh_client.prompt()
                    print(self.ssh_client.before)
                    break
        except Exception as e:
            res = None
            print(e.message)
            self.logger.info('send cmd failed')
            if need_retry:
                self.reconnect_and_resend()
                res = self.send_line_and_wait_result(cmd, False)
        finally:
            return res

    def calculate_fps_from_string(self, res):
        tmp = res[res.find('Reset stats'):]
        self.logger.info('split: %s' % tmp)
        strlist = tmp.split("\r\n")
        i = 0
        s = 0.0
        print (strlist)
        for item in strlist:
            relist = re.findall(r"\d+\.\d+", item)
            if relist:
                i += 1
                s += float(relist[0])
        self.logger.info('i: %d', i)
        self.logger.info('s: %f', s)
        if i > 0:
            return float(s/i)
        else:
            return 0

    def run_test(self):
        activity = self.cfg.get('activity')
        activity_cmd = 'am start -n %s' % activity
        echo_cmd = 'echo -1023 > /sys/module/i915/parameters/gvt_workload_priority'
        cd_cmd = 'cd /root/daimler_ic/'
        daimler_cmd = './daimler_ic-wayland -x 2560 -y 960 -m 61 -fullscreen'
        chmod_cmd = 'chmod +x daimler_ic-wayland'
        self.send_line(cd_cmd)
        self.send_line(chmod_cmd)
        mid_res = []
        for key in self.param_dic:
            param_file_name = self.param_dic[key]
            param_file = cm.get_resource_abs_path(os.path.join(self.param_file_dir, param_file_name))
            device_path = '/data/local/tmp/config.txt'
            self.device.adb_push_file(param_file, device_path)
            self.logger.info('Push config file %s finished' % param_file_name)
            loop_count = 0
            for _ in range(self.rnd_no):
                loop_count += 1
                self.logger.info("%s round %d" % (key, loop_count))
                try:
                    self.device.run_adb_shell(activity_cmd)
                    self.send_line(echo_cmd)
                    resstr = self.send_line_and_wait_result(daimler_cmd)
                    res = self.calculate_fps_from_string(resstr)
                    self.result_dic[key].append(res)
                except Exception as e:
                    self.logger.error(str(e))
                    self.comment_dic[key] = str(e)
                    trace_log = traceback.format_exc()
                    raise_exception_mail.send_mail(self.comment_dic[key], "run", self.testname, trace_log)
                    traceback.print_exc()
                    self.pl.reboot_device()
                finally:
                    if len(self.result_dic[key]) != loop_count:
                        self.result_dic[key].append(int(0))
                        if not self.comment_dic[key]:
                            self.comment_dic[key] = "exception during run test"
            self.pl.reboot_device(True)
            time.sleep(60)
            self.reconnect_and_resend()
            mid_res.append(np.median(self.result_dic[key]))
        self.result_dic['ST_PERF_GPU_Preemption_QoS_Stress_Test'].append(np.min(mid_res))




seria = None
sub_test = None
insert_log = None
round_no = TC_PARAMETERS("ROUND")
#conf = TC_PARAMETERS("PNP_CONF")
conf = None
testname = TC_PARAMETERS("TEST_NAME")
rsd = TC_PARAMETERS("RSD")
test = Test(testname, seria, sub_test, int(round_no), float(rsd), conf)
test.main()
VERDICT = SUCCESS
OUTPUT = "We can get data"