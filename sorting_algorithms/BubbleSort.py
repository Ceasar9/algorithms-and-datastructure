
import os
from dotenv import load_dotenv
from logging import getLogger
from uga.list_utils import list_elements_have_consistent_type


load_dotenv()

logger = getLogger(__name__)

try:
    VERBOSE = os.environ.get("VERBOSE") 
except Exception as e:
    # print(f"ERROR: Cannot load envorinment variable 'VERBOSE': {e}")
    logger.error(msg=f"ERROR: Cannot load envorinment variable 'VERBOSE': {e}")
    
class BubbleSort(object):
    def __init__(self) -> None:
        pass
    
    def sort(self, data_list:list) -> list:
        lenght:int = len(data_list)
        self.data_list = data_list
        
        if list_elements_have_consistent_type(self.data_list):
            
            for i in range(0, lenght-1):
                for j in range(0, lenght-i-1):
                    if self.data_list[j] > self.data_list[j+1]:
                        tmp = self.data_list[j+1]
                        self.data_list[j+1] = self.data_list[j]
                        self.data_list[j] = tmp
        else:
            # print(f"ERROR: Cannot sort the list. It does not contain homogeneous types for all elements: {data_list}")
            err_message = f"ERROR: Cannot sort the list. Type inconsistency detected... the list does not contain homogeneous type for all elements in the list: {data_list}"
            logger.error(msg=err_message)
            return None, err_message
        if VERBOSE:
            print(data_list)
        
        return data_list
    
    # def __checkListTypeConsistency(self, data_list):
    #     first_elm_type: type = type(data_list[0])
    #     is_hougeneousTyped_list: bool = all(isinstance(x, first_elm_type) for x in data_list)
        
    #     return is_hougeneousTyped_list
            

if __name__ == "__main__":
    bubble_sort = BubbleSort()
    bubble_sort.sort([1,2,22,0])
    bubble_sort.sort([1,2,22,"behzad"])