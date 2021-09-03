import requests
import time

class my_hhu:
    account = "1806030126"  # 学号
    wid = "A335B048C8456F75E0538101600A6A04"  # 个人wid
    daka_save_url = "http://form.hhu.edu.cn/pdc/formDesignApi/dataFormSave?wid="+ wid + "&userId=" + account

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4209.2 Safari/537.36'
        }
        self.session = requests.Session()


    def daka(self):
        while True:
            curr_date = time.strftime('%Y/%m/%d', time.localtime(time.time()))
            post_data = {
                'DATETIME_CYCLE': curr_date,
                'XGH_336526': self.account,
                'XM_1474': '李佳鹏',  # 姓名
                'SFZJH_859173': '320721199904082017',  # 身份证号
                'SELECT_941320': '计信院',  # 学院
                'SELECT_459666': '2018级',  # 年级
                'SELECT_814855': '电信',  # 专业
                'SELECT_525884': '电信18_1',  # 班级
                'SELECT_125597': '江宁校区教学区12舍',  # 宿舍楼
                'TEXT_950231': '312',  # 宿舍号
                'TEXT_937296': '15850658969',  # 手机号码
                'RADIO_853789': '否',
                'RADIO_43840': '否',
                'RADIO_579935': '健康',
                'RADIO_138407': '是',
                'RADIO_546905': '否',
                'RADIO_314799': '否',
                'RADIO_209256': '否',
                'RADIO_836972': '否',
                'RADIO_302717': '否',
                'RADIO_701131': '否',
                'RADIO_438985': '否',
                'RADIO_467360': '是',
                'PICKER_956186': '江苏省,南京市,江宁区',
                'TEXT_434598': "",
                'TEXT_515297': "",
                'TEXT_752063': "",
            }
            dakaResponse = self.session.post(self.daka_save_url, data=post_data, headers=self.headers)
            if '{"result":true}' in dakaResponse.text:
                print("打卡成功！")
                break
            else:
                time.sleep(0.5)


if __name__ == '__main__':
    user = my_hhu()
    user.daka()

