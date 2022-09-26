import requests
import json
import time
import re
import urllib.parse
import requests.packages.urllib3.util.ssl_

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

# 配置信息
# 操作的百度云目录
dir = '/IT四叶草铺/无密/2022/00. Web3.0/01. 开课吧-Web3.0应用工程师培养计划 (2022)【完结】'

# 是否urlencode都可以
# dir = '/六级真题/2018年12月CET6/第二套'

# BDTOKEN可在请求的params中找到
BDTOKEN = '4af7a376b2088977389cd0c153b5a96c'
# COOKIE可在请求的headers中找到
COOKIE = 'BIDUPSID=0546069CE7CAE87ECF84DE59FAA9D38D; PSTM=1663921263; BAIDUID=0033F420D1A8C3B632215D7E2D739017:FG=1; PANWEB=1; BDUSS=2gwR2RJbmlWcHJDdFJvZVFZZ3lGNEV4RUFjcXpKMWltREZLWH5Ca0lhSlVlRmRqRVFBQUFBJCQAAAAAAAAAAAEAAAAeQKxRR0xfSVQwMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFTrL2NU6y9jc; BDUSS_BFESS=2gwR2RJbmlWcHJDdFJvZVFZZ3lGNEV4RUFjcXpKMWltREZLWH5Ca0lhSlVlRmRqRVFBQUFBJCQAAAAAAAAAAAEAAAAeQKxRR0xfSVQwMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFTrL2NU6y9jc; STOKEN=597ced8ec19a40460e45e763233aa2ee2d7f15af38a97675f4e27f1af1631a60; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; newlogin=1; BDCLND=UPuaym%2BaatZ98SLuOuGvVJYTa3UsqSi6WsOyNUP6LEM%3D; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1664122160,1664123001,1664123095,1664170014; BA_HECTOR=05ah0h0l0585a02g2g2kksv71hj2e5q19; ZFY=7xDnnWNc0XWyk3aLbvZPr031b0hroDP4455qgEzLxYY:C; BAIDUID_BFESS=0033F420D1A8C3B632215D7E2D739017:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; H_PS_PSSID=37151_36551_37353_36884_34813_37398_36789_26350_37447_37370; BCLID=11459154974005623525; BCLID_BFESS=11459154974005623525; BDSFRCVID=3P-OJexroG0GUFJj-tdIhFCegSNbUdrTDYrEjGc3VtzSGYLVJeC6EG0Pts1-dEu-EHtdogKK0mOTHUFF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=3P-OJexroG0GUFJj-tdIhFCegSNbUdrTDYrEjGc3VtzSGYLVJeC6EG0Pts1-dEu-EHtdogKK0mOTHUFF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3j3Ru8KJjEe-Kk-PnVeTtrqtnZKRvHa2kjKM5IWJFVfbbVMMjTbt-9Xx5PKnjn3N5HKRcTKKO4f-cbQprd3xI8LNj405OTbTADsRbNb66pO-bghPJvyT8DXnO7Lx5lXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVJO-KKChhK84Dx5; H_BDCLCKID_SF_BFESS=tR3j3Ru8KJjEe-Kk-PnVeTtrqtnZKRvHa2kjKM5IWJFVfbbVMMjTbt-9Xx5PKnjn3N5HKRcTKKO4f-cbQprd3xI8LNj405OTbTADsRbNb66pO-bghPJvyT8DXnO7Lx5lXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVJO-KKChhK84Dx5; csrfToken=P_-WdmeUrsDH2Brz6OcB5jGT; PANPSC=13074101914356253531%3AKkwrx6t0uHDk5nS%2BPCsmXBGy4OU887ORNZsHake%2BdxHPzW21GgvS0EpDgNqxv39mho6zf1%2FwxMyvp3VH96pEq2Ke%2Bz%2FOz%2Byx22GSUmHHokmAxdLlYpQggL2A8Uov%2BABbQkXoyNMc021LKfmh%2FJ4BvDGuaZCjAuzWYqZdy9zZ13mvYk3Uwegp7gGrhGW28jstklTmKGuh8uMkMIAFv2dYZOtuQFScyIV%2F; ndut_fmt=6BE384BF472A483716CFA7D5FE9FEF9A8FE8F31C2AE2F5CAD2F5BC735204E120; ab_sr=1.0.1_YjEwNWMyMjFmMWM1ODM0YzU1Njg5MjNiZjcyZjNmZTU0YzA2OGFiNjQ3YzEzZTUyMzQzNDk5NWI1MTcxN2Q0ZDFlZmE3N2ZhZjEyZTlmMTIxZjkxMDQzZjM0OTEyNTZlY2RmMzNjYjAxMWM1ZDhiYWE5ODI4MGYyOTBjMzE4MmM1ODhkOTIzM2JkZjNhM2Q0NDdjN2Q4NThlZmVmNWRiZg=='
# PATTERN和REPLACE分别为要替换的字符和替换成的字符
PATTERN = '666java'
REPLACE = 'it4clover'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': COOKIE,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}


def list_name_desc(dir):
    """
        查询指定dir的文件,以列表方式返回文件信息
        input - dir
        return - file_info_list
    """
    dir = urllib.parse.unquote(dir)
    apilist_url = 'https://pan.baidu.com/api/list'
    params = {
        'dir': dir,
    }
    response = requests.get(apilist_url, params=params, headers=headers)
    response.raise_for_status()
    if response.json()['errno'] == 0:
        file_list = response.json()['list']
        file_info_list = []
        for file in file_list:
            server_filename = file['server_filename']
            isdir = file['isdir']
            path = file['path']
            if 'dir_empty' in file.keys():
                dir_empty = file['dir_empty']
            else:
                dir_empty = 0
            each_file_info = {
                'server_filename': server_filename,
                'isdir': isdir,
                'path': path,
                'dir_empty': dir_empty
            }
            file_info_list.append(each_file_info)
        return file_info_list


def baiduyun_rename(rename_list):
    '''
        按rename_list向接口https://pan.baidu.com/api/filemanager发送重命名请求
        input - rename_list
        print - result
        rename_list格式[{"path":PATH,"newname":NEWNAME},{"path":PATH,"newname":NEWNAME},]
        特别注意用rename_list构造post请求的data时，rename_list需要json.dumps转成字符串
    '''
    try_max = 5
    try_count = 0
    params = {
        'opera': 'rename',
        'async': '2',
        'onnest': 'fail',
        'web': '1',
        'app_id': '250528',
        'bdstoken': BDTOKEN,
        # 'logid':get_logid() ,
        'clienttype': '0',
    }
    if not rename_list == []:
        # ensure_ascii=False 加不加都可以，但key "filelist" 对应的 value 必须用json.dumps()转成字符串类型
        data = {"filelist": json.dumps(rename_list, ensure_ascii=False)}
        url = 'https://pan.baidu.com/api/filemanager'
        response = requests.post(url, params=params, data=data, headers=headers)
        response.raise_for_status()
        errno = response.json()['errno']
        if errno == 0:
            print('[info] : rename successfully!')
        elif errno == 12:
            print('[warning]: 批量处理错误，5s后重试')
            try_count += 1
            if try_count <= try_max:
                time.sleep(5)
                baiduyun_rename(rename_list)
            else:
                print('[error] : 批量处理错误且达到最大重试上限')
        else:
            print(response.json())
    else:
        pass
        # print('[error] : rename_list is empty')


def rename_file_in_dir(dir, renameDirChildren=True):
    """
        调用函数list_name_desc(dir)查询
        调用函数baiduyun_rename(rename_list)重命名
        renameDirChildren=True 如果为文件夹将会迭代，即按相同的规则重命名文件夹中的文件

    """
    file_info_list = list_name_desc(dir)
    rename_list = []
    for each in file_info_list:
        if each['isdir'] == 0:
            old_name = each['server_filename']
            new_name = create_new_name(old_name=old_name, pattern=PATTERN, replace=REPLACE)
            rename_dict = {
                'path': each['path'],
                'newname': new_name,
            }
            if new_name != old_name:
                rename_list.append(rename_dict)
        if renameDirChildren and each['isdir'] == 1 and each['dir_empty'] == 0:
            time.sleep(2)
            rename_file_in_dir(each['path'], renameDirChildren=True)
    baiduyun_rename(rename_list)


def create_new_name(old_name, prefix=None, extension_name=None, pattern=None, replace=None):
    # old_name必要参数
    # prefix 用于添加前缀
    # extension_name 用于改扩展名
    # pattern和replace 用于正则替换
    '''
    old_name = 'mytest.doc'
    # 添加前缀test
    newname1 = create_new_name(old_name,prefix='test')
    # 改扩展名为pdf
    newname1 = create_new_name(old_name,extension_name='pdf')
    # 正则替换 test 改为 aemon
    newname2 = create_new_name(old_name,pattern='test',replace='aemon')
    '''
    new_name = ''
    if old_name:
        if prefix:
            new_name = prefix + old_name
        elif extension_name:
            new_name = old_name[:-3] + extension_name
        elif pattern:
            new_name = re.sub(pattern, replace, old_name, re.S)
        if not new_name == '':
            return new_name
        else:
            raise Exception('create_new_name error')
    else:
        raise Exception('old_name 缺失')


if __name__ == "__main__":
    # for file in list_name_desc(dir):
    #     print(file)
    # renameDirChildren=True 如果为文件夹将会迭代，即按相同的规则重命名文件夹中的文件
    rename_file_in_dir(dir, renameDirChildren=True)
    print('All Rename Successfully!')
