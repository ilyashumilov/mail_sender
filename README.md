## Запуск проекта
docker-compose build
docker-compose up

## входные данные для рассылки

Значение переменных имени, фамилии, адреса электронной почты, и времени, 
через отложенной отправки (в секундах, сколько времени должно пройти до отправки )
заносятся в .csv файл Mailganer/main/app/data.csv

## Метод получения уведомления о прочтении письма

Сервис использует smtp протокол, предоставляемый sendinblue.
sendinblue реализует вэбхук, которым отправляется запрос с информацией о прочтении письма.
Для получения данного запроса реализован апи-эндпроинт /endpoint
