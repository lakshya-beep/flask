from flask import Flask,jsonify,request

app=Flask(__name__)

#creating a array of task which each task as a different object in it
tasks = [
    {
        "id":1,
        "title":u"buy groceries",
        "describtion":u"milk, cheeze, fruits",
        "done":False
    },{
        'id':2,
        "title":u"learn python",
        "describtion":u"need to find good python tutorials on web",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"

        },400)
    
    task={
        "id":tasks[-1]["id"] +1,
        "title":request.json["title"],
        "describtion":request.json.get("description"," "),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks,

    })



@app.route("/")
def hello_world():
    return "Hello World"

if (__name__ == "__main__") :
    app.run()

