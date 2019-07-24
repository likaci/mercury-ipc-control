
## Usage
install packages `rsa` and `requests`   
```
pip install requests   
pip install rsa   
```

## Example
```
python mipcc.py admin password url data
python mipcc.py admin password http://192.168.2.89:80 '{"method":"do","preset":{"goto_preset": {"id": "1"}}}'
```


## Data Example
```
PTZ to preset position      {"method":"do","preset":{"goto_preset": {"id": "1"}}}
PTZ by coord                {"method":"do","motor":{"move":{"x_coord":"10","y_coord":"0"}}}
PTZ horizontal by step      {"method":"do","motor":{"movestep":{"direction":"0"}}}
PTZ vertical by step        {"method":"do","motor":{"movestep":{"direction":"90"}}}
stop PTZ                    {"method":"do","motor":{"stop":"null"}}
add PTZ preset position     {"method":"do","preset":{"set_preset":{"name":"name","save_ptz":"1"}}}
lens mask                   {"method":"set","lens_mask":{"lens_mask_info":{"enabled":"on"}}}
```

ref: http://blog.xiazhiri.com/Mercury-MIPC251C-4-Reverse.html