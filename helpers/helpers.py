from flask import jsonify


def loop_through_response(arr, query):
    for result in query:
        arr.append(result)

    # If there are no results returned by the search then display an informational message
    if (len(arr) < 1):
        return jsonify({"result": f"No restaurants found."})


    