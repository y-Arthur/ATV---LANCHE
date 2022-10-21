from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order
from UserInterface import UserInterface


def test_set_menu_item():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    menu2 = Menu(2, "Test 2", 5)
    menu3 = Menu(3, "Test 3", 2)
    
    # Act
    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)

    # Assert
    assert len(menu_repository.menu_itens) == 2
    assert not menu3 in menu_repository.menu_itens
    assert type(menu_repository.menu_itens) == list


def test_check_if_itens_exists():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    order1 = Order(1, 10)
    order2 = Order(2, 10)
    
    # Act
    menu_repository.set_menu_item(menu1)
    resultOK = menu_repository.check_if_itens_exists(order1)
    resultNOK = menu_repository.check_if_itens_exists(order2)

    # Assert
    assert len(menu_repository.menu_itens) == 1
    assert resultOK == True
    assert resultNOK == False




def test_get_total_price():
    # Arrange
    repository = MenuRepository()
    menu = Menu(1, "teste", 10)
    interface_user = UserInterface(repository)
    teste = Order(1, 20)

    # Act
    repository.set_menu_item(menu)
    total_price = interface_user.get_total_price(teste)
    # Assert
    assert total_price == 200


def test_get_user_input():
    # Arrange
    repository = MenuRepository()
    interface_user = UserInterface(repository)
  

    # Act
    ordem = interface_user.get_user_input()

    # Assert
    assert ordem.code == 2
    assert ordem.quantity == 20