from __future__ import print_function

import argparse
import time
import grpc
import iris_pb2
import iris_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    print("Client application has connected to Server on Port no 50051")
    stub = iris_pb2_grpc.IrisPredictorStub(channel)
    print("Client stub has created")
    sl,sw,pl,pw=map(float,input("Enter Sepal length, width and Petal length, width : ").split())
    request = iris_pb2.IrisPredictRequest(
        sepal_length=sl,
        sepal_width=sw,
        petal_length=pl,
        petal_width=pw
    )
    response = stub.PredictIrisSpecies(request)
    print("Client request sent to Server")
    species_name = ''
    if response.species == 0:
        species_name = 'Iris-setosa'
    elif response.species == 1:
        species_name = 'Iris-versicolor'
    else:
        species_name = 'Iris-virginica'
    print("Server Response - Predicted species name " + species_name)
run()