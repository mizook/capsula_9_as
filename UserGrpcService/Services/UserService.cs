using Grpc.Core;

namespace UserGrpcService.Services;

public class UserService : UserProto.UserService.UserServiceBase
{
    private static readonly List<UserProto.User> Users = new List<UserProto.User>
    {
        new UserProto.User { Id = 1, Email = "user1@example.com", Password = "pass1" },
        new UserProto.User { Id = 2, Email = "user2@example.com", Password = "pass2" },
        new UserProto.User { Id = 3, Email = "user3@example.com", Password = "pass3" },
        new UserProto.User { Id = 4, Email = "carlo.ramirez@alumnos.ucn.cl", Password = "password" }
    };

    public override Task<UserProto.UserResponse> GetUser(UserProto.UserRequest request, ServerCallContext context)
    {
        var user = Users.FirstOrDefault(u => u.Id == request.Id);
        var response = new UserProto.UserResponse
        {
            User = user ?? new UserProto.User()
        };

        return Task.FromResult(response);
    }

    public override Task<UserProto.UsersResponse> GetAllUsers(UserProto.Empty request, ServerCallContext context)
    {
        var response = new UserProto.UsersResponse();
        response.Users.AddRange(Users);
        return Task.FromResult(response);
    }

    public override Task<UserProto.ValidateResponse> ValidateCredentials(UserProto.ValidateRequest request, ServerCallContext context)
    {
        var user = Users.FirstOrDefault(u => u.Email == request.Email && u.Password == request.Password);
        var response = new UserProto.ValidateResponse
        {
            IsValid = user != null
        };

        return Task.FromResult(response);
    }
}
