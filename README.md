## Инструкция по развертыванию
```
docker-compose up --build
```
### backend сервис доступен по адресу: 0.0.0.0:8081
### frontend сервис доступен по адресу: 0.0.0.0:8080

### Учетные данные суперюзера
```
login: admin
password: admin
```


## Описание API

### Поля модели:
```
id: ID,
name: String
companyName: String
positionName: String
hireDate: Date
fireDate: Date
salary: Int
fraction: Int
base: Int
advance: Int
byHours: Boolean
```

### Получение всех должностей
```
Запрос:
query {
  getOccupations{
    id,
    name,
    companyName,
    positionName,
    hireDate,
    fireDate,
    salary,
    fraction,
    base,
    advance,
    byHours
  }
}
```
### Получение должности по id
```
Запрос:
query {
  getOccupations(id: ID){
    id,
    name,
    companyName,
    positionName,
    hireDate,
    fireDate,
    salary,
    fraction,
    base,
    advance,
    byHours
  }
}
```
### Создание новой должности
```
mutation CreateOccupation{
  addOccupation(
    id: ID,
    name: String
    companyName: String
    positionName: String
    hireDate: Date
    fireDate: Date
    salary: Int
    fraction: Int
    base: Int
    advance: Int
    byHours: Boolean
  ){
    occupation {
      id,
      name,
      companyName,
      positionName,
      hireDate,
      fireDate,
      salary,
      fraction,
      base,
      advance,
      byHours
    }
  }
}
```
### Обновление полей должности
```
mutation updateOccupation{
  updateOccupation(
    id: Id,
    name: String,
    companyName: String,
    positionName: String,
    hireDate: Date,
    fireDate: Date
    salary: Int,
    fraction: Int,
    base: Int,
    advance: Int},
    byHours: Boolean
  ){
      occupation{
        id,
        name,
        companyName,
        positionName,
        hireDate,
        fireDate,
        salary,
        fraction,
        base,
        advance,
        byHours
      }
   }
}
```
