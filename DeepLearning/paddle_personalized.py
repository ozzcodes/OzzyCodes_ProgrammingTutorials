
import paddle

movie_info = paddle.dataset.movielens.movie_info()
print(movie_info.values()[0])

user_info = paddle.dataset.movielens.user_info()
print(user_info.values()[0])
