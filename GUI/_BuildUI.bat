cd ..
START "MainWIndow" pipenv run pyside2-uic GUI/Design/MainWindow.ui -o GUI/Base/MainWindow.py
START "TabRecipe" pipenv run pyside2-uic GUI/Design/TabRecipe.ui -o GUI/Base/TabRecipe.py
START "TabIngredients" pipenv run pyside2-uic GUI/Design/TabIngredients.ui -o GUI/Base/TabIngredients.py
START "TabMiscellaneous" pipenv run pyside2-uic GUI/Design/TabMiscellaneous.ui -o GUI/Base/TabMiscellaneous.py
START "TabMash" pipenv run pyside2-uic GUI/Design/TabMash.ui -o GUI/Base/TabMash.py
START "TabFermentation" pipenv run pyside2-uic GUI/Design/TabFermentation.ui -o GUI/Base/TabFermentation.py
START "DialogFermentable" pipenv run pyside2-uic GUI/Design/DialogFermentable.ui -o GUI/Base/DialogFermentable.py
