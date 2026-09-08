from app_factory import create_app
import os

secret_key = os.environ.get("SECRET_KEY")
app = create_app(secret_key=secret_key)

if __name__ == '__main__':
    app.run(debug=True)