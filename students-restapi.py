import json
from flask import Flask, request, jsonify
from urlparse import urlparse

app = Flask(__name__)
myself = ""
original_dic = {"originator": ""}
student_dic = {
    "student": {}
}


@app.route('/student')
def request_student():
    original_dic["originator"] = request.remote_addr
    person_list = ([chr(x) for x in range(ord('a'), ord('z') + 1)])
    if len(original_dic) > 1:
        for persons in person_list:
            if request.remote_addr == originator_dic["originator"]:
                break
            else:
                student_dic["student"]["Person {}".format(persons)] = {"hostname": request.remote_addr}
                break
    return original_dic, student_dic


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12345, threaded=True)
