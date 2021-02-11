### API

| URL                         | Method |
| --------------------------- | ------ |
| `/tokens/`                  | POST   |
| `/users/<int:id>`           | GET    |
| `/users/<int:id>/posts`     | GET    |
| `/users/<int:id>/timeline`  | GET    |
| `/posts`                    | GET    |
| `/posts`                    | POST   |
| `/posts/<int:id>`           | GET    |
| `/posts/<int:id>`           | PUT    |
| `/posts/<int:id>/comments/` | GET    |
| `/posts/<int:id>/comments/` | POST   |
| `/comments/`                | GET    |
| `/comments/<int:id>`        | GET    |

## Example

### Get a token

```sh
http --auth <email>:<password> --json POST \
http://127.0.0.1:5000/api/v1/tokens/

# set token
token=...
```

### Get A user

```sh
http --auth $token: --json GET \
http://127.0.0.1:5000/api/v1/users/1
```

### Get posts written by a user

```sh
http --auth $token: --json GET \
http://127.0.0.1:5000/api/v1/users/1/posts/
```

### Get posts followed by a user

```sh
http --auth $token: --json GET \
http://127.0.0.1:5000/api/v1/users/1/timeline/
```

### Get all posts

```sh
http --auth $token: --json GET \
http://127.0.0.1:5000/api/v1/posts/
```

### Add a Post

```sh
http --auth $token: --json POST \
http://127.0.0.1:5000/api/v1/posts/ \
"body=I'm adding a post."
```

### Get a post

```sh
http --auth $token: --json GET \
http://127.0.0.1:5000/api/v1/posts/1
```

### Edit a post

```sh
http --auth $token: --json PUT \
http://127.0.0.1:5000/api/v1/posts/1 \
"body=I'm adding a post.(edited)"
```

### Get all comments of a post

```sh
http --auth $token: --json GET \
http://127.0.0.1:5000/api/v1/posts/1/comments/
```

### Add a comment of a post

```sh
http --auth $token: --json POST \
http://127.0.0.1:5000/api/v1/posts/1/comments/ \
"body=I'm adding a comment."```

## Get all comments

​```sh
http --auth $token: --json GET \
http://127.0.0.1:5000/api/v1/comments/
```

### Get a comment

```sh
http --auth $token: --json GET \
http://127.0.0.1:5000/api/v1/comments/1```

```