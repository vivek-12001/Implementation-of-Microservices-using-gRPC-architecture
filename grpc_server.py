import os
from concurrent import futures
import time
import argparse

#import sklearn.external.joblib as extjoblib
import joblib
import grpc

import iris_pb2
import iris_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class IrisPredictor(iris_pb2_grpc.IrisPredictorServicer):
    _model = None

    @classmethod
    def get_or_create_model(cls):
        """
        Get or create iris classification model.
        """
        if cls._model is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model', 'iris_model.pickle')
            cls._model = joblib.load(path)
        return cls._model

    def PredictIrisSpecies(self, request, context):
        model = self.__class__.get_or_create_model()
        sepal_length = request.sepal_length
        sepal_width = request.sepal_width
        petal_length = request.petal_length
        petal_width = request.petal_width
        print("Client request has received.")
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        return iris_pb2.IrisPredictReply(species=result[0])


def serve(port, max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    iris_pb2_grpc.add_IrisPredictorServicer_to_server(IrisPredictor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server is running on Port no 50051..!!!")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve(port=50051, max_workers=10)
