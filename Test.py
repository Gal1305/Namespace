def test_function ():
    def inner_function ():
        print("Я в области видимости функции test_function")
    inner_function()            # - Ничего не возвращает, т.к. функция отрабатывает внутри другой фунции,
                                # которая не вызывалась.
inner_function()                # - ошибка "name 'inner_function' is not defined. Did you mean: 'test_function'?"
                                # т.к. попытка вызова функции внутри другой функции,
                                # если я правильно понимаю, то "def inner_function" - локальная функция
                                # и она не может вызываться и работать вне "def test_function"

test_function()              # - выводит текст корректно, т.к. функции отрабатывают последовательно
                                # и принтуется текст в скобках.