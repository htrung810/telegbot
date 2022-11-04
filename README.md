# telegbot
Telegram sử dụng telebot với các ứng dụng căn bản như:
- Kiểm tra top 10 bảng xếp hạng NHA
- Kiểm tra kết quả xổ số và có báo kết quả lúc 7h tối hàng ngày. 
- Sử dụng /help hoặc /start để hiển thị lệnh.
Ngoài ra khi gõ bất kì sẽ có điều kì lạ xảy ra ...
## 1. Installation
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 2. Development
### 2.1 Configuration

```bash
cp .env.sample .env
```
Edit .env file

### 2.2 Bot Start
```bash
export DEBUG=1
python launch.py
```

## 3. Deployment
```bash
python launch.py
```

### Phần đèn là dành cho ESP8266(đang phát triển)

* facebook: [htrung810](https://www.facebook.com/htrung810/)