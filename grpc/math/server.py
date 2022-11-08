import grpc, math_pb2_grpc, math_pb2

from typing import Tuple
from concurrent.futures import ThreadPoolExecutor


def solve_quadratic_equation(a: float, b: float, c: float) -> Tuple[float, float]:
    d = b**2 - 4 * a * c
    d_sqrt = d ** 0.5

    return (-b - d_sqrt) / (2 * a), (-b + d_sqrt) / (2 * a)


class MathService(math_pb2_grpc.MathServicer):

    def QuadraticEquation(self, request, context):
        x1, x2 = solve_quadratic_equation(request.a, request.b, request.c)
        response = math_pb2.QuadraticEquationResponse()

        if isinstance(x1, complex):
            response.complex.x1.x, response.complex.x1.y = x1.real, x1.imag
            response.complex.x2.x, response.complex.x2.y = x2.real, x2.imag
        else:
            response.real.x1 = x1
            response.real.x2 = x2
        
        return response


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=4))

    math_pb2_grpc.add_MathServicer_to_server(MathService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
