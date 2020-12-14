# Final_selenium

## Установка и запуск

1) Создайте виртуальное окружение и скачайте репозиторий к себе на компьютер
    ```
    python -m venv venv
    ```
    ```
    git clone https://github.com/Arthas69/Final_selenium
    ```
2) Войдите в виртуальное окружение и установите зависимости
    ```
    pip install -r requirements.txt
    ```
3) Из корня репозитория запустите тесты командой
    ```
    pytest -v --tb=line --language=en -m need_review
    ```