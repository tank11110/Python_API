# 目前版本ver 2.0

ver1.0：FLASK上下文設置失效，導致無法正確開啟DB (已修正)

---

# 使用說明：
## 下載方式
1. 透過git clone https://github.com/tank11110/Python_API 下載
2. 根目錄下輸入 docker-compose up --build 啟用服務

## 正確啟用
若是正確啟用則會在預設 http://127.0.0.1:5000/

顯示："message": "Hello API Project"訊息

## 使用之前
在使用這些 API 之前，請確保API服務已通過 docker-compose up 啟動，並顯示"Hello API Project"訊息

### GET方法

curl -X GET http://localhost:5000/products

---

### POST方法

curl -X POST http://127.0.0.1:5000/product

POST範例： 
    
    {
       "name": "Product A",
       "code": "A001",
       "category": "Electronics",
       "size": "M",
       "unit_price": 100,
       "inventory": 50,
       "color": "Red",
    }
    
程式碼：

    curl -X POST http://127.0.0.1:5000/product -H "Content-Type: application/json" -d "{\"name\": \"Product A\", \"code\": \"A001\", \"category\": \"Electronics\", \"size\": \"M\", \"unit_price\": 100, \"inventory\": 50, \"color\": \"Red\"}"

---

### PUT方法

curl -X PUT http://localhost:5000/product/(id)

PUT範例：

    {
       "name": "Product A",
       "code": "A001",
       "category": "Electronics",
       "size": "M",
       "unit_price": 100,
       "inventory": 50,
       "color": "Black",
    }

程式碼：

    curl -X PUT http://127.0.0.1:5000/product/1 -H "Content-Type: application/json" -d "{\"name\": \"Product A\", \"code\": \"A001\", \"category\": \"Electronics\", \"size\":\"M\", \"unit_price\": 100, \"inventory\": 50, \"color\": \"Black\"}"

---

### DELETE方法

curl -X DELETE http://localhost:5000/product/(id)

DELETE範例：

    {
      "id":1
    }

程式碼：

    curl -X DELETE http://localhost:5000/product/1

## 結束服務

1. ctrl+c 暫停服務
2. 輸入 docker-compose down 移除服務