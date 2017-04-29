#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        知乎数据分析主程序。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os  # 系统命令
import sys  # python设置
import shutil  # 高级文件操作
import timeit  # 计时相关
from datetime import datetime  # 日期时间

sys.path.append(os.getcwd())  # 添加工程根目录(datamining_py3_yxf)到path环境变量

# module
import zhihu.src.base as base
import zhihu.src.client as client
import zhihu.src.spider as spider
import zhihu.src.show as show


def test_question(url):
    # 给出一个特定的问题
    question = spider.Question(url)
    print(question.id)
    print(question.url)
    print(question.title)
    print(question.details)
    # print(question.answer_num)
    # print(question.follower_num)
    # print(question.viewed_num)
    # print(question.topics)
    # for _, follower in zip(range(10), question.followers):
    #     print(follower.name)
    # # 获取排名第一的回答的点赞数
    # print(question.top_answer.upvote_num)
    # # 197
    #
    # # 获取排名前十的十个回答的点赞数
    # for answer in question.top_i_answers(10):
    #     print(answer.people.name, answer.upvote_num, answer.people.motto)
    # # 获取提问时间
    # ctime = question.creation_time
    # print(ctime)
    # assert ctime == datetime.strptime('2014-08-12 17:58:07', "%Y-%m-%d %H:%M:%S")
    #
    # # 获取最后编辑时间
    # last_edit_time = question.last_edit_time
    # print(last_edit_time)
    # assert last_edit_time >= datetime.strptime('2015-04-01 00:39:21', "%Y-%m-%d %H:%M:%S")
    #
    # # 获取提问者
    # assert question.people is spider.ANONYMOUS  # 匿名用户
    # question = spider.Question('https://www.zhihu.com/question/38531356')
    # assert question.people.name == '杨捷'
    # assert question.people.url == 'https://www.zhihu.com/people/yangjiePro/'
    question.save()


def test_answer():
#     url = 'http://www.zhihu.com/question/24825703/answer/30975949'
#     answer = client.answer(url)
#
#     assert answer.deleted is False
#
#     # 获取答案url
#     print(answer.url)
#
#     # 获取该答案所在问题标题
#     print(answer.question.title)
#     # 关系亲密的人之间要说「谢谢」吗？
#
#     # 获取该答案作者名
#     print(answer.people.name)
#     # 甜阁下
#
#     # 获取答案赞同数
#     print(answer.upvote_num)
#     # 1155
#
#     # 获取答案点赞人昵称和感谢赞同提问回答数
#     for _, upvoter in zip(range(10), answer.upvoters):
#         print(upvoter.name, upvoter.upvote_num, upvoter.thank_num,
#               upvoter.question_num, upvoter.answer_num, upvoter.is_zero_user())
#     # ...
#     # 五月 42 15 3 35
#     # 陈半边 6311 1037 3 101
#     # 刘柯 3107 969 273 36
#     #
#     # 三零用户比例 36.364%
#
#     print(answer.comment_num)
#     assert answer.comment_num >= 161
#
#     # 获取答案下的评论
#     for i, comment in enumerate(answer.comments, 1):
#         if i == 1:
#             assert comment.creation_time == datetime(2014, 9, 25, 9, 18, 56)
#         if i < 11:
#             print(comment.people.name, comment.content)
#
#     assert i >= 161
#
#     for i, comment in enumerate(answer.latest_comments, 1):
#         if i == 1:
#             assert comment.creation_time >= datetime(2015, 9, 21, 19, 50, 42)
#         if i < 11:
#             print(comment.people.name, comment.content)
#
#     assert comment.creation_time == datetime(2014, 9, 25, 9, 18, 56)
#     assert i >= 161
#
#     # 获取答案内容的HTML
#     print(answer.content)
#     # <html>
#     # ...
#     # </html>
#
#     # 获取答案创建时间
#     print(answer.creation_time)
#     assert answer.creation_time == datetime.fromtimestamp(1411567255)
#
#     # 获取答案收藏数量
#     print(answer.collect_num)
#     assert answer.collect_num >= 821
#
#     # 获取收藏答案的收藏夹
#     for _, collection in zip(range(10), answer.collections):
#         print(collection.url, collection.name, collection.owner,
#               collection.follower_num)
#
#     # 保存HTML
#     answer.save(filepath='.')
#     # 当前目录下生成 "亲密关系之间要说「谢谢」吗？ - 甜阁下.html"
#
#     # 保存markdown
#     answer.save(filepath='.', mode="md")
#     # 当前目录下生成 "亲密关系之间要说「谢谢」吗？ - 甜阁下.md"
#
#     answer.refresh()
#
#     # test again
#     print(answer.upvote_num)
#     print(answer.content)
#     print(answer.collect_num)
#     print(answer.comment_num)
#     assert answer.deleted is False
#
#     # test deleted answer
#     url = 'https://www.zhihu.com/question/40185501/answer/85271078'
#     answer = client.answer(url)
#     assert answer.deleted is True
#     answer.refresh()
#     assert answer.deleted is True
#
#     # test answer without collection
#     url = 'https://www.zhihu.com/question/23138285/answer/81246171'
#     answer = client.answer(url)
#     assert answer.collect_num == 0
#     assert sum(1 for _ in answer.collections) == 0
#
#     # test zero comment answer
#     url = 'https://www.zhihu.com/question/39051779/answer/81575803'
#     answer = client.answer(url)
#     assert sum(1 for _ in answer.comments) == 0
#     assert sum(1 for _ in answer.latest_comments) == 0
#
#     # test single page comment answer
#     url = 'https://www.zhihu.com/question/28399220/answer/79799671'
#     answer = client.answer(url)
#     assert 0 < sum(1 for _ in answer.comments) < 30
    pass


def test_people():
#     url = 'http://www.zhihu.com/people/7sdream'
#     people = client.people(url)
#
#     # 获取用户动态
#     for _, act in zip(range(30), people.activities):
#         print(act.content.url)
#         if act.type == base.ActType.FOLLOW_COLUMN:
#             print('%s 在 %s 关注了专栏 %s' %
#                   (people.name, act.time, act.column.name))
#         elif act.type == base.ActType.FOLLOW_QUESTION:
#             print('%s 在 %s 关注了问题 %s' %
#                   (people.name, act.time, act.question.title))
#         elif act.type == base.ActType.ASK_QUESTION:
#             print('%s 在 %s 提了个问题 %s' %
#                   (people.name, act.time, act.question.title))
#         elif act.type == base.ActType.UPVOTE_POST:
#             print('%s 在 %s 赞同了专栏 %s 中 %s 的文章 %s, '
#                   '此文章赞同数 %d, 评论数 %d' %
#                   (people.name, act.time, act.post.column.name,
#                    act.post.people.name, act.post.title, act.post.upvote_num,
#                    act.post.comment_num))
#         elif act.type == base.ActType.PUBLISH_POST:
#             print('%s 在 %s 在专栏 %s 中发布了文章 %s, '
#                   '此文章赞同数 %d, 评论数 %d' %
#                   (people.name, act.time, act.post.column.name,
#                    act.post.title, act.post.upvote_num,
#                    act.post.comment_num))
#         elif act.type == base.ActType.UPVOTE_ANSWER:
#             print('%s 在 %s 赞同了问题 %s 中 %s(motto: %s) 的回答, '
#                   '此回答赞同数 %d' %
#                   (people.name, act.time, act.answer.question.title,
#                    act.answer.people.name, act.answer.people.motto,
#                    act.answer.upvote_num))
#         elif act.type == base.ActType.ANSWER_QUESTION:
#             print('%s 在 %s 回答了问题 %s 此回答赞同数 %d' %
#                   (people.name, act.time, act.answer.question.title,
#                    act.answer.upvote_num))
#         elif act.type == base.ActType.FOLLOW_TOPIC:
#             print('%s 在 %s 关注了话题 %s' %
#                   (people.name, act.time, act.topic.name))
#         elif act.type == base.ActType.FOLLOW_COLLECTION:
#             print('%s 在 %s 关注了收藏夹 %s' %
#                   (people.name, act.time, act.collection.name))
#
#     # 获取用户名称
#     print(people.name)
#     # 7sDream
#
#     # 获取用户介绍
#     print(people.motto)
#     # 二次元新居民/软件爱好者/零回答消灭者
#
#     # 获取用户头像地址
#     print(people.photo_url)
#     # http://pic3.zhimg.com/893fd554c8aa57196d5ab98530ef479a_r.jpg
#
#     # 获取用户得到赞同数
#     print(people.upvote_num)
#     # 1338
#
#     # 获取用户得到感谢数
#     print(people.thank_num)
#     # 468
#
#     # 获取用户关注人数
#     print(people.followee_num)
#     # 82
#
#     # 获取用户关注人
#     for _, followee in zip(range(10), people.followees):
#         print(followee.name)
#     # yuwei
#     # falling
#     # 伍声
#     # bhuztez
#     # 段晓晨
#     # 冯东
#     # ...
#
#     # 获取用户粉丝数
#     print(people.follower_num)
#     # 303
#
#     # 获得用户粉丝
#     for _, follower in zip(range(10), people.followers):
#         print(follower.name)
#     # yuwei
#     # falling
#     # 周非
#     # 陈泓瑾
#     # O1Operator
#     # ...
#
#     # 获取用户提问数
#     print(people.question_num)
#     # 16
#
#     # 获取用户所有提问的标题
#     for _, question in zip(range(10), people.questions):
#         print(question.title)
#     # 用户「松阳先生」的主页出了什么问题？
#     # C++运算符重载在头文件中应该如何定义？
#     # 亚马逊应用市场的应用都是正版的吗？
#     # ...
#
#     # 获取用户答题数
#     print(people.answer_num)
#     # 247
#
#     # 获取用户所有回答
#     for _, answer in zip(range(10), people.answers):
#         print(answer.upvote_num)
#     # 0
#     # 5
#     # 12
#     # 0
#     # ...
#
#     # 获取用户微博
#     print(people.weibo_url)
#
#     # 获取用户行业
#     print(people.business)
#
#     # 获取用户所在地
#     print(people.location)
#
#     # 获取用户教育情况
#     print(people.education)
#
#     # 获取用户性别
#     print(people.gender)
#
#     # 获取用户最后一次活跃时间
#     print(people.last_activity_time)
#
#     # 获取用户文章数
#     print(people.post_num)
#     # 7
#
#     # 获取用户专栏名
#     for column in people.columns:
#         print(column.name)
#     # 科学の禁书目录
#
#     # 获取用户收藏夹数
#     print(people.collection_num)
#     # 3
#
#     # 获取用户收藏夹名
#     for collection in people.collections:
#         print(collection.name)
#     # 教学精品。
#     # 可以留着慢慢看～
#     # OwO
#     # 一句。
#     # Read it later
#
#     # 获取用户关注专栏数
#     print(people.followed_column_num)
#     # 9
#
#     # 获取用户关注的专栏
#     for column in people.followed_columns:
#         print(column.name, column.url, column.follower_num)
#     # 黑客与画家 http://zhuanlan.zhihu.com/hacker-and-painter/ 9743
#     # piapia安全 http://zhuanlan.zhihu.com/ppsec/ 566
#     # Android 科学院 http://zhuanlan.zhihu.com/andlib/ 4347
#     # ...
#
#     # 获取用户关注的话题数
#     print(people.followed_topic_num)
#     # 30
#
#     # 获取用户关注的话题
#     for topic in people.followed_topics:
#         print(topic.name, topic.url)
#         # Python http://www.zhihu.com/topic/19552832/
#         # 计算机 http://www.zhihu.com/topic/19555547/
#         # 生活 http://www.zhihu.com/topic/19551147/
    pass


def test_topics():
    topics = spider.Topics()
    topics.go()


def test():
    test_question("https://www.zhihu.com/question/21373902")
    test_topics()  # 从某个节点处向下遍历
    # test_answer()
    # test_collection()
    # test_column()
    # test_topic()
    # test_questions()
    # test_answers()
    # test_peoples()
    # test_collections()
    # test_columns()
    # test_people()

if __name__ == '__main__':
    print("===== init directory =====")
    BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data')  # 基础路径为data目录
    print("Base dir: ", BASE_DIR)
    os.chdir(BASE_DIR)  # 进入基础路径
    TEST_DIR = os.path.join(BASE_DIR, 'test')  # 测试路径
    print("Test dir: ", TEST_DIR)
    if os.path.exists(TEST_DIR):  # 如果已存在测试路径，就清除
        print("Cleaning...", end='')
        # shutil.rmtree(TEST_DIR)  # 清除test目录下所有的文件和目录
        # os.mkdir(TEST_DIR)
        print("Done")
    else:
        os.mkdir(TEST_DIR)

    print("===== init client =====")
    # client.start_client()  # 判断是否登录，最终返回结果是已登录并加载cookies
    # client.check_login()
    os.chdir(TEST_DIR)
    print("Done")

    print("===== test start =====")
    try:  # 调用test()进入测试，直到测试完成
        time = timeit.timeit('test()', setup='from __main__ import test', number=1)
        print('===== test passed =====')
        print('time used: {0} s'.format(time))  # 计时
    except Exception as e:
        print('===== test failed =====')
        raise e
        pass
    finally:
        print("Done")

    print("===== exit client =====")
    os.chdir(BASE_DIR)
    input("按Enter键退出")
    client.exit_client()
    print("Done")
