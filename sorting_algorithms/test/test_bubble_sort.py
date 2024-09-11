from sorting_algorithms.BubbleSort import BubbleSort


def test__bubble_sort_numeric_values():
    data = [1, 5, 234, 123, 2, 32, 500, 23, 2,96]
    bs_obj = BubbleSort()
    sorted_data = bs_obj.sort(data)
    
    assert sorted_data == [1, 2, 2, 5, 23, 32, 96, 123, 234, 500]


def test__bubble_sort_string_values():
    data = ["Behzad", "behzad", "BEHZAD"]
    bs_obj = BubbleSort()
    sorted_data = bs_obj.sort(data)
    
    assert sorted_data == ["BEHZAD", "Behzad", "behzad"]
    
    
def test__bubble_sort_consistent_listElements_type():
    data = [1,2,22,"behzad",33]
    
    bs_obj = BubbleSort()
    sorted_data = bs_obj.sort(data)
    
    assert sorted_data == (f"ERROR: Cannot sort the list. Type inconsistency detected... the list does not contain homogeneous type for all elements in the list: {data}")