import json


def hello(event, context):
    return {
	"statuscode": 200,
	"body": json.dumps ({
		"message": "Hello From Lambda"
	)}
}
