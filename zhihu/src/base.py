#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        爬取知乎需要的静态规则信息。
        站点特征信息。
        By Yanxingfei(1139),2016.08.10
"""

import re

Default_Header = {  # 不包含cookie的请求头的内容。user-agent和referer是必须自定义的
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Referer': 'https://www.zhihu.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

Data_Header = {  # 用于请求数据信息
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': '*/*',
    'Content-Length': '217',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Referer': 'https://www.zhihu.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

# 知乎主站相关链接
Zhihu_URL = 'https://www.zhihu.com' # 域名
Zhihu_Login_Email = 'https://www.zhihu.com/login/email'
Zhihu_Login_Phone = 'https://www.zhihu.com/login/phone_num'
Captcha_URL = Zhihu_URL + '/captcha.gif' # 验证码地址
Me_Id = 'huang-cun-mi-wu' # 我的个性域名
People_Id = ''
Column_Id = ''
Post_Id = ''
Roundtable_Id = ''
Topic_Id = ''
Question_Id = ''  # 问题id
Answer_Id = ''


# 网址解析
re_phone_num_pattern = re.compile(r'^1\d{10}$')  # 匹配手机号
re_group_url = re.compile(r'')
re_topic_url = re.compile(r'')
re_author_url = re.compile(r'')

# 知乎网站内容模型
Zhihu_Model = {
    'Me': {  # 个人信息
        'settings': {  # 设置
            'profile': {  # 基本资料
                'url': 'https://www.zhihu.com/settings/profile',
                'domain': Me_Id,  # 个性域名
            },
            'account': {  # 账号和密码
                'url': 'https://www.zhihu.com/settings/account',
            },
            'notification': {  # 消息和邮件
                'url': 'https://www.zhihu.com/settings/notification',
            },
            'filter': {  # 屏蔽
                'url': 'https://www.zhihu.com/settings/filter',
            },
        },
        'inbox': {  # 私信
            'url': 'https://www.zhihu.com/inbox',
        },
        'index': {  # 我的主页
            'activities': {  # 动态
                'url': 'https://www.zhihu.com/people/' + Me_Id + '/activities',
            },
            'answers': {  # 回答
                'url': 'https://www.zhihu.com/people/' + Me_Id + '/answers',
            },
            'pins': {  # 分享
                'url': 'https://www.zhihu.com/people/' + Me_Id + '/pins',
            },
            'asks': {  # 提问
                'url': 'https://www.zhihu.com/people/' + Me_Id + '/asks',
            },
            'collections': {  # 收藏
                'url': 'https://www.zhihu.com/people/' + Me_Id + '/collections',
            },
            'following': {  # 关注了
                'url': 'https://www.zhihu.com/people/' + Me_Id + '/following',  # 关注的人
                'topics': {  # 关注的话题
                    'url': 'https://www.zhihu.com/people/' + Me_Id + '/following/topics',
                },
                'columns': {  # 关注的专栏
                    'url': 'https://www.zhihu.com/people/' + Me_Id + '/following/columns',
                },
                'questions': {  # 关注的问题
                    'url': 'https://www.zhihu.com/people/' + Me_Id + '/following/questions',
                },
                'collections': {  # 关注的收藏
                    'url': 'https://www.zhihu.com/people/' + Me_Id + '/following/collections',
                },
            },
            'followers': {  # 关注者
                'url': 'https://www.zhihu.com/people/' + Me_Id + '/followers',
            },
        },
    },
    'Peoples': {  # 知乎所有用户。目标：1.获取最受欢迎的用户。2.获取带有特定标签、关注特定领域的用户
        'url': 'https://www.zhihu.com/people',
    },
    'People': {  # 一个具体用户。
        'url': 'https://www.zhihu.com/people/' + People_Id,
    },
    'Roundtables': {  # 知乎圆桌所有活动。
        'url': 'https://www.zhihu.com/roundtable',
    },
    'Roundtable': {  # 一个具体活动。
        'url': 'https://www.zhihu.com/roundtable/' + Roundtable_Id,
    },
    'Columns': {  # 知乎专栏作者列表和文章列表。
        'url': 'https://zhuanlan.zhihu.com',
    },
    'Column': {  # 专栏里一个具体作者。
        'url': 'https://zhuanlan.zhihu.com/' + Column_Id,
    },
    'Post': {  # 专栏里一个具体文章。
        'url': 'https://zhuanlan.zhihu.com/' + Post_Id,
    },
    'Topics': {  # 话题广场所有话题。
        'url': 'https://www.zhihu.com/topics',
    },
    'Topic': {  # 一个具体话题。
        'url': 'https://www.zhihu.com/topic/' + Topic_Id,
    },
    'Questions': {  # 所有问题。目标：
        'url': 'https://www.zhihu.com/question',
    },
    'Question': {  # 一个具体问题。
        'url': 'https://www.zhihu.com/question' + Question_Id,
    },
    'Answers': {  # 一个问题下的所有回答。
        'url': 'https://www.zhihu.com/question/' + Question_Id + 'answer',
    },
    'Answer': {  # 一个具体回答。
        'url': 'https://www.zhihu.com/question/' + Question_Id + 'answer/' + Answer_Id,
    },
}
