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
