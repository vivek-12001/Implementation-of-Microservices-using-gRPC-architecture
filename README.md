# Implementing microservices using gRPC

The machine learning model predicts iris species by given sepal length, sepal width, petal length and petal width. gRPC framework is used for Client and Server communication.

## Implement the files

1. Train machine learning model for iris data with `./model/train.py`
  - As a result, it saves a model to predict iris species in `iris_model.pickle`
2. Define the Service defination ( protocol-buffer ) file in `iris.proto`
  - We have define two services IrisPredictRequest and IrisPredictReply
3. Implement a command to generate python files from `iris.proto` in `codegen.py`
  - Stub creation file for Server and Client `iris_pb2.py`
  - Service implementation file `iris_pb2_grpc.py` are auto generated.
4. Implement `grpc_server.py`
  - gRPC server is created here running on port 50051
5. Implement `iris_client.py`.
  - client connected to server and send request to gRPC server


# Run gRPC server.
python grpc_server.py

# Run client.
python iris_client.py

# GROUP NO - 9
  - SHRAVAN BHAT - 09
  - VIVEK CHOUDHARY - 16
  - ADITYA DEOPURKAR - 19
  - SAHIL TALREJA - 65
