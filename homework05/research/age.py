import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    """
    Наивный прогноз возраста пользователя по возрасту его друзей.

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: Идентификатор пользователя.
    :return: Медианный возраст пользователя.
    """
    age = 0
    friend_ages = []
    f = get_friends(user_id)
    for i in range(0, len(f)):
        try:
            friend_ages.append(f[i]["bdate"].split(".")[2])
        except KeyError:
            continue
        except IndexError:
            continue
    for j in range(len(friend_ages)):
        age += int(friend_ages[j])
    try:
        age = 2022 - age // len(friend_ages)
    except ZeroDivisionError:
        return None
    return age


# print(age_predict(195797232))
