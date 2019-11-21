#-*- coding:utf-8 -*-

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/info/weather')
def get_weather():
    try:
        args = request.args.to_dict()
        print(args)
        info = requests.get(f'api.openweathermap.org/data/2.5/weather?lat={args["lat"]}&lon={args["lon"]}&APPID=802a80fdfe342bbe836c82a46b9d2d23')
        return jsonify({'weather': info['weather']['main'], 'temp': info['main']['temp'], 'humidity': info['main']['humidity']}), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 500


@app.route('/info/shelter/')
def get_shelter():
    try:
        args = request.args.to_dict()
        info = requests.get(f'http://api.data.go.kr/openapi/clns-shunt-fclty-std?serviceKey=0xoZmFtpQb7pY6%2B3wv7k1SWquqsj0l09EnJSTZOY%2F4vJpBWltCpKmQa1KwZ%2FeIKQJRNZyHMnN8C6Gjxe1oiJbg%3D%3D&pageNo=1&numOfRows=5&type=json&latitude={args["lat"]}&hardness={args["lon"]}&openYn=Y')
        print(info.text)
        if 'NODATA_ERROR' in info.text:
            raise Exception('no data')
        else:
            return jsonify({'name': info['clnsShuntFcltyNm'], 'location': info['rdnmadr']}), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 500


@app.route('/info/disaster/')
def get_disaster():
    pass


if __name__ == '__main__':
    app.run(debug=True)
