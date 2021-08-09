import yaml
import math
from speedtest import Speedtest
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from win10toast import ToastNotifier

def job():
    helper = Speedtest()

    helper.get_best_server()
    helper.download()
    helper.upload()

    result = helper.results.dict()

    download = float(result.get('download'))
    upload = float(result.get('upload'))
    f = open('./config.yml', 'r')

    data = yaml.load(f.read(), Loader=yaml.FullLoader)
    originalspeed = data.get('originalSpeed')

    mbdownload = math.floor(download / 1e+6)
    mbupload = math.floor(upload / 1e+6)

    timestr = time.strftime('%c', time.localtime(time.time()))
    
    if download < (originalspeed / 4) or upload < (originalspeed / 4):
        print(f'[{timestr}] 다운로드: {mbdownload}Mbps 업로드: {mbupload}Mbps 아니 25%도 안나온다고요 ㅁㅊ')
        ToastNotifier().show_toast("아니 속도 25% 미만이라구요!", f"다운로드 : {mbdownload}Mbps, 업로드: {mbupload}Mbps")
    else:
        print(f'[{timestr}] 다운로드: {mbdownload}Mbps 업로드: {mbupload}Mbps')
    f.close()


scheduler = BlockingScheduler()

scheduler.add_job(job, 'interval', minutes=5)
scheduler.start()
