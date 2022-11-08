import grpc, math_pb2_grpc, math_pb2


EQUATION_CASES = (
    (1, 2, 3),
    (3, 2, 1),
    (1, 0, 0),
)


def number_to_complex(num: math_pb2.ComplexNumber) -> complex:
    return complex(num.x, num.y)


def start():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = math_pb2_grpc.MathStub(channel)

        for case in EQUATION_CASES:
            print(f"a = {case[0]} | b = {case[1]} | c = {case[2]}")

            response = stub.QuadraticEquation(math_pb2.QuadraticEquationRequest(
                a=case[0], b=case[1], c=case[2]
            ))
            roots_obj = getattr(response, response.WhichOneof('roots'))

            if isinstance(roots_obj, math_pb2.RealRoots):
                print("Roots:", response.real.x1, response.real.x2, end='\n\n')
            else:
                print("Roots:", number_to_complex(response.complex.x1), 
                                number_to_complex(response.complex.x2), end='\n\n')


if __name__ == '__main__':
    start()
