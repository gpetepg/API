from flask_rest_psql_docker import app


def main():
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()




