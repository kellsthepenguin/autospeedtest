from speedtest import Speedtest
import yaml

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

if download < (originalSpeed / 4) or upload < (originalSpeed / 4):
    print('아니 25%도 안나온다고요 ㅁㅊ')

print(download)
print(upload)

f.close()
