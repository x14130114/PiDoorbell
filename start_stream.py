import subprocess

p = subprocess.call('gst-launch-1.0 -v v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,width=640,height=480,framerate=30/1,format=I420 ! omxh264enc periodicty-idr=45 inline-header=FALSE ! h264parse ! video/x-h264,stream-format=avc,alignment=au,profile=baseline ! kvssink name=sink stream-name="test" access-key="AKIAIEKOVTSQMMS4JRTQ" secret-key="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" alsasrc device=hw:2,0 ! audioconvert ! avenc_aac ! queue ! sink.', shell=True)
