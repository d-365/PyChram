# -*- coding: utf-8 -*- 
# @Time : 2021/3/19 15:36 
# @Author : dujun
# @describe : 概率计算
# @File : prob.py
from pprint import pprint
from Interface_Yss.project.user import userProject
from Interface_Yss.project.prob import prob_project
import math


class prob:

    def __init__(self):
        environment_current = 'online'
        # 考生登录
        payload = {
            'loginName': 'haitun2',
            'password': 'Test1234'
        }
        user = userProject(environment=environment_current)
        reStu = user.stuLogin(data=payload)
        stuTicket = reStu['ticket']

        # 获取统考成绩信息
        data = {"p": {}, "m": ""}
        datas = {
            "data": data,
            "ticket": stuTicket
        }
        zhiYuan = prob_project(environment=environment_current)
        reStu = zhiYuan.getUser(data=datas)
        self.stuInfo = reStu['datas']['obj']

        # 志愿管理员登录
        zhiLogin = {
            'loginName': 'zhiyuan',
            'password': 'Test1234'
        }
        zhiRe = user.stuLogin(data=zhiLogin)
        zhiTicket = zhiRe['ticket']

        # 省份分数线相关信息
        ScoreLine_data = {
            'dataYear': 2020,  # 年份
            'provinceId': 330000,  # 省份 330000=浙江省
            "ticket": zhiTicket
        }
        ScoreLine = zhiYuan.loadProvinceScoreLineData(data=ScoreLine_data)
        self.province_list = ScoreLine['datas']['page']['dataList'][0]

        # 统考计算公式信息
        loadJointScoreData = {
            'provinceID': 330000,  # 省份 330000=浙江省
            'schoolID': 10335,  # 学校ID
            'dataYear': 2020,  # 年份
            'ticket': zhiTicket
        }

        loadJointScoreData_re = zhiYuan.loadJointScoreExpressionData(data=loadJointScoreData)
        self.loadJointScore_list = loadJointScoreData_re['datas']['page']['dataList'][0]

        # 'enrollBasisType'：录取方式类型：1 - 综合分, 2 - 文化分, 3 - 专业分, 4 - 专业分排名, 5 - 英语成绩, 6 - 文化折算分
        self.enrollBasisType = self.loadJointScore_list['enrollBasisType']
        # 'archiveRule'：'投档规则：1-平行志愿 2-梯度志愿'
        self.archiveRule = self.loadJointScore_list['archiveRule']

        # 校考计算公式信息
        loadJointScoreData_school = {
            'provinceID': 330000,
            'schoolID': 10335,
            'dataYear': 2020,
            'ticket': zhiTicket
        }

        loadJointScoreData_school = zhiYuan.loadSchoolScoreExpressionData(data=loadJointScoreData_school)
        self.schoolExamScore_list = loadJointScoreData_school['datas']['page']['dataList'][0]

        # 'enrollBasisType'：录取方式类型 1-综合分 2-文化分 3-专业分 4-专业分排名
        self.enrollBasisType_school = self.schoolExamScore_list['enrollBasisType']

    ##判断考生是否过线
    def cross_line(self):

        """
            省分数线判断_统考合格线
            1：统考合格线---统考成绩

            省批次线_批次层次判断
            1:空  省批次表 (专业分数线--统考成绩、文化分数线--文化成绩、综合分数线---考生综合分 )
            2:本科 省分数表 ( 统考本科线---统考成绩、文化本科线---文化成绩 )
            3：专科  省分数表 ( 统考专科线 -- 统考成绩、文化专科线 ---文化成绩)
        """
        # 统考专业成绩
        stuUniformScore = self.stuInfo['jointExamScore']
        # 文化成绩
        stuCultureScore = self.stuInfo['collEntrExamScore']
        # 省综合分计算公式
        equation = self.loadJointScore_list['expression']
        ##浙江省统考合格线
        province_UniformScore = self.province_list['i']
        # 批次层次 batchLevel
        batchLevel = None
        # 考生综合分
        equation = equation.replace('R', str(stuCultureScore))
        equation = equation.replace('U', str(stuUniformScore))
        stuComprehensive_score = eval(equation)

        # 省批次表专业分数线
        # 省批次表文化分数线
        # 综合分数线

        # 考生是否过线 0 不过线, 1 过线
        stuCross_line_mark = 0

        if stuUniformScore >= province_UniformScore:
            print('该考生已过浙江省统考合格线')
            if batchLevel == '':
                # 省批次表专业分数线
                # 省批次表文化分数线
                # 综合分数线
                pass
            elif batchLevel == '本科':
                pass
            elif batchLevel == '专科':
                pass
        else:
            print('该考生分数未过省统考合格线')

    ##按位次计算概率
    def test_precedence(self):

        """
        'enrollBasisType'：录取方式类型：1-综合分 2-文化分 3-专业分 4-专业分排名 5-英语成绩 6-文化折算分
        archiveMode : 投档方式
        'archiveRule'：'投档规则：1-平行志愿 2-梯度志愿'
        'archiveRank' : 投档位次
        'expectArchiveRank' ：预计投档位次
        ATAN((考生位次-投档位次/预计投档位次)/投档位次/预计投档位次)*（-1）+p5)*100%
        """

        # 考生综合分位次：
        comprehensiveRank = self.stuInfo['comprehensiveRank']
        # 考生统考专业分位次：
        jointRank = self.stuInfo['jointRank']
        # archiveRank : 投档位次
        archiveRank = self.loadJointScore_list['archiveRank']
        # 预计投档位次
        expectArchiveRank = self.loadJointScore_list['expectArchiveRank']

        p5 = self.loadJointScore_list['p5']

        ##参与计算投档位次
        archiveRank_calculate = None
        # 参与计算考生位次
        stuPrecedence = None

        # 'archiveRule'：'投档规则：1-平行志愿 2-梯度志愿'
        if self.archiveRule == 1:
            # enrollBasisType = 1 录取方式类型 --->综合分(综合分位次)
            if self.enrollBasisType == 1:
                # p = ATAN((考生位次-投档位次/预计投档位次)/投档位次/预计投档位次)*（-1）+p5)*100%
                stuPrecedence = comprehensiveRank
                if archiveRank is not None:
                    archiveRank_calculate = archiveRank
                    p = math.atan((((stuPrecedence - archiveRank_calculate) / archiveRank_calculate) * -1)) + p5
                    print('按位次计算(综合分位次 %s + 投档位次 %s)概率为：' % (stuPrecedence, archiveRank_calculate),
                          '%.2f%%' % (p * 100))
                else:
                    archiveRank_calculate = expectArchiveRank
                    p = math.atan((((stuPrecedence - archiveRank_calculate) / archiveRank_calculate) * -1)) + p5
                    print('按位次计算(综合分位次 %s + 投档位次 %s)概率为：' % (stuPrecedence, archiveRank_calculate),
                          '%.2f%%' % (p * 100))

            # enrollBasisType 录取方式类型 ---> 2-文化分 3-专业分 4-专业分排名( 统考位次 )
            elif self.enrollBasisType == 2 or self.enrollBasisType == 3 or self.enrollBasisType == 4:
                stuPrecedence = jointRank
                if archiveRank is not None:
                    archiveRank_calculate = archiveRank
                    p = math.atan((((stuPrecedence - archiveRank_calculate) / archiveRank_calculate) * -1)) + p5
                    print('按位次计算(综合分位次 %s + 投档位次 %s)概率为：' % (stuPrecedence, archiveRank_calculate),
                          '%.2f%%' % (p * 100))
                else:
                    archiveRank_calculate = expectArchiveRank
                    p = math.atan((((stuPrecedence - archiveRank_calculate) / archiveRank_calculate) * -1)) + p5
                    print('按位次计算(综合分位次 %s + 投档位次 %s)概率为：' % (stuPrecedence, archiveRank_calculate),
                          '%.2f%%' % (p * 100))
        else:
            pass

    # 按分数计算( 统考 )
    def test_calculate_score(self):
        """
        enrollBasisType'：录取方式类型：1-综合分 2-文化分 3-专业分 4-专业分排名 5-英语成绩 6-文化折算分
        archiveMode : 投档方式
        """
        # 考生综合分计算公式
        equation = self.loadJointScore_list['expression']
        # 考生专业分--统考成绩
        jointExamScore = self.stuInfo['jointExamScore']
        # 考生文化成绩
        collEntrExamScore = self.stuInfo['collEntrExamScore']
        # 校考成绩
        schoolExam_score = None
        # 考生综合分--非校考
        equation = equation.replace('R', str(collEntrExamScore))
        equation = equation.replace('U', str(jointExamScore))
        stuComprehensive_score = eval(equation)

        # 投档方式
        archiveMode = self.loadJointScore_list['archiveMode']
        # p0概率计算基础值
        p0 = self.loadJointScore_list['p0']
        # 投档最低分
        archiveMinScore = self.loadJointScore_list['archiveMinScore']
        # 预计投档最低分
        preArchiveScoreMin = self.loadJointScore_list['preArchiveScoreMin']
        # 录取最低分
        entrolScoreMin = self.loadJointScore_list['entrolScoreMin']
        # 预计录取最低分
        preEnrollScoreMin = self.loadJointScore_list['preEnrollScoreMin']

        ##参与计算考生分数
        stu_score = None
        # 参与计算投档分
        archive_score = None

        # 平行志愿计算
        if self.archiveRule == 1:
            # 投档方式==1 综合分,考生分数=综合分
            if archiveMode == 1:
                # 考生分数等于综合分
                stu_score = stuComprehensive_score
                if archiveMinScore is not None:
                    # 投档分=archiveMinScore
                    archive_score = archiveMinScore
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分%s +投档最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
                elif preArchiveScoreMin is not None:
                    # 投档分=preArchiveScoreMin
                    archive_score = preArchiveScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分%s +预计投档最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
                elif entrolScoreMin is not None:
                    # 投档分=entrolScoreMin
                    archive_score = entrolScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分%s +录取最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
                elif preEnrollScoreMin is not None:
                    # 投档分=preEnrollScoreMin
                    archive_score = preEnrollScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分%s +预计录取最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
            # 投档方式==3 专业分,考生分数=专业分(统考成绩)
            elif archiveMode == 3:
                stu_score = jointExamScore
                if archiveMinScore is not None:
                    # 投档分=archiveMinScore
                    archive_score = archiveMinScore
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分%s +投档最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
                elif preArchiveScoreMin is not None:
                    # 投档分=preArchiveScoreMin
                    archive_score = preArchiveScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分%s +预计投档最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
                elif archiveMinScore is not None:
                    # 投档分=entrolScoreMin
                    archive_score = entrolScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分%s +录取最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
                elif preArchiveScoreMin is not None:
                    # 投档分=preEnrollScoreMin
                    archive_score = preEnrollScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分%s +预计录取最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
            else:
                pass
        # 梯度志愿计算
        elif self.archiveRule == 2:
            # 投档方式==1 综合分,考生分数=综合分
            if archiveMode == 1:
                # 考生分数等于综合分
                stu_score = stuComprehensive_score
                if archiveMinScore is not None:
                    # 投档分=archiveMinScore
                    archive_score = archiveMinScore
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分+投档最低分)概率为：', '%.3f%%' % (p * 100))
                elif preArchiveScoreMin is not None:
                    # 投档分=preArchiveScoreMin
                    archive_score = preArchiveScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分+预计投档最低分)概率为：', '%.3f%%' % (p * 100))
                elif archiveMinScore is not None:
                    # 投档分=entrolScoreMin
                    archive_score = entrolScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分+录取最低分)概率为：', '%.3f%%' % (p * 100))
                elif preArchiveScoreMin is not None:
                    # 投档分=preEnrollScoreMin
                    archive_score = preEnrollScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分+预计录取最低分)概率为：', '%.3f%%' % (p * 100))
            # 投档方式==3 专业分,考生分数=专业分(统考成绩)
            elif archiveMode == 3:
                stu_score = jointExamScore
                if archiveMinScore is not None:
                    # 投档分=archiveMinScore
                    archive_score = archiveMinScore
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分+投档最低分)概率为：', '%.3f%%' % (p * 100))
                elif preArchiveScoreMin is not None:
                    # 投档分=preArchiveScoreMin
                    archive_score = preArchiveScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分+预计投档最低分)概率为：', '%.3f%%' % (p * 100))
                elif archiveMinScore is not None:
                    # 投档分=entrolScoreMin
                    archive_score = entrolScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分+录取最低分)概率为：', '%.3f%%' % (p * 100))
                elif preArchiveScoreMin is not None:
                    # 投档分=preEnrollScoreMin
                    archive_score = preEnrollScoreMin
                    p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                    print('统考按分数计算(综合分+预计录取最低分)概率为：', '%.3f%%' % (p * 100))
            else:
                pass

    # 按分数计算( 校考 )
    def test_schoolExam_score(self, schoolExam_score=''):
        """
        enrollBasisType'：录取方式类型：1-综合分 2-文化分 3-专业分 4-专业分排名 5-英语成绩 6-文化折算分
        schoolExam_score：var 考生校考成绩

        """
        # 考生综合分计算公式
        equation = self.schoolExamScore_list['expression']
        # 考生专业分--统考成绩
        jointExamScore = self.stuInfo['jointExamScore']
        # 考生文化成绩
        collEntrExamScore = self.stuInfo['collEntrExamScore']
        # 校考成绩
        # 考生综合分--校考
        equation = equation.replace('R', str(collEntrExamScore))
        equation = equation.replace('T', str(schoolExam_score))
        stuComprehensive_score = eval(equation)

        # # 投档方式
        # archiveMode = self.schoolExamScore_list['archiveMode']
        # p0概率计算基础值
        p0 = self.schoolExamScore_list['p0']
        # 投档最低分
        archiveMinScore = self.schoolExamScore_list['archiveMinScore']
        # 预计投档最低分
        preArchiveScoreMin = self.schoolExamScore_list['preArchiveScoreMin']
        # 录取最低分
        entrolScoreMin = self.schoolExamScore_list['entrolScoreMin']
        # 预计录取最低分
        preEnrollScoreMin = self.schoolExamScore_list['preEnrollScoreMin']

        ##参与计算考生分数
        stu_score = None
        # 参与计算投档分
        archive_score = None

        # 平行志愿计算
        if self.archiveRule == 1:
            # 考生分数等于综合分
            stu_score = stuComprehensive_score
            if archiveMinScore is not None:
                # 投档分=archiveMinScore
                archive_score = archiveMinScore
                p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                print('校考按分数计算(综合分%s +投档最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
            elif preArchiveScoreMin is not None:
                # 投档分=preArchiveScoreMin
                archive_score = preArchiveScoreMin
                p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                print('校考按分数计算(综合分%s +预计投档最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
            elif entrolScoreMin is not None:
                # 投档分=entrolScoreMin
                archive_score = entrolScoreMin
                p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                print('校考按分数计算(综合分%s +录取最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))
            elif preEnrollScoreMin is not None:
                # 投档分=preEnrollScoreMin
                archive_score = preEnrollScoreMin
                p = math.atan(((stu_score - archive_score) / archive_score) * 5.1) + p0
                print('校考按分数计算(综合分%s +预计录取最低分%s)概率为：' % (stu_score, archive_score), '%.3f%%' % (p * 100))


if __name__ == "__main__":
    run = prob()
    # 按位次计算
    run.test_precedence()
    # 按分数计算
    run.test_calculate_score()
    # 按分数计算-校考
    run.test_schoolExam_score(150)
