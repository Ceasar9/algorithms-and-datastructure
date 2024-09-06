from sorting_algorithms.BubbleSort import BubbleSort


def test__bubble_sort():
    data = [1, 5, 234, 123, 2, 32, 500, 23, 2,96]
    bs_obj = BubbleSort()
    sorted_data = bs_obj.sort(data)
    
    assert sorted_data == [1, 2, 2, 5, 23, 32, 96, 123, 234, 500]
