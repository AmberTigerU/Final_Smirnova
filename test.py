import request


# Смирнова_Анна, 12- когорта,"Финальный проект,инженер по тестированию плюс "
# Проверка создания заказа
def test_order_creation():
    creation_response = request.post_new_order()
    track_id = creation_response.json()['track']
    response = request.get_orders_track(track_id)
    assert response.status_code == 200
