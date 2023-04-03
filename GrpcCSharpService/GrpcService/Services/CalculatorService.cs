using Grpc.Core;

namespace GrpcService.Services;

public class CalculatorService : Calculator.CalculatorBase
{
  private static readonly Random _random = new Random();
    public override Task<AddReply> Add(AddRequest request, ServerCallContext context)
    {
      var reply = new AddReply
      {
        Sum = request.A + request.B
      };
      return Task.FromResult(reply);
    }

    public override Task<RandomReply> Random(RandomRequest request, ServerCallContext context)
    {
      var reply = new RandomReply
      {
        Result =
          request.Max.HasValue && request.Min.HasValue ? _random.Next(request.Min.Value, request.Max.Value) :
          request.Max.HasValue ? _random.Next(request.Max.Value) : _random.Next()
      };
      return Task.FromResult(reply);
    }
}
