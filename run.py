from flask_rest_psql_docker import create_app


if __name__ == '__main__':
    create_app(config='development').run(host='0.0.0.0', port=5000)

