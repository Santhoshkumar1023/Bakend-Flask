
from flask import Flask,jsonify,make_response, request
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
# app=Flask(__name__)

# api=Api(app)

stores=[
    {
        'id':1,
        'name':"First Store",
        'items':[
            {
                'name':'first item',
                 'price':23.23
            }
        ]
    },
     {
        'id':2,
        'name':"Second Store",
        'items':[
            {
                'name':'second item',
                 'price':23.23
            }
        ]
    }
]


class Store(Resource):

    def post(self):
        # if next(filter(lambda x:x['name] ==  name,stores ),None):
           #return make_response(jsonify({"message ":"already exit"},401))  
        data=request.get_json()
        new_store=data
        new_store['id']=len(stores) + 1    
        stores.append(new_store)
        return make_response(jsonify({"status":"true","message":"successfully created..!","data":stores}),201)

    
    def get_by_name(self,name):
        print(name)
        new_value= next(filter(lambda x:x['name'] == name, stores),None)
        return jsonify({"data",new_value})

    # @jwt_required()
    def get(self):
        return make_response({"data":stores})
    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
        type=float,
        required=True,
        help="This is cannot be left blank!")
        data=parser.parse_args()
        print(data['another'])
        return data


    def get_store_by_id(self,id):
        pass

    def update_store_by_id(self,id):
        pass

    def delete(self,id):
        deleted_item = list(filter(lambda x : x['id'] == id,stores))
        return deleted_item
        
    
# api.add_resource(Store,'/stores')