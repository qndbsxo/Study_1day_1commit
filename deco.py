from flask import Flask, jsonify, request
from flask.json import JSONEncoder

## Default JSON encoder를 set를 JSON으로 변환할 수 없다.
## 그럼으로 커스텀 엔코더를 작성해서 set을 list로 변환하여
## JSON으로 변환 가능하게 해주어야 한다.
class CustomJSONEncoder(JSON):
	def defy