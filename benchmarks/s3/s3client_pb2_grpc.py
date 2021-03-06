# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import s3client_pb2 as s3client__pb2


class S3Stub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateBucket = channel.unary_unary(
        '/s3client.S3/CreateBucket',
        request_serializer=s3client__pb2.CreateBucketRequest.SerializeToString,
        response_deserializer=s3client__pb2.Reply.FromString,
        )
    self.PutObject = channel.stream_stream(
        '/s3client.S3/PutObject',
        request_serializer=s3client__pb2.Object.SerializeToString,
        response_deserializer=s3client__pb2.Reply.FromString,
        )
    self.UpdateTags = channel.stream_stream(
        '/s3client.S3/UpdateTags',
        request_serializer=s3client__pb2.UpdateTagsRequest.SerializeToString,
        response_deserializer=s3client__pb2.Reply.FromString,
        )
    self.LoadDataset = channel.unary_stream(
        '/s3client.S3/LoadDataset',
        request_serializer=s3client__pb2.LoadDatasetRequest.SerializeToString,
        response_deserializer=s3client__pb2.Object.FromString,
        )


class S3Servicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateBucket(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutObject(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTags(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LoadDataset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_S3Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateBucket': grpc.unary_unary_rpc_method_handler(
          servicer.CreateBucket,
          request_deserializer=s3client__pb2.CreateBucketRequest.FromString,
          response_serializer=s3client__pb2.Reply.SerializeToString,
      ),
      'PutObject': grpc.stream_stream_rpc_method_handler(
          servicer.PutObject,
          request_deserializer=s3client__pb2.Object.FromString,
          response_serializer=s3client__pb2.Reply.SerializeToString,
      ),
      'UpdateTags': grpc.stream_stream_rpc_method_handler(
          servicer.UpdateTags,
          request_deserializer=s3client__pb2.UpdateTagsRequest.FromString,
          response_serializer=s3client__pb2.Reply.SerializeToString,
      ),
      'LoadDataset': grpc.unary_stream_rpc_method_handler(
          servicer.LoadDataset,
          request_deserializer=s3client__pb2.LoadDatasetRequest.FromString,
          response_serializer=s3client__pb2.Object.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      's3client.S3', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
