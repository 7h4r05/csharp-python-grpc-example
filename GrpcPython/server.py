import grpc
import calculator_pb2
import calculator_pb2_grpc
import random
from concurrent import futures
from calculator_pb2_grpc import CalculatorServicer


class CalculatorServicerImpl:
    CalculatorServicer

    def Add(self, request, context):
        return calculator_pb2.AddReply(sum=request.a + request.b)

    def Random(self, request, context):
        result = random.randint(request.min.value, request.max.value)
        return calculator_pb2.RandomReply(result=result)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculator_pb2_grpc.add_CalculatorServicer_to_server(
    CalculatorServicerImpl(), server)
server.add_insecure_port('[::]:5029')
server.start()
server.wait_for_termination()
