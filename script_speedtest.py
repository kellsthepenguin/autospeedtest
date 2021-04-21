import yaml
import math
from speedtest import Speedtest
from apscheduler.schedulers.blocking import BlockingScheduler


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
    originalSpeed = data.get('originalSpeed')

    mbDownload = math.floor(download / 1e+6)
    mbUpload = math.floor(upload / 1e+6)

    if download < (originalSpeed / 4) or upload < (originalSpeed / 4):
        print(f'다운로드: {mbDownload}Mbps 업로드: {mbUpload}Mbps 아니 25%도 안나온다고요 ㅁㅊ')

    print(f'다운로드: {mbDownload}Mbps 업로드: {mbUpload}Mbps')

    f.close()


scheduler = BlockingScheduler()

scheduler.add_job(job, 'interval', minutes=5)
scheduler.start()
