# paqmos
Perceived Audio Quality Mean Opinion Score 

```shell
brew install blackhole-16ch
brew install ffmpeg
ffmpeg -f avfoundation -list_devices true -i ""
ffmpeg -f avfoundation -i ":1" -ar 16000 -ac 1 deg2_16K.wav

pip3 install pesq
pip3 install scipy
```
