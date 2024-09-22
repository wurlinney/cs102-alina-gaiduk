list_of_films = 'films.txt'
watch_history = 'history.txt'

class User:
    def __init__(self, watched_films):
        self.watched_films = set(map(int, watched_films))

    def same_views(self, other):
        same_films = len(self.watched_films & other.watched_films)
        if len(self.watched_films) > 0:
            similarity = same_films / len(self.watched_films)
            return similarity
        else:
            return 0

    def unwatched_films(self, other):
        return other.watched_films - self.watched_films

class Recommendation:


    def __init__(self, list_of_films, watch_history):
        self.films = self.films_list(list_of_films)
        self.history = self.history_list(watch_history)


    def films_list(self, list_of_films):
        films = {}
        with open(list_of_films, 'r') as f:
            for string in f:
                film_id, title = string.strip().split(',')
                films[int(film_id)] = title
            return films

    def history_list(self, watch_history):
        users_history = []
        with open(watch_history, 'r') as f:
            for string in f:
                watched_films = string.strip().split(',')
                users_history.append(User(watched_films))
            return users_history

    def recommend(self, our_user):
        our_user = User(our_user)
        potential_films = {}
        for user_history in self.history:
            same_views = our_user.same_views(user_history)
            if same_views >= 0.5:
                unwatched = our_user.unwatched_films(user_history)
                for film_id in unwatched:
                    if film_id not in potential_films:
                        potential_films[film_id] = same_views
                    else:
                        potential_films[film_id] += same_views

        if potential_films:
            recommendation_id = max(potential_films, key =  potential_films.get)
            return self.films[recommendation_id]
        else:
            return 'Не удалось подобрать фильм для Вас'
if __name__ == '__main__':
    get_recommendation = Recommendation(list_of_films, watch_history)
    input_data = input("Введите историю просмотров через запятую: ")
    user_history = list(map(int, input_data.split(',')))
    recommended_film = get_recommendation.recommend(user_history)
    print(f'Рекомендуем Вам {recommended_film}')