
## Usage
install packages `rsa` and `requests`   
```bash
pip install requests
pip install rsa
# or
python2 -m pip install requests
python2 -m pip install requests
```

## Example
```
python2 mipcc.py admin password url data
python2 mipcc.py admin password http://192.168.2.89:80 '{"method":"do","preset":{"goto_preset": {"id": "1"}}}'
```


## Data Example
```json
// add PTZ preset position 添加预置点
{"method":"do","preset":{"set_preset":{"name":"name","save_ptz":"1"}}}

// PTZ to preset position 转动到预置点
{"method":"do","preset":{"goto_preset": {"id": "1"}}}

// PTZ by coord 按坐标转动
{"method":"do","motor":{"move":{"x_coord":"10","y_coord":"0"}}}

// PTZ horizontal by step 水平步进
{"method":"do","motor":{"movestep":{"direction":"0"}}}

// PTZ vertical by step 垂直步进
{"method":"do","motor":{"movestep":{"direction":"90"}}}

// stop PTZ 停止步进
{"method":"do","motor":{"stop":"null"}}

//reset PTZ 云台重置
{"method":"do","motor":{"manual_cali":"null"}}

// lens mask 镜头遮蔽
{"method":"set","lens_mask":{"lens_mask_info":{"enabled":"on"}}}

// manual alarm 手动报警
{"method":"do","msg_alarm":{"manual_msg_alarm":{"action":"start"}}}
{"method":"do","msg_alarm":{"manual_msg_alarm":{"action":"stop"}}}

// toggle green led 绿色led开关
{"method":"set","led":{"config":{"enabled":"off"}}}
{"method":"set","led":{"config":{"enabled":"on"}}}

//auto track moving obj 智能追踪 摄像机追随移动物体
{"method":"set","target_track":{"target_track_info":{"enabled":"on"}}}
{"method":"set","target_track":{"target_track_info":{"enabled":"off"}}}

//alarm if found moving obj 检测到移动物体时报警
{"method":"set","msg_alarm":{"chn1_msg_alarm_info":{"enabled":"on","alarm_type":"0","alarm_mode":["sound"]}}}
{"method":"set","msg_alarm":{"chn1_msg_alarm_info":{"enabled":"on","alarm_type":"0","alarm_mode":["light"]}}}
{"method":"set","msg_alarm":{"chn1_msg_alarm_info":{"enabled":"on","alarm_type":"0","alarm_mode":["sound","light"]}}}
{"method":"set","msg_alarm_plan":{"chn1_msg_alarm_plan":{"enabled":"on","alarm_plan_1":"0000-0000%2c127"}}}

//motion detection 移动侦测 与 侦测灵敏度
{"method":"set","motion_detection":{"motion_det":{"enabled":"off"}}}
{"method":"set","motion_detection":{"motion_det":{"enabled":"on"}}}
{"method":"set","motion_detection":{"motion_det":{"digital_sensitivity":"20"}}}
{"method":"set","motion_detection":{"motion_det":{"digital_sensitivity":"50"}}}
{"method":"set","motion_detection":{"motion_det":{"digital_sensitivity":"80"}}}

//enable record and plan 是否录制与录制计划
{"method":"set","record_plan":{"chn1_channel":{"enabled":"off","monday":"%5b%220000-2400%3a2%22%5d","tuesday":"%5b%220000-2400%3a2%22%5d","wednesday":"%5b%220000-2400%3a2%22%5d","thursday":"%5b%220000-2400%3a2%22%5d","friday":"%5b%220000-2400%3a2%22%5d","saturday":"%5b%220000-2400%3a2%22%5d","sunday":"%5b%220000-2400%3a2%22%5d"}}}
{"method":"set","record_plan":{"chn1_channel":{"enabled":"on","monday":"%5b%220000-2400%3a2%22%5d","tuesday":"%5b%220000-2400%3a2%22%5d","wednesday":"%5b%220000-2400%3a2%22%5d","thursday":"%5b%220000-2400%3a2%22%5d","friday":"%5b%220000-2400%3a2%22%5d","saturday":"%5b%220000-2400%3a2%22%5d","sunday":"%5b%220000-2400%3a2%22%5d"}}}

//reboot and timing reboot 重启与定时重启
{"method":"do","system":{"reboot":"null"}}
{"method":"set","timing_reboot":{"reboot":{"enabled":"off","day":"7","time":"03%3a00%3a00"}}}
{"method":"set","timing_reboot":{"reboot":{"enabled":"on","day":"7","time":"03%3a00%3a00"}}}

//greetings 个性语音提示
{"method":"set","greeter":{"chn1_greeter_ctrl":{"enabled":"on"}}}
{"method":"set","greeter":{"chn1_greeter_ctrl":{"enabled":"off"}}}
//greeting volume 音量
{"method":"set","greeter":{"chn1_greeter_audio":{"enter_volume":"77","leave_volume":"77"}}}
//play greetings 播放语音
{"method":"do","greeter":{"test_audio":{"force":"1"}}} 播放默认语音
{"method":"do","greeter":{"test_audio":{"id":"4096","force":"1"}}} 播放指定语音
//id
//0 无
//12288 你好
//4096-4104 依次为 你好欢迎光临 ..... 
//set enter or leave greetings 设置进入或离开语音
{"method":"set","greeter":{"chn1_greeter_audio":{"enter_audio_id":"0"}}} 无
{"method":"set","greeter":{"chn1_greeter_audio":{"leave_audio_id":"4104"}}}
```

ref: http://blog.xiazhiri.com/Mercury-MIPC251C-4-Reverse.html