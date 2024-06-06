# GeoPic-Server(지오픽 서버)
---
실시간 지도를 기반으로 정확한 위치에 무슨 일이 일어났는 지 눈으로 볼 수 있는 **실시간 지도 기반** SNS 서비스입니다.
이를 위한 백엔드 서버입니다. fastapi 위에 구성된 pynest를 이용하여 구현하였습니다.

# Getting Start
## 0. Pre-need
### - NaverAPI code
### - DB setup

you have to make .env file. Add .env file on the root directory
your .env file should look like this,
``` .env
NAVER_CLIENT_ID={YOUR_CLIENT_ID}
NAVER_CLIENT_SECRET={YOUR_CLIENT_SECRET}

DB_PASSWORD=password
DB_USER=admin
DB_NAME=admin
DB_HOST=localhost

GRPC_SERVER_IP=0.0.0.0
GRPC_SERVER_PORT=4040
```

## 1. Install Dependencies
``` bash
poetry install
```
## 2. Run Service using poetry
``` bash
poetry run uvicorn "src.app_module:http_server" --host "0.0.0.0" --port "8000" --reload
```

## 3. Send requests
Go to the fastapi docs and use your api endpoints - http://0.0.0.0/docs

# Project Structure
  - Use MVC Pattern
```
📦fullstack_BE  
 ┣ 📂proto  
 ┃ ┗ 📜service.proto  
 ┣ 📂src  
 ┃ ┣ 📂articles  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┣ 📜articles_controller.py  
 ┃ ┃ ┣ 📜articles_entity.py  
 ┃ ┃ ┣ 📜articles_model.py  
 ┃ ┃ ┣ 📜articles_module.py  
 ┃ ┃ ┗ 📜articles_service.py  
 ┃ ┣ 📂commons  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┣ 📜file_upload.py  
 ┃ ┃ ┗ 📜grpc.py  
 ┃ ┣ 📂geocodes  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┣ 📜geocodes_controller.py  
 ┃ ┃ ┣ 📜geocodes_model.py  
 ┃ ┃ ┣ 📜geocodes_moudle.py  
 ┃ ┃ ┗ 📜geocodes_service.py  
 ┃ ┣ 📂live_streams  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┣ 📜live_stream_controller.py  
 ┃ ┃ ┣ 📜live_stream_model.py  
 ┃ ┃ ┣ 📜live_stream_module.py  
 ┃ ┃ ┣ 📜live_stream_service.py  
 ┃ ┃ ┗ 📜live_streams_entity.py  
 ┃ ┣ 📂pb  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┣ 📜service_pb2.py  
 ┃ ┃ ┗ 📜service_pb2_grpc.py  
 ┃ ┣ 📜__init__.py  
 ┃ ┣ 📜app_controller.py  
 ┃ ┣ 📜app_module.py  
 ┃ ┣ 📜app_service.py  
 ┃ ┗ 📜config.py  
 ┣ 📜.env  
 ┣ 📜.gitignore  
 ┣ 📜Dockerfile  
 ┣ 📜README.md  
 ┣ 📜__init__.py  
 ┣ 📜docker-compose.yaml  
 ┣ 📜main.py  
 ┣ 📜poetry.lock  
 ┣ 📜pyproject.toml  
 ┗ 📜requirements.txt
```
