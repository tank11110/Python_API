## 目前版本問題

FLASK上下文設置失效，導致無法正確開啟DB

## 啟用方式
1. git clone https://github.com/tank11110/Python_API
2. docker-compose up --build


在使用這些 API 之前，請確保您的服務已通過 `docker-compose up` 命令啟動。

## GET方法

curl -X GET http://localhost:5000/product

## POST方法

curl -X POST http://localhost:5000/product -H "Content-Type: application/json" -d '{
  "name": "Sample Product",
  "code": "SP001",
  "category": "Sample Category",
  "size": "M",
  "unit_price": 100,
  "inventory": 50,
  "color": "Red"
}'

## PUT方法

curl -X PUT http://localhost:5000/product/<id>

## DELETE方法

curl -X DELETE http://localhost:5000/product/<id>
