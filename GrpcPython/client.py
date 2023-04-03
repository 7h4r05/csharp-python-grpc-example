import grpc
import calculator_pb2
import calculator_pb2_grpc
from google.protobuf import wrappers_pb2

channel = grpc.insecure_channel('localhost:5028')
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Add request
request = calculator_pb2.AddRequest(a=1, b=2)
reply = stub.Add(request)

assert reply.sum == 3

# Random request
request = calculator_pb2.RandomRequest(max=wrappers_pb2.Int32Value(
    value=50), min=wrappers_pb2.Int32Value(value=10))
reply = stub.Random(request)

assert reply.result >= 10 and reply.result <= 50
