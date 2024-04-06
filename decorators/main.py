"""
Создать декоратор @http_handler
который будет навешиваться на функции или методы, возвращающие словарь
Задача декоратора кодировать результат функции в json и формировать
из этого стандартный ответ по протоколу http
"""


"""
    HTTP/1.1 200 OK
    Date: Sat, 09 Oct 2010 14:28:02 GMT {вычисляем}
    Server: Apache
    Accept-Ranges: bytes
    Content-Length: 29769 {вычисляем}
    Content-Type: application/json

    {"id": 1,"username":"Id_dev","is_admin":true}
"""

@http_handler
def index():
    data = {
        "foo": "bar"
    }
    return data
    