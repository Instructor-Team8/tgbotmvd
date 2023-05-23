

from vk_api import VkApi
from set import token

session = VkApi(token=token)
vk = session.get_api()

def users_search(number):
    users_sear = vk.users.search(count = 100,university = '569', sex = 1, age_to = 25)
    user_info = vk.users.get(user_id=users_sear['items'][number]['id'], fields='exports, education,photo_max_orig, university_name,domain  ')
    data = {}
    try:
        data['id'] = users_sear['items'][number]['id']
    except (KeyError, IndexError):
        pass
    try:
        data['first_name'] = users_sear['items'][number]['first_name']
    except (KeyError, IndexError):
        pass
    try:
        data['last_name'] = users_sear['items'][number]['last_name']
    except (KeyError, IndexError):
        pass
    try:
        data['can_access_closed'] = users_sear['items'][number]['can_access_closed']
    except (KeyError, IndexError):
        pass
    try:
        data['photo'] = user_info[0]['photo_max_orig']
    except (KeyError, IndexError):
        pass
    return data






#
# def get_user_info(user_ids):
#
#     user_info = vk.users.get(user_id=user_ids, fields='education, university_name,domain  ')
#     print(user_info)
#     data = {}
#     try:
#         data['edu'] = user_info[0]['education']
#     except (KeyError, IndexError):
#         pass
#     try:
#         data['first_name'] = user_info[0]['first_name']
#     except (KeyError, IndexError):
#         pass
#     try:
#         data['last_name'] = user_info[0]['last_name']
#     except (KeyError, IndexError):
#         pass
#     try:
#         data['bdate'] = user_info[0]['bdate']
#     except (KeyError, IndexError):
#         pass
#     try:
#         data['country'] = user_info[0]['country']['title']
#     except (KeyError, IndexError):
#         pass
#     try:
#         data['city'] = user_info[0]['city']['title']
#     except (KeyError, IndexError):
#         pass
#     try:
#         data['vk_prof'] = f'https://vk.com/id{user_ids}'
#     except (KeyError, IndexError):
#         pass
#     try:
#         data['photo'] = user_info[0]['photo_max_orig']
#     except (KeyError, IndexError):
#         pass
#
#     return data
#
# print(get_user_info(413320194))