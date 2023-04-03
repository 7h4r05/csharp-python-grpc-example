using GrpcService;
using GrpcService.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddGrpc();
builder.Services.AddGrpcClient<GrpcService.Calculator.CalculatorClient>(o =>
{
  o.Address = new Uri("http://localhost:5029");
});

var app = builder.Build();
app.MapGrpcService<CalculatorService>();
app.MapPost("/add", async (httpContext) =>
{
  var request = await httpContext.Request.ReadFromJsonAsync<AddRequest>();
  var client = httpContext.RequestServices.GetService<GrpcService.Calculator.CalculatorClient>();
  var result = await client.AddAsync(request);

  await httpContext.Response.WriteAsJsonAsync(new
  {
    Sum = result.Sum
  });
});
app.MapPost("/random", async (httpContext) =>
{
  var request = await httpContext.Request.ReadFromJsonAsync<RandomRequest>();
  var client = httpContext.RequestServices.GetService<GrpcService.Calculator.CalculatorClient>();
  var result = await client.RandomAsync(request);
  await httpContext.Response.WriteAsJsonAsync(new
  {
    Random = result.Result
  });
});

app.Run();
