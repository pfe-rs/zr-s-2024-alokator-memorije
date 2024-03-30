from konkurentno_bez_random import funkcija, main_task
from program_bez_random import  Alokator, Element

def test_funkcija():
    a = Alokator(50, "BestFit")  # Inicijalizacija Alokator objekta sa odgovarajućim parametrima
    e = Element([3, 4])  # Primer ulaza e
    i = 0 # Indeks elementa

    # Poziv funkcije koju testiramo
    funkcija(a, e, 1, 2, i)

    # Provera očekivanog stanja a.allocated_list, a.memory_list i a.positions_list
    assert a.allocated_list == [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]  # Očekivana vrednost a.allocated_list
    assert a.memory_list == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Očekivana vrednost a.memory_list
    assert a.positions_list == [(7, 2)]  # Očekivana vrednost a.positions_list

def test_main_task():
    e_list = [[3, 4], [5, 6], [7, 8, 9], [0, 1, 2]]  # Lista ulaza e
    a = Alokator(50, "BestFit")  # Inicijalizacija Alokator objekta sa odgovarajućim parametrima

    # Poziv funkcije koju testiramo
    main_task(e_list, a)

    # Provera očekivanog stanja a.allocated_list, a.memory_list i a.positions_list nakon izvršenja main_task funkcije
    assert a.allocated_list == [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]  # Očekivana vrednost a.allocated_list
    assert a.memory_list == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Očekivana vrednost a.memory_list
    assert a.positions_list == [(30, 3), (37, 3), (7, 2), (34, 2)]

    





