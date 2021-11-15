#***.***.***.253 デフォルトゲートウェイ
ping ***.***.***.253 -c 5   

if [[ $? = 0 ]]; then
	/usr/bin/python3 mail-log.py
fi

#***.***.***.25 DNS
ping ***.***.***.25 -c 5   

if [[ $? = 0 ]]; then
	/usr/bin/python3 mail-log.py
fi
