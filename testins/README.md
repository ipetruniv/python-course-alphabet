Run file as unit tests vith 
python -m unittest -v utest_cals.py

-m - use module "unittest"
-v - verbose  - applied to the module (not to Python ent)



#Fixtures
fixtures - забезпечують підготовку оточення для виконання тестів
- мінімальна копія бази даних, дані з API-ок etc - може бути створення баз даних деплой етс

#Test case - одиниця тестування (fixtures это то что разработчики используют вместо реальных данных, чтобы тесты прошли и пожар случился только на проде и принёс максимум убытков)

#Test suite - набір test cases

#Test runner - інструмент який оркеструє виконнання тест кейсів


#Methods
setUP() - run before test
tearDown() - run on exit

setUP() -> Tests -> tearDown()



#Command line options
python -m unittest - find and run all tests

python -m unitthest -v utest_calc.py.calc.div

#To read

https://realpython.com/python-testing/
https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
