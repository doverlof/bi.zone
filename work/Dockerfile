# Используем Python-образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
# Убедитесь, что копируете requirements.txt в контейнер
COPY requirements.txt /app/requirements.txt

# Установите зависимости
RUN pip install --no-cache-dir -r /app/requirements.txt
# Копируем весь проект
COPY . .

# Указываем порт, который будет слушать контейнер
EXPOSE 8000

# Команда по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]