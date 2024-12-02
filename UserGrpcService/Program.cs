using UserGrpcService.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddGrpc();

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<UserService>();
app.MapGet("/", () => "Para comunicarse con este servicio gRPC, use un cliente gRPC. Por ejemplo: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
