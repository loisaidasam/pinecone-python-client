#
# Copyright (c) 2020-2021 Pinecone Systems Inc. All right reserved.
#

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pinecone.core.grpc.protos.core_pb2 as core__pb2

class RPCClientStub(object):
    """*
    The core `gRPC` service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.stream_stream(
                '/core.RPCClient/Call',
                request_serializer=core__pb2.Request.SerializeToString,
                response_deserializer=core__pb2.Request.FromString,
                )
        self.CallUnary = channel.unary_unary(
                '/core.RPCClient/CallUnary',
                request_serializer=core__pb2.Request.SerializeToString,
                response_deserializer=core__pb2.Request.FromString,
                )


class RPCClientServicer(object):
    """*
    The core `gRPC` service.
    """

    def Call(self, request_iterator, context):
        """If you pass in a request, completed requests will be returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CallUnary(self, request, context):
        """If you pass in a single request, a completed request will be returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCClientServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.stream_stream_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=core__pb2.Request.FromString,
                    response_serializer=core__pb2.Request.SerializeToString,
            ),
            'CallUnary': grpc.unary_unary_rpc_method_handler(
                    servicer.CallUnary,
                    request_deserializer=core__pb2.Request.FromString,
                    response_serializer=core__pb2.Request.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'core.RPCClient', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPCClient(object):
    """*
    The core `gRPC` service.
    """

    @staticmethod
    def Call(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/core.RPCClient/Call',
            core__pb2.Request.SerializeToString,
            core__pb2.Request.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CallUnary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.RPCClient/CallUnary',
            core__pb2.Request.SerializeToString,
            core__pb2.Request.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)